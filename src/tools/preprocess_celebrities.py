# src/tools/preprocess_celebrities.py

import os
import sys
import cv2
import numpy as np
import pickle
import json
from tqdm import tqdm
from datetime import datetime
from pathlib import Path
from src.core.face_processor import FaceProcessor
def convert_to_serializable(obj):
    """Convert an object to a serializable format"""
    if obj is None:
        return None
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    elif isinstance(obj, (int, float, str, bool)):
        return obj
    elif isinstance(obj, (list, tuple)):
        return [convert_to_serializable(item) for item in obj]
    elif isinstance(obj, dict):
        return {k: convert_to_serializable(v) for k, v in obj.items()}
    else:
        try:
            # Try to convert to dict if it's an object with attributes
            return {k: convert_to_serializable(v) for k, v in vars(obj).items()}
        except:
            # If all else fails, convert to string
            return str(obj)

def load_manifest(manifest_path):
    """Load the processing manifest"""
    try:
        if os.path.exists(manifest_path):
            with open(manifest_path, 'r') as f:
                return json.load(f)
        return {}
    except Exception as e:
        print(f"Error loading manifest: {e}")
        return {}

def save_manifest(manifest_path, manifest):
    """Save the processing manifest"""
    try:
        with open(manifest_path, 'w') as f:
            json.dump(manifest, f, indent=2)
    except Exception as e:
        print(f"Error saving manifest: {e}")

def file_needs_processing(file_path, manifest, force_reprocess=False):
    """Check if a file needs processing based on modification time or force flag"""
    if force_reprocess:
        return True
        
    if not os.path.exists(file_path):
        return False
        
    mod_time = os.path.getmtime(file_path)
    return (file_path not in manifest or 
            manifest[file_path]['modified_time'] < mod_time)

