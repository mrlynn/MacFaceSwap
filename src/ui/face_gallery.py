# src/ui/face_gallery.py

from PyQt6.QtWidgets import QDialog, QVBoxLayout, QGridLayout, QPushButton, QLabel, QScrollArea, QWidget
from PyQt6.QtGui import QPixmap, QImage, QIcon
from PyQt6.QtCore import Qt
import cv2

class FaceGallery(QDialog):
    def __init__(self, predefined_faces, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select a Face")
        self.setMinimumSize(800, 600)
        self.predefined_faces = predefined_faces
        self.selected_face = None
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        
        # Add scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        layout.addWidget(scroll)
        
        # Create container widget for scroll area
        container = QWidget()
        grid_layout = QGridLayout(container)
        scroll.setWidget(container)

        # Add faces to grid
        row, col = 0, 0
        for name, data in self.predefined_faces.items():
            try:
                # Create frame for each celebrity
                frame = QWidget()
                frame_layout = QVBoxLayout(frame)
                
                # Create image button
                button = QPushButton()
                button.setFixedSize(150, 150)
                
                # Load and set image
                if 'preview_image' in data:
                    image = cv2.imread(data['preview_image'])
                    if image is not None:
                        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                        h, w = image.shape[:2]
                        q_image = QImage(image.data, w, h, w * 3, QImage.Format.Format_RGB888)
                        pixmap = QPixmap.fromImage(q_image)
                        scaled_pixmap = pixmap.scaled(
                            150, 150,
                            Qt.AspectRatioMode.KeepAspectRatio,
                            Qt.TransformationMode.SmoothTransformation
                        )
                        button.setIcon(QIcon(scaled_pixmap))
                        button.setIconSize(button.size())
                
                button.clicked.connect(lambda checked, n=name: self.select_face(n))
                frame_layout.addWidget(button)
                
                # Add name label
                label = QLabel(name)
                label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                frame_layout.addWidget(label)
                
                grid_layout.addWidget(frame, row, col)
                
                # Update grid position
                col += 1
                if col > 3:
                    col = 0
                    row += 1
                    
            except Exception as e:
                print(f"Error adding {name} to gallery: {str(e)}")

    def select_face(self, name):
        """Face selection with debug output"""
        print(f"\nFace Gallery - Selected: {name}")
        self.selected_face = name
        print("Accepting dialog...")
        self.accept()