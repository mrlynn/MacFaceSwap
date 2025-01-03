"""
# src/ui/main_window.py
Main window implementation for the MacFaceSwap application.

This module implements the primary user interface for MacFaceSwap, providing:
- Camera input selection and control
- Face selection and management
- Real-time face swapping visualization
- Video recording capabilities
- Settings management
- Tutorial system

The MainWindow class serves as the central hub for user interaction and coordinates
between the UI components and the core face swapping functionality.
"""

import os
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGroupBox,
    QPushButton, QLabel, QComboBox, QFileDialog, QMessageBox, QSlider,
    QCheckBox, QTabWidget, QDialog, QTextBrowser, QMenu
)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QImage, QPixmap, QAction  # Here's where QAction belongs
import cv2
import numpy as np
import qtawesome as qta
import sounddevice as sd
from src.core.face_processor import FaceProcessor, preprocess_celebrities
from src.core.video_handler import VideoHandler
from src.ui.face_mapping import FaceMappingWidget
from src.core.mapping_loader import load_celebrity_mappings
from src.core.face_processor import preprocess_celebrities
from src.core.video_recorder import VideoRecorder
from src.ui.watermark import VideoWatermark
from src.ui.camera_settings import CameraSettings
from src.ui.tutorial_overlay import TutorialOverlay
from src.core.model_manager import MacFaceSwapModelManager
class MainWindow(QMainWindow):
    """
    Main application window for MacFaceSwap.
    
    This class manages the primary user interface and coordinates between:
    - Video capture and display
    - Face detection and swapping
    - User interface controls
    - Settings management
    - Recording functionality
    
    The window is organized into:
    - A left sidebar with tabbed controls (Camera, Face, Settings)
    - A main video display area
    - Top menu bar with help and tutorial options
    """
    
    def __init__(self):
        super().__init__()
        
        self.model_manager = MacFaceSwapModelManager(self)
        if not self.model_manager.initialize():
            QMessageBox.critical(
                self,
                "Initialization Error",
                "Failed to initialize required models. The application may not function correctly."
            )        
        
        self.face_processor = FaceProcessor()
        self.video_handler = VideoHandler()
        self.source_face = None
        self.video_window = None  # Add this line
        self.init_ui()
        self.setup_styles()
        self.setup_tutorial()  # Add this line

        self.show_face_brackets = False  # Set initial state
        self.face_processor.set_debug_mode(False)  # Set initial debug mode
        self.timer = QTimer()
        self.face_processor.similarity_threshold = 0.0  # Start with 0.5 as default
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(33)
        self.video_recorder = VideoRecorder()

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
        
    
    def setup_tutorial(self):
        """
        Initialize the tutorial system with step-by-step guidance.
        
        Sets up a sequence of tutorial steps that guide new users through:
        - Camera selection and setup
        - Face selection process
        - Settings configuration
        - Basic operations
        """
        try:
            print("Setting up tutorial...")
            self.tutorial_overlay = None
            self.steps = [
                {
                    'message': 'Welcome to MacFaceSwap! First, go to the Camera tab and select your camera device from the dropdown menu at the top.',
                    'highlight': True
                },
                {
                    'message': 'Once your camera is selected, click the "Start Camera" button in the video window to begin your camera feed.',
                    'highlight': True
                },
                {
                    'message': 'Next, click the Face tab. Here you can either upload your own face image or use our celebrity gallery.',
                    'highlight': True
                },
                {
                    'message': 'For quick testing, click "Open Face Gallery" to choose from our pre-configured celebrity faces.',
                    'highlight': True
                },
                {
                    'message': 'Finally, in the Settings tab, enable Face Enhancement and adjust the slider for better results. You can also toggle face brackets to see the detection boxes.',
                    'highlight': True
                }
            ]
            self.current_tutorial_step = 0
            print("Tutorial setup complete")
        except Exception as e:
            print(f"Error in setup_tutorial: {e}")
            
    
    def start_tutorial(self):
        """
        Launch the interactive tutorial overlay.
        
        Creates and displays the tutorial overlay window that guides users
        through the application's features step by step.
        """
        try:
            print("Starting tutorial")
            self.tutorial_overlay = TutorialOverlay(self)
            self.tutorial_overlay.tutorial_completed.connect(self.on_tutorial_completed)
            self.tutorial_overlay.show()
        except Exception as e:
            print(f"Error in start_tutorial: {e}")
        
    def show_tutorial_step(self):
        print("Show tutorial step called...")
        if self.current_tutorial_step >= len(self.tutorial_steps):
            print("Tutorial complete")
            #self.tutorial_overlay.hide()
            return
            
        step = self.tutorial_steps[self.current_tutorial_step]
        print(f"Current step: {step}")
        
        target_widget = getattr(self, step['target'])
        print(f"Target widget: {target_widget}")
        self.tutorial_overlay.setGeometry(self.geometry())

        # Position overlay and show
        self.tutorial_overlay.resize(self.size())
        self.tutorial_overlay.move(self.mapToGlobal(self.rect().topLeft()))
        self.tutorial_overlay.raise_()
        self.tutorial_overlay.set_target(target_widget)
        self.tutorial_overlay.set_message(step['message'])        
        # Update content
        self.tutorial_overlay.set_target(target_widget)
        self.tutorial_overlay.set_message(step['message'])
        print("Tutorial step updated")
            
    def next_tutorial_step(self):
        self.current_tutorial_step += 1
        self.show_tutorial_step()

    def on_tutorial_completed(self):
        self.tutorial_overlay.hide()
        QMessageBox.information(self, "Tutorial Complete", 
            "You're all set! Start swapping faces by selecting a source face and enabling the camera.")
        
    # Update toggle_recording method
    def toggle_recording(self):
        """
        Toggle video recording state.
        
        Starts or stops video recording based on current state:
        - When starting: Initializes video writer with current frame dimensions
        - When stopping: Finalizes video file and saves to Downloads folder
        Updates UI elements to reflect recording status.
        """
        if not self.video_recorder.is_recording:
            frame = self.video_handler.get_latest_frame()
            if frame is not None:
                h, w = frame.shape[:2]
                filepath = self.video_recorder.start_recording((w, h))
                self.record_button.setText("Stop Recording")
                self.record_button.setIcon(qta.icon('fa.stop', color='red'))
                self.recording_status.setText("Recording...")
                self.recording_status.setStyleSheet("color: red;")
        else:
            filepath = self.video_recorder.stop_recording()
            self.record_button.setText("Start Recording")
            self.record_button.setIcon(qta.icon('fa.circle', color='red'))
            if filepath:
                self.recording_status.setText(f"Saved to Downloads folder")
                QMessageBox.information(self, "Recording Saved", 
                    f"Your recording has been saved to:\n{filepath}")
            self.recording_status.setStyleSheet("color: green;")
        
    def toggle_face_brackets(self):
        """
        Toggle the visibility of face detection boxes in the live video feed.
        
        Controls whether face detection boundaries are shown on the video feed.
        Updates both the UI button text and the face processor's debug mode.
        """
        self.show_face_brackets = not self.show_face_brackets
        button_text = "Hide Face Brackets" if self.show_face_brackets else "Show Face Brackets"
        self.face_bracket_button.setText(button_text)
        # Update the debug mode in face processor
        self.face_processor.set_debug_mode(self.show_face_brackets)
                
    def init_ui(self):
        """
        Initialize and configure all UI elements.
        
        Sets up the main window layout including:
        - Window title and size
        - Left sidebar with tabbed interface (Camera, Face, Settings)
        - Main video display area
        - Video controls (Start/Stop, Record, Popout)
        - Menu bar with Help options
        - Status indicators
        """
        self.setWindowTitle("MacFaceSwap")
        self.resize(1200, 800)  # Maintaining original size

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        # Create left sidebar with tabs
        sidebar = QWidget()
        sidebar.setFixedWidth(320)
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setSpacing(10)

        # Create tab widget
        self.tab_widget = QTabWidget()
        self.tab_widget.setStyleSheet("""
            QTabWidget::pane {
                border: 1px solid #d2d2d7;
                border-radius: 8px;
                background: white;
            }
            QTabBar::tab {
                padding: 8px 16px;
                margin: 2px 0;
                border-radius: 4px;
            }
            QTabBar::tab:selected {
                background: #0071e3;
                color: white;
            }
        """)

        # Create Camera tab without the toggle button
        camera_tab = QWidget()
        camera_layout = QVBoxLayout(camera_tab)
        camera_layout.setSpacing(12)

        camera_layout.addWidget(QLabel("Camera"))
        self.camera_combo = QComboBox()
        self.camera_combo.setToolTip("Select which camera to use for video input")
        self.update_camera_list()
        self.camera_combo.currentIndexChanged.connect(self.change_camera)
        camera_layout.addWidget(self.camera_combo)

        camera_layout.addWidget(QLabel("Audio Device"))
        self.audio_combo = QComboBox()
        self.audio_combo.setToolTip("Select which microphone to use for video recording")
        self.update_audio_device_list()
        self.audio_combo.currentIndexChanged.connect(self.change_audio_device)
        camera_layout.addWidget(self.audio_combo)
        
        self.camera_settings_button = QPushButton("Camera Settings")
        self.camera_settings_button.setIcon(qta.icon('fa.cog'))
        self.camera_settings_button.clicked.connect(self.show_camera_settings)
        camera_layout.addWidget(self.camera_settings_button)
        camera_layout.addStretch()
        self.tab_widget.addTab(camera_tab, "Camera")

        # Create Face Control tab
        face_tab = QWidget()
        face_layout = QVBoxLayout(face_tab)
        face_layout.setSpacing(12)

        face_layout.addWidget(QLabel("Face Control"))
        self.source_button = QPushButton("Load Source Face")
        self.source_button.setIcon(qta.icon('fa.upload'))
        self.source_button.clicked.connect(self.load_source_face)
        face_layout.addWidget(self.source_button)

        self.clear_button = QPushButton("Clear Face")
        self.clear_button.setIcon(qta.icon('fa.trash'))
        self.clear_button.setStyleSheet("background-color: #ff3b30; color: white;")
        self.clear_button.clicked.connect(self.clear_source_face)
        face_layout.addWidget(self.clear_button)

        self.gallery_button = QPushButton("Open Face Gallery")
        self.gallery_button.setIcon(qta.icon('fa.image'))
        self.gallery_button.clicked.connect(self.open_face_gallery)
        face_layout.addWidget(self.gallery_button)

        # Face preview in Face Control tab
        face_layout.addWidget(QLabel("Source Face Preview"))
        self.source_preview = QLabel()
        self.source_preview.setFixedSize(280, 280)
        self.source_preview.setStyleSheet("""
            background-color: #f5f5f7;
            border-radius: 8px;
        """)
        self.source_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        face_layout.addWidget(self.source_preview)
        
        face_layout.addStretch()
        self.tab_widget.addTab(face_tab, "Face")

        # Create Settings tab
        settings_tab = QWidget()
        settings_layout = QVBoxLayout(settings_tab)
        settings_layout.setSpacing(12)
                
        # Add Model Management section
        model_group = QGroupBox("Model Management")
        model_layout = QVBoxLayout()
        
        # Add model check button
        self.check_models_button = QPushButton("Check for Model Updates")
        self.check_models_button.setIcon(qta.icon('fa.refresh'))
        self.check_models_button.clicked.connect(self.check_model_updates)
        model_layout.addWidget(self.check_models_button)
        
        # Add model cleanup button
        self.cleanup_models_button = QPushButton("Clean Unused Models")
        self.cleanup_models_button.setIcon(qta.icon('fa.trash'))
        self.cleanup_models_button.clicked.connect(self.cleanup_unused_models)
        model_layout.addWidget(self.cleanup_models_button)
        
        model_group.setLayout(model_layout)
        settings_layout.addWidget(model_group)

        # Face brackets toggle
        self.face_bracket_button = QPushButton("Toggle Face Brackets")
        self.face_bracket_button.setIcon(qta.icon('fa.square-o'))
        self.face_bracket_button.clicked.connect(self.toggle_face_brackets)
        settings_layout.addWidget(self.face_bracket_button)

        # # Similarity threshold
        # threshold_widget = QWidget()
        # threshold_layout = QHBoxLayout(threshold_widget)
        # threshold_layout.setContentsMargins(0, 0, 0, 0)
        # threshold_layout.setSpacing(8)

        # threshold_layout.addWidget(QLabel("Similarity:"))
        # self.threshold_slider = QSlider(Qt.Orientation.Horizontal)
        # self.threshold_slider.setRange(0, 100)
        # initial_threshold = 20
        # self.threshold_slider.setValue(initial_threshold)
        # self.threshold_slider.valueChanged.connect(self.update_threshold)
        # threshold_layout.addWidget(self.threshold_slider)

        # self.threshold_label = QLabel(f"{self.face_processor.similarity_threshold:.2f}")
        # self.threshold_label.setFixedWidth(40)
        # threshold_layout.addWidget(self.threshold_label)

        # settings_layout.addWidget(threshold_widget)

        # Quality controls
        quality_group = QGroupBox("Quality Settings")
        quality_layout = QVBoxLayout()

        self.enhancement_toggle = QCheckBox("Enable Face Enhancement")
        self.enhancement_toggle.setChecked(True)
        self.enhancement_toggle.stateChanged.connect(self.toggle_enhancement)
        quality_layout.addWidget(self.enhancement_toggle)

        strength_layout = QHBoxLayout()
        strength_layout.addWidget(QLabel("Enhancement:"))
        self.enhancement_slider = QSlider(Qt.Orientation.Horizontal)
        self.enhancement_slider.setRange(0, 100)
        self.enhancement_slider.setValue(50)
        self.enhancement_slider.valueChanged.connect(self.update_enhancement)
        strength_layout.addWidget(self.enhancement_slider)
        quality_layout.addLayout(strength_layout)

        quality_group.setLayout(quality_layout)
        settings_layout.addWidget(quality_group)
        
        # Create menubar properly
        menubar = self.menuBar()
        help_menu = menubar.addMenu("&Help")
        help_menu.setObjectName("help_menu")

        # Add tutorial action first
        self.start_tutorial_action = QAction("Start Tutorial", self)
        self.start_tutorial_action.triggered.connect(self.start_tutorial)
        help_menu.addAction(self.start_tutorial_action)

        # Then add other actions
        help_contents = QAction("&Help Contents", self)
        help_contents.setShortcut("F1")
        help_contents.triggered.connect(self.show_help_dialog)
        help_menu.addAction(help_contents)

        help_menu.addSeparator()
        about_action = QAction("&About MacFaceSwap", self)
        about_action.triggered.connect(self.show_about_dialog)
        help_menu.addAction(about_action)
        
        settings_layout.addStretch()
        self.tab_widget.addTab(settings_tab, "Settings")

        # Add tab widget to sidebar
        sidebar_layout.addWidget(self.tab_widget)
        main_layout.addWidget(sidebar)

        # Video container with enhanced styling
        video_container = QWidget()
        video_container.setStyleSheet("""
            QWidget {
                background-color: #1d1d1f;
                border-radius: 8px;
            }
        """)
        video_layout = QVBoxLayout(video_container)
        video_layout.setContentsMargins(10, 10, 10, 10)
        video_layout.setSpacing(10)

        # Video controls at the top
        video_controls = QHBoxLayout()
        video_controls.setContentsMargins(0, 5, 0, 0)
        video_controls.addStretch()

        # Camera toggle button
        self.toggle_button = QPushButton("Start Camera")
        self.toggle_button.setToolTip("Start or stop the camera feed")
        self.toggle_button.setIcon(qta.icon('fa.camera'))
        self.toggle_button.clicked.connect(self.toggle_camera)
        video_controls.addWidget(self.toggle_button)

        # Recording button
        self.record_button = QPushButton("Start Recording")
        self.record_button.setIcon(qta.icon('fa.circle', color='red'))
        self.record_button.clicked.connect(self.toggle_recording)
        video_controls.addWidget(self.record_button)

        # Popout button
        self.popout_button = QPushButton("Popout Video")
        self.popout_button.setIcon(qta.icon('fa.window-maximize'))
        self.popout_button.clicked.connect(self.toggle_video_window)
        video_controls.addWidget(self.popout_button)

        # Add controls to video layout
        video_layout.addLayout(video_controls)

        # Video display
        self.video_label = QLabel()
        self.video_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.video_label.setStyleSheet("background-color: #1d1d1f; border-radius: 8px;")
        video_layout.addWidget(self.video_label)

        # Recording status
        recording_controls = QHBoxLayout()
        recording_controls.setSpacing(10)
        self.recording_status = QLabel("")
        recording_controls.addWidget(self.recording_status)
        recording_controls.addStretch()
        video_layout.addLayout(recording_controls)

        main_layout.addWidget(video_container)
        main_layout.setStretch(1, 1)  # Video area takes up remaining space

    def change_audio_device(self, index):
        """Handle changes to the selected audio device."""
        selected_device = self.audio_combo.currentData()  # Get the device index from the dropdown
        if selected_device is not None:
            self.video_recorder.audio_device = selected_device
            print(f"Audio device manually set to: {selected_device}")

    def update_audio_device_list(self):
        """Populate the audio device dropdown."""
        self.audio_combo.clear()
        for i, device in enumerate(sd.query_devices()):
            if device['max_input_channels'] > 0:  # Only include devices with input channels
                self.audio_combo.addItem(f"{device['name']} ({device['hostapi']})", i)

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
            
        if self.face_processor and hasattr(self.face_processor, 'process_frame'):
            processed_frame = self.face_processor.process_frame(frame)
            if processed_frame is not None:
                frame = processed_frame
                
                # Add frame to recording if active
                if self.video_recorder.is_recording:
                    self.video_recorder.add_frame(frame)
        
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
        
    def show_help_dialog(self):
        """Show the help contents dialog"""
        dialog = QDialog(self)
        dialog.setWindowTitle("MacFaceSwap Help")
        dialog.resize(600, 400)
        
        layout = QVBoxLayout(dialog)
        help_browser = QTextBrowser()
        help_browser.setOpenExternalLinks(True)
        
        help_text = """
        <h2>MacFaceSwap Help</h2>
        
        <h3>Getting Started</h3>
        <p>MacFaceSwap allows you to swap faces in real-time video. Here's how to use it:</p>
        
        <h4>Basic Steps:</h4>
        <ol>
            <li>Select your camera from the Camera tab</li>
            <li>Click "Start Camera" to begin the video feed</li>
            <li>Load a source face using either:
                <ul>
                    <li>The "Load Source Face" button to use your own image</li>
                    <li>The "Open Face Gallery" to use a celebrity face</li>
                </ul>
            </li>
        </ol>
        
        <h4>Controls:</h4>
        <ul>
            <li><b>Camera Tab:</b> Select and control your camera and audio devices</li>
            <li><b>Face Tab:</b> Load and manage source faces for swapping</li>
            <li><b>Settings Tab:</b> Adjust face detection and enhancement settings</li>
        </ul>
        
        <h4>Advanced Features:</h4>
        <ul>
            <li><b>Face Brackets:</b> Toggle visibility of face detection boxes</li>
            <li><b>Similarity Threshold:</b> Adjust face matching sensitivity</li>
            <li><b>Face Enhancement:</b> Enable/disable and adjust face enhancement quality</li>
            <li><b>Video Recording:</b> Record your face-swapped video feed</li>
            <li><b>Popout Video:</b> Open the video feed in a separate window</li>
        </ul>
        """
        
        help_browser.setHtml(help_text)
        layout.addWidget(help_browser)
        
        dialog.exec()
        
    def show_about_dialog(self):
        """Show the about dialog"""
        QMessageBox.about(self, 
            "About MacFaceSwap",
            """<h3>MacFaceSwap</h3>
            <p>A real-time face swapping application for macOS.</p>
            <p>Features:</p>
            <ul>
                <li>Real-time face detection and swapping</li>
                <li>Support for multiple cameras</li>
                <li>Face enhancement capabilities</li>
                <li>Video recording</li>
                <li>Celebrity face gallery</li>
            </ul>
            <p>Press F1 or use Help menu for usage instructions.</p>
            """
        )
            
    def show_camera_settings(self):
        """Show the camera settings dialog with current settings"""
        try:
            # Get current settings
            if self.video_handler.camera and self.video_handler.is_running:
                current_width = int(self.video_handler.camera.get(cv2.CAP_PROP_FRAME_WIDTH))
                current_height = int(self.video_handler.camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
                current_fps = int(self.video_handler.camera.get(cv2.CAP_PROP_FPS))
                current_brightness = int(self.video_handler.camera.get(cv2.CAP_PROP_BRIGHTNESS) * 100)
            else:
                # Use the current frame_size from VideoHandler
                current_width, current_height = self.video_handler.frame_size
                current_fps = 30
                current_brightness = 50
                
            current_settings = {
                'resolution': f"{current_width}x{current_height}",
                'fps': current_fps,
                'brightness': current_brightness,
                'autofocus': True,
                'threshold': self.face_processor.similarity_threshold
            }
            
            print(f"Current camera settings: {current_settings}")
            
            settings_dialog = CameraSettings(self, current_settings)
            if settings_dialog.exec() == QDialog.DialogCode.Accepted:
                settings = settings_dialog.get_settings()
                self.apply_camera_settings(settings)
                
        except Exception as e:
            print(f"Error showing camera settings: {str(e)}")
            import traceback
            traceback.print_exc()

    def apply_camera_settings(self, settings):
        """Apply the camera settings"""
        try:
            # Get current camera ID
            current_camera = self.camera_combo.currentData()
            
            # Parse resolution
            width, height = map(int, settings['resolution'].split('x'))
            
            # Update frame size in VideoHandler
            self.video_handler.frame_size = (width, height)
            
            # Stop current camera
            self.video_handler.stop_camera()
            
            # Start camera with new settings
            if self.video_handler.start_camera(current_camera):
                # Apply additional settings if camera is running
                if self.video_handler.camera and self.video_handler.camera.isOpened():
                    self.video_handler.camera.set(cv2.CAP_PROP_FPS, settings['fps'])
                    self.video_handler.camera.set(cv2.CAP_PROP_BRIGHTNESS, settings['brightness'] / 100.0)
                    if settings['autofocus']:
                        self.video_handler.camera.set(cv2.CAP_PROP_AUTOFOCUS, 1)
                    else:
                        self.video_handler.camera.set(cv2.CAP_PROP_AUTOFOCUS, 0)
                        
                # Update threshold
                if 'threshold' in settings:
                    self.face_processor.similarity_threshold = settings['threshold']
                    if hasattr(self, 'threshold_slider'):
                        self.threshold_slider.setValue(int(settings['threshold'] * 100))
                        
                print(f"Camera settings applied successfully: {settings}")
            else:
                print("Failed to start camera with new settings")
                
        except Exception as e:
            print(f"Error applying camera settings: {str(e)}")
            # Try to restart the camera with original settings
            try:
                self.video_handler.start_camera(self.camera_combo.currentData())
            except Exception as restart_error:
                print(f"Error restarting camera: {str(restart_error)}")
                        
    # Update this method in src/ui/main_window.py

    def check_model_updates(self):
        """Check for model updates and download if available."""
        try:
            # Get current config state
            current_config = self.model_manager.model_config

            # Reload config from disk to check for updates
            new_config = self.model_manager.load_config()
            if not new_config:
                QMessageBox.warning(
                    self,
                    "Update Check Failed",
                    "Unable to load model configuration."
                )
                return
                
            updates_needed = []
            for model_name, model_info in new_config['models'].items():
                # If model is new or hash doesn't match, it needs updating
                if (model_name not in current_config['models'] or 
                    current_config['models'][model_name]['sha256'] != model_info['sha256']):
                    updates_needed.append(model_name)
                    continue
                    
                # Check if existing file matches expected hash
                model_path, _ = self.model_manager.find_model(model_name)
                if model_path is None or not self.model_manager.verify_model(model_path, model_info['sha256']):
                    updates_needed.append(model_name)
                    
            if updates_needed:
                message = (
                    "The following models have updates available:\n\n" +
                    "\n".join(f"• {model}" for model in updates_needed) +
                    f"\n\nTotal download size: {self.model_manager.get_total_download_size(updates_needed)}" +
                    "\n\nWould you like to download the updates?"
                )
                
                reply = QMessageBox.question(
                    self,
                    "Model Updates Available",
                    message,
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
                )
                
                if reply == QMessageBox.StandardButton.Yes:
                    # Update the model config before downloading
                    self.model_manager.model_config = new_config
                    success = self.model_manager.download_models(updates_needed)
                    if success:
                        QMessageBox.information(
                            self,
                            "Update Complete",
                            "Models have been successfully updated!"
                        )
            else:
                QMessageBox.information(
                    self,
                    "Model Status",
                    "All models are up to date!"
                )
            
        except Exception as e:
            import traceback
            print(f"Error checking for updates: {str(e)}")
            traceback.print_exc()
            QMessageBox.warning(
                self,
                "Update Check Failed",
                f"Failed to check for updates: {str(e)}"
            )

    def cleanup_unused_models(self):
        """Remove unused or outdated model files."""
        try:
            current_config = self.model_manager.model_config
            if not current_config:
                return
                
            # Get list of existing model files
            model_files = list(self.model_manager.models_dir.glob("*.pth"))
            
            # Find unused models
            unused_models = []
            for model_file in model_files:
                model_name = model_file.stem
                if model_name not in current_config['models']:
                    unused_models.append(model_file)
                    
            if unused_models:
                message = (
                    "The following unused models were found:\n\n" +
                    "\n".join(f"• {model.name}" for model in unused_models) +
                    "\n\nWould you like to remove them?"
                )
                
                reply = QMessageBox.question(
                    self,
                    "Clean Unused Models",
                    message,
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
                )
                
                if reply == QMessageBox.StandardButton.Yes:
                    for model_file in unused_models:
                        try:
                            model_file.unlink()
                        except Exception as e:
                            self.logger.error(f"Failed to delete {model_file}: {e}")
                            
                    QMessageBox.information(
                        self,
                        "Cleanup Complete",
                        "Unused models have been removed."
                    )
            else:
                QMessageBox.information(
                    self,
                    "Cleanup Status",
                    "No unused models found."
                )
                
        except Exception as e:
            QMessageBox.warning(
                self,
                "Cleanup Failed",
                f"Failed to cleanup unused models: {str(e)}"
            )

    def closeEvent(self, event):
        """Handle application closing"""
        try:
            if self.video_window:
                self.video_window.close()
            self.video_handler.stop_camera()
            self.model_manager.cleanup()  # Add this line
            event.accept()
        except Exception as e:
            print(f"Error closing application: {str(e)}")
            event.accept()
