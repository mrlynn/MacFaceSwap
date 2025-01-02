# src/utils/hash_generator.py

import hashlib
import requests
from pathlib import Path
import argparse
from tqdm import tqdm
import json

def download_and_hash_model(url: str, save_path: Path = None) -> tuple[str, Path]:
    """
    Download a model file and generate its SHA-256 hash.
    
    Args:
        url: Direct download URL for the model
        save_path: Optional path to save the downloaded model
        
    Returns:
        tuple: (SHA-256 hash, Path to downloaded file)
    """
    # If no save path provided, save in current directory with filename from URL
    if save_path is None:
        save_path = Path(url.split('/')[-1])
    
    # Create parent directories if they don't exist
    save_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Download the file with progress bar
    response = requests.get(url, stream=True)
    response.raise_for_status()
    
    total_size = int(response.headers.get('content-length', 0))
    block_size = 8192
    hash_obj = hashlib.sha256()
    
    print(f"\nDownloading {url} to {save_path}")
    
    with open(save_path, 'wb') as f:
        with tqdm(total=total_size, unit='iB', unit_scale=True) as pbar:
            for data in response.iter_content(block_size):
                size = f.write(data)
                pbar.update(size)
                hash_obj.update(data)
    
    return hash_obj.hexdigest(), save_path

def hash_existing_model(file_path: Path) -> str:
    """
    Generate SHA-256 hash for an existing model file.
    
    Args:
        file_path: Path to the model file
        
    Returns:
        str: SHA-256 hash
    """
    hash_obj = hashlib.sha256()
    total_size = file_path.stat().st_size
    
    with open(file_path, 'rb') as f:
        with tqdm(total=total_size, unit='iB', unit_scale=True) as pbar:
            while chunk := f.read(8192):
                hash_obj.update(chunk)
                pbar.update(len(chunk))
    
    return hash_obj.hexdigest()

def update_model_config(config_path: Path, model_name: str, model_hash: str, url: str):
    """
    Update the model configuration file with new hash.
    
    Args:
        config_path: Path to the config file
        model_name: Name of the model
        model_hash: SHA-256 hash of the model
        url: Download URL for the model
    """
    if config_path.exists():
        with open(config_path, 'r') as f:
            config = json.load(f)
    else:
        config = {"version": "1.0.0", "models": {}}
    
    config["models"][model_name] = {
        "url": url,
        "sha256": model_hash,
        "required": True,
        "description": f"{model_name} model"
    }
    
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=4)
    
    print(f"\nUpdated {config_path} with new hash for {model_name}")

def main():
    parser = argparse.ArgumentParser(description="Download and generate SHA-256 hash for model files")
    parser.add_argument("--url", help="URL to download the model from")
    parser.add_argument("--file", help="Path to existing model file", type=Path)
    parser.add_argument("--save-path", help="Path to save the downloaded model", type=Path)
    parser.add_argument("--model-name", help="Name of the model for config file")
    parser.add_argument("--config", help="Path to config file to update", type=Path)
    
    args = parser.parse_args()
    
    if args.url:
        # Download and hash
        model_hash, saved_path = download_and_hash_model(args.url, args.save_path)
        print(f"\nDownloaded to: {saved_path}")
    elif args.file:
        # Hash existing file
        model_hash = hash_existing_model(args.file)
        saved_path = args.file
    else:
        parser.error("Either --url or --file must be provided")
    
    print(f"\nSHA-256 hash: {model_hash}")
    
    # Update config if requested
    if args.config and args.model_name:
        update_model_config(
            args.config,
            args.model_name,
            model_hash,
            args.url if args.url else str(saved_path)
        )

if __name__ == "__main__":
    main()