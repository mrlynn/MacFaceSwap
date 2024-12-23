# Create project directory
mkdir MacFaceSwap
cd MacFaceSwap

# Create and activate virtual environment
python3 -m venv venv

# For macOS/Linux:
source venv/bin/activate

# Verify Python installation and version
python --version
which python

# Create initial project structure
mkdir -p {src,models,assets,resources}
mkdir -p src/{core,ui}

# Install initial dependencies
pip install --upgrade pip
pip install wheel setuptools

# Save initial requirements
pip freeze > requirements.txt

# Add .gitignore
cat > .gitignore << EOL
# Virtual Environment
venv/
env/
.env/

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# macOS
.DS_Store
.AppleDouble
.LSOverride
._*

# IDE
.idea/
.vscode/
*.swp
*.swo

# Project specific
models/*.onnx
models/*.pth
EOL
