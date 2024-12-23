from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, 
    QLabel, QScrollArea, QFrame, QFileDialog, QMessageBox
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QImage, QPixmap
import cv2
import numpy as np

class FaceMappingWidget(QWidget):
    mapping_updated = pyqtSignal(dict)
    
    def __init__(self, face_processor, parent=None):
        super().__init__(parent)
        self.face_processor = face_processor
        self.face_mappings = {}
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout(self)
        
        # Controls
        controls_layout = QHBoxLayout()
        
        # Add single image button
        self.add_image_btn = QPushButton("Add Source Image")
        self.add_image_btn.clicked.connect(self.add_source_image)
        controls_layout.addWidget(self.add_image_btn)
        
        # Add batch upload button
        self.batch_upload_btn = QPushButton("Batch Upload")
        self.batch_upload_btn.clicked.connect(self.batch_upload_images)
        controls_layout.addWidget(self.batch_upload_btn)
        
        self.clear_btn = QPushButton("Clear All")
        self.clear_btn.clicked.connect(self.clear_mappings)
        controls_layout.addWidget(self.clear_btn)
        
        layout.addLayout(controls_layout)
        
        # Scroll area for mappings
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        self.mappings_container = QWidget()
        self.mappings_layout = QVBoxLayout(self.mappings_container)
        scroll.setWidget(self.mappings_container)
        
        layout.addWidget(scroll)

    def add_source_image(self):
        """Add a single source image"""
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Select Source Face Image",
            "",
            "Image Files (*.png *.jpg *.jpeg)"
        )
        
        if file_name:
            self.process_source_image(file_name)
            
    def batch_upload_images(self):
        """Handle batch upload of multiple source images"""
        file_names, _ = QFileDialog.getOpenFileNames(
            self,
            "Select Source Face Images",
            "",
            "Image Files (*.png *.jpg *.jpeg)"
        )
        
        for file_name in file_names:
            self.process_source_image(file_name)
            
    def process_source_image(self, file_name):
        """Process a source image and add it to mappings"""
        try:
            image = cv2.imread(file_name)
            if image is not None:
                face_data = self.face_processor.analyze_face(image)
                if face_data:
                    mapping_id = len(self.face_mappings)
                    mapping = FaceMappingRow(mapping_id)
                    mapping.deleted.connect(self.remove_mapping)
                    mapping.update_source_preview(face_data['image'])
                    
                    self.mappings_layout.addWidget(mapping)
                    self.face_mappings[mapping_id] = {
                        'source_face': {
                            'face': face_data['face'],
                            'embedding': face_data['embedding']
                        },
                        'image': face_data['image'],
                        'widget': mapping
                    }
                    
                    self.mapping_updated.emit(self.get_mappings())
                else:
                    QMessageBox.warning(self, "Error", f"No face detected in {file_name}")
            else:
                QMessageBox.warning(self, "Error", f"Failed to load {file_name}")
                
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error processing {file_name}: {str(e)}")
            
    def get_mappings(self):
        """Get all active face mappings"""
        return {k: {
            'source_face': v['source_face']
        } for k, v in self.face_mappings.items() if 'source_face' in v}

    def remove_mapping(self, mapping_id):
        if mapping_id in self.face_mappings:
            widget = self.face_mappings[mapping_id]['widget']
            self.mappings_layout.removeWidget(widget)
            widget.deleteLater()
            del self.face_mappings[mapping_id]
            self.mapping_updated.emit(self.get_mappings())
            
    def clear_mappings(self):
        for mapping_id in list(self.face_mappings.keys()):
            self.remove_mapping(mapping_id)

class FaceMappingRow(QFrame):
    deleted = pyqtSignal(int)
    updated = pyqtSignal(int, object)
    
    def __init__(self, mapping_id):
        super().__init__()
        self.mapping_id = mapping_id
        self.face_data = None
        self.init_ui()
        
    def init_ui(self):
        layout = QHBoxLayout(self)
        
        # Source face preview
        self.face_preview = QLabel()
        self.face_preview.setFixedSize(100, 100)
        self.face_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.face_preview)
        
        # Delete button
        self.delete_btn = QPushButton("×")
        self.delete_btn.setFixedSize(30, 30)
        self.delete_btn.clicked.connect(lambda: self.deleted.emit(self.mapping_id))
        layout.addWidget(self.delete_btn)
        
    def update_source_preview(self, face_img):
        if face_img is not None:
            self.face_data = face_img
            pixmap = self.create_preview_pixmap(face_img)
            self.face_preview.setPixmap(pixmap)
            self.updated.emit(self.mapping_id, face_img)
            
    def create_preview_pixmap(self, img):
        if isinstance(img, np.ndarray):
            height, width = img.shape[:2]
            bytes_per_line = 3 * width
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            q_img = QImage(rgb_img.data, width, height, bytes_per_line, QImage.Format.Format_RGB888)
            return QPixmap.fromImage(q_img).scaled(
                100, 100,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
        return None