# src/tools/preprocess_celebrities.py

import os
import sys
import cv2
import numpy as np
import pickle
from tqdm import tqdm

# Add project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

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

def process_all_celebrity_images(images_dir, output_file):
    """Process all celebrity images and save to a binary file."""
    face_processor = FaceProcessor()
    celebrity_data = {}
    
    print(f"\nProcessing celebrity images from: {images_dir}")
    
    # Verify images directory exists
    if not os.path.exists(images_dir):
        print(f"Error: Images directory not found at {images_dir}")
        return None
        
    # Get all celebrity directories
    celebrity_dirs = [d for d in os.listdir(images_dir) 
                     if os.path.isdir(os.path.join(images_dir, d))]
    
    print(f"Found {len(celebrity_dirs)} celebrity directories")
    
    for celebrity in tqdm(celebrity_dirs, desc="Processing celebrities"):
        print(f"\nProcessing {celebrity}...")
        celebrity_dir = os.path.join(images_dir, celebrity)
        all_embeddings = []
        all_faces = []
        all_images = []  # Store actual image data
        preview_image = None
        
        # Get all images for this celebrity
        image_files = [f for f in os.listdir(celebrity_dir) 
                      if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        
        print(f"Found {len(image_files)} images for {celebrity}")
        
        for img_file in tqdm(image_files, desc=f"Processing {celebrity} images"):
            img_path = os.path.join(celebrity_dir, img_file)
            try:
                image = cv2.imread(img_path)
                if image is not None:
                    face_data = face_processor.analyze_face(image)
                    if face_data:
                        # Save the embedding
                        embedding = convert_to_serializable(face_data['embedding'])
                        if embedding:
                            all_embeddings.append(embedding)
                            
                            # Save face data
                            face_data_serializable = convert_to_serializable(face_data)
                            if face_data_serializable:
                                all_faces.append(face_data_serializable)
                                
                            # Save processed image path
                            all_images.append(img_path)
                            
                            if preview_image is None:
                                preview_image = img_path
            except Exception as e:
                print(f"Error processing {img_path}: {str(e)}")
                continue
        
        if all_embeddings:
            # Calculate average embedding
            avg_embedding = np.mean(np.array(all_embeddings), axis=0)
            avg_embedding = avg_embedding / np.linalg.norm(avg_embedding)
            
            # Store all data for this celebrity
            celebrity_data[celebrity] = {
                'preview_image': preview_image,
                'embedding': convert_to_serializable(avg_embedding),
                'all_embeddings': all_embeddings,
                'all_faces': all_faces,
                'all_images': all_images,
                'total_processed': len(all_embeddings)
            }
            
            print(f"Successfully processed {len(all_embeddings)} faces for {celebrity}")
        else:
            print(f"No valid faces found for {celebrity}")
    
    if not celebrity_data:
        print("Error: No celebrity data was processed")
        return None
        
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Save processed data
    print(f"\nSaving {len(celebrity_data)} celebrity mappings to {output_file}")
    try:
        with open(output_file, 'wb') as f:
            pickle.dump(celebrity_data, f)
            
        # Verify the file was written
        if os.path.exists(output_file):
            file_size = os.path.getsize(output_file)
            print(f"Successfully wrote {file_size} bytes to {output_file}")
            
            # Verify we can read it back
            with open(output_file, 'rb') as f:
                verification_data = pickle.load(f)
            print(f"Successfully verified data for {len(verification_data)} celebrities")
            
            # Print sample of data structure
            first_celeb = next(iter(verification_data.items()))
            print("\nSample data structure:")
            print(f"Celebrity: {first_celeb[0]}")
            print(f"Keys: {first_celeb[1].keys()}")
            print(f"Number of faces: {first_celeb[1]['total_processed']}")
            
            return celebrity_data
        else:
            print("Error: File was not created")
            return None
            
    except Exception as e:
        print(f"Error saving celebrity data: {str(e)}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == '__main__':
    # Set up paths
    images_dir = os.path.join(project_root, "images")
    output_file = os.path.join(project_root, "resources", "celebrity_mappings.pkl")
    
    print(f"Project root: {project_root}")
    print(f"Images directory: {images_dir}")
    print(f"Output file: {output_file}")
    
    # Process the celebrities
    result = process_all_celebrity_images(images_dir, output_file)
    
    if result:
        print("\nProcessing completed successfully!")
        print(f"Processed data for {len(result)} celebrities")
        print("Celebrity names:", list(result.keys()))
        
        # Print detailed stats
        print("\nDetailed statistics:")
        for celeb, data in result.items():
            print(f"{celeb}: {data['total_processed']} faces processed")
    else:
        print("\nProcessing failed!")