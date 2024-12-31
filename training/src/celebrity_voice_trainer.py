# Path: src/celebrity_voice_trainer.py
import os
import json
import logging
from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass
from datetime import datetime
import yt_dlp
from pydub import AudioSegment
import torch
import torchaudio
import numpy as np

@dataclass
class VoiceTrainingData:
    celebrity_name: str
    voice_samples: List[Path]
    metadata: Dict
    model_path: Optional[Path] = None
    quality_score: float = 0.0

class CelebrityVoiceTrainer:
    def __init__(self, base_dir: str = "celebrity_voices"):
        """Initialize the voice trainer with a base directory"""
        self.base_dir = Path(base_dir)
        self.raw_samples_dir = self.base_dir / "raw_samples"
        self.processed_dir = self.base_dir / "processed_samples"
        self.models_dir = self.base_dir / "models"
        self.metadata_dir = self.base_dir / "metadata"
        
        # Create directories if they don't exist
        for directory in [self.base_dir, self.raw_samples_dir, 
                         self.processed_dir, self.models_dir, 
                         self.metadata_dir]:
            directory.mkdir(parents=True, exist_ok=True)
        
        self.min_sample_length = 3.0  # seconds
        self.max_sample_length = 15.0  # seconds
        self.target_sample_rate = 22050
        self.logger = logging.getLogger(__name__)
        
        # Initialize metadata
        self.metadata_path = self.metadata_dir / "voice_models_metadata.json"
        self.load_metadata()

    def load_metadata(self):
        """Load or create metadata file"""
        if self.metadata_path.exists():
            with open(self.metadata_path, 'r') as f:
                self.metadata = json.load(f)
        else:
            self.metadata = {
                "models": {},
                "training_history": {},
                "version": "1.0"
            }
            self.save_metadata()

    def save_metadata(self):
        """Save current metadata"""
        with open(self.metadata_path, 'w') as f:
            json.dump(self.metadata, f, indent=2)

    def download_celebrity_samples(self, 
                                 celebrity_name: str,
                                 youtube_urls: List[str],
                                 min_samples: int = 10) -> VoiceTrainingData:
        """Download voice samples from YouTube URLs"""
        celebrity_dir = self.raw_samples_dir / self._sanitize_name(celebrity_name)
        celebrity_dir.mkdir(exist_ok=True)
        
        samples = []
        for url in youtube_urls:
            try:
                # Configure yt-dlp
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'wav',
                    }],
                    'outtmpl': str(celebrity_dir / f'%(id)s.%(ext)s'),
                    'quiet': True,
                    'no_warnings': True
                }
                
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    self.logger.info(f"Downloading audio from {url}")
                    info = ydl.extract_info(url, download=True)
                    samples.append(celebrity_dir / f"{info['id']}.wav")
                    
            except Exception as e:
                self.logger.error(f"Error downloading {url}: {e}")
                continue
        
        if len(samples) < min_samples:
            raise ValueError(f"Only found {len(samples)} samples, minimum required is {min_samples}")
        
        return VoiceTrainingData(
            celebrity_name=celebrity_name,
            voice_samples=samples,
            metadata={"source": "youtube", "sample_count": len(samples)}
        )

    def process_voice_samples(self, training_data: VoiceTrainingData) -> VoiceTrainingData:
        """Process raw voice samples for training"""
        processed_samples = []
        celebrity_processed_dir = self.processed_dir / self._sanitize_name(training_data.celebrity_name)
        celebrity_processed_dir.mkdir(exist_ok=True)
        
        for sample_path in training_data.voice_samples:
            try:
                # Load audio
                audio = AudioSegment.from_wav(str(sample_path))
                
                # Split into chunks
                chunks = self._split_audio(audio)
                
                # Process each chunk
                for i, chunk in enumerate(chunks):
                    processed_path = celebrity_processed_dir / f"chunk_{i}.wav"
                    processed_chunk = self._preprocess_audio(chunk)
                    processed_chunk.export(str(processed_path), format='wav')
                    
                    if self._validate_sample(processed_path):
                        processed_samples.append(processed_path)
                
            except Exception as e:
                self.logger.error(f"Error processing {sample_path}: {e}")
                continue
        
        training_data.voice_samples = processed_samples
        return training_data

    def _split_audio(self, audio: AudioSegment) -> List[AudioSegment]:
        """Split audio into appropriate length chunks"""
        chunks = []
        chunk_length = int(self.max_sample_length * 1000)  # Convert to milliseconds
        
        for i in range(0, len(audio), chunk_length):
            chunk = audio[i:i + chunk_length]
            if len(chunk) >= self.min_sample_length * 1000:
                chunks.append(chunk)
        
        return chunks

    def _preprocess_audio(self, audio: AudioSegment) -> AudioSegment:
        """Apply preprocessing to audio chunk"""
        # Convert to mono
        audio = audio.set_channels(1)
        
        # Set sample rate
        audio = audio.set_frame_rate(self.target_sample_rate)
        
        # Normalize volume
        audio = audio.normalize()
        
        return audio

    def _validate_sample(self, sample_path: Path) -> bool:
        """Validate processed sample quality"""
        try:
            waveform, sample_rate = torchaudio.load(str(sample_path))
            
            # Check duration
            duration = len(waveform[0]) / sample_rate
            if not (self.min_sample_length <= duration <= self.max_sample_length):
                return False
            
            # Check signal-to-noise ratio
            noise_floor = torch.mean(torch.abs(waveform[0][:int(sample_rate * 0.1)]))
            signal_mean = torch.mean(torch.abs(waveform[0]))
            if signal_mean / noise_floor < 3:  # SNR threshold
                return False
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error validating {sample_path}: {e}")
            return False

    def _sanitize_name(self, name: str) -> str:
        """Create a safe filename from a name"""
        return "".join(c for c in name if c.isalnum() or c in (' ', '-', '_')).rstrip()

    def train_voice_model(self, training_data: VoiceTrainingData) -> Path:
        """Train a voice model using processed samples"""
        model_name = self._sanitize_name(training_data.celebrity_name)
        model_path = self.models_dir / f"{model_name}_model.pth"
        
        try:
            # For now, just create a dummy model file
            # This should be replaced with actual model training
            torch.save({
                'metadata': training_data.metadata,
                'created_at': str(datetime.now()),
                'sample_count': len(training_data.voice_samples)
            }, model_path)
            
            # Update metadata
            self.metadata["models"][model_name] = {
                "path": str(model_path),
                "sample_count": len(training_data.voice_samples),
                "created_at": str(datetime.now()),
                "quality_score": training_data.quality_score
            }
            self.save_metadata()
            
            training_data.model_path = model_path
            return model_path
            
        except Exception as e:
            self.logger.error(f"Error training model for {training_data.celebrity_name}: {e}")
            raise