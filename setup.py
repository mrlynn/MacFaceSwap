from setuptools import setup

APP = ['src/main.py']
DATA_FILES = [
    ('models', ['models/inswapper_128.onnx', 'models/GFPGANv1.4.pth']),
    ('resources', ['resources/icon.icns'])
]

OPTIONS = {
    'argv_emulation': True,
    'packages': [
        'cv2', 
        'numpy', 
        'insightface',
        'onnxruntime',
        'PyQt6',
        'src'
    ],
    'excludes': ['pytest', 'jaraco.path', '_typeshed'],
    'iconfile': 'resources/icon.icns',
    'plist': {
        'CFBundleIdentifier': 'com.mlynnorg.macfaceswap',
        'CFBundleName': 'MacFaceSwap',
        'CFBundleDisplayName': 'MacFaceSwap',
        'CFBundleShortVersionString': '1.0.0',
        'CFBundleVersion': '1.0.0',
        'LSMinimumSystemVersion': '10.15',
        'NSHighResolutionCapable': True,
        'NSCameraUsageDescription': 'MacFaceSwap needs access to your camera for face swapping functionality.',
    }
}

setup(
    app=APP,
    name='MacFaceSwap',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    install_requires=[
        'opencv-python',
        'numpy',
        'insightface',
        'onnxruntime-silicon',
        'PyQt6'
    ]
)