# ~/face_swap/utils/model_downloader.py

import os
import hashlib
import requests
from pathlib import Path
from typing import Dict, Optional, Callable
from tqdm import tqdm
import json
import logging
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import QProgressDialog, QMessageBox


class ModelDownloadWorker(QThread):
    """Worker thread for downloading models with progress updates."""
    progress = pyqtSignal(int)
    status = pyqtSignal(str)
    finished = pyqtSignal(bool, str)
    
    def __init__(self, url: str, save_path: Path, expected_hash: str):
        super().__init__()
        self.url = url
        self.save_path = save_path
        self.expected_hash = expected_hash
        
    def run(self):
        try:
            print(f"\n=== Starting download from {self.url} ===")
            self.status.emit(f"Connecting to {self.url}")
            
            response = requests.get(self.url, stream=True, timeout=30)
            response.raise_for_status()
            
            total_size = int(response.headers.get('content-length', 0))
            print(f"Total file size: {total_size / (1024*1024):.2f} MB")
            
            block_size = 8192
            downloaded = 0
            
            self.save_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(self.save_path, 'wb') as f:
                for data in response.iter_content(block_size):
                    if self.isInterruptionRequested():
                        print("Download interrupted")
                        self.finished.emit(False, "Download cancelled")
                        return
                        
                    downloaded += len(data)
                    f.write(data)
                    
                    if total_size:
                        progress = int((downloaded / total_size) * 100)
                        self.progress.emit(progress)
                        
                        if progress % 10 == 0:
                            mb_downloaded = downloaded / (1024*1024)
                            mb_total = total_size / (1024*1024)
                            self.status.emit(f"Downloaded {mb_downloaded:.1f} MB of {mb_total:.1f} MB")
            
            if self.verify_file():
                self.finished.emit(True, "")
            else:
                self.save_path.unlink(missing_ok=True)
                self.finished.emit(False, "File verification failed")
                
        except Exception as e:
            print(f"Download error: {e}")
            self.finished.emit(False, str(e))
            
    def verify_file(self) -> bool:
        """Verify downloaded file using SHA-256 hash."""
        try:
            sha256_hash = hashlib.sha256()
            with open(self.save_path, "rb") as f:
                for byte_block in iter(lambda: f.read(65536), b""):
                    sha256_hash.update(byte_block)
            return sha256_hash.hexdigest() == self.expected_hash
        except Exception as e:
            print(f"Verification error: {e}")
            return False

