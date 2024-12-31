# Path: setup_project.py
import os
import sys
from pathlib import Path
import subprocess
import logging
import json

class ProjectSetup:
    """
    Sets up the directory structure and initializes the voice training environment
    """
    def __init__(self, base_dir: str = "deep_live_cam"):
        self.base_dir = Path(base_dir)
        self.logger = logging.getLogger(__name__)
        
        # Define project structure
        self.structure = {
            "src": {
                "voice_modeling.py": None,  # From previous artifact
                "celebrity_voice_trainer.py": None,  # From previous artifact
                "__init__.py": ""
            },
            "celebrity_voices": {
                "raw_samples": {},
                "processed_samples": {},
                "models": {},
                "metadata": {
                    "voice_models_metadata.json": {
                        "models": {},
                        "training_history": {},
                        "version": "1.0"
                    }
                }
            },
            "configs": {
                "logging_config.json": {
                    "version": 1,
                    "disable_existing_loggers": False,
                    "formatters": {
                        "standard": {
                            "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
                        }
                    },
                    "handlers": {
                        "default": {
                            "level": "INFO",
                            "formatter": "standard",
                            "class": "logging.StreamHandler",
                            "stream": "ext://sys.stdout"
                        },
                        "file": {
                            "level": "INFO",
                            "formatter": "standard",
                            "class": "logging.FileHandler",
                            "filename": "voice_training.log",
                            "mode": "a"
                        }
                    },
                    "loggers": {
                        "": {
                            "handlers": ["default", "file"],
                            "level": "INFO",
                            "propagate": True
                        }
                    }
                }
            },
            "tests": {
                "__init__.py": "",
                "test_voice_trainer.py": None
            },
            "examples": {
                "sample_usage.py": None
            },
            "requirements.txt": """
torch>=2.0.0
torchaudio>=2.0.0
numpy>=1.21.0
librosa>=0.9.0
resemblyzer>=0.1.1
transformers>=4.20.0
soundfile>=0.10.3
yt-dlp>=2023.3.4
pydub>=0.25.1
"""
        }

    def create_directory_structure(self):
        """Create the project directory structure"""
        for path, content in self._walk_structure(self.structure):
            full_path = self.base_dir / path
            
            if isinstance(content, dict) and not path.endswith('.json'):
                full_path.mkdir(parents=True, exist_ok=True)
                self.logger.info(f"Created directory: {full_path}")
            else:
                # Create parent directories if they don't exist
                full_path.parent.mkdir(parents=True, exist_ok=True)
                
                # Write file content if provided
                if content is not None:
                    if path.endswith('.json'):
                        with open(full_path, 'w') as f:
                            json.dump(content, f, indent=2)
                    else:
                        with open(full_path, 'w') as f:
                            f.write(content.strip())
                    self.logger.info(f"Created file: {full_path}")

    def _walk_structure(self, structure, parent_path=""):
        """Walk through the directory structure definition"""
        for name, content in structure.items():
            path = Path(parent_path) / name
            yield str(path), content
            
            if isinstance(content, dict):
                yield from self._walk_structure(content, path)

    def setup_virtualenv(self):
        """Set up virtual environment and install requirements"""
        venv_path = self.base_dir / "venv"
        
        try:
            # Create virtual environment
            subprocess.run([sys.executable, "-m", "venv", str(venv_path)], check=True)
            self.logger.info(f"Created virtual environment at {venv_path}")
            
            # Determine pip path
            pip_path = venv_path / "bin" / "pip" if os.name != "nt" else venv_path / "Scripts" / "pip"
            
            # Install requirements
            subprocess.run([str(pip_path), "install", "-r", 
                          str(self.base_dir / "requirements.txt")], check=True)
            self.logger.info("Installed requirements")
            
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Error setting up virtual environment: {e}")
            raise

    def create_example_script(self):
        """Create an example script to demonstrate usage"""
        example_content = '''
# Example usage of the Celebrity Voice Trainer
from src.celebrity_voice_trainer import CelebrityVoiceTrainer

def main():
    # Initialize trainer
    trainer = CelebrityVoiceTrainer()
    
    # Example: Train a celebrity voice model
    celebrity_data = trainer.download_celebrity_samples(
        "Morgan_Freeman",
        [
            "https://www.youtube.com/watch?v=example1",
            "https://www.youtube.com/watch?v=example2"
        ]
    )
    
    # Process the samples
    processed_data = trainer.process_voice_samples(celebrity_data)
    
    # Train the model
    model_path = trainer.train_voice_model(processed_data)
    
    print(f"Successfully trained model: {model_path}")

if __name__ == "__main__":
    main()
'''
        
        example_path = self.base_dir / "examples" / "sample_usage.py"
        with open(example_path, 'w') as f:
            f.write(example_content.strip())
        self.logger.info(f"Created example script at {example_path}")

def setup_project():
    """Main setup function"""
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s'
    )
    
    # Initialize and run setup
    setup = ProjectSetup()
    setup.create_directory_structure()
    setup.setup_virtualenv()
    setup.create_example_script()
    
    print("\nProject setup complete! To get started:")
    print("\n1. Activate the virtual environment:")
    if os.name == "nt":
        print("   .\\venv\\Scripts\\activate")
    else:
        print("   source venv/bin/activate")
    print("\n2. Run the example script:")
    print("   python examples/sample_usage.py")
    print("\n3. Check the 'celebrity_voices' directory for trained models")

if __name__ == "__main__":
    setup_project()
