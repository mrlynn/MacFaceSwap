#!/bin/bash

# Exit on error
set -e

APP_NAME="MacFaceSwap"
DMG_NAME="${APP_NAME}_Installer"
APP_PATH="dist/${APP_NAME}.app"
DMG_PATH="dist/${DMG_NAME}.dmg"
VOL_NAME="${APP_NAME} Installer"

# Check if create-dmg is installed
if ! command -v create-dmg &> /dev/null; then
    echo "Installing create-dmg..."
    brew install create-dmg
fi

# Remove any existing DMG
rm -f "${DMG_PATH}"

# Create DMG
create-dmg \
    --volname "${VOL_NAME}" \
    --window-pos 200 120 \
    --window-size 800 400 \
    --icon-size 100 \
    --icon "${APP_NAME}.app" 200 190 \
    --hide-extension "${APP_NAME}.app" \
    --app-drop-link 600 185 \
    "${DMG_PATH}" \
    "${APP_PATH}"

# Sign the DMG (uncomment when ready for distribution)
# codesign --sign "Developer ID Application: Your Name (TEAMID)" "${DMG_PATH}"

echo "DMG created at: ${DMG_PATH}"