class ModelDownloader:
    def __init__(self, models_dir: str, config_url: str, parent=None):
        """
        Initialize the model downloader.
        
        Args:
            models_dir (str): Directory where models will be stored
            config_url (str): URL to the JSON config file containing model information
            parent: Optional Qt parent widget for progress dialogs
        """
        self.models_dir = Path(models_dir)
        self.config_url = config_url
        self.models_dir.mkdir(parents=True, exist_ok=True)
        self.logger = logging.getLogger(__name__)
        self.parent = parent
        self.workers = []
        
    def get_models_config(self) -> Dict:
        """Fetch the models configuration from the remote server."""
        try:
            response = requests.get(self.config_url)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            self.logger.error(f"Failed to fetch models config: {e}")
            raise

    def verify_model(self, file_path: Path, expected_hash: str) -> bool:
        """Verify model file integrity."""
        if not file_path.exists():
            return False
            
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(65536), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest() == expected_hash

    def download_model(self, model_name: str, url: str, expected_hash: str) -> Optional[Path]:
        """Download a model file with progress tracking."""
        model_path = self.models_dir / f"{model_name}.pth"
        
        # Check if model already exists and is valid
        if model_path.exists() and self.verify_model(model_path, expected_hash):
            self.logger.info(f"Model {model_name} already exists and is valid")
            return model_path

        if self.parent:  # GUI mode
            return self._download_with_gui(model_name, url, expected_hash, model_path)
        else:  # CLI mode
            return self._download_with_tqdm(model_name, url, expected_hash, model_path)

    def _download_with_gui(self, model_name: str, url: str, expected_hash: str, model_path: Path) -> Optional[Path]:
        """Download with Qt progress dialog."""
        try:
            # Create progress dialog
            progress = QProgressDialog(
                f"Downloading {model_name}...",
                "Cancel",
                0, 100,
                self.parent
            )
            progress.setWindowTitle(f"Downloading {model_name}")
            progress.setMinimumDuration(0)
            progress.setMinimumWidth(400)
            
            # Create and configure worker
            worker = ModelDownloadWorker(url, model_path, expected_hash)
            worker.progress.connect(progress.setValue)
            worker.status.connect(lambda msg: progress.setLabelText(msg))
            
            # Handle completion
            download_completed = False
            def on_finished(success, error):
                nonlocal download_completed
                download_completed = True
                if not success:
                    QMessageBox.critical(
                        self.parent,
                        "Download Error",
                        f"Failed to download {model_name}: {error}"
                    )
            
            worker.finished.connect(on_finished)
            
            # Start download
            self.workers.append(worker)  # Keep reference
            worker.start()
            
            # Show dialog
            progress.exec()
            
            # Handle cancellation
            if progress.wasCanceled():
                worker.requestInterruption()
                worker.wait()
                return None
                
            # Wait for completion if needed
            if not download_completed:
                worker.wait()
            
            return model_path if model_path.exists() and self.verify_model(model_path, expected_hash) else None
            
        except Exception as e:
            self.logger.error(f"Error in GUI download of {model_name}: {e}")
            if model_path.exists():
                model_path.unlink()
            return None
        
    def _download_with_tqdm(self, model_name: str, url: str, expected_hash: str, model_path: Path) -> Optional[Path]:
        """Download with tqdm progress bar (CLI mode)."""
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            total_size = int(response.headers.get('content-length', 0))

            with open(model_path, 'wb') as f:
                with tqdm(total=total_size, unit='iB', unit_scale=True) as pbar:
                    for data in response.iter_content(chunk_size=8192):
                        size = f.write(data)
                        pbar.update(size)

            if self.verify_model(model_path, expected_hash):
                return model_path
            else:
                model_path.unlink()
                return None

        except Exception as e:
            self.logger.error(f"Error in CLI download of {model_name}: {e}")
            if model_path.exists():
                model_path.unlink()
            return None

    def ensure_models(self, required_models: Optional[list] = None) -> Dict[str, Path]:
        """
        Ensure all required models are downloaded and verified.
        
        Args:
            required_models (Optional[list]): List of specific models to download, 
                                            or None for all models
        
        Returns:
            Dict[str, Path]: Dictionary mapping model names to their file paths
        """
        config = self.get_models_config()
        downloaded_models = {}
        
        for model_name, model_info in config['models'].items():
            if required_models is None or model_name in required_models:
                model_path = self.download_model(
                    model_name,
                    model_info['url'],
                    model_info['sha256']
                )
                if model_path:
                    downloaded_models[model_name] = model_path
                else:
                    raise RuntimeError(f"Failed to download required model: {model_name}")
                    
        return downloaded_models

class ModelManager:
    """Manages the lifecycle of models in the application."""
    
    def __init__(self, downloader: ModelDownloader):
        self.downloader = downloader
        self.loaded_models = {}
        self.logger = logging.getLogger(__name__)
        
    def load_model(self, model_name: str):
        """Load a model into memory."""
        if model_name in self.loaded_models:
            return self.loaded_models[model_name]
            
        try:
            models = self.downloader.ensure_models([model_name])
            if model_name not in models:
                raise RuntimeError(f"Failed to download model: {model_name}")
                
            # Here you would implement the actual model loading logic
            # depending on your ML framework (PyTorch, TensorFlow, etc.)
            # model = YourModelClass.load(models[model_name])
            # self.loaded_models[model_name] = model
            # return model
            
        except Exception as e:
            self.logger.error(f"Error loading model {model_name}: {e}")
            raise
            
    def unload_model(self, model_name: str):
        """Unload a model from memory."""
        if model_name in self.loaded_models:
            del self.loaded_models[model_name]
            
    def cleanup(self):
        """Cleanup all loaded models."""
        self.loaded_models.clear()