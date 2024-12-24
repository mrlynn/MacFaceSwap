# src/core/mapping_loader.py

import os
import pickle
import numpy as np
from typing import Dict, Any, Optional

def convert_to_numpy(data):
    """Convert serialized data back to numpy arrays where needed"""
    if isinstance(data, list):
        return np.array(data)
    elif isinstance(data, dict):
        return {k: convert_to_numpy(v) for k, v in data.items()}
    return data

def load_celebrity_mappings(mapping_file: str) -> Optional[Dict[str, Any]]:
    """Load pre-computed celebrity mappings."""
    print("\nAttempting to load celebrity mappings...")
    print(f"Looking for mapping file at: {os.path.abspath(mapping_file)}")
    
    try:
        if not os.path.exists(mapping_file):
            print(f"Mapping file not found at {mapping_file}")
            return None
        
        print(f"Loading mappings from: {mapping_file}")
        with open(mapping_file, 'rb') as f:
            data = pickle.load(f)
            
        # Convert lists back to numpy arrays
        processed_data = {}
        for celebrity, celeb_data in data.items():
            processed_data[celebrity] = {
                'preview_image': celeb_data['preview_image'],
                'embedding': np.array(celeb_data['embedding']),
                'all_embeddings': [np.array(emb) for emb in celeb_data['all_embeddings']],
                'all_faces': celeb_data['all_faces'],  # Keep as dict representation
                'all_images': celeb_data['all_images'],
                'total_processed': celeb_data['total_processed']
            }
            
        print(f"Successfully loaded mappings for {len(processed_data)} celebrities")
        print("Celebrity names:", list(processed_data.keys()))
        return processed_data
            
    except Exception as e:
        print(f"Error loading celebrity mappings: {str(e)}")
        import traceback
        traceback.print_exc()
        return None