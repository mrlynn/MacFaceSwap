# MacFaceSwap

**MacFaceSwap** is an interactive, fun, and professional desktop application for live face-swapping and video manipulation using AI. Built with PyQt6, OpenCV, and advanced face-processing techniques, it provides a robust platform for face detection, processing, and swapping in real-time.

---

## Features

- **Live Face Swapping:** Swap faces in real-time from camera feeds.
- **Predefined Celebrity Faces:** Choose from a gallery of preloaded celebrity faces for swapping.
- **Custom Face Uploads:** Upload and use your own images for face swapping.
- **Face Bracket Toggle:** Enable or disable face brackets on the live video feed.
- **Popout Video Window:** View the live feed in a separate, popout window.
- **User-Friendly Interface:** Modern design with vibrant colors and interactive controls.

---

## Requirements

- Python 3.10+
- Virtual Environment (recommended)

### Python Dependencies:

Install dependencies via `pip`:
```bash
pip install PyQt6 opencv-python qtawesome numpy
```

---

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-repo/MacFaceSwap.git
   cd MacFaceSwap
   ```

2. **Set Up Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add Resources:**
   Ensure the following directories are in place:
   - `resources/icons/`: Add icons for buttons.
   - `images/`: Add predefined face images (organized in subdirectories for each face).

---

## Usage

1. **Run the Application:**
   ```bash
   python src/main.py
   ```

2. **Features in the UI:**
   - **Camera Selection:** Select and toggle camera feeds.
   - **Load Source Face:** Upload your image for face swapping.
   - **Open Face Gallery:** Choose from predefined celebrity faces.
   - **Toggle Face Brackets:** Enable or disable face detection brackets.
   - **Popout Video:** View the video feed in a separate window.

3. **Quit the Application:**
   Close the window or press `Ctrl + Q`.

---

## Project Structure

```
MacFaceSwap/
├── src/
│   ├── core/
│   │   ├── face_processor.py   # Face processing logic
│   │   ├── video_handler.py    # Camera and video feed handling
│   ├── ui/
│   │   ├── main_window.py      # Main application interface
│   │   ├── face_gallery.py     # Face gallery window
│   │   ├── video_window.py     # Popout video window
│   └── main.py                 # Entry point for the application
├── resources/
│   ├── icons/                  # Icons for UI buttons
│   └── images/                 # Predefined celebrity face images
├── README.md                   # Project documentation
├── requirements.txt            # Python dependencies
├── setup.py                    # Installation setup
└── run.sh                      # Shortcut to start the application
```

---

## How to Add Predefined Faces

1. **Create Subdirectories for Each Celebrity:**
   Place images in the `images` directory, organized by celebrity name:
   ```
   images/
   ├── Tom_Hanks/
   │   ├── image1.jpg
   │   ├── image2.jpg
   ├── Scarlett_Johansson/
   │   ├── image1.jpg
   │   ├── image2.jpg
   ```

2. **Update the Application:**
   The application will dynamically load these images into the gallery.

---

## Troubleshooting

### Common Issues

- **Blank Popout Window:**
  Ensure `toggle_video_window` connects the video feed to the popout window.
- **Distorted Gallery Images:**
  Verify that images are loaded and processed correctly in `face_gallery.py`.
- **Face Bracket KeyError:**
  Ensure `face` and `embedding` keys are correctly set in the source face data.

### Debugging

Run the application in verbose mode:
```bash
python src/main.py
```

Check logs for errors and adjust as necessary.

---

## Contributing

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/your-feature
   ```
5. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

- **PyQt6:** For the powerful GUI toolkit.
- **OpenCV:** For robust video processing.
- **Font Awesome:** For providing icons via `qtawesome`.
