#!/bin/bash

# Exit on error
set -e

echo "Starting clean build process..."

# Ensure we're in the project root
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_ROOT"

# Clean previous builds and cache
echo "Cleaning previous builds..."
rm -rf build dist __pycache__ *.pyc
find . -type d -name "__pycache__" -exec rm -r {} +

# Ensure clean virtual environment
echo "Setting up virtual environment..."
if [ -d "venv" ]; then
    rm -rf venv
fi

python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Ensure matplotlib and key dependencies are installed
echo "Installing additional dependencies..."
pip install matplotlib==3.7.1  # Use a specific version known to work
pip install PyQt6 QtAwesome insightface onnxruntime-silicon

# build.sh addition (before pyinstaller command)
echo "Verifying project structure..."
if [ ! -d "images" ]; then
    echo "ERROR: 'images' directory not found!"
    exit 1
fi

# Build the application
echo "Building application..."
pyinstaller MacFaceSwap.spec

# After pyinstaller command
echo "Verifying built application structure..."
if [ ! -d "dist/MacFaceSwap.app/Contents/Resources/images" ]; then
    echo "WARNING: 'images' directory not found in built application!"
fi

echo "Build complete! Check the dist directory for MacFaceSwap.app"