# src/ui/camera_settings.py
from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, 
                           QLabel, QSlider, QComboBox, QCheckBox, QPushButton)
from PyQt6.QtCore import Qt

class CameraSettings(QDialog):
    def __init__(self, parent=None, current_settings=None):
        super().__init__(parent)
        self.setWindowTitle("Camera Settings")
        self.current_settings = current_settings or {}
        self.init_ui()
        self.load_current_settings()
        
    def init_ui(self):
        layout = QVBoxLayout()
        
        # Resolution settings
        res_layout = QHBoxLayout()
        res_layout.addWidget(QLabel("Resolution:"))
        self.resolution_combo = QComboBox()
        self.resolution_combo.addItems([
            "640x480",
            "1280x720",
            "1920x1080"
        ])
        res_layout.addWidget(self.resolution_combo)
        layout.addLayout(res_layout)
        
        # Frame rate settings
        fps_layout = QHBoxLayout()
        fps_layout.addWidget(QLabel("Frame Rate:"))
        self.fps_slider = QSlider(Qt.Orientation.Horizontal)
        self.fps_slider.setMinimum(1)
        self.fps_slider.setMaximum(60)
        self.fps_slider.setValue(30)
        self.fps_label = QLabel("30 FPS")
        self.fps_slider.valueChanged.connect(
            lambda v: self.fps_label.setText(f"{v} FPS"))
        fps_layout.addWidget(self.fps_slider)
        fps_layout.addWidget(self.fps_label)
        layout.addLayout(fps_layout)
        
        # Brightness control
        bright_layout = QHBoxLayout()
        bright_layout.addWidget(QLabel("Brightness:"))
        self.brightness_slider = QSlider(Qt.Orientation.Horizontal)
        self.brightness_slider.setMinimum(0)
        self.brightness_slider.setMaximum(100)
        self.brightness_slider.setValue(50)
        self.brightness_label = QLabel("50")
        self.brightness_slider.valueChanged.connect(
            lambda v: self.brightness_label.setText(f"{v}"))
        bright_layout.addWidget(self.brightness_slider)
        bright_layout.addWidget(self.brightness_label)
        layout.addLayout(bright_layout)
        
        # Auto-focus toggle
        self.autofocus_check = QCheckBox("Auto Focus")
        self.autofocus_check.setChecked(True)
        layout.addWidget(self.autofocus_check)
        
        # Threshold setting
        threshold_layout = QHBoxLayout()
        threshold_layout.addWidget(QLabel("Motion Threshold:"))
        self.threshold_slider = QSlider(Qt.Orientation.Horizontal)
        self.threshold_slider.setMinimum(0)
        self.threshold_slider.setMaximum(100)
        self.threshold_slider.setValue(0)
        self.threshold_label = QLabel("0.0")
        self.threshold_slider.valueChanged.connect(
            lambda v: self.threshold_label.setText(f"{v/100:.1f}"))
        threshold_layout.addWidget(self.threshold_slider)
        threshold_layout.addWidget(self.threshold_label)
        layout.addLayout(threshold_layout)
        
        # Buttons
        button_layout = QHBoxLayout()
        save_button = QPushButton("Save")
        cancel_button = QPushButton("Cancel")
        save_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(save_button)
        button_layout.addWidget(cancel_button)
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
    
    def load_current_settings(self):
        """Load the current settings into the UI"""
        if not self.current_settings:
            return
            
        # Set resolution
        if 'resolution' in self.current_settings:
            index = self.resolution_combo.findText(self.current_settings['resolution'])
            if index >= 0:
                self.resolution_combo.setCurrentIndex(index)
        
        # Set FPS
        if 'fps' in self.current_settings:
            self.fps_slider.setValue(self.current_settings['fps'])
            
        # Set brightness
        if 'brightness' in self.current_settings:
            self.brightness_slider.setValue(self.current_settings['brightness'])
            
        # Set autofocus
        if 'autofocus' in self.current_settings:
            self.autofocus_check.setChecked(self.current_settings['autofocus'])
            
        # Set threshold
        if 'threshold' in self.current_settings:
            self.threshold_slider.setValue(int(self.current_settings['threshold'] * 100))
    
    def get_settings(self):
        """Return the current settings as a dictionary"""
        return {
            'resolution': self.resolution_combo.currentText(),
            'fps': self.fps_slider.value(),
            'brightness': self.brightness_slider.value(),
            'autofocus': self.autofocus_check.isChecked(),
            'threshold': self.threshold_slider.value() / 100.0
        }