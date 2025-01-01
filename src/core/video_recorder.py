import cv2
import time
import numpy as np
from threading import Thread, Lock, Event
from queue import Queue
import sounddevice as sd
import soundfile as sf
import os
from pathlib import Path
import platform
import subprocess

class VideoRecorder:
    def __init__(self):
        self.is_recording = False
        self.writer = None
        self.frame_queue = Queue(maxsize=300)
        self.audio_queue = Queue()
        self.lock = Lock()
        self.recording_thread = None
        self.audio_thread = None
        self.current_recording_path = None
        self.start_time = None
        self.frame_count = 0
        self.target_fps = 30.0
        self.sample_rate = 44100
        self.audio_device = None  # Default to None, or specify a default device
        self.audio_channels = self._get_default_audio_channels()  # Now safely called
        self.temp_audio_path = None
        self.temp_video_path = None

    def _get_default_audio_channels(self):
        """Get the default number of input channels for the selected device."""
        try:
            device_info = sd.query_devices(self.audio_device or sd.default.device[0], 'input')
            return device_info.get('max_input_channels', 2)  # Default to 2 if undefined
        except Exception as e:
            print(f"Error querying audio device: {e}")
            return 2  # Fallback to stereo

    def start_recording(self, frame_size, fps=30.0):
        if self.is_recording:
            return None
            
        self.target_fps = fps
        self.start_time = time.time()
        self.frame_count = 0
        
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        base_path = os.path.join(self._get_downloads_dir(), f"recording_{timestamp}")
        self.temp_video_path = f"{base_path}_temp.mp4"
        self.current_recording_path = f"{base_path}.mp4"
        self.temp_audio_path = f"{base_path}_audio.wav"
        
        fourcc = cv2.VideoWriter_fourcc(*'avc1')
        self.writer = cv2.VideoWriter(
            self.temp_video_path,
            fourcc,
            self.target_fps,
            frame_size,
            True
        )
        
        if not self.writer.isOpened():
            return None
            
        self.is_recording = True
        self.audio_thread = Thread(target=self._audio_loop)
        self.audio_thread.start()
        time.sleep(0.1)  # Wait for audio to initialize
        
        return self.current_recording_path


    def add_frame(self, frame):
        if self.is_recording and self.writer and self.writer.isOpened():
            elapsed_time = time.time() - self.start_time
            expected_frame_count = int(elapsed_time * self.target_fps)

            while self.frame_count < expected_frame_count:
                self.writer.write(frame)
                self.frame_count += 1

    def _recording_loop(self):
        while not self.stop_event.is_set() or not self.frame_queue.empty():
            try:
                frame, timestamp = self.frame_queue.get(timeout=0.1)
                with self.lock:
                    if self.writer and self.writer.isOpened():
                        self.writer.write(frame)
            except:
                continue

    def _audio_callback(self, indata, frames, time, status):
        if status:
            print(f"Audio status: {status}")
        if self.is_recording:
            self.audio_queue.put(indata.copy())
            print(f"Captured audio frames: {indata.shape}")  # Debug

    def _audio_loop(self):
        try:
            print(f"Starting audio recording: {self.temp_audio_path}")
            with sf.SoundFile(self.temp_audio_path, mode='w',
                            samplerate=self.sample_rate,
                            channels=self.audio_channels) as audio_file, \
                sd.InputStream(device=self.audio_device,
                                channels=self.audio_channels,
                                samplerate=self.sample_rate,
                                callback=self._audio_callback):
                print(f"Audio device: {self.audio_device}, Channels: {self.audio_channels}")
                while self.is_recording:
                    try:
                        data = self.audio_queue.get(timeout=0.1)  # Fetch audio data
                        audio_file.write(data)  # Write data to the file
                        print(f"Written {data.shape[0]} frames to audio file.")
                    except Exception as e:
                        print(f"Audio queue error: {e}")
        except Exception as e:
            print(f"Audio loop error: {e}")

    def stop_recording(self):
        self.is_recording = False

        if self.audio_thread:
            self.audio_thread.join()

        if self.writer:
            self.writer.release()
            self.writer = None

        if os.path.exists(self.temp_audio_path) and os.path.exists(self.temp_video_path):
            try:
                subprocess.run([
                    'ffmpeg',
                    '-i', self.temp_video_path,  # Input video
                    '-i', self.temp_audio_path,  # Input audio
                    '-c:v', 'copy',  # Copy video without re-encoding
                    '-c:a', 'aac',   # Encode audio as AAC
                    '-strict', 'experimental',
                    self.current_recording_path  # Output file
                ], check=True)
                print(f"Recording saved to: {self.current_recording_path}")
            except Exception as e:
                print(f"FFmpeg error: {e}")

        # Cleanup temp files
        if os.path.exists(self.temp_audio_path):
            os.remove(self.temp_audio_path)
        if os.path.exists(self.temp_video_path):
            os.remove(self.temp_video_path)

        return self.current_recording_path

    def __del__(self):
        if self.is_recording:
            self.stop_recording()
            
    def _get_downloads_dir(self):
        if platform.system() == 'Darwin':
            return str(Path.home() / "Downloads")
        return str(Path.home() / "Downloads")