from PyQt6.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPixmap
import os

class TutorialOverlay(QDialog):
    tutorial_completed = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.WindowType.Dialog)
        self.setModal(True)
        self.current_step = 0
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

        self.images = [os.path.join(base_dir, "resources", f"step-{i}.png") for i in range(1, 6)]
        print(f"Loading images from: {base_dir}")
        
        self.steps = [
            {'message': 'Welcome to MacFaceSwap! First, go to the Camera tab and select your camera device from the dropdown menu at the top.'},
            {'message': 'Once your camera is selected, click the "Start Camera" button in the video window to begin your camera feed.'},
            {'message': 'Next, click the Face tab. Here you can either upload your own face image or use our celebrity gallery.'},
            {'message': 'For quick testing, click "Open Face Gallery" to choose from our pre-configured celebrity faces.'},
            {'message': 'Finally, in the Settings tab, enable Face Enhancement and adjust the slider for better results.'}
        ]
        
        self.setup_ui()
        self.update_step()

    def setup_ui(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(40, 40, 40, 40)
        self.layout.setSpacing(20)

        title = QLabel("MacFaceSwap Tutorial")
        title.setStyleSheet("color: #333; font-size: 24px; font-weight: bold;")
        self.step_counter = QLabel()
        self.step_counter.setStyleSheet("color: #666; font-size: 14px;")

        container = QWidget()
        container.setStyleSheet("""
            QWidget {
                background-color: white; 
                border-radius: 15px;
                padding: 20px;
            }
            QLabel {
                background: transparent;
            }
        """)
        container_layout = QVBoxLayout(container)

        self.image_label = QLabel()
        self.image_label.setFixedSize(800, 500)
        self.image_label.setScaledContents(True)
        self.image_label.setStyleSheet("background-color: #f5f5f5; border-radius: 8px;")

        self.message_label = QLabel()
        self.message_label.setWordWrap(True)
        self.message_label.setStyleSheet("font-size: 16px; padding: 20px; color: #333;")

        container_layout.addWidget(self.image_label)
        container_layout.addWidget(self.message_label)

        button_layout = QHBoxLayout()
        self.prev_button = QPushButton("Previous")
        self.next_button = QPushButton("Next")
        
        for btn in [self.prev_button, self.next_button]:
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #0071e3;
                    color: white;
                    border: none;
                    padding: 12px 24px;
                    border-radius: 8px;
                    font-size: 15px;
                    font-weight: 500;
                }
                QPushButton:hover {
                    background-color: #0077ED;
                }
            """)
        
        button_layout.addWidget(self.prev_button)
        button_layout.addWidget(self.next_button)

        self.prev_button.clicked.connect(self.prev_step)
        self.next_button.clicked.connect(self.next_step)

        self.layout.addWidget(title)
        self.layout.addWidget(self.step_counter)
        self.layout.addWidget(container)
        self.layout.addLayout(button_layout)
        self.setMinimumSize(900, 700)

    def update_step(self):
        try:
            image_path = self.images[self.current_step]
            print(f"Loading image from: {image_path}")
            pixmap = QPixmap(image_path)
            if pixmap.isNull():
                print(f"Failed to load image - pixmap is null")
            else:
                print(f"Successfully loaded image: {pixmap.width()}x{pixmap.height()}")
                self.image_label.setPixmap(pixmap)
        except Exception as e:
            print(f"Error loading image: {str(e)}")
            self.image_label.setText("Failed to load image")
            
    def next_step(self):
        if self.current_step < len(self.steps) - 1:
            self.current_step += 1
            self.update_step()
        else:
            self.accept()

    def prev_step(self):
        if self.current_step > 0:
            self.current_step -= 1
            self.update_step()