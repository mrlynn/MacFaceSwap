#!/bin/bash
set -e

APP_NAME="MacFaceSwap"
DMG_PATH="dist/${APP_NAME}_Installer.dmg"
APP_PATH="dist/${APP_NAME}.app"

rm -f "${DMG_PATH}"

create-dmg \
    --volname "${APP_NAME}" \
    --background "resources/installer_background.png" \
    --window-pos 200 120 \
    --window-size 800 400 \
    --icon-size 100 \
    --icon "${APP_NAME}.app" 200 190 \
    --hide-extension "${APP_NAME}.app" \
    --app-drop-link 600 185 \
    --no-internet-enable \
    --format UDZO \
    "${DMG_PATH}" \
    "${APP_PATH}"