# src/core/image_loader.py

import os
import cv2

def load_celebrity_images(images_dir):
    """Load celebrity images from the specified directory."""
    celebrities = {}
    for celebrity in os.listdir(images_dir):
        celebrity_dir = os.path.join(images_dir, celebrity)
        if os.path.isdir(celebrity_dir):
            # Collect all images in the celebrity's directory
            images = [
                os.path.join(celebrity_dir, file)
                for file in os.listdir(celebrity_dir)
                if file.lower().endswith(('.png', '.jpg', '.jpeg'))
            ]
            if images:
                celebrities[celebrity] = images
    return celebrities
