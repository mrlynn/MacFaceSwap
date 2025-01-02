# src/core/model_manager.py

import os
import json
import logging
import shutil
from pathlib import Path
from typing import Dict, Optional, Tuple
import requests
from PyQt6.QtWidgets import QProgressDialog, QMessageBox
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from src.utils.model_downloader import ModelDownloadWorker
class MacFaceSwapModelManager:
    """Manages AI models for the MacFaceSwap application."""
    
    def __init__(self, main_window):
        self.main_window = main_window
        self.logger = logging.getLogger(__name__)
        
        # Set up source and destination directories
        self.src_models_dir = Path(__file__).parent.parent.parent / "models"
        self.dest_models_dir = Path.home() / "Library/Application Support/MacFaceSwap/models"
        self.dest_models_dir.mkdir(parents=True, exist_ok=True)
        
        # Load configuration from source directory
        self.config_path = self.src_models_dir / "config.json"
        self.model_config = self.load_config()
        self.download_workers = []
        
        self.logger.info(f"Source models directory: {self.src_models_dir}")
        self.logger.info(f"Destination models directory: {self.dest_models_dir}")
        
    def load_config(self) -> dict:
        """Load model configuration from config file."""
        try:
            print(f"\nLoading config from: {self.config_path}")
            with open(self.config_path, 'r') as f:
                config = json.load(f)
                print("Config loaded successfully")
                print("Models in config:", list(config['models'].keys()))
                return config
        except Exception as e:
            print(f"Error loading config: {e}")
            return None
            
    def initialize(self) -> bool:
        """Initialize the model manager and check for required models."""
        try:
            if not self.model_config:
                self.logger.error("No valid configuration found")
                return False
                
            # Check for required models
            missing_models = self.check_required_models()
            if missing_models:
                return self.handle_missing_models(missing_models)
                
            return True
            
        except Exception as e:
            self.logger.error(f"Error initializing model manager: {e}")
            return False
            
    def find_model(self, model_name: str) -> Tuple[Optional[Path], bool]:
        """
        Find a model file in either source or destination directory.
        
        Returns:
            Tuple[Optional[Path], bool]: (path to model if found, True if needs copying)
        """
        print(f"\n=== Looking for model: {model_name} ===")
        print(f"Source directory: {self.src_models_dir}")
        print(f"Destination directory: {self.dest_models_dir}")
        
        # Determine correct file extension
        file_ext = '.onnx' if model_name == 'inswapper' else '.pth'
        print(f"Using file extension: {file_ext}")
        
        # Check destination directory first
        dest_path = self.dest_models_dir / f"{model_name}{file_ext}"
        print(f"\nChecking destination path: {dest_path}")
        print(f"Destination path exists: {dest_path.exists()}")
        
        if dest_path.exists():
            expected_hash = self.model_config['models'][model_name]['sha256']
            is_valid = self.verify_model(dest_path, expected_hash)
            print(f"Destination file validation: {is_valid}")
            if is_valid:
                print("Found valid model in destination directory")
                return dest_path, False
        
        # Check source directory
        src_path = self.src_models_dir / f"{model_name}{file_ext}"
        print(f"\nChecking source path: {src_path}")
        print(f"Source path exists: {src_path.exists()}")
        
        if src_path.exists():
            expected_hash = self.model_config['models'][model_name]['sha256']
            is_valid = self.verify_model(src_path, expected_hash)
            print(f"Source file validation: {is_valid}")
            if is_valid:
                print("Found valid model in source directory")
                return src_path, True
                
        print("Model not found in either location")
        return None, False
        
    def check_required_models(self) -> list:
        """Check for required models and return list of missing ones."""
        missing_models = []
        models_to_copy = []
        
        for model_name, model_info in self.model_config['models'].items():
            if model_info.get('required', False):
                model_path, needs_copying = self.find_model(model_name)
                
                if model_path is None:
                    missing_models.append(model_name)
                elif needs_copying:
                    models_to_copy.append((model_name, model_path))
                    
        # Copy models from source to destination if needed
        if models_to_copy:
            self.copy_models(models_to_copy)
            
        return missing_models
        
    def copy_models(self, models_to_copy: list):
        """Copy models from source to destination directory."""
        for model_name, src_path in models_to_copy:
            try:
                file_ext = '.onnx' if model_name == 'inswapper' else '.pth'
                dest_path = self.dest_models_dir / f"{model_name}{file_ext}"
                
                self.logger.info(f"Copying {model_name} from {src_path} to {dest_path}")
                shutil.copy2(src_path, dest_path)
                
            except Exception as e:
                self.logger.error(f"Error copying {model_name}: {e}")
                
    def verify_model(self, model_path: Path, expected_hash: str) -> bool:
        """Verify model file integrity."""
        print(f"\nVerifying model at: {model_path}")
        print(f"Expected hash: {expected_hash}")
        
        if not model_path.exists():
            print("File does not exist!")
            return False
            
        try:
            with open(model_path, "rb") as f:
                import hashlib
                sha256_hash = hashlib.sha256()
                # Read in larger chunks for efficiency
                for byte_block in iter(lambda: f.read(65536), b""):
                    sha256_hash.update(byte_block)
                actual_hash = sha256_hash.hexdigest()
                print(f"Actual hash:   {actual_hash}")
                print(f"Expected hash: {expected_hash}")
                is_valid = actual_hash == expected_hash
                print(f"Hash match: {is_valid}")
                return is_valid
        except Exception as e:
            print(f"Error verifying model: {e}")
            return False
            
    def handle_missing_models(self, missing_models: list) -> bool:
        """Handle downloading of missing required models."""
        if not missing_models:
            return True
            
        message = (
            "Some required models are missing and need to be downloaded:\n\n" +
            "\n".join(f"• {model}" for model in missing_models) +
            f"\n\nTotal download size: {self.get_total_download_size(missing_models)}\n\n" +
            "Would you like to download them now?"
        )
        
        reply = QMessageBox.question(
            self.main_window,
            "Download Required Models",
            message,
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            return self.download_models(missing_models)
        return False
        
    def get_total_download_size(self, model_names: list) -> str:
        """Calculate total download size for given models."""
        total_bytes = sum(
            self.model_config['models'][name]['size']
            for name in model_names
            if name in self.model_config['models']
        )
        
        # Convert to appropriate unit
        for unit in ['B', 'KB', 'MB', 'GB']:
            if total_bytes < 1024:
                return f"{total_bytes:.1f} {unit}"
            total_bytes /= 1024
        return f"{total_bytes:.1f} GB"
        
    def download_models(self, model_names: list) -> bool:
        """Download specified models with progress tracking."""
        success = True
        for model_name in model_names:
            model_info = self.model_config['models'][model_name]
            
            # Determine correct file extension
            file_ext = '.onnx' if model_name == 'inswapper' else '.pth'
            save_path = self.dest_models_dir / f"{model_name}{file_ext}"
            
            # Create progress dialog
            progress = QProgressDialog(
                f"Downloading {model_name}...\n\n"
                f"Size: {self.get_total_download_size([model_name])}",
                "Cancel",
                0, 100,
                self.main_window
            )
            progress.setWindowModality(Qt.WindowModality.WindowModal)
            
            # Create and configure download worker
            worker = ModelDownloadWorker(model_info['url'], save_path, model_info['sha256'])
            worker.progress.connect(progress.setValue)
            worker.finished.connect(
                lambda ok, err, p=progress: self.handle_download_complete(ok, err, p)
            )
            
            # Start download
            worker.start()
            self.download_workers.append(worker)
            
            # Show progress dialog
            progress.exec()
            
            # Check if download was cancelled or failed
            if progress.wasCanceled() or not save_path.exists():
                success = False
                break
                
        return success
        
    def handle_download_complete(self, success: bool, error: str, progress_dialog):
        """Handle completion of model download."""
        progress_dialog.close()
        
        if not success:
            QMessageBox.critical(
                self.main_window,
                "Download Error",
                f"Failed to download model: {error}"
            )
            
    def get_model_path(self, model_name: str) -> Optional[Path]:
        """Get path to a model file, downloading if necessary."""
        # First try to find existing model
        model_path, needs_copying = self.find_model(model_name)
        
        if model_path is not None:
            if needs_copying:
                # Copy from source to destination
                file_ext = '.onnx' if model_name == 'inswapper' else '.pth'
                dest_path = self.dest_models_dir / f"{model_name}{file_ext}"
                shutil.copy2(model_path, dest_path)
                return dest_path
            return model_path
            
        # If not found, try to download
        if not self.download_models([model_name]):
            return None
            
        # Return path after download
        file_ext = '.onnx' if model_name == 'inswapper' else '.pth'
        return self.dest_models_dir / f"{model_name}{file_ext}"
        
    def cleanup(self):
        """Cleanup resources and cancel any pending downloads."""
        for worker in self.download_workers:
            if worker.isRunning():
                worker.terminate()
                worker.wait()