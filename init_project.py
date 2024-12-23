# init_project.py
import os
import urllib.request
from tqdm import tqdm
import ssl

def download_file(url: str, filename: str):
    """Download a file with progress bar"""
    ssl._create_default_https_context = ssl._create_unverified_context
    
    # Create a request with headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    request = urllib.request.Request(url, headers=headers)
    
    response = urllib.request.urlopen(request)
    total_size = int(response.headers.get('Content-Length', 0))
    
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    with tqdm(total=total_size, unit='B', unit_scale=True, desc=filename) as pbar:
        urllib.request.urlretrieve(
            url,
            filename,
            reporthook=lambda count, block_size, total_size: pbar.update(block_size)
        )

def init_project():
    """Initialize project structure and download required models"""
    print("Initializing MacFaceSwap project...")
    
    # Define model URLs and paths
    models = {
        'inswapper_128.onnx': 'https://github.com/facefusion/facefusion-assets/releases/download/models/inswapper_128.onnx',
        'GFPGANv1.4.pth': 'https://github.com/TencentARC/GFPGAN/releases/download/v1.3.4/GFPGANv1.4.pth'
    }
    
    # Download models
    for model_name, url in models.items():
        model_path = os.path.join('models', model_name)
        if not os.path.exists(model_path):
            print(f"\nDownloading {model_name}...")
            try:
                download_file(url, model_path)
            except Exception as e:
                print(f"Error downloading {model_name}: {str(e)}")
                print(f"Please download manually from: {url}")
                print(f"And place it in the models/ directory as: {model_name}")
        else:
            print(f"\n{model_name} already exists, skipping download.")

    # Install required packages
    print("\nInstalling required packages...")
    os.system('pip install -r requirements.txt')

    print("\nProject initialization complete!")

if __name__ == '__main__':
    init_project()