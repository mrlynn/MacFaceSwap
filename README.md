# Mac Face Swap

A native macOS application for real-time face swapping using deep learning technology.

## Requirements

- macOS 10.15 (Catalina) or later
- Python 3.10
- Apple Silicon (M1/M2) or Intel processor
- Minimum 8GB RAM
- 2GB free disk space
- Webcam access

## Installation

1. Download the latest `.dmg` file from the [Releases](https://github.com/yourusername/mac-face-swap/releases) page
2. Open the `.dmg` file
3. Drag the Face Swap app to your Applications folder
4. Right-click the app and select "Open" for first launch (required for Gatekeeper)

## Building from Source

### Prerequisites

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

Required packages (see requirements.txt for specific versions):
- opencv-python
- numpy
- torch
- torchvision
- PyQt6
- dlib
- mediapipe

### Build Steps

1. Install development dependencies:
```bash
pip install pyinstaller create-dmg
```

2. Build the .app bundle:
```bash
pyinstaller --windowed --name "Face Swap" --icon assets/icon.icns main.py
```

3. Create the .dmg installer:
```bash
create-dmg \
  --volname "Face Swap" \
  --window-pos 200 120 \
  --window-size 800 400 \
  --icon-size 100 \
  --icon "Face Swap.app" 200 190 \
  --hide-extension "Face Swap.app" \
  --app-drop-link 600 185 \
  "Face Swap.dmg" \
  "dist/Face Swap.app"
```

## Development

### Project Structure
```
mac-face-swap/
├── src/
│   ├── main.py           # Application entry point
│   ├── face_swap/        # Core face swapping logic
│   ├── gui/             # PyQt6 GUI components
│   └── utils/           # Helper functions
├── assets/              # Icons and resources
├── tests/              # Unit and integration tests
└── scripts/            # Build and packaging scripts
```

### Running Tests
```bash
pytest tests/
```

## Troubleshooting

### Common Issues

1. **App won't open**: Ensure you right-click and select "Open" for first launch
2. **Camera access denied**: Grant camera permissions in System Preferences > Security & Privacy
3. **Performance issues**: Check minimum system requirements and close resource-intensive applications

### Error Reporting

Please report issues on the [GitHub Issues](https://github.com/yourusername/mac-face-swap/issues) page with:
- macOS version
- Hardware specifications
- Steps to reproduce
- Error messages or screenshots

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Acknowledgments

- [MediaPipe](https://mediapipe.dev/) for face detection
- [PyTorch](https://pytorch.org/) for deep learning framework
- [OpenCV](https://opencv.org/) for image processing

## Security

- App is signed and notarized with Apple Developer certificate
- No data collection or network access required
- All processing done locally on device
