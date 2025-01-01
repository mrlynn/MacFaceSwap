#!/bin/bash

# Create DMG after building app
if [ -d "dist/MacFaceSwap.app" ]; then
    echo "Creating DMG..."
    
    # Install create-dmg if not already installed
    if ! command -v create-dmg &> /dev/null; then
        brew install create-dmg
    fi
    
    # Create DMG
    create-dmg \
        --volname "MacFaceSwap" \
        --volicon "resources/icon.icns" \
        --window-pos 200 120 \
        --window-size 800 400 \
        --icon-size 100 \
        --icon "MacFaceSwap.app" 200 190 \
        --hide-extension "MacFaceSwap.app" \
        --app-drop-link 600 185 \
        "dist/MacFaceSwap.dmg" \
        "dist/MacFaceSwap.app"
fi