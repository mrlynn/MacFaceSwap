"""
# src/main.py
Main entry point for the MacFaceSwap application.
This module initializes the Qt application and launches the main window.
It handles high DPI scaling settings and sets up the main event loop.
"""

import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from src.ui.main_window import MainWindow  # Updated import

def main():
    """
    Initialize and launch the MacFaceSwap application.
    
    This function:
    1. Configures high DPI display settings for crisp rendering on modern displays
    2. Creates the Qt application instance
    3. Instantiates and displays the main application window
    4. Starts the application event loop
    """
    # Enable high DPI scaling for modern high-resolution displays
    if hasattr(Qt, 'AA_EnableHighDpiScaling'):
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    
    # Initialize the Qt application instance
    app = QApplication(sys.argv)
    
    # Create and display the main application window
    window = MainWindow()
    window.show()
    
    # Start the Qt event loop and wait for user interaction
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
