# src/ui/face_gallery.py

from PyQt6.QtWidgets import QDialog, QVBoxLayout, QGridLayout, QPushButton, QLabel
from PyQt6.QtGui import QPixmap, QImage, QIcon  # Import QIcon
from PyQt6.QtCore import Qt
import cv2

class FaceGallery(QDialog):
    def __init__(self, predefined_faces, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select a Face")
        self.setMinimumSize(800, 600)
        self.predefined_faces = predefined_faces
        self.selected_face = None

        layout = QVBoxLayout(self)
        grid_layout = QGridLayout()
        layout.addLayout(grid_layout)

        row, col = 0, 0
        for name, data in self.predefined_faces.items():
            # Create a button with the face image
            button = QPushButton()
            button.setFixedSize(150, 150)
            pixmap = self.load_face_image(data['image'])
            # button.setIcon(pixmap)
            button.setIcon(self.load_face_image(data['image']))
            button.setIconSize(button.size())
            button.clicked.connect(lambda _, n=name: self.select_face(n))
            grid_layout.addWidget(button, row, col)

            # Label for the face name
            label = QLabel(name)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            grid_layout.addWidget(label, row + 1, col)

            col += 1
            if col > 3:  # 4 columns
                col = 0
                row += 2

    def load_face_image(self, file_path):
        """Load and return a QIcon from the image path."""
        image = cv2.imread(file_path)

        # Verify the image was loaded
        if image is None:
            print(f"Failed to load image: {file_path}")
            return QIcon()

        # Convert BGR (OpenCV) to RGB (Qt)
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Create a QImage from the RGB image
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        q_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)

        # Scale the QImage and convert to QPixmap
        pixmap = QPixmap.fromImage(q_image).scaled(
            150, 150, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation
        )

        # Wrap the QPixmap in a QIcon
        return QIcon(pixmap)

    def select_face(self, name):
        self.selected_face = name
        self.accept()
