#!/bin/bash

# Exit on error
set -e

# Configuration
CERTIFICATE_NAME="Apple Development: Michael Lynn (34ABWK95Y5)"
ENTITLEMENTS_PATH="resources/entitlements.plist"

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

python3.10 -m venv venv
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Ensure matplotlib and key dependencies are installed
echo "Installing additional dependencies..."
pip install matplotlib==3.7.1  # Use a specific version known to work
pip install PyQt6 QtAwesome insightface onnxruntime-silicon
pip install pyinstaller

# Verify project structure
echo "Verifying project structure..."
if [ ! -d "images" ]; then
    echo "ERROR: 'images' directory not found in project root!"
    exit 1
fi

# Build the application
echo "Building application..."
pyinstaller MacFaceSwap.spec

# Check the built application structure
echo "Verifying built application structure..."
if [ ! -d "dist/MacFaceSwap.app/Contents/Resources/images" ]; then
    echo "WARNING: 'images' directory not found in built application! Expected at Contents/Resources/images"
fi

# Sign the application
echo "Signing application..."
if [ -f "$ENTITLEMENTS_PATH" ]; then
    echo "✍️  Signing with entitlements..."
    codesign --force --deep --options runtime \
        --entitlements "$ENTITLEMENTS_PATH" \
        --sign "$CERTIFICATE_NAME" \
        "dist/MacFaceSwap.app"
    
    # Verify signature
    echo "✅ Verifying signature..."
    codesign -vvv --deep --strict "dist/MacFaceSwap.app"
else
    echo "⚠️  WARNING: Entitlements file not found at $ENTITLEMENTS_PATH"
    echo "⚠️  Proceeding with basic signing..."
    codesign --force --deep --sign "$CERTIFICATE_NAME" "dist/MacFaceSwap.app"
fi

# Create DMG (optional)
if command -v create-dmg &> /dev/null; then
    echo "💿 Creating DMG..."
    VERSION=$(date +%Y%m%d)  # Use date as version if no version file exists
    DMG_NAME="MacFaceSwap_${VERSION}.dmg"
    
    create-dmg \
        --volname "MacFaceSwap" \
        --window-pos 200 120 \
        --window-size 800 400 \
        --icon-size 100 \
        --icon "MacFaceSwap.app" 200 190 \
        --hide-extension "MacFaceSwap.app" \
        --app-drop-link 600 185 \
        "dist/${DMG_NAME}" \
        "dist/MacFaceSwap.app"
        
    # Sign the DMG as well
    codesign --force --sign "$CERTIFICATE_NAME" "dist/${DMG_NAME}"
else
    echo "ℹ️  Skipping DMG creation (create-dmg not installed)"
fi

echo "✨ Build complete! Check the dist directory for MacFaceSwap.app"