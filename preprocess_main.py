# preprocess_main.py

import os
import sys
from pathlib import Path

def setup_project():
    """Setup project directories and environment"""
    # Get project root directory
    project_root = Path(__file__).parent
    
    # Ensure necessary directories exist
    directories = [
        'models',
        'resources',
        'images'
    ]
    
    for directory in directories:
        dir_path = project_root / directory
        dir_path.mkdir(exist_ok=True)
        print(f"Checked directory: {dir_path}")
    
    # Add project root to Python path
    sys.path.insert(0, str(project_root))
    
    return project_root

def main():
    """Main preprocessing script"""
    project_root = setup_project()
    
    # Import after setting up path
    from src.tools.preprocess_celebrities import process_all_celebrity_images
    
    # Set paths relative to project root
    images_dir = project_root / "images"
    output_file = project_root / "resources" / "celebrity_mappings.pkl"
    
    print(f"\nProject root: {project_root}")
    print(f"Images directory: {images_dir}")
    print(f"Output file: {output_file}")
    
    if not images_dir.exists():
        print(f"\nError: Images directory not found at {images_dir}")
        return
    
    # Process celebrities
    try:
        celebrity_data = process_all_celebrity_images(str(images_dir), str(output_file))
        print(f"\nSuccessfully processed {len(celebrity_data)} celebrities")
    except Exception as e:
        print(f"\nError during processing: {str(e)}")

if __name__ == '__main__':
    main()