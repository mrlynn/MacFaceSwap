# src/ui/video_window.py

import cv2
import numpy as np
from PyQt6.QtWidgets import QMainWindow, QLabel, QMenuBar, QMenu, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QImage, QPixmap, QAction

class VideoWindow(QMainWindow):
    closed = pyqtSignal()  # Signal emitted when window is closed

    def __init__(self, parent=None):
        super().__init__(parent)
        self.last_size = None  # Store last valid size
        self.init_ui()

    def init_ui(self):
        """Initialize the UI"""
        self.setWindowTitle("Video Feed")
        self.setMinimumSize(640, 480)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)

        # Create video display label
        self.video_label = QLabel()
        self.video_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.video_label.setMinimumSize(640, 480)
        self.video_label.setStyleSheet("""
            QLabel {
                background-color: #222;
                border: 1px solid #666;
            }
        """)
        layout.addWidget(self.video_label)

        # Create menu bar
        menubar = QMenuBar()
        self.setMenuBar(menubar)

        # View menu
        view_menu = QMenu("View", self)
        menubar.addMenu(view_menu)

        # Size presets
        self.add_size_presets(view_menu)

    def add_size_presets(self, menu):
        """Add size preset options to menu"""
        sizes = {
            "640x480": (640, 480),
            "800x600": (800, 600),
            "1280x720": (1280, 720),
            "1920x1080": (1920, 1080)
        }

        size_menu = menu.addMenu("Window Size")
        for name, (width, height) in sizes.items():
            action = QAction(name, self)
            action.triggered.connect(lambda checked, w=width, h=height: self.resize(w, h))
            size_menu.addAction(action)

    def update_frame(self, frame):
        """Update the video frame displayed in the QLabel"""
        if frame is None:
            return
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_frame.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(qt_image)
        self.video_label.setPixmap(pixmap)

    def resizeEvent(self, event):
        """Handle resize events"""
        try:
            super().resizeEvent(event)
            current_pixmap = self.video_label.pixmap()
            if current_pixmap and not current_pixmap.isNull():
                scaled_pixmap = current_pixmap.scaled(
                    self.video_label.size(),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                )
                self.video_label.setPixmap(scaled_pixmap)
                self.last_size = self.size()
            elif self.last_size:
                # Restore last valid size if current resize fails
                self.resize(self.last_size)
                
        except Exception as e:
            print(f"Error handling resize: {str(e)}")

    def closeEvent(self, event):
        """Handle window close event"""
        try:
            self.closed.emit()
            super().closeEvent(event)
        except Exception as e:
            print(f"Error closing video window: {str(e)}")
            event.accept()