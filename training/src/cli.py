# training/src/cli.py
import click
import logging
import json
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.logging import RichHandler
from typing import List, Optional, Dict
from celebrity_voice_trainer import CelebrityVoiceTrainer

console = Console()

def setup_logging():
    """Configure logging with rich output"""
    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        handlers=[RichHandler(console=console, rich_tracebacks=True)]
    )

class CelebrityConfig:
    """Handles celebrity configuration loading and validation"""
    def __init__(self, config_path: Path):
        self.config_path = config_path
        self.config = self.load_config()
    
    def load_config(self) -> Dict:
        """Load and validate the configuration file"""
        try:
            with open(self.config_path, 'r') as f:
                config = json.load(f)
            
            # Validate basic structure
            assert 'celebrities' in config, "Missing 'celebrities' key in config"
            assert isinstance(config['celebrities'], list), "'celebrities' must be a list"
            
            # Validate each celebrity entry
            for celeb in config['celebrities']:
                assert 'name' in celeb, "Each celebrity must have a name"
                assert 'urls' in celeb, "Each celebrity must have URLs"
                assert isinstance(celeb['urls'], list), "URLs must be a list"
            
            return config
            
        except (json.JSONDecodeError, AssertionError) as e:
            console.print(f"[bold red]Error in configuration file:[/] {str(e)}")
            raise click.Abort()
        except FileNotFoundError:
            console.print(f"[bold red]Configuration file not found:[/] {self.config_path}")
            raise click.Abort()

@click.group()
def cli():
    """Celebrity Voice Training CLI - Manage voice models for your deepfake app"""
    setup_logging()

@cli.command()
@click.argument('celebrity_name')
@click.argument('urls', nargs=-1)
@click.option('--min-samples', default=10, help='Minimum number of voice samples required')
@click.option('--output-dir', default='celebrity_voices', help='Custom output directory for the model')
def train(celebrity_name: str, urls: List[str], min_samples: int, output_dir: str):
    """Train a new voice model for a celebrity using YouTube URLs"""
    _train_single_celebrity(celebrity_name, urls, min_samples, output_dir)

def _train_single_celebrity(celebrity_name: str, urls: List[str], min_samples: int, output_dir: str):
    """Helper function to train a single celebrity model"""
    trainer = CelebrityVoiceTrainer(base_dir=output_dir)
    
    with console.status(f"[bold green]Training voice model for {celebrity_name}...") as status:
        try:
            # Download samples
            console.print(f"\n📥 Downloading samples from {len(urls)} sources...")
            celebrity_data = trainer.download_celebrity_samples(
                celebrity_name,
                urls,
                min_samples=min_samples
            )
            
            # Process samples
            console.print("🔍 Processing voice samples...")
            processed_data = trainer.process_voice_samples(celebrity_data)
            
            # Train model
            console.print("🚀 Training voice model...")
            model_path = trainer.train_voice_model(processed_data)
            
            console.print(f"\n✨ [bold green]Success![/] Model saved to: {model_path}")
            return True
            
        except Exception as e:
            console.print(f"[bold red]Error training {celebrity_name}:[/] {str(e)}")
            return False

@cli.command()
@click.argument('config_file', type=click.Path(exists=True, path_type=Path))
@click.option('--output-dir', default='celebrity_voices', help='Custom output directory for the models')
def batch_train(config_file: Path, output_dir: str):
    """Train multiple celebrity voice models using a configuration file"""
    config = CelebrityConfig(config_file)
    
    # Create summary table
    table = Table(title="Batch Training Results")
    table.add_column("Celebrity", style="cyan")
    table.add_column("Status", style="green")
    table.add_column("Details")
    
    total = len(config.config['celebrities'])
    successful = 0
    
    for celeb in config.config['celebrities']:
        name = celeb['name']
        urls = celeb['urls']
        min_samples = config.config.get('settings', {}).get('min_samples', 10)
        
        console.print(f"\n[bold cyan]Processing {name}[/]")
        try:
            success = _train_single_celebrity(name, urls, min_samples, output_dir)
            if success:
                successful += 1
                table.add_row(name, "✅ Success", "Model trained successfully")
            else:
                table.add_row(name, "❌ Failed", "Training failed")
        except Exception as e:
            table.add_row(name, "❌ Failed", str(e))
    
    console.print("\n[bold]Batch Training Summary[/]")
    console.print(table)
    console.print(f"\nSuccessfully trained {successful}/{total} models")

@cli.command()
@click.option('--output-dir', default='celebrity_voices', help='Custom output directory for the models')
def list(output_dir: str):
    """List all trained voice models"""
    trainer = CelebrityVoiceTrainer(base_dir=output_dir)
    
    if not trainer.metadata["models"]:
        console.print("[yellow]No voice models found.[/]")
        return
        
    table = Table(title="Available Voice Models")
    table.add_column("Celebrity", style="cyan")
    table.add_column("Samples", justify="right")
    table.add_column("Created", style="green")
    table.add_column("Quality Score", justify="right")
    table.add_column("Path")
    
    for name, info in trainer.metadata["models"].items():
        table.add_row(
            name,
            str(info.get("sample_count", "N/A")),
            info.get("created_at", "Unknown"),
            f"{info.get('quality_score', 0):.2f}",
            info["path"]
        )
    
    console.print(table)

@cli.command()
@click.argument('config_file', type=click.Path(exists=True, path_type=Path))
def validate(config_file: Path):
    """Validate a celebrity configuration file"""
    try:
        config = CelebrityConfig(config_file)
        console.print("[bold green]✓ Configuration file is valid!")
        
        # Show summary
        console.print("\n[bold]Configuration Summary:[/]")
        console.print(f"Total celebrities: {len(config.config['celebrities'])}")
        console.print(f"Total URLs: {sum(len(c['urls']) for c in config.config['celebrities'])}")
        
        if 'settings' in config.config:
            console.print("\n[bold]Global Settings:[/]")
            for key, value in config.config['settings'].items():
                console.print(f"  {key}: {value}")
        
    except Exception as e:
        console.print(f"[bold red]Configuration is invalid:[/] {str(e)}")
        raise click.Abort()

if __name__ == '__main__':
    cli()
