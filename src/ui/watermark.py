# Path: src/ui/watermark.py
import cv2
import numpy as np
from typing import Tuple
import logging
from typing import Optional

class VideoWatermark:
    def __init__(self, logo_path: str, opacity: float = 0.5, premium_manager: Optional['PremiumManager'] = None):
        self.logo_path = logo_path
        self.opacity = opacity
        self.premium_manager = premium_manager
        """
        Initialize the watermark processor with a static bottom-right position
        
        Args:
            logo_path: Path to the PNG logo file
            opacity: Float between 0 and 1 for logo opacity (default 0.5)
        """
        try:
            # Try to load with alpha channel
            self.logo = cv2.imread(logo_path, cv2.IMREAD_UNCHANGED)
            if self.logo is None:
                raise ValueError(f"Could not load logo from {logo_path}")
            
            # Convert RGB to RGBA if necessary
            if len(self.logo.shape) == 3 and self.logo.shape[2] == 3:
                # Create alpha channel
                alpha = np.ones(self.logo.shape[:2], dtype=self.logo.dtype) * 255
                self.logo = cv2.merge([self.logo, alpha])
            
            self.opacity = opacity
            self.logo_size: Tuple[int, int] = self._get_initial_size()
            # Resize logo once during initialization
            self.logo = cv2.resize(self.logo, self.logo_size)
            
            logging.info(f"Watermark initialized: shape={self.logo.shape}, size={self.logo_size}")
            
        except Exception as e:
            logging.error(f"Error initializing watermark: {str(e)}")
            # Create a small default watermark (red square) as fallback
            self.logo = np.zeros((40, 40, 4), dtype=np.uint8)
            self.logo[:, :, 2] = 255  # Red color
            self.logo[:, :, 3] = 255  # Full alpha
            self.logo_size = (40, 40)
            self.opacity = 0.3
    
    def _get_initial_size(self) -> Tuple[int, int]:
        """Set initial size of logo - relatively small by default"""
        target_width = 80
        aspect_ratio = self.logo.shape[1] / self.logo.shape[0]
        target_height = int(target_width / aspect_ratio)
        return (target_width, target_height)
    
    def _get_position(self, frame_width: int, frame_height: int) -> Tuple[int, int]:
        """Calculate bottom-right position with padding"""
        padding = 10  # pixels from edge
        x = frame_width - self.logo_size[0] - padding
        y = frame_height - self.logo_size[1] - padding
        return (x, y)
    
    def apply_watermark(self, frame: np.ndarray) -> np.ndarray:
        """
        Apply watermark to a single frame
        
        Args:
            frame: numpy array representing the video frame (BGR format)
            
        Returns:
            Watermarked frame
        """
        try:
            # Make sure frame is valid
            if frame is None or len(frame.shape) != 3:
                return frame
                
            # Get position for watermark
            x, y = self._get_position(frame.shape[1], frame.shape[0])
            
            # Ensure coordinates are within frame bounds
            if x < 0 or y < 0 or x + self.logo_size[0] > frame.shape[1] or y + self.logo_size[1] > frame.shape[0]:
                return frame
            
            # Create mask from alpha channel
            mask = (self.logo[:, :, 3] / 255.0 * self.opacity)
            mask = np.dstack([mask] * 3)  # Create 3-channel mask
            
            # Extract RGB channels from logo
            logo_rgb = self.logo[:, :, :3]
            
            # Get region of interest (ROI)
            roi = frame[y:y+self.logo_size[1], x:x+self.logo_size[0]]
            
            # Ensure ROI and logo_rgb have same shape
            if roi.shape != logo_rgb.shape:
                return frame
            
            # Blend logo with frame
            blended = (1 - mask) * roi + mask * logo_rgb
            
            # Put blended region back into frame
            frame[y:y+self.logo_size[1], x:x+self.logo_size[0]] = blended.astype(np.uint8)
            
            return frame
            
        except Exception as e:
            logging.error(f"Error applying watermark: {str(e)}")
            return frame  # Return original frame if there's an error
    
    @property
    def is_valid(self) -> bool:
        """Check if watermark was initialized properly"""
        return self.logo is not None and len(self.logo.shape) == 3 and self.logo.shape[2] == 4