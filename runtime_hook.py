
import os
import sys

# Disable albumentations update check
os.environ['NO_ALBUMENTATIONS_UPDATE'] = '1'

# Add binary path to system path
if getattr(sys, 'frozen', False):
    os.environ['PATH'] = sys._MEIPASS + os.pathsep + os.environ['PATH']
