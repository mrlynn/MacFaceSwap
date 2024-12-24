# src/core/video_handler.py

import cv2
import numpy as np
from typing import Optional, Tuple, Callable, List, Dict
from threading import Thread, Lock
import time
import platform
import signal
import subprocess
import sys

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
        
        # Frame caching for smooth transitions
        self.last_processed_frames = []
        self.max_cache_frames = 3
        self.last_successful_swap = None
        self.last_face_positions = None
        
        # Set up signal handler for segfault protection
        if platform.system() == 'Darwin':
            signal.signal(signal.SIGSEGV, self._handle_segfault)
            
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
                    return cap
                time.sleep(0.1)
                
            # If we couldn't get a frame, release and return None
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
        self.stop_camera()
        time.sleep(0.5)
        
        try:
            self.camera = cv2.VideoCapture(camera_id)
            
            if not self.camera.isOpened():
                if platform.system() == 'Darwin':
                    self.camera = cv2.VideoCapture(camera_id, cv2.CAP_AVFOUNDATION)
                    
            if not self.camera.isOpened():
                return False
            
            # Force specific frame size
            self.frame_size = (1280, 720)  # Fixed size
            self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_size[0])
            self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_size[1])
            
            # Verify size was set
            actual_width = self.camera.get(cv2.CAP_PROP_FRAME_WIDTH)
            actual_height = self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
            print(f"Camera resolution: {actual_width}x{actual_height}")
            
            self.is_running = True
            self.capture_thread = Thread(target=self._protected_capture_loop, daemon=True)
            self.capture_thread.start()
            return True
            
        except Exception as e:
            print(f"Error starting camera: {e}")
            self.stop_camera()
            return False

    def _protected_capture_loop(self):
        """Protected version of capture loop"""
        try:
            self._capture_loop()
        except Exception as e:
            print(f"Error in capture loop: {str(e)}")
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
        """Main capture loop running in separate thread"""
        frame_counter = 0
        while self.is_running and self.camera and self.camera.isOpened():
            ret, frame = self.camera.read()
            if not ret or frame is None:
                continue
                
            frame_counter += 1
            if frame_counter % self.process_every_n_frames != 0:
                continue
                
            processed_frame = frame.copy()
            
            if self.processing_callback:
                try:
                    result = self.processing_callback(processed_frame)
                    if result is not None:
                        processed_frame = result
                except Exception as e:
                    print(f"Error in frame processing: {e}")
            
            # Thread-safe frame update
            with self.frame_lock:
                self.current_frame = processed_frame
        
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