# src/__init__.py
import os
import sys

def get_bundle_dir():
    """Get the directory where resources are stored"""
    if getattr(sys, 'frozen', False):
        # Running in a bundle
        return sys._MEIPASS
    # Running in normal Python environment
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_resource_path(relative_path):
    """Get absolute path to resource"""
    return os.path.join(get_bundle_dir(), relative_path)