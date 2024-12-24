# src/ui/main_window.py
import os
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGroupBox,
    QPushButton, QLabel, QComboBox, QFileDialog, QMessageBox, QSlider,
    QCheckBox
)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QImage, QPixmap
import cv2
import numpy as np
import qtawesome as qta

from src.core.face_processor import FaceProcessor, preprocess_celebrities
from src.core.video_handler import VideoHandler
from src.ui.face_mapping import FaceMappingWidget
from src.core.mapping_loader import load_celebrity_mappings
from src.core.face_processor import preprocess_celebrities

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.face_processor = FaceProcessor()
        self.video_handler = VideoHandler()
        self.source_face = None
        self.video_window = None  # Add this line
        self.init_ui()
        self.setup_styles()
        self.show_face_brackets = False  # Set initial state
        self.face_processor.set_debug_mode(False)  # Set initial debug mode
        self.timer = QTimer()
        self.face_processor.similarity_threshold = 0.5  # Start with 0.5 as default
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(33)
        
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        mapping_file = os.path.join(project_root, "resources", "celebrity_mappings.pkl")
        print(f"Project root: {project_root}")
        print(f"Looking for mapping file at: {mapping_file}")
        
        # Try to load pre-computed mappings
        print("\nAttempting to load pre-computed mappings...")
        self.predefined_faces = load_celebrity_mappings(mapping_file)
        
        if self.predefined_faces is not None:
            print("\nSuccessfully loaded pre-computed mappings:")
            print(f"Number of celebrities: {len(self.predefined_faces)}")
            print("Celebrity names:", list(self.predefined_faces.keys()))
            print("Data structure for first celebrity:")
            first_celeb = next(iter(self.predefined_faces.items()))
            print(f"- Name: {first_celeb[0]}")
            print(f"- Keys in data: {first_celeb[1].keys()}")
        else:
            print("\nFalling back to real-time processing...")
            images_dir = os.path.join(project_root, "images")
            print(f"Processing images from: {images_dir}")
            self.predefined_faces = preprocess_celebrities(self.face_processor, images_dir)
            print(f"Real-time processing complete. Processed {len(self.predefined_faces)} celebrities")
        
        print("\nInitializing UI...")

        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 #f1a8f4, stop: 0.5 #c773ca, stop: 1 #771b7a
                );
            }
            QPushButton {
                background-color: #FF6F61;  /* Vivid Coral */
                color: white;
                border-radius: 8px;
                padding: 10px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #FF856E;  /* Slightly lighter coral for hover */
            }
            QPushButton:pressed {
                background-color: #D95550;  /* Darker coral for pressed state */
            }
            QPushButton:disabled {
                background-color: #B0B0B0;  /* Gray for disabled state */
                color: #FFFFFF;
            }
        """)
    def toggle_face_brackets(self):
        """Toggle the visibility of face brackets in the live video feed."""
        self.show_face_brackets = not self.show_face_brackets
        button_text = "Hide Face Brackets" if self.show_face_brackets else "Show Face Brackets"
        self.face_bracket_button.setText(button_text)
        # Update the debug mode in face processor
        self.face_processor.set_debug_mode(self.show_face_brackets)
        
    def init_ui(self):
        self.setWindowTitle("MacFaceSwap")
        self.resize(1200, 800)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QHBoxLayout(central_widget)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        # Left sidebar
        sidebar = QWidget()
        sidebar.setFixedWidth(320)
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setSpacing(24)

        # Camera controls
        camera_layout = QVBoxLayout()
        camera_layout.setSpacing(12)
        camera_layout.addWidget(QLabel("Camera"))
        
        self.camera_combo = QComboBox()
        self.update_camera_list()
        self.camera_combo.currentIndexChanged.connect(self.change_camera)
        camera_layout.addWidget(self.camera_combo)
        
        self.toggle_button = QPushButton("Start Camera")
        self.toggle_button.setIcon(qta.icon('fa.camera'))  # Font Awesome camera icon
        self.toggle_button.clicked.connect(self.toggle_camera)
        camera_layout.addWidget(self.toggle_button)
        sidebar_layout.addLayout(camera_layout)

        # Add face bracket toggle button
        self.face_bracket_button = QPushButton("Toggle Face Brackets")
        self.face_bracket_button.setIcon(qta.icon('fa.square-o'))  # Add an icon for clarity
        self.face_bracket_button.clicked.connect(self.toggle_face_brackets)
        sidebar_layout.addWidget(self.face_bracket_button)
        # Face controls
        face_layout = QVBoxLayout()
        face_layout.setSpacing(12)
        face_layout.addWidget(QLabel("Face Control"))
        
        self.source_button = QPushButton("Load Source Face")
        self.source_button.setIcon(qta.icon('fa.upload'))  # Upload icon
        self.source_button.clicked.connect(self.load_source_face)
        face_layout.addWidget(self.source_button)
        
        self.clear_button = QPushButton("Clear Face")
        self.clear_button.setIcon(qta.icon('fa.trash'))  # Trash icon
        self.clear_button.setStyleSheet("background-color: #ff3b30; color: white;")
        self.clear_button.clicked.connect(self.clear_source_face)
        face_layout.addWidget(self.clear_button)
        
        sidebar_layout.addLayout(face_layout)

        # Settings
        settings_layout = QVBoxLayout()
        settings_layout.setSpacing(12)
        settings_layout.addWidget(QLabel("Settings"))
        
        # Similarity threshold
        threshold_widget = QWidget()
        threshold_layout = QHBoxLayout(threshold_widget)
        threshold_layout.setContentsMargins(0, 0, 0, 0)
        threshold_layout.setSpacing(8)
        
        threshold_layout.addWidget(QLabel("Similarity:"))
        self.threshold_slider = QSlider(Qt.Orientation.Horizontal)
        self.threshold_slider.setRange(0, 100)
        initial_threshold = 20  # 0.2 as default
        self.threshold_slider.setValue(initial_threshold)
        print(f"Initial similarity threshold set to: {initial_threshold/100.0:.2f}")
        self.threshold_slider.valueChanged.connect(self.update_threshold)
        threshold_layout.addWidget(self.threshold_slider)
        
        self.threshold_label = QLabel(f"{self.face_processor.similarity_threshold:.2f}")
        self.threshold_label.setFixedWidth(40)
        threshold_layout.addWidget(self.threshold_label)
        
        settings_layout.addWidget(threshold_widget)
        sidebar_layout.addLayout(settings_layout)

        # Quality controls
        quality_group = QGroupBox("Quality Settings")
        quality_layout = QVBoxLayout()

        # Enhancement toggle
        self.enhancement_toggle = QCheckBox("Enable Face Enhancement")
        self.enhancement_toggle.setChecked(True)
        self.enhancement_toggle.stateChanged.connect(self.toggle_enhancement)
        quality_layout.addWidget(self.enhancement_toggle)

        # Enhancement strength slider
        strength_layout = QHBoxLayout()
        strength_layout.addWidget(QLabel("Enhancement:"))
        self.enhancement_slider = QSlider(Qt.Orientation.Horizontal)
        self.enhancement_slider.setRange(0, 100)
        self.enhancement_slider.setValue(50)
        self.enhancement_slider.valueChanged.connect(self.update_enhancement)
        strength_layout.addWidget(self.enhancement_slider)
        quality_layout.addLayout(strength_layout)

        quality_group.setLayout(quality_layout)
        sidebar_layout.addWidget(quality_group)

        sidebar_layout.addStretch()

        # Source preview
        preview_layout = QVBoxLayout()
        preview_layout.addWidget(QLabel("Source Face Preview"))
        self.source_preview = QLabel()
        self.source_preview.setFixedSize(280, 280)
        self.source_preview.setStyleSheet("""
            background-color: #f5f5f7;
            border-radius: 8px;
        """)
        self.source_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        preview_layout.addWidget(self.source_preview)
        sidebar_layout.addLayout(preview_layout)

        layout.addWidget(sidebar)
        
        # popout_layout = QHBoxLayout()
        # self.popout_button = QPushButton("Popout Video")
        # self.popout_button.clicked.connect(self.toggle_video_window)
        # popout_layout.addWidget(self.popout_button)
        # popout_layout.addStretch()
        # layout.addLayout(popout_layout)

        # Video area
        video_container = QWidget()
        video_layout = QVBoxLayout(video_container)
        video_layout.setContentsMargins(0, 0, 0, 0)
        
        # Add a horizontal layout for the "Popout Video" button
        video_controls_layout = QHBoxLayout()
        video_controls_layout.setContentsMargins(0, 0, 0, 0)
        video_controls_layout.addStretch()

        self.popout_button = QPushButton("Popout Video")
        self.popout_button.setIcon(qta.icon('fa.window-maximize'))  # Popout icon
        self.popout_button.clicked.connect(self.toggle_video_window)
        layout.addWidget(self.popout_button)
        video_layout.addLayout(video_controls_layout)

        video_controls_layout.addWidget(self.popout_button)
        self.video_label = QLabel()
        self.video_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.video_label.setStyleSheet("background-color: #1d1d1f; border-radius: 8px;")
        video_layout.addWidget(self.video_label)
        
        layout.addWidget(video_container)
        layout.setStretch(1, 1)
        
        self.gallery_button = QPushButton("Open Face Gallery")
        self.gallery_button.setIcon(qta.icon('fa.image'))  # Single image icon
        self.gallery_button.clicked.connect(self.open_face_gallery)
        sidebar_layout.addWidget(self.gallery_button)

    def open_face_gallery(self):
        """Open the gallery pop-out window with debug output."""
        try:
            from src.ui.face_gallery import FaceGallery
            
            print("\nOpening Face Gallery:")
            print(f"Number of predefined faces: {len(self.predefined_faces)}")
            print("Available celebrities:", list(self.predefined_faces.keys()))
            
            if not self.predefined_faces:
                print("No predefined faces available")
                QMessageBox.warning(self, "Error", "No predefined faces available")
                return
            
            gallery = FaceGallery(self.predefined_faces, self)
            
            if gallery.exec():  # Modal dialog
                selected_face = gallery.selected_face
                print(f"\nSelected celebrity: {selected_face}")
                
                if selected_face and selected_face in self.predefined_faces:
                    face_data = self.predefined_faces[selected_face]
                    print("\nPre-processed face data:")
                    print(f"Keys available: {list(face_data.keys())}")
                    
                    if 'preview_image' in face_data:
                        image = cv2.imread(face_data['preview_image'])
                        if image is not None:
                            print("Successfully loaded preview image")
                            
                            # Create face mapping
                            self.source_face = {
                                'face': face_data.get('face_dict', {}),
                                'embedding': np.array(face_data['embedding']) if 'embedding' in face_data else None,
                                'all_embeddings': [np.array(emb) for emb in face_data['all_embeddings']] if 'all_embeddings' in face_data else None,
                                'image': image
                            }
                            
                            # Update the UI and processor
                            self.update_preview(image)
                            
                            print("\nSetting up face processor:")
                            self.set_frame_processor()
                            print("Face processor setup completed")
                        else:
                            print(f"Failed to load image: {face_data['preview_image']}")
                    else:
                        print("No preview image path in face data")
                else:
                    print(f"Invalid selection or face not found: {selected_face}")
        except Exception as e:
            print(f"Error in open_face_gallery: {str(e)}")
            import traceback
            traceback.print_exc()

    def setup_styles(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f7;
            }
            QPushButton {
                background-color: #0071e3;
                color: white;
                border-radius: 6px;
                padding: 8px 16px;
                font-weight: 500;
                border: none;
                min-height: 32px;
            }
            QPushButton:hover {
                background-color: #0077ED;
            }
            QPushButton:pressed {
                background-color: #005BBF;
            }
            QPushButton:disabled {
                background-color: #999999;
            }
            QLabel {
                color: #1d1d1f;
                font-size: 13px;
                padding: 4px;
            }
            QComboBox {
                padding: 8px;
                border-radius: 6px;
                border: 1px solid #d2d2d7;
                background: white;
                min-height: 32px;
            }
            QSlider {
                height: 32px;
            }
            QSlider::groove:horizontal {
                height: 4px;
                background: #d2d2d7;
                border-radius: 2px;
            }
            QSlider::handle:horizontal {
                background: #0071e3;
                width: 18px;
                height: 18px;
                margin: -7px 0;
                border-radius: 9px;
            }
            QGroupBox {
                margin-top: 16px;
            }
        """)

    def load_source_face(self):
        """Load and analyze a source face image from file."""
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Select Source Face Image", "", "Image Files (*.png *.jpg *.jpeg)"
        )
        if file_name:
            print(f"Loading source face from: {file_name}")
            image = cv2.imread(file_name)
            if image is not None:
                self.set_source_face(image)
            else:
                QMessageBox.warning(self, "Error", "Failed to load image")


    def update_preview(self, image):
        """Update source face preview"""
        h, w = image.shape[:2]
        bytes_per_line = 3 * w
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        q_image = QImage(
            rgb_image.data,
            w, h,
            bytes_per_line,
            QImage.Format.Format_RGB888
        )
        
        pixmap = QPixmap.fromImage(q_image)
        scaled_pixmap = pixmap.scaled(
            128, 128,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.source_preview.setPixmap(scaled_pixmap)

    def update_camera_list(self):
        """Update the list of available cameras"""
        self.camera_combo.clear()
        cameras = self.video_handler.get_camera_list()
        
        if not cameras:
            self.camera_combo.addItem("No cameras found")
            print("No cameras were detected")
            return
            
        print(f"Adding {len(cameras)} cameras to combo box")
        for camera in cameras:
            self.camera_combo.addItem(camera['name'], camera['id'])
            print(f"Added camera: {camera['name']}")

    def change_camera(self, index):
        """Change the active camera"""
        if index >= 0:
            camera_id = self.camera_combo.currentData()
            if camera_id is not None:
                print(f"Changing to camera {camera_id}")
                self.video_handler.stop_camera()
                if self.video_handler.start_camera(camera_id):
                    print(f"Successfully started camera {camera_id}")
                else:
                    print(f"Failed to start camera {camera_id}")

    def toggle_camera(self):
        """Toggle camera on/off"""
        if self.video_handler.is_running:
            print("Stopping camera")
            self.video_handler.stop_camera()
            self.toggle_button.setText("Start Camera")
        else:
            camera_id = self.camera_combo.currentData()
            if camera_id is not None:
                print(f"Starting camera {camera_id}")
                if self.video_handler.start_camera(camera_id):
                    self.toggle_button.setText("Stop Camera")
                    # Re-enable face processor if we have a source face
                    if self.source_face:
                        print("Reconnecting face processor")
                        self.set_frame_processor()
                    print("Camera started successfully")
                else:
                    print("Failed to start camera")
                    
    def process_frame(self, frame):
        """Process frame with face swapping and route to appropriate display"""
        if frame is None:
            return None
            
        try:
            # Apply face swapping if processor is available
            if self.face_processor and hasattr(self.face_processor, 'process_frame'):
                processed_frame = self.face_processor.process_frame(frame)
                if processed_frame is not None:
                    frame = processed_frame

            # Clear face brackets if the toggle is off
            if not self.show_face_brackets:
                frame = self.clear_brackets(frame)
                
            # Update both main window and popout window if it exists
            if self.video_window:
                self.video_window.update_frame(frame)
                
            return frame
            
        except Exception as e:
            print(f"Error processing frame: {str(e)}")
            return frame

    def update_frame(self):
        """Update the video frame in the main window"""
        frame = self.video_handler.get_latest_frame()
        if frame is None:
            return
            
        # Process the frame
        processed_frame = self.process_frame(frame)
        if processed_frame is None:
            return
            
        # Convert and display the frame
        rgb_frame = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)
        h, w = processed_frame.shape[:2]
        bytes_per_line = 3 * w
        qt_image = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(qt_image).scaled(
            640, 480, 
            Qt.AspectRatioMode.KeepAspectRatio, 
            Qt.TransformationMode.SmoothTransformation
        )
        self.video_label.setPixmap(pixmap)
        
    def clear_brackets(self, frame):
        """Clear face brackets from the frame."""
        # If your face processor adds face brackets, modify this function to remove them.
        return frame

    def closeEvent(self, event):
        """Handle application closing"""
        try:
            if self.video_window:
                self.video_window.close()
            self.video_handler.stop_camera()
            event.accept()
        except Exception as e:
            print(f"Error closing application: {str(e)}")
            event.accept()

    def clear_source_face(self):
        """Clear the current source face"""
        self.source_face = None
        self.source_preview.clear()
        self.set_frame_processor()
        print("Source face cleared")

    def set_frame_processor(self):
        """Set up frame processing based on current source face."""
        if self.source_face:
            print("\nSetting up frame processor:")
            print("Source face information:")
            for key, value in self.source_face.items():
                if key == 'image':
                    print(f"- Has image: {value is not None}")
                elif isinstance(value, np.ndarray):
                    print(f"- {key} shape: {value.shape}")
                elif isinstance(value, dict):
                    print(f"- {key} keys: {list(value.keys())}")
                elif isinstance(value, list):
                    print(f"- {key} length: {len(value)}")
                else:
                    print(f"- {key}: {type(value)}")
            
            # Create mapping with detailed debug output
            print("\nCreating face mapping...")
            mapping_data = {
                'default': {
                    'source_face': {
                        'face_dict': self.source_face.get('face', {}),
                        'embedding': self.source_face['embedding'].tolist() if isinstance(self.source_face.get('embedding'), np.ndarray) else None,
                        'all_embeddings': [emb.tolist() for emb in self.source_face['all_embeddings']] if self.source_face.get('all_embeddings') else None
                    }
                }
            }
            
            print("Mapping data created:")
            print(f"Keys in mapping: {list(mapping_data['default']['source_face'].keys())}")
            
            print("\nSetting face mappings in processor...")
            self.face_processor.set_face_mappings(mapping_data)
            
            # Connect video processing
            print("Connecting video processor...")
            self.video_handler.set_processing_callback(self.face_processor.process_frame)
            print("Frame processor setup complete")
        else:
            print("No source face available - clearing processor")
            self.video_handler.set_processing_callback(None)

    def toggle_debug(self, checked):
        """Toggle debug visualization"""
        self.debug_toggle.setText("Debug: On" if checked else "Debug: Off")
        if hasattr(self, 'face_processor'):
            self.face_processor.set_debug_mode(checked)

    def update_threshold(self, value):
        """Update similarity threshold"""
        threshold = value / 100.0
        print(f"\nUpdating similarity threshold:")
        print(f"Slider value: {value}")
        print(f"Calculated threshold: {threshold:.4f}")
        self.face_processor.similarity_threshold = threshold
        self.threshold_label.setText(f"{threshold:.2f}")

    def toggle_preprocessing(self, checked):
        """Toggle preprocessing of face embeddings"""
        self.face_processor.enable_preprocessing = checked
        self.preprocess_toggle.setText("Preprocessing: On" if checked else "Preprocessing: Off")

    def update_frame_skip(self, value):
        """Update frame processing rate"""
        try:
            n_frames = int(value)
            self.video_handler.set_frame_processing_rate(n_frames)
        except ValueError:
            pass
        
    def update_fps_display(self):
        """Update FPS display"""
        if hasattr(self.video_handler, 'fps_stats'):
            fps = self.video_handler.fps_stats['fps']
            self.fps_label.setText(f"FPS: {fps:.1f}")

    def toggle_fps_display(self, checked):
        """Toggle FPS counter visibility"""
        self.show_fps = checked
        self.fps_toggle.setText("FPS: Visible" if checked else "FPS: Hidden")
        self.video_handler.show_fps = checked
        print(f"FPS display {'enabled' if checked else 'disabled'}")

    def toggle_detection_display(self, checked):
        """Toggle face detection box visibility"""
        self.show_detection = checked
        self.detection_toggle.setText("Detection Box: Visible" if checked else "Detection Box: Hidden")
        if hasattr(self, 'face_processor'):
            self.face_processor.debug_mode = checked
        print(f"Detection box display {'enabled' if checked else 'disabled'}")

    def toggle_video_window(self):
        """Toggle the video window while maintaining face swapping"""
        try:
            if self.video_window is None:
                from src.ui.video_window import VideoWindow
                self.video_window = VideoWindow(self)
                self.video_window.closed.connect(self.on_video_window_closed)
                self.video_window.show()
                self.popout_button.setText("Close Video Window")
                
                # Update video handler callback to process frames
                self.video_handler.set_processing_callback(self.process_frame)
            else:
                self.video_window.close()
                self.video_window = None
                self.popout_button.setText("Popout Video")
                
                # Reset video handler callback
                self.video_handler.set_processing_callback(self.process_frame)
        except Exception as e:
            print(f"Error toggling video window: {str(e)}")

    def on_video_window_closed(self):
        """Handle video window being closed"""
        try:
            self.video_window = None
            self.popout_button.setText("Popout Video")
            if hasattr(self, 'video_label'):
                self.video_label.show()
        except Exception as e:
            print(f"Error handling video window close: {str(e)}")

    def update_face_mappings(self, mappings):
        """Update face processor with new mappings"""
        self.face_processor.set_face_mappings(mappings)
        if self.video_handler.is_running:
            self.set_frame_processor()

    def create_group_box(self, title):
        group = QGroupBox(title)
        group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: none;
                margin-top: 1ex;
            }
            QGroupBox::title {
                color: #1d1d1f;
            }
        """)
        return group
    
    def set_source_face(self, image, data=None):
        """Set the source face and update the UI with debug output."""
        print("\nSetting source face:")
        if image is None:
            print("Error: No image provided")
            QMessageBox.warning(self, "Error", "No valid image provided")
            return

        try:
            if data is None:
                print("Processing new image (no pre-existing data)")
                face_data = self.face_processor.analyze_face(image)
                if not face_data:
                    print("No face detected in image")
                    QMessageBox.warning(self, "Error", "No face detected in the image")
                    return
                    
                self.source_face = {
                    'face': face_data['face'],
                    'embedding': face_data['embedding'],
                    'image': face_data['image']
                }
            else:
                print("Using pre-processed face data")
                print("Data keys:", list(data.keys()))
                self.source_face = {
                    'face': data.get('face_dict', {}),  # Store the face dictionary
                    'embedding': np.array(data['embedding']) if 'embedding' in data else None,
                    'image': None  # Will be set from preview image
                }
                
                if 'preview_image' in data:
                    self.source_face['image'] = cv2.imread(data['preview_image'])
                    
            if self.source_face['image'] is not None:
                print("Updating preview image")
                self.update_preview(self.source_face['image'])
                
            self.set_frame_processor()
            print("Source face set successfully")
            
        except Exception as e:
            print(f"Error setting source face: {str(e)}")
            import traceback
            traceback.print_exc()
            QMessageBox.warning(self, "Error", f"Error setting source face: {str(e)}")

    def toggle_enhancement(self, state):
        """Toggle face enhancement"""
        self.face_processor.use_face_enhancement = bool(state)

    def update_enhancement(self, value):
        """Update enhancement strength"""
        self.face_processor.enhancement_level = value / 50.0  # Scale to 0-2 range
