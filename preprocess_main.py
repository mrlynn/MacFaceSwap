# preprocess_main.py

import os
import sys
from pathlib import Path
import argparse

def setup_project():
    """Setup project directories and environment"""
    project_root = Path(__file__).parent
    
    directories = [
        'models',
        'resources',
        'images'
    ]
    
    for directory in directories:
        dir_path = project_root / directory
        dir_path.mkdir(exist_ok=True)
        print(f"Checked directory: {dir_path}")
    
    sys.path.insert(0, str(project_root))
    
    return project_root

def main():
    """Main preprocessing script"""
    parser = argparse.ArgumentParser(description='Preprocess celebrity images for face swapping')
    parser.add_argument('--force', '-f', action='store_true', 
                      help='Force reprocessing of all images')
    parser.add_argument('--images-dir', type=str,
                      help='Custom path to images directory')
    parser.add_argument('--output-file', type=str,
                      help='Custom path for output file')
    args = parser.parse_args()

    project_root = setup_project()
    
    # Import after setting up path
    from src.tools.preprocess_celebrities import process_all_celebrity_images
    
    # Set paths relative to project root, allowing for custom paths
    images_dir = Path(args.images_dir) if args.images_dir else project_root / "images"
    output_file = Path(args.output_file) if args.output_file else project_root / "resources" / "celebrity_mappings.pkl"
    
    print(f"\nProject root: {project_root}")
    print(f"Images directory: {images_dir}")
    print(f"Output file: {output_file}")
    print(f"Force reprocess: {args.force}")
    
    if not images_dir.exists():
        print(f"\nError: Images directory not found at {images_dir}")
        return
    
    # Process celebrities
    try:
        celebrity_data = process_all_celebrity_images(
            str(images_dir), 
            str(output_file),
            force_reprocess=args.force
        )
        if celebrity_data:
            print(f"\nSuccessfully processed {len(celebrity_data)} celebrities")
    except Exception as e:
        print(f"\nError during processing: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()