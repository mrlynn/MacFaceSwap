import cv2
import numpy as np
from typing import Optional, Tuple, Callable, List, Dict
from threading import Thread, Lock
import time
import platform
import signal
import subprocess
import sys
from src.ui.watermark import VideoWatermark
import tracemalloc
import gc
import resource
import logging
import tracemalloc

# Lazy load psutil
_psutil = None
def get_psutil():
    global _psutil
    if _psutil is None:
        try:
            import psutil
            _psutil = psutil
        except ImportError:
            logging.warning("psutil not available")
            return None
    return _psutil

if not tracemalloc.is_tracing():
    tracemalloc.start()

class VideoHandler:
    def __init__(self):
        self.camera = None
        self.is_running = False
        self.frame_lock = Lock()
        self.current_frame = None
        self.processing_callback = None
        self.frame_size = (1280, 720)
        self.fps_stats = {'last_time': time.time(), 'frames': 0, 'fps': 0}
        self.process_every_n_frames = 2
        self.frame_count = 0
        self.show_fps = False
        self.capture_thread = None
        self.watermark = VideoWatermark(
            logo_path="resources/logo.png",
            opacity=0.5
        )
        
        # Frame caching for smooth transitions
        self.last_processed_frames = []
        self.max_cache_frames = 3
        self.last_successful_swap = None
        self.last_face_positions = None
        
        # Set up signal handler for segfault protection
        if platform.system() == 'Darwin':
            signal.signal(signal.SIGSEGV, self._handle_segfault)

    # Add inside VideoHandler class, after __init__
    def _monitor_memory(self):
        """Monitor memory usage"""
        try:
            process = psutil.Process()
            mem_info = process.memory_info()
            logging.debug(f"Memory usage: {mem_info.rss / 1024 / 1024:.2f} MB")
            if tracemalloc.is_tracing():
                snapshot = tracemalloc.take_snapshot()
                top_stats = snapshot.statistics('lineno')[:3]
                logging.debug("Top 3 memory allocations:")
                for stat in top_stats:
                    logging.debug(stat)
        except Exception as e:
            logging.error(f"Memory monitoring error: {e}")

    def _handle_segfault(self, signum, frame):
        """Handle segmentation faults gracefully"""
        print("Caught segmentation fault - cleaning up...")
        self.stop_camera()
        # Restart the application
        os.execv(sys.executable, ['python'] + sys.argv)
        
    def _init_camera_backend(self):
        """Initialize appropriate camera backend for the platform"""
        # if platform.system() == 'Darwin':
        #     # Try to use AVFoundation backend on macOS
        #     self.camera_backend = cv2.CAP_AVFOUNDATION
        # else:
        #     self.camera_backend = cv2.CAP_ANY

        self.camera_backend = cv2.CAP_QT

    def _safe_camera_open(self, camera_id: int, backend=None) -> Optional[cv2.VideoCapture]:
        """Safely try to open a camera with timeout"""
        try:
            if backend is not None:
                cap = cv2.VideoCapture(camera_id, backend)
            else:
                cap = cv2.VideoCapture(camera_id)
                
            if not cap.isOpened():
                return None
                
            # Try to read a test frame with timeout
            cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
            start_time = time.time()
            while time.time() - start_time < 2.0:  # 2 second timeout
                ret, frame = cap.read()
                if ret and frame is not None:
                    # Apply watermark correctly using instance method
                    frame = self.watermark.apply_watermark(frame)
                    return cap
                time.sleep(0.1)
            
            cap.release()
            return None
            
        except Exception as e:
            print(f"Error opening camera {camera_id}: {str(e)}")
            return None
            
    def _create_capture(self, camera_id: int) -> cv2.VideoCapture:
        """Create camera capture with appropriate settings"""
        if platform.system() == 'Darwin':
            capture = cv2.VideoCapture(camera_id, cv2.CAP_AVFOUNDATION)
        else:
            capture = cv2.VideoCapture(camera_id)
            
        if capture.isOpened():
            capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_size[0])
            capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_size[1])
            capture.set(cv2.CAP_PROP_FPS, 30)
            capture.set(cv2.CAP_PROP_BUFFERSIZE, 1)
            
        return capture
        
    def start_camera(self, camera_id: int = 0) -> bool:
        try:
            self.stop_camera()
            time.sleep(0.5)
            gc.collect()

            self.camera = cv2.VideoCapture(camera_id)
            if not self.camera.isOpened() and platform.system() == 'Darwin':
                self.camera = cv2.VideoCapture(camera_id, cv2.CAP_AVFOUNDATION)
                
            if not self.camera.isOpened():
                logging.error(f"Failed to open camera {camera_id}")
                return False

            self.frame_size = (1280, 720)
            self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_size[0])
            self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_size[1])
            
            actual_width = self.camera.get(cv2.CAP_PROP_FRAME_WIDTH)
            actual_height = self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
            logging.info(f"Camera resolution: {actual_width}x{actual_height}")
            
            self.is_running = True
            self.capture_thread = Thread(target=self._protected_capture_loop, daemon=True)
            self.capture_thread.start()
            return True
                
        except Exception as e:
            logging.error(f"Camera start error: {e}")
            self.stop_camera()
            return False

    def _protected_capture_loop(self):
        try:
            self._capture_loop()
        except MemoryError:
            logging.error("Memory error in capture loop")
            self.stop_camera()
        except Exception as e:
            logging.error(f"Capture loop error: {e}")
            self.stop_camera()
            
    def stop_camera(self):
        """Stop camera and clear cache"""
        self.is_running = False
        if self.capture_thread:
            self.capture_thread.join(timeout=1.0)
        if self.camera:
            self.camera.release()
            self.camera = None
        time.sleep(0.5)  # Allow camera to fully release
        with self.frame_lock:
            self.current_frame = None

    def _capture_loop(self):
        frame_counter = 0
        while self.is_running and self.camera and self.camera.isOpened():
            try:
                ret, frame = self.camera.read()
                if not ret or frame is None:
                    continue
                    
                # Memory cleanup every 100 frames    
                if frame_counter % 100 == 0:
                    gc.collect()

                processed_frame = frame.copy()
                del frame  # Explicit cleanup
                
                processed_frame = self.watermark.apply_watermark(processed_frame)
                
                with self.frame_lock:
                    self.current_frame = processed_frame
                    
                frame_counter += 1
                
            except Exception as e:
                logging.error(f"Frame processing error: {e}")
                break
        
    def _update_fps(self):
        """Update FPS calculation"""
        current_time = time.time()
        delta_time = current_time - self.fps_stats['last_time']
        
        if delta_time >= 1.0:
            self.fps_stats['fps'] = self.fps_stats['frames'] / delta_time
            self.fps_stats['frames'] = 0
            self.fps_stats['last_time'] = current_time
        else:
            self.fps_stats['frames'] += 1
            
    def get_camera_list(self) -> List[dict]:
        """Get list of available cameras"""
        cameras = []
        # Only check first few indices on macOS
        max_cameras = 3 if platform.system() == 'Darwin' else 5
        
        for i in range(max_cameras):
            try:
                print(f"Checking camera {i}...")
                cap = cv2.VideoCapture(i)
                if cap.isOpened():
                    ret, test_frame = cap.read()
                    if ret and test_frame is not None:
                        cameras.append({
                            'id': i,
                            'name': f'Camera {i}'
                        })
                        print(f"Found working camera {i}")
                cap.release()
            except Exception as e:
                print(f"Error checking camera {i}: {str(e)}")
                
        return cameras
        
    def get_latest_frame(self) -> Optional[np.ndarray]:
        """Thread-safe method to get the latest frame"""
        with self.frame_lock:
            if self.current_frame is None:
                return None
            return self.current_frame.copy()

    def set_frame_size(self, width: int, height: int):
        """Set capture frame size"""
        self.frame_size = (width, height)
        if self.camera and self.camera.isOpened():
            self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
            self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
            
    def set_processing_callback(self, callback: Callable):
        """Set callback for frame processing"""
        self.processing_callback = callback

    def set_frame_processing_rate(self, process_every_n: int):
        """Set how often frames should be processed"""
        self.process_every_n_frames = max(1, process_every_n)
        print(f"Processing every {self.process_every_n_frames} frames")

    def clear_cache(self):
        """Clear the frame cache"""
        self.last_processed_frames = []
        self.last_successful_swap = None
        self.last_face_positions = None