def process_all_celebrity_images(images_dir, output_file, force_reprocess=False):
    """
    Process all celebrity images and save to a binary file.
    
    Args:
        images_dir: Directory containing celebrity image folders
        output_file: Path to save the processed data
        force_reprocess: If True, reprocess all images regardless of cache
    """
    face_processor = FaceProcessor()
    celebrity_data = {}
    failed_images = []
    
    # Setup manifest
    manifest_path = os.path.join(os.path.dirname(output_file), 'processing_manifest.json')
    manifest = {} if force_reprocess else load_manifest(manifest_path)
    
    if force_reprocess:
        print("\nForce reprocess enabled - will process all images")
    
    print(f"\nProcessing celebrity images from: {images_dir}")
    
    if not os.path.exists(images_dir):
        print(f"Error: Images directory not found at {images_dir}")
        return None
        
    celebrity_dirs = [d for d in os.listdir(images_dir) 
                     if os.path.isdir(os.path.join(images_dir, d))]
    
    print(f"Found {len(celebrity_dirs)} celebrity directories")
    
    # Load existing celebrity data if it exists
    if os.path.exists(output_file) and not force_reprocess:
        try:
            with open(output_file, 'rb') as f:
                celebrity_data = pickle.load(f)
            print(f"Loaded existing data for {len(celebrity_data)} celebrities")
        except Exception as e:
            print(f"Error loading existing data: {e}")
            celebrity_data = {}
    
    for celebrity in tqdm(celebrity_dirs, desc="Processing celebrities"):
        print(f"\nProcessing {celebrity}...")
        celebrity_dir = os.path.join(images_dir, celebrity)
        all_embeddings = []
        all_faces = []
        all_images = []
        preview_image = None
        
        # Get existing celebrity data if available
        existing_data = celebrity_data.get(celebrity, {})
        existing_embeddings = existing_data.get('all_embeddings', [])
        existing_faces = existing_data.get('all_faces', [])
        existing_images = existing_data.get('all_images', [])
        
        image_files = [f for f in os.listdir(celebrity_dir) 
                      if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        
        print(f"Found {len(image_files)} images for {celebrity}")
        
        for img_file in tqdm(image_files, desc=f"Processing {celebrity} images"):
            img_path = os.path.join(celebrity_dir, img_file)
            
            # Check if file needs processing
            if not file_needs_processing(img_path, manifest, force_reprocess):
                # Use existing data
                idx = existing_images.index(img_path) if img_path in existing_images else -1
                if idx >= 0:
                    all_embeddings.append(existing_embeddings[idx])
                    all_faces.append(existing_faces[idx])
                    all_images.append(img_path)
                    if preview_image is None:
                        preview_image = img_path
                    continue
            
            try:
                image = cv2.imread(img_path)
                if image is None:
                    failed_images.append((img_path, "Failed to load image"))
                    continue
                    
                # Process new image
                faces = face_processor.face_analyzer.get(image)
                if not faces:
                    failed_images.append((img_path, "No face detected"))
                    continue
                    
                face = faces[0]
                
                if hasattr(face, 'embedding') and face.embedding is not None:
                    embedding = face.embedding
                    embedding_list = convert_to_serializable(embedding)
                    if embedding_list:
                        all_embeddings.append(embedding_list)
                        all_images.append(img_path)
                        
                        face_dict = {}
                        if hasattr(face, 'bbox') and face.bbox is not None:
                            face_dict['bbox'] = face.bbox.tolist()
                        if hasattr(face, 'kps') and face.kps is not None:
                            face_dict['kps'] = face.kps.tolist()
                        if hasattr(face, 'landmark_2d_106') and face.landmark_2d_106 is not None:
                            try:
                                face_dict['landmark_2d_106'] = face.landmark_2d_106.tolist()
                            except:
                                face_dict['landmark_2d_106'] = None
                        
                        all_faces.append(face_dict)
                        
                        if preview_image is None:
                            preview_image = img_path
                            
                        # Update manifest
                        manifest[img_path] = {
                            'modified_time': os.path.getmtime(img_path),
                            'processed_time': datetime.now().timestamp()
                        }
                else:
                    failed_images.append((img_path, "No embedding generated"))
                    continue
                    
            except Exception as e:
                failed_images.append((img_path, f"Processing error: {str(e)}"))
                continue
        
        if all_embeddings:
            try:
                avg_embedding = np.mean(np.array(all_embeddings), axis=0)
                avg_embedding = avg_embedding / np.linalg.norm(avg_embedding)
                
                celebrity_data[celebrity] = {
                    'preview_image': preview_image,
                    'embedding': convert_to_serializable(avg_embedding),
                    'all_embeddings': all_embeddings,
                    'all_faces': all_faces,
                    'all_images': all_images,
                    'total_processed': len(all_embeddings)
                }
                
                print(f"Successfully processed {len(all_embeddings)} faces for {celebrity}")
            except Exception as e:
                print(f"Error processing embeddings for {celebrity}: {str(e)}")
                continue
        else:
            print(f"No valid faces found for {celebrity}")
    
    # Save manifest
    save_manifest(manifest_path, manifest)
    
    # Report failed images
    if failed_images:
        print("\nFailed images report:")
        for img_path, reason in failed_images:
            print(f"- {img_path}: {reason}")
    
    if not celebrity_data:
        print("Error: No celebrity data was processed")
        return None
        
    # Save processed data
    print(f"\nSaving {len(celebrity_data)} celebrity mappings to {output_file}")
    try:
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, 'wb') as f:
            pickle.dump(celebrity_data, f)
        
        if os.path.exists(output_file):
            file_size = os.path.getsize(output_file)
            print(f"Successfully wrote {file_size} bytes to {output_file}")
            
            with open(output_file, 'rb') as f:
                verification_data = pickle.load(f)
            print(f"Successfully verified data for {len(verification_data)} celebrities")
            return celebrity_data
    except Exception as e:
        print(f"Error saving celebrity data: {str(e)}")
        return None

if __name__ == '__main__':
    # If run directly, provide a simple test
    if len(sys.argv) > 1:
        images_dir = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else 'celebrity_mappings.pkl'
        process_all_celebrity_images(images_dir, output_file)
    else:
        print("Please provide images directory path")