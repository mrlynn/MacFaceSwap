# .gitignore

```
.aidigestignore
venv
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
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
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec
.DS_Store

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# UV
#   Similar to Pipfile.lock, it is generally recommended to include uv.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#uv.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/latest/usage/project/#working-with-version-control
.pdm.toml
.pdm-python
.pdm-build/

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/

# PyPI configuration file
.pypirc

```

# build.sh

```sh
#!/bin/bash

# Exit on error
set -e

echo "Starting clean build process..."

# Ensure we're in the project root
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_ROOT"

# Clean previous builds and cache
echo "Cleaning previous builds..."
rm -rf build dist __pycache__ *.pyc
find . -type d -name "__pycache__" -exec rm -r {} +

# Ensure clean virtual environment
echo "Setting up virtual environment..."
if [ -d "venv" ]; then
    rm -rf venv
fi

python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Ensure matplotlib and key dependencies are installed
echo "Installing additional dependencies..."
pip install matplotlib==3.7.1  # Use a specific version known to work
pip install PyQt6 QtAwesome insightface onnxruntime-silicon

# build.sh addition (before pyinstaller command)
echo "Verifying project structure..."
if [ ! -d "images" ]; then
    echo "ERROR: 'images' directory not found!"
    exit 1
fi

# Build the application
echo "Building application..."
pyinstaller MacFaceSwap.spec

# After pyinstaller command
echo "Verifying built application structure..."
if [ ! -d "dist/MacFaceSwap.app/Contents/Resources/images" ]; then
    echo "WARNING: 'images' directory not found in built application!"
fi

echo "Build complete! Check the dist directory for MacFaceSwap.app"
```

# images/Angelina Jolie/001_fe3347c0.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/002_8f8da10e.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/003_57612506.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/004_f61e7d0c.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/005_582c121a.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/006_9135205d.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/007_cabbfcbb.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/008_d1f87068.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/009_fb3e6174.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/010_f99d79e3.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/011_7344ca35.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/012_cfcd4007.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/013_95ecbd39.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/014_0d29db88.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/015_8bac79b5.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/016_8945d6ca.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/017_e28ea9d4.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/018_fcafe1a8.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/019_57ab290d.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/020_4c4b655f.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/021_6e419870.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/022_b497b92e.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/023_7781dd1c.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/024_ca32be97.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/025_41cee764.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/026_2828fcaf.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/027_58887f30.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/028_6a0ff8de.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/029_f2882b0d.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/030_66bddeb6.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/031_2364f4d8.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/032_db66bd61.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/033_23e68208.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/034_418fbbdb.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/035_2e497561.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/036_3e807a88.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/037_62d00a09.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/038_e40d5b16.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/039_6b10ab98.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/040_2ef814c7.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/041_abf5c9cb.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/042_2ccd070f.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/043_b812749f.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/044_512dfd33.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/045_c560251e.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/046_d93a2c2d.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/047_5350c8c0.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/048_0a32a483.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/049_4d6df392.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/050_7c5b026c.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/051_268fdfd7.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/052_6db5f5bf.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/053_05c78fa1.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/054_7ba62f81.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/055_aaaf063c.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/056_97412d14.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/057_7f34f0f4.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/058_02860eff.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/059_df425619.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/060_4037f0f7.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/061_e18ba2b0.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/062_6aa9cf8f.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/063_c486d5ef.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/064_0de68937.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/065_689150aa.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/066_b378479b.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/067_ff52c2fe.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/068_2fb110d1.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/069_9d0e44d5.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/070_1a4312d2.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/071_b537dbca.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/072_8d068904.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/073_9f1d377a.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/074_0ec79719.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/075_4c504eec.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/076_1d914d5b.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/077_27650aa3.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/078_044866e7.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/079_40a598dc.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/080_e998ab00.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/081_12fb31ec.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/082_047778bb.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/083_bdada1e2.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/084_da751ddd.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/085_f579db33.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/086_f2c730f3.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/087_f325890f.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/088_029ffc54.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/089_33e36564.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/090_da55509f.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/091_b5b4a62f.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/092_26130bb1.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/093_6ce62543.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/094_c255b703.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/095_0be163a1.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/096_75710434.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/097_9a6bf61f.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/098_dd1405fc.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/099_c22d3e48.jpg

This is a binary file of the type: Image

# images/Angelina Jolie/100_31ff9373.jpg

This is a binary file of the type: Image

# images/Brad Pitt/001_c04300ef.jpg

This is a binary file of the type: Image

# images/Brad Pitt/002_cc1b9701.jpg

This is a binary file of the type: Image

# images/Brad Pitt/003_7a6b2156.jpg

This is a binary file of the type: Image

# images/Brad Pitt/004_777c50d0.jpg

This is a binary file of the type: Image

# images/Brad Pitt/005_02ab3a1b.jpg

This is a binary file of the type: Image

# images/Brad Pitt/006_87166f38.jpg

This is a binary file of the type: Image

# images/Brad Pitt/007_74ccfb4a.jpg

This is a binary file of the type: Image

# images/Brad Pitt/008_31e90c6b.jpg

This is a binary file of the type: Image

# images/Brad Pitt/009_23c94f29.jpg

This is a binary file of the type: Image

# images/Brad Pitt/010_08c44431.jpg

This is a binary file of the type: Image

# images/Brad Pitt/011_270cd3ea.jpg

This is a binary file of the type: Image

# images/Brad Pitt/012_8de7a736.jpg

This is a binary file of the type: Image

# images/Brad Pitt/013_0c83ca91.jpg

This is a binary file of the type: Image

# images/Brad Pitt/014_871b0d80.jpg

This is a binary file of the type: Image

# images/Brad Pitt/015_82889ec9.jpg

This is a binary file of the type: Image

# images/Brad Pitt/016_8bb23f7e.jpg

This is a binary file of the type: Image

# images/Brad Pitt/017_4748675b.jpg

This is a binary file of the type: Image

# images/Brad Pitt/018_136dbb40.jpg

This is a binary file of the type: Image

# images/Brad Pitt/019_ddcd5687.jpg

This is a binary file of the type: Image

# images/Brad Pitt/020_45c8d790.jpg

This is a binary file of the type: Image

# images/Brad Pitt/021_143b276f.jpg

This is a binary file of the type: Image

# images/Brad Pitt/022_a8206d1a.jpg

This is a binary file of the type: Image

# images/Brad Pitt/023_98d91529.jpg

This is a binary file of the type: Image

# images/Brad Pitt/024_54112f36.jpg

This is a binary file of the type: Image

# images/Brad Pitt/025_25dc7dcf.jpg

This is a binary file of the type: Image

# images/Brad Pitt/026_805241a7.jpg

This is a binary file of the type: Image

# images/Brad Pitt/027_78f200c3.jpg

This is a binary file of the type: Image

# images/Brad Pitt/028_181cbb8a.jpg

This is a binary file of the type: Image

# images/Brad Pitt/029_36dac19e.jpg

This is a binary file of the type: Image

# images/Brad Pitt/030_716e4856.jpg

This is a binary file of the type: Image

# images/Brad Pitt/031_8fc10a75.jpg

This is a binary file of the type: Image

# images/Brad Pitt/032_fd37a8e2.jpg

This is a binary file of the type: Image

# images/Brad Pitt/033_46c95715.jpg

This is a binary file of the type: Image

# images/Brad Pitt/034_984e63b3.jpg

This is a binary file of the type: Image

# images/Brad Pitt/035_a767728d.jpg

This is a binary file of the type: Image

# images/Brad Pitt/036_5e0af3bf.jpg

This is a binary file of the type: Image

# images/Brad Pitt/037_b5467841.jpg

This is a binary file of the type: Image

# images/Brad Pitt/038_5e10a567.jpg

This is a binary file of the type: Image

# images/Brad Pitt/039_1c018deb.jpg

This is a binary file of the type: Image

# images/Brad Pitt/040_9b4bfe5b.jpg

This is a binary file of the type: Image

# images/Brad Pitt/041_cc0957bf.jpg

This is a binary file of the type: Image

# images/Brad Pitt/042_8030e553.jpg

This is a binary file of the type: Image

# images/Brad Pitt/043_6973a308.jpg

This is a binary file of the type: Image

# images/Brad Pitt/044_ac060de4.jpg

This is a binary file of the type: Image

# images/Brad Pitt/045_6895fe7e.jpg

This is a binary file of the type: Image

# images/Brad Pitt/046_8bf34269.jpg

This is a binary file of the type: Image

# images/Brad Pitt/047_80045019.jpg

This is a binary file of the type: Image

# images/Brad Pitt/048_185402c6.jpg

This is a binary file of the type: Image

# images/Brad Pitt/049_31625c44.jpg

This is a binary file of the type: Image

# images/Brad Pitt/050_3e39c960.jpg

This is a binary file of the type: Image

# images/Brad Pitt/051_fd8a292f.jpg

This is a binary file of the type: Image

# images/Brad Pitt/052_b80b0a3f.jpg

This is a binary file of the type: Image

# images/Brad Pitt/053_be062c12.jpg

This is a binary file of the type: Image

# images/Brad Pitt/054_9f01aefa.jpg

This is a binary file of the type: Image

# images/Brad Pitt/055_14a5e7bc.jpg

This is a binary file of the type: Image

# images/Brad Pitt/056_8362ff51.jpg

This is a binary file of the type: Image

# images/Brad Pitt/057_545ca96d.jpg

This is a binary file of the type: Image

# images/Brad Pitt/058_ca613f72.jpg

This is a binary file of the type: Image

# images/Brad Pitt/059_ef2c0ca7.jpg

This is a binary file of the type: Image

# images/Brad Pitt/060_136e5ef5.jpg

This is a binary file of the type: Image

# images/Brad Pitt/061_38d21dc0.jpg

This is a binary file of the type: Image

# images/Brad Pitt/062_f0c8d0c8.jpg

This is a binary file of the type: Image

# images/Brad Pitt/063_a90951c4.jpg

This is a binary file of the type: Image

# images/Brad Pitt/064_213e2850.jpg

This is a binary file of the type: Image

# images/Brad Pitt/065_34848907.jpg

This is a binary file of the type: Image

# images/Brad Pitt/066_1867585d.jpg

This is a binary file of the type: Image

# images/Brad Pitt/067_571d88eb.jpg

This is a binary file of the type: Image

# images/Brad Pitt/068_5ebbf7fb.jpg

This is a binary file of the type: Image

# images/Brad Pitt/069_8533eee4.jpg

This is a binary file of the type: Image

# images/Brad Pitt/070_0acb9d53.jpg

This is a binary file of the type: Image

# images/Brad Pitt/071_2d51687a.jpg

This is a binary file of the type: Image

# images/Brad Pitt/072_da45cf8f.jpg

This is a binary file of the type: Image

# images/Brad Pitt/073_aa4e37e8.jpg

This is a binary file of the type: Image

# images/Brad Pitt/074_6f4720aa.jpg

This is a binary file of the type: Image

# images/Brad Pitt/075_a7a83d60.jpg

This is a binary file of the type: Image

# images/Brad Pitt/076_75b9dd73.jpg

This is a binary file of the type: Image

# images/Brad Pitt/077_ddf0abd8.jpg

This is a binary file of the type: Image

# images/Brad Pitt/078_b546dff5.jpg

This is a binary file of the type: Image

# images/Brad Pitt/079_e3171916.jpg

This is a binary file of the type: Image

# images/Brad Pitt/080_569bb446.jpg

This is a binary file of the type: Image

# images/Brad Pitt/081_4d677d83.jpg

This is a binary file of the type: Image

# images/Brad Pitt/082_545afee5.jpg

This is a binary file of the type: Image

# images/Brad Pitt/083_d6f1d5ac.jpg

This is a binary file of the type: Image

# images/Brad Pitt/084_4876da64.jpg

This is a binary file of the type: Image

# images/Brad Pitt/085_5c4b6432.jpg

This is a binary file of the type: Image

# images/Brad Pitt/086_8274c0d1.jpg

This is a binary file of the type: Image

# images/Brad Pitt/087_155f1f74.jpg

This is a binary file of the type: Image

# images/Brad Pitt/088_b1977c95.jpg

This is a binary file of the type: Image

# images/Brad Pitt/089_7a7d2c5d.jpg

This is a binary file of the type: Image

# images/Brad Pitt/090_12e1f614.jpg

This is a binary file of the type: Image

# images/Brad Pitt/091_8561b34e.jpg

This is a binary file of the type: Image

# images/Brad Pitt/092_22d9de5d.jpg

This is a binary file of the type: Image

# images/Brad Pitt/093_c4d318cd.jpg

This is a binary file of the type: Image

# images/Brad Pitt/094_16e562f0.jpg

This is a binary file of the type: Image

# images/Brad Pitt/095_1104d364.jpg

This is a binary file of the type: Image

# images/Brad Pitt/096_b096ebfe.jpg

This is a binary file of the type: Image

# images/Brad Pitt/097_df404aa1.jpg

This is a binary file of the type: Image

# images/Brad Pitt/098_36dd62c5.jpg

This is a binary file of the type: Image

# images/Brad Pitt/099_151b7575.jpg

This is a binary file of the type: Image

# images/Brad Pitt/100_f4b2c7a7.jpg

This is a binary file of the type: Image

# images/Denzel Washington/001_d3323f3c.jpg

This is a binary file of the type: Image

# images/Denzel Washington/002_f44b8d45.jpg

This is a binary file of the type: Image

# images/Denzel Washington/003_b622e925.jpg

This is a binary file of the type: Image

# images/Denzel Washington/004_677c65bf.jpg

This is a binary file of the type: Image

# images/Denzel Washington/005_cb37c7b2.jpg

This is a binary file of the type: Image

# images/Denzel Washington/006_2880115c.jpg

This is a binary file of the type: Image

# images/Denzel Washington/007_1f6f632a.jpg

This is a binary file of the type: Image

# images/Denzel Washington/008_7619a328.jpg

This is a binary file of the type: Image

# images/Denzel Washington/009_817304c7.jpg

This is a binary file of the type: Image

# images/Denzel Washington/010_47031d88.jpg

This is a binary file of the type: Image

# images/Denzel Washington/011_c2d9c2a1.jpg

This is a binary file of the type: Image

# images/Denzel Washington/012_6b8f22bf.jpg

This is a binary file of the type: Image

# images/Denzel Washington/013_5928728c.jpg

This is a binary file of the type: Image

# images/Denzel Washington/014_9742cf0f.jpg

This is a binary file of the type: Image

# images/Denzel Washington/015_72bb2861.jpg

This is a binary file of the type: Image

# images/Denzel Washington/016_61188e3c.jpg

This is a binary file of the type: Image

# images/Denzel Washington/017_f308fc36.jpg

This is a binary file of the type: Image

# images/Denzel Washington/018_e4ed6557.jpg

This is a binary file of the type: Image

# images/Denzel Washington/019_330f0c75.jpg

This is a binary file of the type: Image

# images/Denzel Washington/020_9f8446bb.jpg

This is a binary file of the type: Image

# images/Denzel Washington/021_8295d645.jpg

This is a binary file of the type: Image

# images/Denzel Washington/022_b60724f6.jpg

This is a binary file of the type: Image

# images/Denzel Washington/023_75fd6b60.jpg

This is a binary file of the type: Image

# images/Denzel Washington/024_54153da7.jpg

This is a binary file of the type: Image

# images/Denzel Washington/025_61e2c5e5.jpg

This is a binary file of the type: Image

# images/Denzel Washington/026_2f832037.jpg

This is a binary file of the type: Image

# images/Denzel Washington/027_c7a10f8d.jpg

This is a binary file of the type: Image

# images/Denzel Washington/028_29634e07.jpg

This is a binary file of the type: Image

# images/Denzel Washington/029_cf7e7736.jpg

This is a binary file of the type: Image

# images/Denzel Washington/030_90c3e21e.jpg

This is a binary file of the type: Image

# images/Denzel Washington/031_2fe075a5.jpg

This is a binary file of the type: Image

# images/Denzel Washington/032_a67c5aa8.jpg

This is a binary file of the type: Image

# images/Denzel Washington/033_f49a691c.jpg

This is a binary file of the type: Image

# images/Denzel Washington/034_e09c630c.jpg

This is a binary file of the type: Image

# images/Denzel Washington/035_014caeb7.jpg

This is a binary file of the type: Image

# images/Denzel Washington/036_7ec2e5de.jpg

This is a binary file of the type: Image

# images/Denzel Washington/037_39f2db43.jpg

This is a binary file of the type: Image

# images/Denzel Washington/038_d967a9c7.jpg

This is a binary file of the type: Image

# images/Denzel Washington/039_faa6425d.jpg

This is a binary file of the type: Image

# images/Denzel Washington/040_e534b74f.jpg

This is a binary file of the type: Image

# images/Denzel Washington/041_c8998bae.jpg

This is a binary file of the type: Image

# images/Denzel Washington/042_b0c87dc0.jpg

This is a binary file of the type: Image

# images/Denzel Washington/043_9bfd94a4.jpg

This is a binary file of the type: Image

# images/Denzel Washington/044_c38d661d.jpg

This is a binary file of the type: Image

# images/Denzel Washington/045_60fc8dc5.jpg

This is a binary file of the type: Image

# images/Denzel Washington/046_b67077e0.jpg

This is a binary file of the type: Image

# images/Denzel Washington/047_05f6a63f.jpg

This is a binary file of the type: Image

# images/Denzel Washington/048_cd8dc27d.jpg

This is a binary file of the type: Image

# images/Denzel Washington/049_40f1ba49.jpg

This is a binary file of the type: Image

# images/Denzel Washington/050_a5810700.jpg

This is a binary file of the type: Image

# images/Denzel Washington/051_d27cd673.jpg

This is a binary file of the type: Image

# images/Denzel Washington/052_244a9729.jpg

This is a binary file of the type: Image

# images/Denzel Washington/053_4f937ab4.jpg

This is a binary file of the type: Image

# images/Denzel Washington/054_b8e917f6.jpg

This is a binary file of the type: Image

# images/Denzel Washington/055_fbbcb3c7.jpg

This is a binary file of the type: Image

# images/Denzel Washington/056_ccaa5638.jpg

This is a binary file of the type: Image

# images/Denzel Washington/057_ce4bc775.jpg

This is a binary file of the type: Image

# images/Denzel Washington/058_3743cf7d.jpg

This is a binary file of the type: Image

# images/Denzel Washington/059_3b848154.jpg

This is a binary file of the type: Image

# images/Denzel Washington/060_fa55e260.jpg

This is a binary file of the type: Image

# images/Denzel Washington/061_6bf34908.jpg

This is a binary file of the type: Image

# images/Denzel Washington/062_f1f905e2.jpg

This is a binary file of the type: Image

# images/Denzel Washington/063_7656840a.jpg

This is a binary file of the type: Image

# images/Denzel Washington/064_b2ccbaf6.jpg

This is a binary file of the type: Image

# images/Denzel Washington/065_b2b4591d.jpg

This is a binary file of the type: Image

# images/Denzel Washington/066_0411d529.jpg

This is a binary file of the type: Image

# images/Denzel Washington/067_ee6435dc.jpg

This is a binary file of the type: Image

# images/Denzel Washington/068_d9509f11.jpg

This is a binary file of the type: Image

# images/Denzel Washington/069_37296c7d.jpg

This is a binary file of the type: Image

# images/Denzel Washington/070_8020c2b5.jpg

This is a binary file of the type: Image

# images/Denzel Washington/071_30155b02.jpg

This is a binary file of the type: Image

# images/Denzel Washington/072_648a84c5.jpg

This is a binary file of the type: Image

# images/Denzel Washington/073_2880f59c.jpg

This is a binary file of the type: Image

# images/Denzel Washington/074_2a4ca70b.jpg

This is a binary file of the type: Image

# images/Denzel Washington/075_b5f2a9e5.jpg

This is a binary file of the type: Image

# images/Denzel Washington/076_7dd9c0bd.jpg

This is a binary file of the type: Image

# images/Denzel Washington/077_a0ceecbd.jpg

This is a binary file of the type: Image

# images/Denzel Washington/078_8a19b2b4.jpg

This is a binary file of the type: Image

# images/Denzel Washington/079_b055b519.jpg

This is a binary file of the type: Image

# images/Denzel Washington/080_42f1d0a7.jpg

This is a binary file of the type: Image

# images/Denzel Washington/081_7e097924.jpg

This is a binary file of the type: Image

# images/Denzel Washington/082_359c4774.jpg

This is a binary file of the type: Image

# images/Denzel Washington/083_9436dbb0.jpg

This is a binary file of the type: Image

# images/Denzel Washington/084_43b55cdf.jpg

This is a binary file of the type: Image

# images/Denzel Washington/085_8366382f.jpg

This is a binary file of the type: Image

# images/Denzel Washington/086_8eefe9d0.jpg

This is a binary file of the type: Image

# images/Denzel Washington/087_cec971ab.jpg

This is a binary file of the type: Image

# images/Denzel Washington/088_fb4a5e01.jpg

This is a binary file of the type: Image

# images/Denzel Washington/089_2539e4d9.jpg

This is a binary file of the type: Image

# images/Denzel Washington/090_2f85a193.jpg

This is a binary file of the type: Image

# images/Denzel Washington/091_cc106747.jpg

This is a binary file of the type: Image

# images/Denzel Washington/092_8f204d71.jpg

This is a binary file of the type: Image

# images/Denzel Washington/093_4027b1e2.jpg

This is a binary file of the type: Image

# images/Denzel Washington/094_7858a9ff.jpg

This is a binary file of the type: Image

# images/Denzel Washington/095_0a05b6dc.jpg

This is a binary file of the type: Image

# images/Denzel Washington/096_9ff8b67f.jpg

This is a binary file of the type: Image

# images/Denzel Washington/097_b745e092.jpg

This is a binary file of the type: Image

# images/Denzel Washington/098_1559ae78.jpg

This is a binary file of the type: Image

# images/Denzel Washington/099_b7d16411.jpg

This is a binary file of the type: Image

# images/Denzel Washington/100_26562919.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/001_9adc92c2.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/002_85eab275.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/003_8889ec2c.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/004_41caa173.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/005_3ba56da0.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/006_ff6876d9.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/007_68abd54d.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/008_d5553651.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/009_11c22a3b.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/010_cce39614.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/011_17b8991d.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/012_b33b05c6.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/013_025c288f.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/014_07f2f9cb.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/015_186b4bbf.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/016_e319349e.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/017_fad27cd4.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/018_3bdca9f6.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/019_2d261ea3.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/020_edd8803c.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/021_4d5264fd.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/022_9b0e7dc8.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/023_53e3d0b3.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/024_2a9dc3ca.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/025_31c04ded.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/026_4e67d826.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/027_ded82a08.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/028_7214d33e.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/029_c6e0a7f3.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/030_c2291830.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/031_e8d3b475.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/032_0e6a520a.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/033_06f1823f.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/034_09baeb19.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/035_79812fd1.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/036_0be99621.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/037_f5b8733a.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/038_69b748e3.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/039_80446065.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/040_4baf02be.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/041_efeaa4c3.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/042_31710794.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/043_1d38d614.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/044_1844df0f.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/045_24b44c3d.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/046_de6d6bf0.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/047_54ea04fa.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/048_9d5874a5.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/049_beaf3777.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/050_509d326a.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/051_12956682.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/052_f394c931.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/053_62909c7b.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/054_4274a548.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/055_bfeb8aab.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/056_11835953.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/057_6aecaa18.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/058_48dcb96c.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/059_aef6a0a8.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/060_2b7fbba5.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/061_2de5a089.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/062_5db87e94.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/063_6f1c7f3e.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/064_12d52b76.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/065_db7b31f5.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/066_03ff28be.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/067_296269c3.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/068_474081ea.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/069_429fc9ee.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/070_e88788cd.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/071_071d0cfc.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/072_c6df94c3.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/073_812b8d10.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/074_d205687c.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/075_31d85976.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/076_b53060b4.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/077_08ff1da6.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/078_fd557ae2.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/079_dbb72b1d.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/080_52addc92.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/081_9f4d7bcb.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/082_bf5ea9df.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/083_3ab573ea.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/084_c4bb2e0e.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/085_394c2c3c.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/086_269deff5.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/087_7f9336ac.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/088_2ec116fe.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/089_a49ffdf2.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/090_916ba69a.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/091_2ace2ad8.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/092_4e8dad7c.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/093_4faba724.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/094_bcb2a8f4.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/095_b464eda0.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/096_b2e35bd2.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/097_21a9bff5.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/098_5cb67f9d.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/099_8a31fcb9.jpg

This is a binary file of the type: Image

# images/Hugh Jackman/100_1ea80814.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/001_21a7d5e6.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/002_533748b2.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/003_963a3627.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/004_94f26ed9.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/005_7f198c47.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/006_2d0dccd4.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/007_72ad75ba.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/008_35fbbb0c.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/009_bcd380a7.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/010_34d63b53.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/011_8c50c05f.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/012_12d61e14.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/013_78060c8a.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/014_0100b141.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/015_48a3c3ec.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/016_d731baf7.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/017_b67e0915.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/018_2974b20a.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/019_ab6f69c3.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/020_5a08581b.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/021_2eaafb9f.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/022_e214ba9f.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/023_5bc0c09d.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/024_bfe8d1d4.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/025_f5a5036b.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/026_cf5be1f1.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/027_3290d1bc.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/028_7191558a.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/029_7cc8d551.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/030_4f246d8f.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/031_0785344e.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/032_bed86546.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/033_c27f428c.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/034_de792370.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/035_39bf8fcb.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/036_e76dcff2.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/037_46ec39ce.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/038_ca50cc93.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/039_f2610531.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/040_b392a367.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/041_54a9280d.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/042_db56b563.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/043_cccb0e88.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/044_2619e688.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/045_9f391be6.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/046_7a3818f6.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/047_6e08a927.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/048_2646d85d.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/049_d3ba5c55.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/050_f545b0ea.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/051_2aace444.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/052_f7f4e937.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/053_235dbe3b.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/054_cc2a9231.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/055_7b8dfc3a.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/056_f22ab393.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/057_3911a64f.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/058_a8b460e9.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/059_dd54feaf.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/060_bb963eed.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/061_2306ab5b.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/062_99dd69cb.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/063_67d7dfda.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/064_3e07b8f6.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/065_0dc771a5.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/066_4c979163.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/067_2cd39306.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/068_9718f48b.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/069_bdd7c91d.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/070_d8f59abc.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/071_70e7bd88.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/072_47470694.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/073_2c17626c.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/074_ed2be25f.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/075_5a5afdfa.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/076_caf65a53.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/077_0fd24d01.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/078_d1d62b6f.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/079_cf4c7dee.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/080_7e43a953.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/081_132549cb.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/082_2251d7b7.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/083_c22f1140.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/084_0f0f27e4.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/085_b2827d47.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/086_7ddf4f90.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/087_2fd20b9a.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/088_1229c0dd.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/089_152cf5f6.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/090_14fe77d5.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/091_e8f3497f.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/092_aebdc10e.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/093_07692aea.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/094_c0a66044.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/095_0ccffcb8.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/096_a0626390.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/097_f19b4cfc.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/098_fa237ecc.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/099_384306de.jpg

This is a binary file of the type: Image

# images/Jennifer Lawrence/100_6882dc21.jpg

This is a binary file of the type: Image

# images/Johnny Depp/001_2288a4f6.jpg

This is a binary file of the type: Image

# images/Johnny Depp/002_331d0423.jpg

This is a binary file of the type: Image

# images/Johnny Depp/003_64926b97.jpg

This is a binary file of the type: Image

# images/Johnny Depp/004_18e08ab4.jpg

This is a binary file of the type: Image

# images/Johnny Depp/005_9406f32d.jpg

This is a binary file of the type: Image

# images/Johnny Depp/006_8fc31fd7.jpg

This is a binary file of the type: Image

# images/Johnny Depp/007_1bc0bcd6.jpg

This is a binary file of the type: Image

# images/Johnny Depp/008_35d1be70.jpg

This is a binary file of the type: Image

# images/Johnny Depp/009_f4a38fec.jpg

This is a binary file of the type: Image

# images/Johnny Depp/010_610eea60.jpg

This is a binary file of the type: Image

# images/Johnny Depp/011_c826a613.jpg

This is a binary file of the type: Image

# images/Johnny Depp/012_563f0843.jpg

This is a binary file of the type: Image

# images/Johnny Depp/013_f44c68a1.jpg

This is a binary file of the type: Image

# images/Johnny Depp/014_68248214.jpg

This is a binary file of the type: Image

# images/Johnny Depp/015_0474556e.jpg

This is a binary file of the type: Image

# images/Johnny Depp/016_8b4d3698.jpg

This is a binary file of the type: Image

# images/Johnny Depp/017_aadefe7b.jpg

This is a binary file of the type: Image

# images/Johnny Depp/018_14e5366f.jpg

This is a binary file of the type: Image

# images/Johnny Depp/019_3eb26944.jpg

This is a binary file of the type: Image

# images/Johnny Depp/020_6b7d8470.jpg

This is a binary file of the type: Image

# images/Johnny Depp/021_9ab18f1b.jpg

This is a binary file of the type: Image

# images/Johnny Depp/022_a0763313.jpg

This is a binary file of the type: Image

# images/Johnny Depp/023_4e454f96.jpg

This is a binary file of the type: Image

# images/Johnny Depp/024_bfac5f5b.jpg

This is a binary file of the type: Image

# images/Johnny Depp/025_4f2ec7c1.jpg

This is a binary file of the type: Image

# images/Johnny Depp/026_20c41942.jpg

This is a binary file of the type: Image

# images/Johnny Depp/027_2eab41f9.jpg

This is a binary file of the type: Image

# images/Johnny Depp/028_ce59b46d.jpg

This is a binary file of the type: Image

# images/Johnny Depp/029_30aec656.jpg

This is a binary file of the type: Image

# images/Johnny Depp/030_ddacf348.jpg

This is a binary file of the type: Image

# images/Johnny Depp/031_86ed9fca.jpg

This is a binary file of the type: Image

# images/Johnny Depp/032_4b3ee537.jpg

This is a binary file of the type: Image

# images/Johnny Depp/033_ef398d45.jpg

This is a binary file of the type: Image

# images/Johnny Depp/034_52d180f0.jpg

This is a binary file of the type: Image

# images/Johnny Depp/035_2a1b8bcf.jpg

This is a binary file of the type: Image

# images/Johnny Depp/036_c93144a5.jpg

This is a binary file of the type: Image

# images/Johnny Depp/037_f2fb045b.jpg

This is a binary file of the type: Image

# images/Johnny Depp/038_081386a5.jpg

This is a binary file of the type: Image

# images/Johnny Depp/039_13af66c8.jpg

This is a binary file of the type: Image

# images/Johnny Depp/040_2e8934ea.jpg

This is a binary file of the type: Image

# images/Johnny Depp/041_6ec992c9.jpg

This is a binary file of the type: Image

# images/Johnny Depp/042_05ce6c69.jpg

This is a binary file of the type: Image

# images/Johnny Depp/043_77e393de.jpg

This is a binary file of the type: Image

# images/Johnny Depp/044_18b89b8d.jpg

This is a binary file of the type: Image

# images/Johnny Depp/045_865604b0.jpg

This is a binary file of the type: Image

# images/Johnny Depp/046_31d6a7d8.jpg

This is a binary file of the type: Image

# images/Johnny Depp/047_6c6a66d2.jpg

This is a binary file of the type: Image

# images/Johnny Depp/048_8af82c54.jpg

This is a binary file of the type: Image

# images/Johnny Depp/049_9254f6f2.jpg

This is a binary file of the type: Image

# images/Johnny Depp/050_6641bd32.jpg

This is a binary file of the type: Image

# images/Johnny Depp/051_2505e244.jpg

This is a binary file of the type: Image

# images/Johnny Depp/052_e2e5ef6b.jpg

This is a binary file of the type: Image

# images/Johnny Depp/053_5b42d9d9.jpg

This is a binary file of the type: Image

# images/Johnny Depp/054_50f42b56.jpg

This is a binary file of the type: Image

# images/Johnny Depp/055_cf9af56c.jpg

This is a binary file of the type: Image

# images/Johnny Depp/056_c5e6243c.jpg

This is a binary file of the type: Image

# images/Johnny Depp/057_ee633567.jpg

This is a binary file of the type: Image

# images/Johnny Depp/058_7e4aeab8.jpg

This is a binary file of the type: Image

# images/Johnny Depp/059_27a0e6f1.jpg

This is a binary file of the type: Image

# images/Johnny Depp/060_3cf86eaf.jpg

This is a binary file of the type: Image

# images/Johnny Depp/061_4544a552.jpg

This is a binary file of the type: Image

# images/Johnny Depp/062_23b3470a.jpg

This is a binary file of the type: Image

# images/Johnny Depp/063_bdcf4753.jpg

This is a binary file of the type: Image

# images/Johnny Depp/064_aa733f0c.jpg

This is a binary file of the type: Image

# images/Johnny Depp/065_6f1ed846.jpg

This is a binary file of the type: Image

# images/Johnny Depp/066_653f2a94.jpg

This is a binary file of the type: Image

# images/Johnny Depp/067_5234e510.jpg

This is a binary file of the type: Image

# images/Johnny Depp/068_006344c5.jpg

This is a binary file of the type: Image

# images/Johnny Depp/069_2b2270ce.jpg

This is a binary file of the type: Image

# images/Johnny Depp/070_1e22daa2.jpg

This is a binary file of the type: Image

# images/Johnny Depp/071_d3036d43.jpg

This is a binary file of the type: Image

# images/Johnny Depp/072_f2c8b6e9.jpg

This is a binary file of the type: Image

# images/Johnny Depp/073_71584704.jpg

This is a binary file of the type: Image

# images/Johnny Depp/074_bd6f3a84.jpg

This is a binary file of the type: Image

# images/Johnny Depp/075_21e87f0f.jpg

This is a binary file of the type: Image

# images/Johnny Depp/076_b28d1fac.jpg

This is a binary file of the type: Image

# images/Johnny Depp/077_5cbf1ecc.jpg

This is a binary file of the type: Image

# images/Johnny Depp/078_b7114bcb.jpg

This is a binary file of the type: Image

# images/Johnny Depp/079_241963dc.jpg

This is a binary file of the type: Image

# images/Johnny Depp/080_38c2109a.jpg

This is a binary file of the type: Image

# images/Johnny Depp/081_059a278c.jpg

This is a binary file of the type: Image

# images/Johnny Depp/082_742073a1.jpg

This is a binary file of the type: Image

# images/Johnny Depp/083_16b5e7ab.jpg

This is a binary file of the type: Image

# images/Johnny Depp/084_3dcf601a.jpg

This is a binary file of the type: Image

# images/Johnny Depp/085_e9f6ea07.jpg

This is a binary file of the type: Image

# images/Johnny Depp/086_f052c533.jpg

This is a binary file of the type: Image

# images/Johnny Depp/087_f9794152.jpg

This is a binary file of the type: Image

# images/Johnny Depp/088_1fcc7b2c.jpg

This is a binary file of the type: Image

# images/Johnny Depp/089_2f2e823a.jpg

This is a binary file of the type: Image

# images/Johnny Depp/090_c5d1d9eb.jpg

This is a binary file of the type: Image

# images/Johnny Depp/091_c3ad83af.jpg

This is a binary file of the type: Image

# images/Johnny Depp/092_3943353c.jpg

This is a binary file of the type: Image

# images/Johnny Depp/093_8cb84a89.jpg

This is a binary file of the type: Image

# images/Johnny Depp/094_42a45a8d.jpg

This is a binary file of the type: Image

# images/Johnny Depp/095_233dc3f2.jpg

This is a binary file of the type: Image

# images/Johnny Depp/096_78a5a076.jpg

This is a binary file of the type: Image

# images/Johnny Depp/097_11415581.jpg

This is a binary file of the type: Image

# images/Johnny Depp/098_16b30dda.jpg

This is a binary file of the type: Image

# images/Johnny Depp/099_d88c0793.jpg

This is a binary file of the type: Image

# images/Johnny Depp/100_120c14bc.jpg

This is a binary file of the type: Image

# images/Kate Winslet/001_5992faf7.jpg

This is a binary file of the type: Image

# images/Kate Winslet/002_590bb980.jpg

This is a binary file of the type: Image

# images/Kate Winslet/003_acb20793.jpg

This is a binary file of the type: Image

# images/Kate Winslet/004_0816d969.jpg

This is a binary file of the type: Image

# images/Kate Winslet/005_93b2fce9.jpg

This is a binary file of the type: Image

# images/Kate Winslet/006_eda1948f.jpg

This is a binary file of the type: Image

# images/Kate Winslet/007_572cf58c.jpg

This is a binary file of the type: Image

# images/Kate Winslet/008_6c01eb52.jpg

This is a binary file of the type: Image

# images/Kate Winslet/009_07c15c37.jpg

This is a binary file of the type: Image

# images/Kate Winslet/010_6102c83d.jpg

This is a binary file of the type: Image

# images/Kate Winslet/011_dbc62ba7.jpg

This is a binary file of the type: Image

# images/Kate Winslet/012_a2bb90dc.jpg

This is a binary file of the type: Image

# images/Kate Winslet/013_b59e4acc.jpg

This is a binary file of the type: Image

# images/Kate Winslet/014_76fd590c.jpg

This is a binary file of the type: Image

# images/Kate Winslet/015_3a0f9ec8.jpg

This is a binary file of the type: Image

# images/Kate Winslet/016_211776b6.jpg

This is a binary file of the type: Image

# images/Kate Winslet/017_fb53f84d.jpg

This is a binary file of the type: Image

# images/Kate Winslet/018_738a56fd.jpg

This is a binary file of the type: Image

# images/Kate Winslet/019_4402a7fe.jpg

This is a binary file of the type: Image

# images/Kate Winslet/020_a7a653f4.jpg

This is a binary file of the type: Image

# images/Kate Winslet/021_40180588.jpg

This is a binary file of the type: Image

# images/Kate Winslet/022_6cc0e508.jpg

This is a binary file of the type: Image

# images/Kate Winslet/023_06dbacd1.jpg

This is a binary file of the type: Image

# images/Kate Winslet/024_cc39b61d.jpg

This is a binary file of the type: Image

# images/Kate Winslet/025_0131eaa3.jpg

This is a binary file of the type: Image

# images/Kate Winslet/026_92cdfd7c.jpg

This is a binary file of the type: Image

# images/Kate Winslet/027_f8cd6e70.jpg

This is a binary file of the type: Image

# images/Kate Winslet/028_669aab36.jpg

This is a binary file of the type: Image

# images/Kate Winslet/029_890b58a4.jpg

This is a binary file of the type: Image

# images/Kate Winslet/030_92cca8fa.jpg

This is a binary file of the type: Image

# images/Kate Winslet/031_a92db443.jpg

This is a binary file of the type: Image

# images/Kate Winslet/032_e3bf7f23.jpg

This is a binary file of the type: Image

# images/Kate Winslet/033_c27883e5.jpg

This is a binary file of the type: Image

# images/Kate Winslet/034_60fff082.jpg

This is a binary file of the type: Image

# images/Kate Winslet/035_8e23d941.jpg

This is a binary file of the type: Image

# images/Kate Winslet/036_1533e4ff.jpg

This is a binary file of the type: Image

# images/Kate Winslet/037_895f9cda.jpg

This is a binary file of the type: Image

# images/Kate Winslet/038_74aabb03.jpg

This is a binary file of the type: Image

# images/Kate Winslet/039_1fcf8174.jpg

This is a binary file of the type: Image

# images/Kate Winslet/040_a52339de.jpg

This is a binary file of the type: Image

# images/Kate Winslet/041_79dd00e0.jpg

This is a binary file of the type: Image

# images/Kate Winslet/042_043c0405.jpg

This is a binary file of the type: Image

# images/Kate Winslet/043_f14565e2.jpg

This is a binary file of the type: Image

# images/Kate Winslet/044_c2d670fb.jpg

This is a binary file of the type: Image

# images/Kate Winslet/045_c36430d1.jpg

This is a binary file of the type: Image

# images/Kate Winslet/046_1086f507.jpg

This is a binary file of the type: Image

# images/Kate Winslet/047_c6dd0c78.jpg

This is a binary file of the type: Image

# images/Kate Winslet/048_453e6cb3.jpg

This is a binary file of the type: Image

# images/Kate Winslet/049_6cf6b364.jpg

This is a binary file of the type: Image

# images/Kate Winslet/050_0c20b215.jpg

This is a binary file of the type: Image

# images/Kate Winslet/051_06409457.jpg

This is a binary file of the type: Image

# images/Kate Winslet/052_0d214eb0.jpg

This is a binary file of the type: Image

# images/Kate Winslet/053_e8b9dd3f.jpg

This is a binary file of the type: Image

# images/Kate Winslet/054_ca0da4ca.jpg

This is a binary file of the type: Image

# images/Kate Winslet/055_30dc3531.jpg

This is a binary file of the type: Image

# images/Kate Winslet/056_64fde18d.jpg

This is a binary file of the type: Image

# images/Kate Winslet/057_b1a0b23b.jpg

This is a binary file of the type: Image

# images/Kate Winslet/058_7f95baf4.jpg

This is a binary file of the type: Image

# images/Kate Winslet/059_089c6dcd.jpg

This is a binary file of the type: Image

# images/Kate Winslet/060_58b1413c.jpg

This is a binary file of the type: Image

# images/Kate Winslet/061_9885f065.jpg

This is a binary file of the type: Image

# images/Kate Winslet/062_92c7c5ef.jpg

This is a binary file of the type: Image

# images/Kate Winslet/063_c6f8603d.jpg

This is a binary file of the type: Image

# images/Kate Winslet/064_1b7da2f6.jpg

This is a binary file of the type: Image

# images/Kate Winslet/065_86617a5e.jpg

This is a binary file of the type: Image

# images/Kate Winslet/066_9c2fdc93.jpg

This is a binary file of the type: Image

# images/Kate Winslet/067_fb02357d.jpg

This is a binary file of the type: Image

# images/Kate Winslet/068_712660e4.jpg

This is a binary file of the type: Image

# images/Kate Winslet/069_591ac4fc.jpg

This is a binary file of the type: Image

# images/Kate Winslet/070_257cc94f.jpg

This is a binary file of the type: Image

# images/Kate Winslet/071_6e010995.jpg

This is a binary file of the type: Image

# images/Kate Winslet/072_5372b2f8.jpg

This is a binary file of the type: Image

# images/Kate Winslet/073_f39658d0.jpg

This is a binary file of the type: Image

# images/Kate Winslet/074_a880665b.jpg

This is a binary file of the type: Image

# images/Kate Winslet/075_98fb973f.jpg

This is a binary file of the type: Image

# images/Kate Winslet/076_2e9c4a35.jpg

This is a binary file of the type: Image

# images/Kate Winslet/077_9bcf9b8c.jpg

This is a binary file of the type: Image

# images/Kate Winslet/078_d36c2be3.jpg

This is a binary file of the type: Image

# images/Kate Winslet/079_898bcd6c.jpg

This is a binary file of the type: Image

# images/Kate Winslet/080_40110c00.jpg

This is a binary file of the type: Image

# images/Kate Winslet/081_e9a7882a.jpg

This is a binary file of the type: Image

# images/Kate Winslet/082_4bbff9c3.jpg

This is a binary file of the type: Image

# images/Kate Winslet/083_a685594b.jpg

This is a binary file of the type: Image

# images/Kate Winslet/084_25462eb9.jpg

This is a binary file of the type: Image

# images/Kate Winslet/085_c957f9b7.jpg

This is a binary file of the type: Image

# images/Kate Winslet/086_c7665b8f.jpg

This is a binary file of the type: Image

# images/Kate Winslet/087_4ec19123.jpg

This is a binary file of the type: Image

# images/Kate Winslet/088_f6c2c5d2.jpg

This is a binary file of the type: Image

# images/Kate Winslet/089_16077370.jpg

This is a binary file of the type: Image

# images/Kate Winslet/090_f67e981f.jpg

This is a binary file of the type: Image

# images/Kate Winslet/091_930fe784.jpg

This is a binary file of the type: Image

# images/Kate Winslet/092_7716bdbb.jpg

This is a binary file of the type: Image

# images/Kate Winslet/093_4876af22.jpg

This is a binary file of the type: Image

# images/Kate Winslet/094_b043e45c.jpg

This is a binary file of the type: Image

# images/Kate Winslet/095_8ffab61d.jpg

This is a binary file of the type: Image

# images/Kate Winslet/096_32a79dde.jpg

This is a binary file of the type: Image

# images/Kate Winslet/097_51a924c1.jpg

This is a binary file of the type: Image

# images/Kate Winslet/098_f4f39b7c.jpg

This is a binary file of the type: Image

# images/Kate Winslet/099_61c7b659.jpg

This is a binary file of the type: Image

# images/Kate Winslet/100_6cee7c73.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/001_08194468.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/002_86e8aa58.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/003_85990366.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/004_af012af1.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/005_7fe5b764.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/006_30010640.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/007_6ca7c622.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/008_35daa4bc.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/009_b86449f6.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/010_2f9c83bc.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/011_0549f94d.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/012_d7aea1e6.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/013_ca6af517.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/014_539eee38.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/015_2872d02b.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/016_7b57be6a.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/017_51311450.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/018_2c458568.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/019_78627223.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/020_14f28bc8.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/021_eecdee92.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/022_66e94346.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/023_0367d72c.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/024_bf83d073.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/025_e5920270.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/026_ecbdaaa7.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/027_7094e195.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/028_38a65d29.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/029_8522ebc8.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/030_60acb78e.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/031_28a211fc.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/032_00aee064.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/033_312ea9ed.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/034_00c6d43e.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/035_ab7cf1c4.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/036_f5ea9e84.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/037_fe4d2d8f.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/038_b52784d4.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/039_d49e8191.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/040_3a2c98cd.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/041_c91b0923.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/042_bfbfd7d8.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/043_93a5e582.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/044_f13caf17.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/045_d074e61c.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/046_db08e5f7.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/047_ce57f03b.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/048_f82caaae.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/049_37f969c1.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/050_e7bdecc0.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/051_38196d60.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/052_74c7be90.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/053_8bfac05e.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/054_1de20f77.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/055_ba4ace00.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/056_13edab75.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/057_f0c37eee.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/058_0a6c61e9.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/059_1027f3c2.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/060_668ebb3f.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/061_57c86521.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/062_67f50ec4.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/063_55002ecd.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/064_397fd4d4.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/065_e739f721.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/066_f048ba09.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/067_a0efbd88.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/068_a703f85f.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/069_b5219746.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/070_ae3a4fa0.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/071_a052296d.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/072_c887ec5c.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/073_42e32f65.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/074_2b2a84b6.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/075_c2c28553.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/076_6fca3a0c.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/077_cd8dcf22.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/078_a7fd9be1.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/079_6ec91919.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/080_2bffea0b.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/081_a32678db.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/082_d797cdf3.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/083_f80d8a01.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/085_a292bf25.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/086_a1441427.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/087_1382b266.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/088_41213f8b.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/089_8e7757ef.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/090_b316be20.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/091_e39f525d.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/092_cbc6d525.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/093_811dc474.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/094_78e0fb7b.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/095_7ffaffe6.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/096_c30a9446.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/097_1837d89e.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/098_f0bc37c7.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/099_c25b7b04.jpg

This is a binary file of the type: Image

# images/Leonardo DiCaprio/100_ec9fe97f.jpg

This is a binary file of the type: Image

# images/Megan Fox/001_dfb62d96.jpg

This is a binary file of the type: Image

# images/Megan Fox/002_6e289116.jpg

This is a binary file of the type: Image

# images/Megan Fox/003_61dd1e53.jpg

This is a binary file of the type: Image

# images/Megan Fox/004_6aede3d3.jpg

This is a binary file of the type: Image

# images/Megan Fox/005_9574c208.jpg

This is a binary file of the type: Image

# images/Megan Fox/006_4e33c943.jpg

This is a binary file of the type: Image

# images/Megan Fox/007_e3073d58.jpg

This is a binary file of the type: Image

# images/Megan Fox/008_74bda018.jpg

This is a binary file of the type: Image

# images/Megan Fox/009_3283c30e.jpg

This is a binary file of the type: Image

# images/Megan Fox/010_0479e335.jpg

This is a binary file of the type: Image

# images/Megan Fox/011_b2354fd0.jpg

This is a binary file of the type: Image

# images/Megan Fox/012_d461a2b5.jpg

This is a binary file of the type: Image

# images/Megan Fox/013_f4968d00.jpg

This is a binary file of the type: Image

# images/Megan Fox/014_d6e920d4.jpg

This is a binary file of the type: Image

# images/Megan Fox/015_b4a21d28.jpg

This is a binary file of the type: Image

# images/Megan Fox/016_bd51d057.jpg

This is a binary file of the type: Image

# images/Megan Fox/017_eed36648.jpg

This is a binary file of the type: Image

# images/Megan Fox/018_394cfad7.jpg

This is a binary file of the type: Image

# images/Megan Fox/019_8e696057.jpg

This is a binary file of the type: Image

# images/Megan Fox/020_467a9bd7.jpg

This is a binary file of the type: Image

# images/Megan Fox/021_2d9dd3a2.jpg

This is a binary file of the type: Image

# images/Megan Fox/022_784eea3c.jpg

This is a binary file of the type: Image

# images/Megan Fox/023_55dd20e3.jpg

This is a binary file of the type: Image

# images/Megan Fox/024_2c2a7324.jpg

This is a binary file of the type: Image

# images/Megan Fox/025_b7dee9f2.jpg

This is a binary file of the type: Image

# images/Megan Fox/026_9ebf29ab.jpg

This is a binary file of the type: Image

# images/Megan Fox/027_308c9885.jpg

This is a binary file of the type: Image

# images/Megan Fox/028_44417c0b.jpg

This is a binary file of the type: Image

# images/Megan Fox/029_19296e1d.jpg

This is a binary file of the type: Image

# images/Megan Fox/030_02e7f231.jpg

This is a binary file of the type: Image

# images/Megan Fox/031_d719ba67.jpg

This is a binary file of the type: Image

# images/Megan Fox/032_4feb9977.jpg

This is a binary file of the type: Image

# images/Megan Fox/033_4e5edeac.jpg

This is a binary file of the type: Image

# images/Megan Fox/034_27326b4e.jpg

This is a binary file of the type: Image

# images/Megan Fox/035_21c88485.jpg

This is a binary file of the type: Image

# images/Megan Fox/036_e61191e5.jpg

This is a binary file of the type: Image

# images/Megan Fox/037_f01637d6.jpg

This is a binary file of the type: Image

# images/Megan Fox/038_fe7a12d1.jpg

This is a binary file of the type: Image

# images/Megan Fox/039_45475171.jpg

This is a binary file of the type: Image

# images/Megan Fox/040_11ad3b6e.jpg

This is a binary file of the type: Image

# images/Megan Fox/041_139bb2a5.jpg

This is a binary file of the type: Image

# images/Megan Fox/042_870cbd50.jpg

This is a binary file of the type: Image

# images/Megan Fox/043_8ab0e1e6.jpg

This is a binary file of the type: Image

# images/Megan Fox/044_bad2076f.jpg

This is a binary file of the type: Image

# images/Megan Fox/045_22823571.jpg

This is a binary file of the type: Image

# images/Megan Fox/046_953d292e.jpg

This is a binary file of the type: Image

# images/Megan Fox/047_3043a87c.jpg

This is a binary file of the type: Image

# images/Megan Fox/048_aae58619.jpg

This is a binary file of the type: Image

# images/Megan Fox/049_2efe85b0.jpg

This is a binary file of the type: Image

# images/Megan Fox/050_b4742a63.jpg

This is a binary file of the type: Image

# images/Megan Fox/051_d62b71ee.jpg

This is a binary file of the type: Image

# images/Megan Fox/052_3f3b6764.jpg

This is a binary file of the type: Image

# images/Megan Fox/053_6ad198c0.jpg

This is a binary file of the type: Image

# images/Megan Fox/054_5a9566eb.jpg

This is a binary file of the type: Image

# images/Megan Fox/055_9508128d.jpg

This is a binary file of the type: Image

# images/Megan Fox/056_ce828b1f.jpg

This is a binary file of the type: Image

# images/Megan Fox/057_d2d179a5.jpg

This is a binary file of the type: Image

# images/Megan Fox/058_1b5b5422.jpg

This is a binary file of the type: Image

# images/Megan Fox/059_d09c7676.jpg

This is a binary file of the type: Image

# images/Megan Fox/060_f5a38fe0.jpg

This is a binary file of the type: Image

# images/Megan Fox/061_d844ec74.jpg

This is a binary file of the type: Image

# images/Megan Fox/062_2539f58f.jpg

This is a binary file of the type: Image

# images/Megan Fox/063_10c723ae.jpg

This is a binary file of the type: Image

# images/Megan Fox/064_61385762.jpg

This is a binary file of the type: Image

# images/Megan Fox/065_016dc8e2.jpg

This is a binary file of the type: Image

# images/Megan Fox/066_50092138.jpg

This is a binary file of the type: Image

# images/Megan Fox/067_4017d5e9.jpg

This is a binary file of the type: Image

# images/Megan Fox/068_b8b844e2.jpg

This is a binary file of the type: Image

# images/Megan Fox/069_0ffb5c63.jpg

This is a binary file of the type: Image

# images/Megan Fox/070_4de04405.jpg

This is a binary file of the type: Image

# images/Megan Fox/071_d75194ff.jpg

This is a binary file of the type: Image

# images/Megan Fox/072_5debf32c.jpg

This is a binary file of the type: Image

# images/Megan Fox/073_b7f93635.jpg

This is a binary file of the type: Image

# images/Megan Fox/074_59a9ebff.jpg

This is a binary file of the type: Image

# images/Megan Fox/075_9b57684f.jpg

This is a binary file of the type: Image

# images/Megan Fox/076_424b03b7.jpg

This is a binary file of the type: Image

# images/Megan Fox/077_de6b59a7.jpg

This is a binary file of the type: Image

# images/Megan Fox/078_6af10def.jpg

This is a binary file of the type: Image

# images/Megan Fox/079_4e33cd00.jpg

This is a binary file of the type: Image

# images/Megan Fox/080_bff10b31.jpg

This is a binary file of the type: Image

# images/Megan Fox/081_f78b8266.jpg

This is a binary file of the type: Image

# images/Megan Fox/082_768aecdd.jpg

This is a binary file of the type: Image

# images/Megan Fox/083_323ae1e8.jpg

This is a binary file of the type: Image

# images/Megan Fox/084_70354863.jpg

This is a binary file of the type: Image

# images/Megan Fox/085_2a0a4182.jpg

This is a binary file of the type: Image

# images/Megan Fox/086_b9831d16.jpg

This is a binary file of the type: Image

# images/Megan Fox/087_90c1dd76.jpg

This is a binary file of the type: Image

# images/Megan Fox/088_29b6bf25.jpg

This is a binary file of the type: Image

# images/Megan Fox/089_ae8644ab.jpg

This is a binary file of the type: Image

# images/Megan Fox/090_a2269658.jpg

This is a binary file of the type: Image

# images/Megan Fox/091_4858eb13.jpg

This is a binary file of the type: Image

# images/Megan Fox/092_bbd39177.jpg

This is a binary file of the type: Image

# images/Megan Fox/093_82a4677f.jpg

This is a binary file of the type: Image

# images/Megan Fox/094_1095eeb6.jpg

This is a binary file of the type: Image

# images/Megan Fox/095_fc25a60b.jpg

This is a binary file of the type: Image

# images/Megan Fox/096_2ca8243d.jpg

This is a binary file of the type: Image

# images/Megan Fox/097_e1dabc00.jpg

This is a binary file of the type: Image

# images/Megan Fox/098_24676238.jpg

This is a binary file of the type: Image

# images/Megan Fox/099_82722976.jpg

This is a binary file of the type: Image

# images/Megan Fox/100_f0e45dd1.jpg

This is a binary file of the type: Image

# images/Natalie Portman/001_9cd1160a.jpg

This is a binary file of the type: Image

# images/Natalie Portman/002_3a2ef5df.jpg

This is a binary file of the type: Image

# images/Natalie Portman/003_13b7bb9d.jpg

This is a binary file of the type: Image

# images/Natalie Portman/004_09c5d285.jpg

This is a binary file of the type: Image

# images/Natalie Portman/005_f8b76ad5.jpg

This is a binary file of the type: Image

# images/Natalie Portman/006_51ad8fdd.jpg

This is a binary file of the type: Image

# images/Natalie Portman/007_b82eb947.jpg

This is a binary file of the type: Image

# images/Natalie Portman/008_8fc20495.jpg

This is a binary file of the type: Image

# images/Natalie Portman/009_3300e98f.jpg

This is a binary file of the type: Image

# images/Natalie Portman/010_9f899833.jpg

This is a binary file of the type: Image

# images/Natalie Portman/011_7b37bf1f.jpg

This is a binary file of the type: Image

# images/Natalie Portman/012_36c352b5.jpg

This is a binary file of the type: Image

# images/Natalie Portman/013_46b35530.jpg

This is a binary file of the type: Image

# images/Natalie Portman/014_2c325a73.jpg

This is a binary file of the type: Image

# images/Natalie Portman/015_d425c0eb.jpg

This is a binary file of the type: Image

# images/Natalie Portman/016_b170ab55.jpg

This is a binary file of the type: Image

# images/Natalie Portman/017_22f7f808.jpg

This is a binary file of the type: Image

# images/Natalie Portman/018_cadc0487.jpg

This is a binary file of the type: Image

# images/Natalie Portman/019_58c32d1b.jpg

This is a binary file of the type: Image

# images/Natalie Portman/020_c1a8bc2c.jpg

This is a binary file of the type: Image

# images/Natalie Portman/021_0b9bd77d.jpg

This is a binary file of the type: Image

# images/Natalie Portman/022_0b6f73be.jpg

This is a binary file of the type: Image

# images/Natalie Portman/023_b70934ce.jpg

This is a binary file of the type: Image

# images/Natalie Portman/024_036921f7.jpg

This is a binary file of the type: Image

# images/Natalie Portman/025_c55c4e11.jpg

This is a binary file of the type: Image

# images/Natalie Portman/026_588e5bb5.jpg

This is a binary file of the type: Image

# images/Natalie Portman/027_ffa4c67b.jpg

This is a binary file of the type: Image

# images/Natalie Portman/028_0021b8a3.jpg

This is a binary file of the type: Image

# images/Natalie Portman/029_2f4ca9e5.jpg

This is a binary file of the type: Image

# images/Natalie Portman/030_ff4d2ab8.jpg

This is a binary file of the type: Image

# images/Natalie Portman/031_972f207f.jpg

This is a binary file of the type: Image

# images/Natalie Portman/032_79db7bb4.jpg

This is a binary file of the type: Image

# images/Natalie Portman/033_34c27ce3.jpg

This is a binary file of the type: Image

# images/Natalie Portman/034_c658f190.jpg

This is a binary file of the type: Image

# images/Natalie Portman/035_2238b9ea.jpg

This is a binary file of the type: Image

# images/Natalie Portman/036_b81fcbb5.jpg

This is a binary file of the type: Image

# images/Natalie Portman/037_aa4ba2b1.jpg

This is a binary file of the type: Image

# images/Natalie Portman/038_4930b73f.jpg

This is a binary file of the type: Image

# images/Natalie Portman/039_defb8d63.jpg

This is a binary file of the type: Image

# images/Natalie Portman/040_d80d3727.jpg

This is a binary file of the type: Image

# images/Natalie Portman/041_e75de60a.jpg

This is a binary file of the type: Image

# images/Natalie Portman/042_8168b9f8.jpg

This is a binary file of the type: Image

# images/Natalie Portman/043_a95c3f60.jpg

This is a binary file of the type: Image

# images/Natalie Portman/044_775d6581.jpg

This is a binary file of the type: Image

# images/Natalie Portman/045_2538be49.jpg

This is a binary file of the type: Image

# images/Natalie Portman/046_87ab3cfe.jpg

This is a binary file of the type: Image

# images/Natalie Portman/047_d39de18c.jpg

This is a binary file of the type: Image

# images/Natalie Portman/048_9f118a78.jpg

This is a binary file of the type: Image

# images/Natalie Portman/049_f7490e79.jpg

This is a binary file of the type: Image

# images/Natalie Portman/050_4bfee337.jpg

This is a binary file of the type: Image

# images/Natalie Portman/051_9dbec6e1.jpg

This is a binary file of the type: Image

# images/Natalie Portman/052_f9072013.jpg

This is a binary file of the type: Image

# images/Natalie Portman/053_5b6de4ba.jpg

This is a binary file of the type: Image

# images/Natalie Portman/054_f0cd83d5.jpg

This is a binary file of the type: Image

# images/Natalie Portman/055_39a3d190.jpg

This is a binary file of the type: Image

# images/Natalie Portman/056_666b6673.jpg

This is a binary file of the type: Image

# images/Natalie Portman/057_a633d34a.jpg

This is a binary file of the type: Image

# images/Natalie Portman/058_75c1a7f6.jpg

This is a binary file of the type: Image

# images/Natalie Portman/059_c13d7734.jpg

This is a binary file of the type: Image

# images/Natalie Portman/060_d89f212b.jpg

This is a binary file of the type: Image

# images/Natalie Portman/061_029fc37f.jpg

This is a binary file of the type: Image

# images/Natalie Portman/062_e1d9ac7c.jpg

This is a binary file of the type: Image

# images/Natalie Portman/063_1fb10bab.jpg

This is a binary file of the type: Image

# images/Natalie Portman/064_f261e561.jpg

This is a binary file of the type: Image

# images/Natalie Portman/065_3fcffc66.jpg

This is a binary file of the type: Image

# images/Natalie Portman/066_6d963e5e.jpg

This is a binary file of the type: Image

# images/Natalie Portman/067_706a358a.jpg

This is a binary file of the type: Image

# images/Natalie Portman/068_f1faa56e.jpg

This is a binary file of the type: Image

# images/Natalie Portman/069_c9e3207d.jpg

This is a binary file of the type: Image

# images/Natalie Portman/070_b83e7724.jpg

This is a binary file of the type: Image

# images/Natalie Portman/071_7621368b.jpg

This is a binary file of the type: Image

# images/Natalie Portman/072_7dbad240.jpg

This is a binary file of the type: Image

# images/Natalie Portman/073_dfbed64d.jpg

This is a binary file of the type: Image

# images/Natalie Portman/074_f835bfaf.jpg

This is a binary file of the type: Image

# images/Natalie Portman/075_2b6154c6.jpg

This is a binary file of the type: Image

# images/Natalie Portman/076_2d7a6078.jpg

This is a binary file of the type: Image

# images/Natalie Portman/077_e589a0e2.jpg

This is a binary file of the type: Image

# images/Natalie Portman/078_15befce2.jpg

This is a binary file of the type: Image

# images/Natalie Portman/079_61aaf003.jpg

This is a binary file of the type: Image

# images/Natalie Portman/080_12cefe70.jpg

This is a binary file of the type: Image

# images/Natalie Portman/081_bdc0cced.jpg

This is a binary file of the type: Image

# images/Natalie Portman/082_6883328f.jpg

This is a binary file of the type: Image

# images/Natalie Portman/083_7fc7beca.jpg

This is a binary file of the type: Image

# images/Natalie Portman/084_9db2a724.jpg

This is a binary file of the type: Image

# images/Natalie Portman/085_5abcaccb.jpg

This is a binary file of the type: Image

# images/Natalie Portman/086_e6cb087e.jpg

This is a binary file of the type: Image

# images/Natalie Portman/087_dabfb9e0.jpg

This is a binary file of the type: Image

# images/Natalie Portman/088_c6c7b0b2.jpg

This is a binary file of the type: Image

# images/Natalie Portman/089_7a22dd1d.jpg

This is a binary file of the type: Image

# images/Natalie Portman/090_d2b11902.jpg

This is a binary file of the type: Image

# images/Natalie Portman/091_6985bf33.jpg

This is a binary file of the type: Image

# images/Natalie Portman/092_a67b993f.jpg

This is a binary file of the type: Image

# images/Natalie Portman/093_dbb553bf.jpg

This is a binary file of the type: Image

# images/Natalie Portman/094_6aec42c7.jpg

This is a binary file of the type: Image

# images/Natalie Portman/095_00690f89.jpg

This is a binary file of the type: Image

# images/Natalie Portman/096_e119e862.jpg

This is a binary file of the type: Image

# images/Natalie Portman/097_ec4fe2e9.jpg

This is a binary file of the type: Image

# images/Natalie Portman/098_d82741fc.jpg

This is a binary file of the type: Image

# images/Natalie Portman/099_75aa5bcc.jpg

This is a binary file of the type: Image

# images/Natalie Portman/100_f11d5057.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/001_504d320d.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/002_36285f46.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/003_98a0852a.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/004_3491d187.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/005_0623ac96.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/006_04d74e12.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/007_76dc423a.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/008_3bfedab8.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/009_8844bacc.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/010_ce5bd8a2.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/011_71969f29.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/012_b26d9a9d.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/013_2bff574a.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/014_bbe9116e.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/015_d6354178.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/016_a669f24c.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/017_110dcc6a.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/018_9d776351.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/019_43561f73.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/020_36cd1f03.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/021_7b2a627c.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/022_04cbae20.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/023_559a07b6.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/024_482f43ed.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/025_77aaff05.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/026_0d302cfc.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/027_6ef3705e.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/028_febcaba9.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/029_cb46b2bb.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/030_ea2a7db1.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/031_55e30033.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/032_86343336.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/033_8bed6926.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/034_45ff908d.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/035_2f9d5c12.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/036_8dc5a93c.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/037_cff9f22d.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/038_0eaf6e02.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/039_06b7f1ea.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/040_dec66c8a.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/041_0ab40c12.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/042_daa8a279.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/043_ff5dfc8f.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/044_6662648a.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/045_dc66ee1c.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/046_511d5603.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/047_73f5796f.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/048_1ed346ac.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/049_4d4c9c4e.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/050_2b2e6e7f.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/051_0a2d66b7.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/052_365b9921.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/053_37764f06.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/054_5ab3e260.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/055_1c893dab.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/056_3a21c6af.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/057_72a1674e.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/058_a5eb69fb.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/059_09cd1b4d.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/060_58a7a47c.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/061_edc107ca.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/062_01fbd0fa.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/063_34aa92fe.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/064_1828c4f6.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/065_d10379ec.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/066_08ec842b.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/067_1c283466.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/068_7c776799.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/069_12ae7288.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/070_a4bd7cf0.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/071_e190c3a2.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/072_d81ec336.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/073_0684f60d.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/074_f13e769d.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/075_4b3fac46.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/076_a3e008c1.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/077_98e4d427.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/078_191f4273.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/079_e3bf147b.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/080_af0ab42d.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/081_412ea8f5.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/082_60cd659d.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/083_b9c10851.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/084_1eb9844d.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/085_8f8cc791.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/086_9b7a99a3.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/087_32eed8da.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/088_fce81ee7.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/089_09b45d05.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/090_8252f095.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/091_d4af6789.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/092_62cd3fd3.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/093_874dd692.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/094_4c44e0ab.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/095_bf0ae200.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/096_5c89f563.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/097_d6f6f9cf.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/098_5224652a.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/099_015d5f74.jpg

This is a binary file of the type: Image

# images/Nicole Kidman/100_8a6e3419.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/001_a51bb26a.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/002_cc92e159.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/003_e18853f8.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/004_29776ffe.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/005_8af3cada.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/006_c26122bd.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/007_ecb8599e.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/008_79cd0b7b.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/009_49237aa0.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/010_991a88dc.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/011_da108a07.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/012_e3dd7d69.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/013_9e49009e.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/014_75f93e62.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/015_76c98a92.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/016_375490e8.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/017_fd82d064.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/018_0d23eccd.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/019_ac261615.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/020_b12140b8.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/021_d1cfd3e9.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/022_64141160.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/023_51dce41c.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/024_db7504a3.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/025_467e0866.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/026_76e88f4c.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/027_25f404f4.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/028_10053075.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/029_02077e81.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/030_adb3aa0e.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/031_f2f3733f.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/032_ac85b92c.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/033_255948c8.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/034_71739e5a.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/035_e4be5129.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/036_1b97e72c.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/037_342fdd2c.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/038_165ebb58.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/039_bfbbf1e4.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/040_91c31d91.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/041_b77c7671.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/042_6ac9e24e.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/043_993b1247.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/044_faec2086.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/045_caf1e891.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/046_a658cf42.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/047_389fe7b8.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/048_d7765620.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/049_0f461a3e.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/050_7509d1bb.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/051_8bed72f0.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/052_08084521.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/053_8075590e.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/054_d500397d.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/055_51880515.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/056_f2f25510.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/057_8572457a.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/058_4ed85318.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/059_01c01e72.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/060_19a80cff.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/061_b36635a2.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/062_81d4fb18.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/063_fe99146b.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/064_9ac818ed.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/065_343bfe69.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/066_0bdb9ac3.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/067_fb66d8ac.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/068_72330c63.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/069_0548213f.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/070_6192068e.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/071_a9b71352.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/072_0dbe44e4.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/073_9d58f7ef.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/074_a86aab43.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/075_dff1c336.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/076_318ed434.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/077_a908452a.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/078_adefb117.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/079_91098298.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/080_f5386479.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/081_725684cb.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/082_d9295121.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/083_f284dc2b.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/084_f5991991.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/085_b44c8d35.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/086_9b44c502.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/087_7c6523e6.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/088_ff699567.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/089_b11d4b97.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/090_d347e279.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/091_5307a177.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/092_c27c41de.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/093_8bbca2a0.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/094_087829ab.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/095_dd07ab81.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/096_84100579.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/097_833dba65.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/098_b78efdc8.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/099_0d04ca3f.jpg

This is a binary file of the type: Image

# images/Robert Downey Jr/100_dcb749ca.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/001_5ef3e95c.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/002_24fab375.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/003_0e3303fc.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/004_78847874.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/005_b0b4e2fa.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/006_96ea405c.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/007_5b97655c.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/008_f9ffe0c5.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/009_41aa3ed9.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/010_09f6d2fe.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/011_96913041.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/012_9585a2f6.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/013_3ef4eccf.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/014_fe364387.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/015_8a94d8c7.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/016_206a880f.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/017_8108b7ce.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/018_20e2b978.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/019_7a6470ab.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/020_3af33d4e.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/021_7ae7b9a5.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/022_1c07f2df.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/023_7214d0b2.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/024_9385dcfc.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/025_d5418b1e.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/026_e5342024.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/027_f5294957.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/028_5388c983.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/029_c1a6907a.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/030_642eaf93.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/031_ad150d21.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/032_f3773aa6.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/033_bc82f2a9.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/034_3c156ed0.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/035_bc2e1105.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/036_701f7b42.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/037_c035b16e.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/038_254f6d4c.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/039_7654fd34.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/040_4b9bc437.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/041_642b1b15.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/042_d91db350.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/043_4f352240.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/044_49497c96.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/045_24ebd253.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/046_89b5683b.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/047_afa9bc7d.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/048_ee0ebb84.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/049_0ba44f0d.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/050_4bdc1f8a.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/051_6e09f63c.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/052_18640959.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/053_ae92d5b1.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/054_81a12509.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/055_7e5055b5.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/056_7b1ade09.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/057_bec7ded3.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/058_35da9cd6.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/059_b5b38942.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/060_a274185c.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/061_694af034.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/062_f2c308de.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/063_8e71347c.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/064_84cdff70.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/065_164f7ee0.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/066_54b75717.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/067_259ec75e.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/068_4b87f13b.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/069_1b7a9cf8.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/070_c3d751bb.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/071_45baaf8f.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/072_6abd70dd.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/073_b0bfca72.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/074_6e18fec0.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/075_4b6e8283.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/076_469143b0.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/077_d8ba3326.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/078_d9a9ca25.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/079_c4558d9a.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/080_abc596b4.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/081_9039f6c1.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/082_24911cfe.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/083_d310d201.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/084_6b81d36b.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/085_69f8d759.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/086_1d515df9.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/087_16446f73.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/088_0b2e9007.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/089_15cc8ac7.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/090_f3644e6b.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/091_37b0b664.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/092_8c255f73.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/093_acd4a718.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/094_b654a685.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/095_bcb2e593.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/096_4eb6b8b7.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/097_783b21f0.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/098_529825da.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/099_d22b8b8b.jpg

This is a binary file of the type: Image

# images/Sandra Bullock/100_e1433988.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/001_cb004eea.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/002_ea6e259d.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/003_b416eed5.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/004_bb16ac65.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/005_1fc7405f.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/006_07bd8618.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/007_c72ff5ba.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/008_10846cce.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/009_fc574624.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/010_4eb6eabe.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/011_32193038.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/012_be8f222c.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/013_125e020a.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/014_d5c7b58f.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/015_bca34e2c.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/016_3e4f9139.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/017_4f3f64e7.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/018_a532251b.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/019_9e00e190.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/020_cce4e0e0.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/021_0b380404.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/022_65ffb673.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/023_e57cc529.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/024_6c2e4da8.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/025_cd625bef.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/026_f4a75554.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/027_cdf02996.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/028_f7fab378.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/029_75cdebc2.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/030_16328494.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/031_750d847e.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/032_7c1161c1.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/033_e49f1cf2.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/034_bc5b43ee.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/035_b51d7dae.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/036_829e603f.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/037_ec9df32c.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/038_e44106ce.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/039_f69978ec.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/040_9848047c.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/041_9913ca04.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/042_81d1cfae.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/043_46a213d0.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/044_df20e34a.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/045_6b008fbc.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/046_83629801.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/047_6ec9d887.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/048_85dcb79b.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/049_8398d25d.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/050_c8461888.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/051_f852bd6d.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/052_89d1073b.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/053_ec47a4c0.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/054_e93bb861.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/055_f6e1bf43.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/056_ec9b544d.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/057_317143a9.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/058_90a2b4d3.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/059_07020e9d.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/060_003a8f0c.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/061_bf06c582.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/062_c5a26020.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/063_61a5b737.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/064_4da75fb3.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/065_6b64e773.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/066_8e7dd66e.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/067_590b9254.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/068_45cbb6a4.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/069_da4a375a.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/070_f5ece24f.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/071_9a0f4b21.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/072_c7f23b07.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/073_884e445b.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/074_75c0c81a.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/075_e0b91ee3.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/076_6aac7281.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/077_776d5e0f.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/078_6b17a035.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/079_9f634689.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/080_d7addbd8.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/081_f92d604e.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/082_094c1df4.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/083_b9787470.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/084_96fadaf8.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/085_72293c6d.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/086_38ca81dd.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/087_bb9186aa.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/088_116c6971.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/089_244148b6.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/090_8e8d0b5c.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/091_764fb4f6.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/092_4c27282f.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/093_fda0f117.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/094_ad3f1b0c.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/095_0c6b7820.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/096_9d0cd927.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/097_ca9cfda8.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/098_c71a52d0.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/099_1046eb6d.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/100_0bc6635b.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/101_7850b100.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/102_97fca716.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/103_c4026864.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/104_71469b69.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/105_0e19a5e1.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/106_7d93e0c4.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/107_76e3d093.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/108_e118d7c8.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/109_66b77708.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/110_9b23a9ba.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/111_13e0f9a5.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/112_710c6176.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/113_049adfc0.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/114_4d4c877f.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/115_b22320d3.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/116_24bd5bec.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/117_3aea85fd.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/118_78748ac9.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/119_139bab99.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/120_e5229f43.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/121_2cd88d49.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/122_15d9b213.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/123_827bf807.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/124_2c2d9b34.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/125_b66015af.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/126_27b87531.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/127_9894295d.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/128_40ed3346.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/129_a47a690d.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/130_b42dfae6.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/131_fc6adb6b.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/132_a2dd114f.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/133_9e5b6dda.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/134_736d1702.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/135_a0327bd7.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/136_2b8c824e.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/137_29b565f9.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/138_c2c0dc1f.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/139_30ec33f4.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/140_080f3112.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/141_7d6d4cc8.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/142_5d78bc85.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/143_6b2feb16.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/144_99c39c61.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/145_e968cdd5.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/146_bcd22d45.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/147_dd6adc82.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/148_747f02af.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/149_0668be95.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/150_7d4d26a4.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/151_5ddc0980.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/152_a5f9d1a6.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/153_e68fb09b.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/154_42de3f25.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/155_a52e96fe.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/156_6bd9b374.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/157_8843fa75.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/158_b3e56fdd.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/159_cc64ec9b.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/160_c8047b80.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/161_e9edc289.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/162_e3501030.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/163_b87ecc32.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/164_18440a62.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/165_561e5653.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/166_1a464355.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/167_b2390a04.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/168_aaaf41c4.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/169_b57b3732.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/170_1156035a.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/171_5f2cac37.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/172_adae6b48.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/173_39ab0a7f.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/174_b300c293.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/175_7a73f9a3.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/176_09070ef2.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/177_51e7fd9e.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/178_db9db324.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/179_d219493a.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/180_5521d15f.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/181_52a40655.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/182_56820995.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/183_065be5ce.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/184_2137d05c.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/185_d369de0c.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/186_ab679730.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/187_b430a570.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/188_ebfc6465.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/189_89822da8.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/190_1d7fca25.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/191_6b48d25b.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/192_6f142457.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/193_ccc81566.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/194_3253d10f.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/195_dc745cfd.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/196_08de561a.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/197_ed22acef.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/198_e056989e.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/199_67b0ebbd.jpg

This is a binary file of the type: Image

# images/Scarlett Johansson/200_d8491f8c.jpg

This is a binary file of the type: Image

# images/Tom Cruise/001_08212dcd.jpg

This is a binary file of the type: Image

# images/Tom Cruise/002_6749a2c4.jpg

This is a binary file of the type: Image

# images/Tom Cruise/003_ed3fb7b1.jpg

This is a binary file of the type: Image

# images/Tom Cruise/004_dc64d954.jpg

This is a binary file of the type: Image

# images/Tom Cruise/005_2464c583.jpg

This is a binary file of the type: Image

# images/Tom Cruise/006_46519378.jpg

This is a binary file of the type: Image

# images/Tom Cruise/007_0a40d399.jpg

This is a binary file of the type: Image

# images/Tom Cruise/008_4d5e67ae.jpg

This is a binary file of the type: Image

# images/Tom Cruise/009_1f22d945.jpg

This is a binary file of the type: Image

# images/Tom Cruise/010_18d7b27c.jpg

This is a binary file of the type: Image

# images/Tom Cruise/011_0dda409c.jpg

This is a binary file of the type: Image

# images/Tom Cruise/012_900c5b05.jpg

This is a binary file of the type: Image

# images/Tom Cruise/013_712a38d6.jpg

This is a binary file of the type: Image

# images/Tom Cruise/014_50bc41b8.jpg

This is a binary file of the type: Image

# images/Tom Cruise/015_8adbc3ae.jpg

This is a binary file of the type: Image

# images/Tom Cruise/016_9959338f.jpg

This is a binary file of the type: Image

# images/Tom Cruise/017_e1b1872c.jpg

This is a binary file of the type: Image

# images/Tom Cruise/018_cae0c8ec.jpg

This is a binary file of the type: Image

# images/Tom Cruise/019_99363fad.jpg

This is a binary file of the type: Image

# images/Tom Cruise/020_e616c0af.jpg

This is a binary file of the type: Image

# images/Tom Cruise/021_f04e960b.jpg

This is a binary file of the type: Image

# images/Tom Cruise/022_43b050c3.jpg

This is a binary file of the type: Image

# images/Tom Cruise/023_dd4e8918.jpg

This is a binary file of the type: Image

# images/Tom Cruise/024_e7356978.jpg

This is a binary file of the type: Image

# images/Tom Cruise/025_72e3b32b.jpg

This is a binary file of the type: Image

# images/Tom Cruise/026_f06834e9.jpg

This is a binary file of the type: Image

# images/Tom Cruise/027_7c6c360c.jpg

This is a binary file of the type: Image

# images/Tom Cruise/028_a41d259d.jpg

This is a binary file of the type: Image

# images/Tom Cruise/029_ea3de34c.jpg

This is a binary file of the type: Image

# images/Tom Cruise/030_377fefef.jpg

This is a binary file of the type: Image

# images/Tom Cruise/031_df3204d3.jpg

This is a binary file of the type: Image

# images/Tom Cruise/032_5934eb7a.jpg

This is a binary file of the type: Image

# images/Tom Cruise/033_d891acbd.jpg

This is a binary file of the type: Image

# images/Tom Cruise/034_ed2c8762.jpg

This is a binary file of the type: Image

# images/Tom Cruise/035_34c306d1.jpg

This is a binary file of the type: Image

# images/Tom Cruise/036_f47a2dc9.jpg

This is a binary file of the type: Image

# images/Tom Cruise/037_463cf3bd.jpg

This is a binary file of the type: Image

# images/Tom Cruise/038_02f8e0ee.jpg

This is a binary file of the type: Image

# images/Tom Cruise/039_107ec01f.jpg

This is a binary file of the type: Image

# images/Tom Cruise/040_ca0a46b5.jpg

This is a binary file of the type: Image

# images/Tom Cruise/041_e2eff4e4.jpg

This is a binary file of the type: Image

# images/Tom Cruise/042_495b3b2e.jpg

This is a binary file of the type: Image

# images/Tom Cruise/043_be7cc0ea.jpg

This is a binary file of the type: Image

# images/Tom Cruise/044_8ce8a143.jpg

This is a binary file of the type: Image

# images/Tom Cruise/045_0b1b7a65.jpg

This is a binary file of the type: Image

# images/Tom Cruise/046_9ba44e0e.jpg

This is a binary file of the type: Image

# images/Tom Cruise/047_e8a911aa.jpg

This is a binary file of the type: Image

# images/Tom Cruise/048_21c4f84a.jpg

This is a binary file of the type: Image

# images/Tom Cruise/049_78b42871.jpg

This is a binary file of the type: Image

# images/Tom Cruise/050_278ec040.jpg

This is a binary file of the type: Image

# images/Tom Cruise/051_566647e1.jpg

This is a binary file of the type: Image

# images/Tom Cruise/052_60af6c54.jpg

This is a binary file of the type: Image

# images/Tom Cruise/053_3804bf81.jpg

This is a binary file of the type: Image

# images/Tom Cruise/054_5e6a651d.jpg

This is a binary file of the type: Image

# images/Tom Cruise/055_3fd4465f.jpg

This is a binary file of the type: Image

# images/Tom Cruise/056_158d5258.jpg

This is a binary file of the type: Image

# images/Tom Cruise/057_e3da0420.jpg

This is a binary file of the type: Image

# images/Tom Cruise/058_a119b343.jpg

This is a binary file of the type: Image

# images/Tom Cruise/059_6b515be7.jpg

This is a binary file of the type: Image

# images/Tom Cruise/060_b53036a3.jpg

This is a binary file of the type: Image

# images/Tom Cruise/061_aa29ec4f.jpg

This is a binary file of the type: Image

# images/Tom Cruise/062_d4b7903f.jpg

This is a binary file of the type: Image

# images/Tom Cruise/063_5b917fac.jpg

This is a binary file of the type: Image

# images/Tom Cruise/064_871302d1.jpg

This is a binary file of the type: Image

# images/Tom Cruise/065_22f91b1e.jpg

This is a binary file of the type: Image

# images/Tom Cruise/066_60ea35c5.jpg

This is a binary file of the type: Image

# images/Tom Cruise/067_8dcd661e.jpg

This is a binary file of the type: Image

# images/Tom Cruise/068_02e157e1.jpg

This is a binary file of the type: Image

# images/Tom Cruise/069_be9dbc40.jpg

This is a binary file of the type: Image

# images/Tom Cruise/070_86a8dd4b.jpg

This is a binary file of the type: Image

# images/Tom Cruise/071_0ebe70f4.jpg

This is a binary file of the type: Image

# images/Tom Cruise/072_dccafedf.jpg

This is a binary file of the type: Image

# images/Tom Cruise/073_dc7ca0db.jpg

This is a binary file of the type: Image

# images/Tom Cruise/074_f29224ac.jpg

This is a binary file of the type: Image

# images/Tom Cruise/075_eed20fb4.jpg

This is a binary file of the type: Image

# images/Tom Cruise/076_d4ee20ae.jpg

This is a binary file of the type: Image

# images/Tom Cruise/077_58e430f4.jpg

This is a binary file of the type: Image

# images/Tom Cruise/078_076c27b8.jpg

This is a binary file of the type: Image

# images/Tom Cruise/079_fd41500f.jpg

This is a binary file of the type: Image

# images/Tom Cruise/080_566ea9e9.jpg

This is a binary file of the type: Image

# images/Tom Cruise/081_d6521f1f.jpg

This is a binary file of the type: Image

# images/Tom Cruise/082_1ac0f1ee.jpg

This is a binary file of the type: Image

# images/Tom Cruise/083_63bb9285.jpg

This is a binary file of the type: Image

# images/Tom Cruise/084_31281f33.jpg

This is a binary file of the type: Image

# images/Tom Cruise/085_698d9a21.jpg

This is a binary file of the type: Image

# images/Tom Cruise/086_8a3c6af8.jpg

This is a binary file of the type: Image

# images/Tom Cruise/087_8fff57dd.jpg

This is a binary file of the type: Image

# images/Tom Cruise/088_fde7e34b.jpg

This is a binary file of the type: Image

# images/Tom Cruise/089_20b122f3.jpg

This is a binary file of the type: Image

# images/Tom Cruise/090_8f4eb0e6.jpg

This is a binary file of the type: Image

# images/Tom Cruise/091_a9736a22.jpg

This is a binary file of the type: Image

# images/Tom Cruise/092_53648816.jpg

This is a binary file of the type: Image

# images/Tom Cruise/093_7e0d43d2.jpg

This is a binary file of the type: Image

# images/Tom Cruise/094_2f713c67.jpg

This is a binary file of the type: Image

# images/Tom Cruise/095_08f36cce.jpg

This is a binary file of the type: Image

# images/Tom Cruise/096_b45f1da1.jpg

This is a binary file of the type: Image

# images/Tom Cruise/097_914cebdd.jpg

This is a binary file of the type: Image

# images/Tom Cruise/098_3790f566.jpg

This is a binary file of the type: Image

# images/Tom Cruise/099_705dbe8c.jpg

This is a binary file of the type: Image

# images/Tom Cruise/100_32a5d9d1.jpg

This is a binary file of the type: Image

# images/Tom Hanks/001_986d6c22.jpg

This is a binary file of the type: Image

# images/Tom Hanks/002_f6b26479.jpg

This is a binary file of the type: Image

# images/Tom Hanks/003_21d0aae6.jpg

This is a binary file of the type: Image

# images/Tom Hanks/004_a5881d85.jpg

This is a binary file of the type: Image

# images/Tom Hanks/005_dac94cfe.jpg

This is a binary file of the type: Image

# images/Tom Hanks/006_a28f75e7.jpg

This is a binary file of the type: Image

# images/Tom Hanks/007_ba0aa044.jpg

This is a binary file of the type: Image

# images/Tom Hanks/008_74cd0628.jpg

This is a binary file of the type: Image

# images/Tom Hanks/009_474a6b2e.jpg

This is a binary file of the type: Image

# images/Tom Hanks/010_2181b5f4.jpg

This is a binary file of the type: Image

# images/Tom Hanks/011_1c3b7dfd.jpg

This is a binary file of the type: Image

# images/Tom Hanks/012_39efc245.jpg

This is a binary file of the type: Image

# images/Tom Hanks/013_b87334b3.jpg

This is a binary file of the type: Image

# images/Tom Hanks/014_ff388296.jpg

This is a binary file of the type: Image

# images/Tom Hanks/015_782498ae.jpg

This is a binary file of the type: Image

# images/Tom Hanks/016_edfda289.jpg

This is a binary file of the type: Image

# images/Tom Hanks/017_e4dd8745.jpg

This is a binary file of the type: Image

# images/Tom Hanks/018_b7231fad.jpg

This is a binary file of the type: Image

# images/Tom Hanks/019_c332c45a.jpg

This is a binary file of the type: Image

# images/Tom Hanks/020_0847e879.jpg

This is a binary file of the type: Image

# images/Tom Hanks/021_b7e22acc.jpg

This is a binary file of the type: Image

# images/Tom Hanks/022_df2ce089.jpg

This is a binary file of the type: Image

# images/Tom Hanks/023_2029f686.jpg

This is a binary file of the type: Image

# images/Tom Hanks/024_2c8389f0.jpg

This is a binary file of the type: Image

# images/Tom Hanks/025_ff5fcfbd.jpg

This is a binary file of the type: Image

# images/Tom Hanks/026_bb842452.jpg

This is a binary file of the type: Image

# images/Tom Hanks/027_82e30afe.jpg

This is a binary file of the type: Image

# images/Tom Hanks/028_123163e1.jpg

This is a binary file of the type: Image

# images/Tom Hanks/029_169c07b0.jpg

This is a binary file of the type: Image

# images/Tom Hanks/030_04d77ac9.jpg

This is a binary file of the type: Image

# images/Tom Hanks/031_1d57bbbf.jpg

This is a binary file of the type: Image

# images/Tom Hanks/032_64d86c5b.jpg

This is a binary file of the type: Image

# images/Tom Hanks/033_71aad839.jpg

This is a binary file of the type: Image

# images/Tom Hanks/034_c2570ac6.jpg

This is a binary file of the type: Image

# images/Tom Hanks/035_0902e9ca.jpg

This is a binary file of the type: Image

# images/Tom Hanks/036_5c1a5498.jpg

This is a binary file of the type: Image

# images/Tom Hanks/037_5211d423.jpg

This is a binary file of the type: Image

# images/Tom Hanks/038_339bfc70.jpg

This is a binary file of the type: Image

# images/Tom Hanks/039_d0c3aa09.jpg

This is a binary file of the type: Image

# images/Tom Hanks/040_a8df71eb.jpg

This is a binary file of the type: Image

# images/Tom Hanks/041_8f1aa118.jpg

This is a binary file of the type: Image

# images/Tom Hanks/042_1276f85d.jpg

This is a binary file of the type: Image

# images/Tom Hanks/043_8093149b.jpg

This is a binary file of the type: Image

# images/Tom Hanks/044_de4952a5.jpg

This is a binary file of the type: Image

# images/Tom Hanks/045_b472dfb1.jpg

This is a binary file of the type: Image

# images/Tom Hanks/046_d84ceb59.jpg

This is a binary file of the type: Image

# images/Tom Hanks/047_fa46a4c7.jpg

This is a binary file of the type: Image

# images/Tom Hanks/048_043d84fd.jpg

This is a binary file of the type: Image

# images/Tom Hanks/049_2924cbf0.jpg

This is a binary file of the type: Image

# images/Tom Hanks/050_9269f010.jpg

This is a binary file of the type: Image

# images/Tom Hanks/051_fc2e65a8.jpg

This is a binary file of the type: Image

# images/Tom Hanks/052_4fb52c63.jpg

This is a binary file of the type: Image

# images/Tom Hanks/053_5fde0a5b.jpg

This is a binary file of the type: Image

# images/Tom Hanks/054_e2ea18b5.jpg

This is a binary file of the type: Image

# images/Tom Hanks/055_31123ada.jpg

This is a binary file of the type: Image

# images/Tom Hanks/056_869073c6.jpg

This is a binary file of the type: Image

# images/Tom Hanks/057_153bf359.jpg

This is a binary file of the type: Image

# images/Tom Hanks/058_450266ba.jpg

This is a binary file of the type: Image

# images/Tom Hanks/059_c7c906d9.jpg

This is a binary file of the type: Image

# images/Tom Hanks/060_78fae615.jpg

This is a binary file of the type: Image

# images/Tom Hanks/061_cb7738fd.jpg

This is a binary file of the type: Image

# images/Tom Hanks/062_41f18a02.jpg

This is a binary file of the type: Image

# images/Tom Hanks/063_c13c362e.jpg

This is a binary file of the type: Image

# images/Tom Hanks/064_898b4b7e.jpg

This is a binary file of the type: Image

# images/Tom Hanks/065_10c32ecc.jpg

This is a binary file of the type: Image

# images/Tom Hanks/066_72271d5a.jpg

This is a binary file of the type: Image

# images/Tom Hanks/067_15f0e6bb.jpg

This is a binary file of the type: Image

# images/Tom Hanks/068_0c16cd68.jpg

This is a binary file of the type: Image

# images/Tom Hanks/069_fcdc8fc0.jpg

This is a binary file of the type: Image

# images/Tom Hanks/070_316ffc8a.jpg

This is a binary file of the type: Image

# images/Tom Hanks/071_4de68b99.jpg

This is a binary file of the type: Image

# images/Tom Hanks/072_7deadeff.jpg

This is a binary file of the type: Image

# images/Tom Hanks/073_dcdc4ed3.jpg

This is a binary file of the type: Image

# images/Tom Hanks/074_ab0c61a6.jpg

This is a binary file of the type: Image

# images/Tom Hanks/075_0268d466.jpg

This is a binary file of the type: Image

# images/Tom Hanks/076_66977623.jpg

This is a binary file of the type: Image

# images/Tom Hanks/077_351b17d6.jpg

This is a binary file of the type: Image

# images/Tom Hanks/078_8d2a598e.jpg

This is a binary file of the type: Image

# images/Tom Hanks/079_f5cc99a5.jpg

This is a binary file of the type: Image

# images/Tom Hanks/080_13b6a4b6.jpg

This is a binary file of the type: Image

# images/Tom Hanks/081_ff5f08ea.jpg

This is a binary file of the type: Image

# images/Tom Hanks/082_41697615.jpg

This is a binary file of the type: Image

# images/Tom Hanks/083_1696e0ba.jpg

This is a binary file of the type: Image

# images/Tom Hanks/084_96ce3be4.jpg

This is a binary file of the type: Image

# images/Tom Hanks/085_2a8883ca.jpg

This is a binary file of the type: Image

# images/Tom Hanks/086_e7072dbb.jpg

This is a binary file of the type: Image

# images/Tom Hanks/087_6be1cb96.jpg

This is a binary file of the type: Image

# images/Tom Hanks/088_78e9691e.jpg

This is a binary file of the type: Image

# images/Tom Hanks/089_c8ef8eee.jpg

This is a binary file of the type: Image

# images/Tom Hanks/090_3c8ed08d.jpg

This is a binary file of the type: Image

# images/Tom Hanks/091_da40c2a6.jpg

This is a binary file of the type: Image

# images/Tom Hanks/092_de7a5a68.jpg

This is a binary file of the type: Image

# images/Tom Hanks/093_b1decaaa.jpg

This is a binary file of the type: Image

# images/Tom Hanks/094_ea1110a3.jpg

This is a binary file of the type: Image

# images/Tom Hanks/095_2939d9c5.jpg

This is a binary file of the type: Image

# images/Tom Hanks/096_eb059e84.jpg

This is a binary file of the type: Image

# images/Tom Hanks/097_0c9b7ced.jpg

This is a binary file of the type: Image

# images/Tom Hanks/098_8b5a1524.jpg

This is a binary file of the type: Image

# images/Tom Hanks/099_1b1c4625.jpg

This is a binary file of the type: Image

# images/Tom Hanks/100_b712e7ca.jpg

This is a binary file of the type: Image

# images/Will Smith/001_beebcee2.jpg

This is a binary file of the type: Image

# images/Will Smith/002_078f6fe5.jpg

This is a binary file of the type: Image

# images/Will Smith/003_936c5a43.jpg

This is a binary file of the type: Image

# images/Will Smith/004_af9b4c7c.jpg

This is a binary file of the type: Image

# images/Will Smith/005_37066c18.jpg

This is a binary file of the type: Image

# images/Will Smith/006_bbb6978e.jpg

This is a binary file of the type: Image

# images/Will Smith/007_9656ae64.jpg

This is a binary file of the type: Image

# images/Will Smith/008_cdaf39e7.jpg

This is a binary file of the type: Image

# images/Will Smith/009_a023db5b.jpg

This is a binary file of the type: Image

# images/Will Smith/010_8bd7dba1.jpg

This is a binary file of the type: Image

# images/Will Smith/011_0e0e8b1c.jpg

This is a binary file of the type: Image

# images/Will Smith/012_19e90fb6.jpg

This is a binary file of the type: Image

# images/Will Smith/013_19a43131.jpg

This is a binary file of the type: Image

# images/Will Smith/014_f512d81c.jpg

This is a binary file of the type: Image

# images/Will Smith/015_8da65114.jpg

This is a binary file of the type: Image

# images/Will Smith/016_d9c576a4.jpg

This is a binary file of the type: Image

# images/Will Smith/017_bb6ad7d6.jpg

This is a binary file of the type: Image

# images/Will Smith/018_d5d389eb.jpg

This is a binary file of the type: Image

# images/Will Smith/019_33ab99af.jpg

This is a binary file of the type: Image

# images/Will Smith/020_8e6bdc45.jpg

This is a binary file of the type: Image

# images/Will Smith/021_3cf2aa92.jpg

This is a binary file of the type: Image

# images/Will Smith/022_c9c4cb9f.jpg

This is a binary file of the type: Image

# images/Will Smith/023_cb306a1a.jpg

This is a binary file of the type: Image

# images/Will Smith/024_b222784a.jpg

This is a binary file of the type: Image

# images/Will Smith/025_0dc3ad3d.jpg

This is a binary file of the type: Image

# images/Will Smith/026_4f5bfb2c.jpg

This is a binary file of the type: Image

# images/Will Smith/027_803986e2.jpg

This is a binary file of the type: Image

# images/Will Smith/028_05df393f.jpg

This is a binary file of the type: Image

# images/Will Smith/029_09dcae68.jpg

This is a binary file of the type: Image

# images/Will Smith/030_df8c8fad.jpg

This is a binary file of the type: Image

# images/Will Smith/031_7ad763d7.jpg

This is a binary file of the type: Image

# images/Will Smith/032_2899cee6.jpg

This is a binary file of the type: Image

# images/Will Smith/033_241ed413.jpg

This is a binary file of the type: Image

# images/Will Smith/034_32b04ae9.jpg

This is a binary file of the type: Image

# images/Will Smith/035_9e22f213.jpg

This is a binary file of the type: Image

# images/Will Smith/036_8751d89b.jpg

This is a binary file of the type: Image

# images/Will Smith/037_17e4f89a.jpg

This is a binary file of the type: Image

# images/Will Smith/038_b28dda4c.jpg

This is a binary file of the type: Image

# images/Will Smith/039_3daa67cf.jpg

This is a binary file of the type: Image

# images/Will Smith/040_630a0d6a.jpg

This is a binary file of the type: Image

# images/Will Smith/041_bcfa1766.jpg

This is a binary file of the type: Image

# images/Will Smith/042_f6cff42f.jpg

This is a binary file of the type: Image

# images/Will Smith/043_33815e76.jpg

This is a binary file of the type: Image

# images/Will Smith/044_988edbe9.jpg

This is a binary file of the type: Image

# images/Will Smith/045_810b690c.jpg

This is a binary file of the type: Image

# images/Will Smith/046_6d5b1ed6.jpg

This is a binary file of the type: Image

# images/Will Smith/047_dc7e1839.jpg

This is a binary file of the type: Image

# images/Will Smith/048_bf9c2b11.jpg

This is a binary file of the type: Image

# images/Will Smith/049_15a71c48.jpg

This is a binary file of the type: Image

# images/Will Smith/050_f5bd72ba.jpg

This is a binary file of the type: Image

# images/Will Smith/051_1f3aede9.jpg

This is a binary file of the type: Image

# images/Will Smith/052_f15c0c78.jpg

This is a binary file of the type: Image

# images/Will Smith/053_8405b30f.jpg

This is a binary file of the type: Image

# images/Will Smith/054_cbee29ae.jpg

This is a binary file of the type: Image

# images/Will Smith/055_f9cbb53e.jpg

This is a binary file of the type: Image

# images/Will Smith/056_abd6e06b.jpg

This is a binary file of the type: Image

# images/Will Smith/057_faaa39ed.jpg

This is a binary file of the type: Image

# images/Will Smith/058_38b80eed.jpg

This is a binary file of the type: Image

# images/Will Smith/059_181bfc6b.jpg

This is a binary file of the type: Image

# images/Will Smith/060_8bb5cac3.jpg

This is a binary file of the type: Image

# images/Will Smith/061_4385aa8d.jpg

This is a binary file of the type: Image

# images/Will Smith/062_07fcfec7.jpg

This is a binary file of the type: Image

# images/Will Smith/063_46f560ca.jpg

This is a binary file of the type: Image

# images/Will Smith/064_88de03f4.jpg

This is a binary file of the type: Image

# images/Will Smith/065_5cb55293.jpg

This is a binary file of the type: Image

# images/Will Smith/066_5d45a68f.jpg

This is a binary file of the type: Image

# images/Will Smith/067_9e09ea61.jpg

This is a binary file of the type: Image

# images/Will Smith/068_b778f382.jpg

This is a binary file of the type: Image

# images/Will Smith/069_80468bd5.jpg

This is a binary file of the type: Image

# images/Will Smith/070_6743629d.jpg

This is a binary file of the type: Image

# images/Will Smith/071_5f7cdaaf.jpg

This is a binary file of the type: Image

# images/Will Smith/072_4a17b7fb.jpg

This is a binary file of the type: Image

# images/Will Smith/073_f04cd664.jpg

This is a binary file of the type: Image

# images/Will Smith/074_61fe25d9.jpg

This is a binary file of the type: Image

# images/Will Smith/075_65ffca63.jpg

This is a binary file of the type: Image

# images/Will Smith/076_d36850ba.jpg

This is a binary file of the type: Image

# images/Will Smith/077_eb907a5f.jpg

This is a binary file of the type: Image

# images/Will Smith/078_44637281.jpg

This is a binary file of the type: Image

# images/Will Smith/079_8575a4bc.jpg

This is a binary file of the type: Image

# images/Will Smith/080_94d3ede6.jpg

This is a binary file of the type: Image

# images/Will Smith/081_8dc3b149.jpg

This is a binary file of the type: Image

# images/Will Smith/082_ed9a24cc.jpg

This is a binary file of the type: Image

# images/Will Smith/083_a0692bc1.jpg

This is a binary file of the type: Image

# images/Will Smith/084_0d8b77bc.jpg

This is a binary file of the type: Image

# images/Will Smith/085_97ab4600.jpg

This is a binary file of the type: Image

# images/Will Smith/086_bd951ea7.jpg

This is a binary file of the type: Image

# images/Will Smith/087_6eba84a6.jpg

This is a binary file of the type: Image

# images/Will Smith/088_d6c5d9f4.jpg

This is a binary file of the type: Image

# images/Will Smith/089_97f39eb8.jpg

This is a binary file of the type: Image

# images/Will Smith/090_e959664a.jpg

This is a binary file of the type: Image

# images/Will Smith/091_082508dd.jpg

This is a binary file of the type: Image

# images/Will Smith/092_498e6999.jpg

This is a binary file of the type: Image

# images/Will Smith/093_dc555290.jpg

This is a binary file of the type: Image

# images/Will Smith/094_664a03cd.jpg

This is a binary file of the type: Image

# images/Will Smith/095_8a2dfab4.jpg

This is a binary file of the type: Image

# images/Will Smith/096_0881f6e7.jpg

This is a binary file of the type: Image

# images/Will Smith/097_5c18be93.jpg

This is a binary file of the type: Image

# images/Will Smith/098_6f416b6a.jpg

This is a binary file of the type: Image

# images/Will Smith/099_d652e3b6.jpg

This is a binary file of the type: Image

# images/Will Smith/100_89cbf87f.jpg

This is a binary file of the type: Image

# init_project.py

```py
# init_project.py
import os
import urllib.request
from tqdm import tqdm
import ssl

def download_file(url: str, filename: str):
    """Download a file with progress bar"""
    ssl._create_default_https_context = ssl._create_unverified_context
    
    # Create a request with headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    request = urllib.request.Request(url, headers=headers)
    
    response = urllib.request.urlopen(request)
    total_size = int(response.headers.get('Content-Length', 0))
    
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    with tqdm(total=total_size, unit='B', unit_scale=True, desc=filename) as pbar:
        urllib.request.urlretrieve(
            url,
            filename,
            reporthook=lambda count, block_size, total_size: pbar.update(block_size)
        )

def init_project():
    """Initialize project structure and download required models"""
    print("Initializing MacFaceSwap project...")
    
    # Define model URLs and paths
    models = {
        'inswapper_128.onnx': 'https://github.com/facefusion/facefusion-assets/releases/download/models/inswapper_128.onnx',
        'GFPGANv1.4.pth': 'https://github.com/TencentARC/GFPGAN/releases/download/v1.3.4/GFPGANv1.4.pth'
    }
    
    # Download models
    for model_name, url in models.items():
        model_path = os.path.join('models', model_name)
        if not os.path.exists(model_path):
            print(f"\nDownloading {model_name}...")
            try:
                download_file(url, model_path)
            except Exception as e:
                print(f"Error downloading {model_name}: {str(e)}")
                print(f"Please download manually from: {url}")
                print(f"And place it in the models/ directory as: {model_name}")
        else:
            print(f"\n{model_name} already exists, skipping download.")

    # Install required packages
    print("\nInstalling required packages...")
    os.system('pip install -r requirements.txt')

    print("\nProject initialization complete!")

if __name__ == '__main__':
    init_project()
```

# make_dmg.sh

```sh
#!/bin/bash

# Create DMG after building app
if [ -d "dist/MacFaceSwap.app" ]; then
    echo "Creating DMG..."
    
    # Install create-dmg if not already installed
    if ! command -v create-dmg &> /dev/null; then
        brew install create-dmg
    fi
    
    # Create DMG
    create-dmg \
        --volname "MacFaceSwap" \
        --volicon "resources/icon.icns" \
        --window-pos 200 120 \
        --window-size 800 400 \
        --icon-size 100 \
        --icon "MacFaceSwap.app" 200 190 \
        --hide-extension "MacFaceSwap.app" \
        --app-drop-link 600 185 \
        "dist/MacFaceSwap.dmg" \
        "dist/MacFaceSwap.app"
fi
```

# models/GFPGANv1.4.pth

This is a binary file of the type: Binary

# models/instructions.txt

```txt
just put the models in this folder -

https://huggingface.co/hacksider/deep-live-cam/resolve/main/inswapper_128_fp16.onnx?download=true
https://github.com/TencentARC/GFPGAN/releases/download/v1.3.4/GFPGANv1.4.pth

```

# models/inswapper_128_fp16.onnx

This is a binary file of the type: Binary

# models/inswapper_128.onnx

This is a binary file of the type: Binary

# README.md

```md
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
\`\`\`bash
pip install PyQt6 opencv-python qtawesome numpy
\`\`\`

---

## Installation

1. **Clone the Repository:**
   \`\`\`bash
   git clone https://github.com/your-repo/MacFaceSwap.git
   cd MacFaceSwap
   \`\`\`

2. **Set Up Virtual Environment:**
   \`\`\`bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   \`\`\`

3. **Install Dependencies:**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Add Resources:**
   Ensure the following directories are in place:
   - `resources/icons/`: Add icons for buttons.
   - `images/`: Add predefined face images (organized in subdirectories for each face).

---

## Usage

1. **Run the Application:**
   \`\`\`bash
   python src/main.py
   \`\`\`

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

\`\`\`
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
\`\`\`

---

## How to Add Predefined Faces

1. **Create Subdirectories for Each Celebrity:**
   Place images in the `images` directory, organized by celebrity name:
   \`\`\`
   images/
   ├── Tom_Hanks/
   │   ├── image1.jpg
   │   ├── image2.jpg
   ├── Scarlett_Johansson/
   │   ├── image1.jpg
   │   ├── image2.jpg
   \`\`\`

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
\`\`\`bash
python src/main.py
\`\`\`

Check logs for errors and adjust as necessary.

---

## Contributing

1. Fork the repository.
2. Create a feature branch:
   \`\`\`bash
   git checkout -b feature/your-feature
   \`\`\`
3. Commit your changes:
   \`\`\`bash
   git commit -m "Add your feature"
   \`\`\`
4. Push to your branch:
   \`\`\`bash
   git push origin feature/your-feature
   \`\`\`
5. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

- **PyQt6:** For the powerful GUI toolkit.
- **OpenCV:** For robust video processing.
- **Font Awesome:** For providing icons via `qtawesome`.

```

# requirements.txt

```txt
absl-py==2.1.0
addict==2.4.0
albucore==0.0.21
albumentations==1.4.23
altgraph==0.17.4
annotated-types==0.7.0
astunparse==1.6.3
basicsr==1.4.2
beautifulsoup4==4.12.3
certifi==2024.12.14
charset-normalizer==3.4.0
coloredlogs==15.0.1
comtypes==1.4.8
contourpy==1.3.1
customtkinter==5.2.2
cv2_enumerate_cameras==1.1.15
cycler==0.12.1
Cython==3.0.11
darkdetect==0.8.0
easydict==1.13
eval_type_backport==0.2.2
facexlib==0.3.0
filelock==3.16.1
filterpy==1.4.5
flatbuffers==24.3.25
fonttools==4.55.3
future==1.0.0
gast==0.6.0
gdown==5.2.0
gfpgan==1.3.8
google-pasta==0.2.0
grpcio==1.68.1
h5py==3.12.1
humanfriendly==10.0
idna==3.10
imageio==2.36.1
importlib_resources==6.4.5
insightface==0.7.3
Jinja2==3.1.5
joblib==1.4.2
keras==3.7.0
kiwisolver==1.4.7
lazy_loader==0.4
libclang==18.1.1
llvmlite==0.43.0
lmdb==1.5.1
macholib==1.16.3
Markdown==3.7
markdown-it-py==3.0.0
MarkupSafe==3.0.2
matplotlib==3.10.0
mdurl==0.1.2
ml-dtypes==0.4.1
modulegraph==0.19.6
mpmath==1.3.0
namex==0.0.8
networkx==3.4.2
numba==0.60.0
numpy==1.26.4
onnx==1.16.0
onnxruntime-silicon==1.16.3
opencv-python==4.8.1.78
opencv-python-headless==4.10.0.84
opennsfw2==0.10.2
opt_einsum==3.4.0
optree==0.13.1
packaging==24.2
Pillow==9.5.0
platformdirs==4.3.6
prettytable==3.12.0
protobuf==4.23.2
psutil==5.9.8
py2app==0.28.8
pydantic==2.10.4
pydantic_core==2.27.2
pydeps==2.0.1
Pygments==2.18.0
pygrabber==0.2
pyparsing==3.2.0
PyQt6==6.8.0
PyQt6-Qt6==6.8.1
PyQt6_sip==13.9.1
PySocks==1.7.1
python-dateutil==2.9.0.post0
PyYAML==6.0.2
requests==2.32.3
rich==13.9.4
scikit-image==0.24.0
scikit-learn==1.6.0
scipy==1.14.1
simsimd==6.2.1
six==1.17.0
soupsieve==2.6
stdlib-list==0.11.0
stringzilla==3.11.2
sympy==1.13.3
tb-nightly==2.19.0a20241222
tensorboard==2.18.0
tensorboard-data-server==0.7.2
tensorflow==2.18.0
tensorflow-io-gcs-filesystem==0.37.1
termcolor==2.5.0
threadpoolctl==3.5.0
tifffile==2024.12.12
tk==0.1.0
tkinterdnd2==0.4.2
tomli==2.2.1
torch==2.0.1
torchvision==0.15.2
tqdm==4.66.4
typing_extensions==4.12.2
urllib3==2.3.0
wcwidth==0.2.13
Werkzeug==3.1.3
wrapt==1.17.0
yapf==0.43.0

```

# resources/130ad4d1-9125-4fa8-b288-d713aa1359cf.webp

This is a binary file of the type: Image

# resources/icon.icns

This is a binary file of the type: Binary

# resources/icon.iconset/icon_16x16.png

This is a binary file of the type: Image

# resources/icon.iconset/icon_16x16@2x.png

This is a binary file of the type: Image

# resources/icon.iconset/icon_32x32.png

This is a binary file of the type: Image

# resources/icon.iconset/icon_32x32@2x.png

This is a binary file of the type: Image

# resources/icon.iconset/icon_128x128.png

This is a binary file of the type: Image

# resources/icon.iconset/icon_128x128@2x.png

This is a binary file of the type: Image

# resources/icon.iconset/icon_256x256.png

This is a binary file of the type: Image

# resources/icon.iconset/icon_256x256@2x.png

This is a binary file of the type: Image

# resources/icon.iconset/icon_512x512.png

This is a binary file of the type: Image

# resources/icon.iconset/icon_512x512@2x.png

This is a binary file of the type: Image

# resources/icon.png

This is a binary file of the type: Image

# resources/Info.plist

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleName</key>
    <string>MacFaceSwap</string>
    <key>CFBundleDisplayName</key>
    <string>MacFaceSwap</string>
    <key>CFBundleIdentifier</key>
    <string>com.mlynnorg.macfaceswap</string>
    <key>CFBundleVersion</key>
    <string>1.0.0</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>LSMinimumSystemVersion</key>
    <string>10.15</string>
    <key>NSHighResolutionCapable</key>
    <true/>
    <key>NSCameraUsageDescription</key>
    <string>MacFaceSwap needs access to your camera for face swapping functionality.</string>
    <key>NSCameraUseContinuityCameraDeviceType</key>
    <true/>
    <key>NSMicrophoneUsageDescription</key>
    <string>MacFaceSwap needs access to your microphone for video recording.</string>
</dict>
</plist>

```

# resources/installer_background.png

This is a binary file of the type: Image

# run.sh

```sh
#!/bin/bash
# run.sh

# Add the project root to PYTHONPATH
export PYTHONPATH="$PYTHONPATH:$(pwd)"

# Run the application
python src/main.py

```

# setup.py

```py
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
```

# setup.sh

```sh
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

```

# src/__init__.py

```py
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
```

# src/core/__init__.py

```py

```

# src/core/face_mapping.py

```py
# src/ui/face_mapping.py

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, 
    QLabel, QScrollArea, QFrame, QFileDialog, QMessageBox
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QImage, QPixmap
import cv2
import numpy as np

class FaceMappingWidget(QWidget):
    """Widget for managing face mappings"""
    mapping_updated = pyqtSignal(dict)  # Emitted when mapping changes
    
    def __init__(self, face_processor, parent=None):
        super().__init__(parent)
        self.face_processor = face_processor
        self.face_mappings = {}  # Dictionary to store source->target mappings
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
        
    def add_new_mapping(self):
        """Add a new face mapping row"""
        mapping = FaceMappingRow(len(self.face_mappings))
        mapping.deleted.connect(self.remove_mapping)
        mapping.updated.connect(self.update_mapping)
        
        self.mappings_layout.addWidget(mapping)
        self.face_mappings[mapping.mapping_id] = {
            'source_face': None,
            'target_face': None,
            'widget': mapping
        }
        
    def remove_mapping(self, mapping_id):
        """Remove a face mapping"""
        if mapping_id in self.face_mappings:
            widget = self.face_mappings[mapping_id]['widget']
            self.mappings_layout.removeWidget(widget)
            widget.deleteLater()
            del self.face_mappings[mapping_id]
            self.mapping_updated.emit(self.get_mappings())
            
    def clear_mappings(self):
        """Clear all mappings"""
        for mapping_id in list(self.face_mappings.keys()):
            self.remove_mapping(mapping_id)
            
    def update_mapping(self, mapping_id, source_face=None, target_face=None):
        """Update a face mapping"""
        if mapping_id in self.face_mappings:
            if source_face is not None:
                self.face_mappings[mapping_id]['source_face'] = source_face
            if target_face is not None:
                self.face_mappings[mapping_id]['target_face'] = target_face
            self.mapping_updated.emit(self.get_mappings())
            
    def get_mappings(self):
        """Get all active face mappings"""
        return {k: {
            'source_face': v['source_face']
        } for k, v in self.face_mappings.items() if 'source_face' in v}

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
                    mapping = FaceMappingRow(mapping_id, self)
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
```

# src/core/face_processor.py

```py
# src/core/face_processor.py

import os
import sys
import cv2
import numpy as np
from typing import Optional, List, Dict, Any, Tuple
import insightface
from insightface.app import FaceAnalysis
import platform
import time
from src import get_resource_path

class FaceProcessor:
    def __init__(self):
        """Initialize face processing components with enhanced quality settings"""
        try:
            print("\nInitializing FaceProcessor...")
            self.face_mappings = {}
            self.models_dir = self._get_models_dir()
            self.execution_provider = self._get_execution_provider()
            self.prev_face_positions = []
            self.position_smoothing_window = 3
            self.position_threshold = 10.0  # pixels
            # Initialize face analyzer with higher resolution
            print("Loading face analyzer...")
            self.face_analyzer = FaceAnalysis(
                name='buffalo_l',
                providers=[self.execution_provider],
                allowed_modules=['detection', 'recognition']
            )
            # Increase detection size for better quality
            self.face_analyzer.prepare(ctx_id=0, det_size=(640, 640))
            print("Face analyzer ready")
            
            # Load face swapper model
            print("Loading face swapper model...")
            model_path = os.path.join(self.models_dir, 'inswapper_128.onnx')
            if not os.path.exists(model_path):
                raise FileNotFoundError(f"Model not found: {model_path}")
            
            self.face_swapper = insightface.model_zoo.get_model(
                model_path,
                providers=[self.execution_provider]
            )
            
            # Enhanced similarity settings
            self.similarity_threshold = 0.1  # Lower threshold for better matching
            self.cache_size = 10  # Increased cache size
            self.process_every_n_frames = 1  # Process every frame
            
            # Face detection settings
            self.detection_threshold = 0.5  # Increased confidence threshold
            self.min_face_size = 20  # Minimum face size to process

            # Add face tracking
            self.last_face_location = None
            self.last_successful_swap = None
            self.face_track_threshold = 50  # pixels
            self.stable_frames_required = 3
            self.stable_frame_count = 0            
            # Image enhancement settings
            self.use_face_enhancement = True
            self.enhancement_level = 1.0  # Adjustable enhancement strength
            
            print("FaceProcessor initialization complete with enhanced settings")
            
        except Exception as e:
            print(f"Error initializing FaceProcessor: {str(e)}")
            raise
        
    def smooth_face_position(self, current_bbox):
        """Apply temporal smoothing to face positions"""
        if not self.prev_face_positions:
            self.prev_face_positions.append(current_bbox)
            return current_bbox
            
        # Convert to center point
        curr_center = [(current_bbox[0] + current_bbox[2])/2, 
                    (current_bbox[1] + current_bbox[3])/2]
                    
        # Calculate smoothed position
        smoothed_center = curr_center
        if len(self.prev_face_positions) > 0:
            prev_centers = [[(box[0] + box[2])/2, (box[1] + box[3])/2] 
                        for box in self.prev_face_positions]
            
            # Check if movement is within threshold
            prev_center = prev_centers[-1]
            movement = np.sqrt((curr_center[0] - prev_center[0])**2 + 
                            (curr_center[1] - prev_center[1])**2)
                            
            if movement < self.position_threshold:
                # Apply smoothing
                weights = np.linspace(0.5, 1.0, len(prev_centers) + 1)
                weights = weights / weights.sum()
                
                smoothed_x = np.average([c[0] for c in prev_centers + [curr_center]], 
                                    weights=weights)
                smoothed_y = np.average([c[1] for c in prev_centers + [curr_center]], 
                                    weights=weights)
                smoothed_center = [smoothed_x, smoothed_y]
        
        # Update position history
        self.prev_face_positions.append(current_bbox)
        if len(self.prev_face_positions) > self.position_smoothing_window:
            self.prev_face_positions.pop(0)
            
        # Convert back to bbox
        width = current_bbox[2] - current_bbox[0]
        height = current_bbox[3] - current_bbox[1]
        return [
            smoothed_center[0] - width/2,
            smoothed_center[1] - height/2,
            smoothed_center[0] + width/2,
            smoothed_center[1] + height/2
        ]

    def set_face_mappings(self, mappings: Dict[str, Any]) -> None:
        """Update the face mappings dictionary with validation"""
        print("\nSetting face mappings:")
        self.face_mappings = {}
        
        for mapping_id, mapping in mappings.items():
            print(f"\nValidating mapping {mapping_id}:")
            if 'source_face' in mapping and mapping['source_face'] is not None:
                source_face = mapping['source_face']
                if 'face' in source_face and 'embedding' in source_face:
                    print("- Source face complete with embedding")
                    print(f"- Embedding shape: {source_face['embedding'].shape}")
                    print(f"- Embedding norm: {np.linalg.norm(source_face['embedding'])}")
                    self.face_mappings[mapping_id] = mapping
                else:
                    print("- Source face missing face or embedding data")
            else:
                print("- No source face data")
                
        print(f"\nTotal valid mappings: {len(self.face_mappings)}")
        
    def detect_faces(self, frame: np.ndarray) -> List[dict]:
        """Detect and analyze faces in a frame"""
        if frame is None:
            print("Frame is None")
            return []
                
        try:
            print(f"Frame shape: {frame.shape}")
            print(f"Frame dtype: {frame.dtype}")
            print("Attempting face detection...")
            faces = self.face_analyzer.get(frame)
            print(f"Detected {len(faces)} faces")
            return [{
                'face': face,
                'bbox': face.bbox,
                'embedding': face.normed_embedding,
                'landmarks': face.landmark_2d_106
            } for face in faces]
        except Exception as e:
            print(f"Error detecting faces: {str(e)}")
            import traceback
            traceback.print_exc()
            return []
        
    def find_best_match(self, target_embedding: np.ndarray) -> Optional[Dict[str, Any]]:
        """Find the best matching source face for a target embedding"""
        try:
            if not self.face_mappings:
                print("No face mappings available")
                return None
            
            best_match = None
            best_similarity = 0  # Start from 0 instead of threshold
            
            # Preprocess target embedding
            target_embedding = self.preprocess_embedding(target_embedding)
            
            for mapping_id, mapping in self.face_mappings.items():
                if 'source_face' not in mapping:
                    continue
                    
                source_data = mapping['source_face']
                
                # Check if we have multiple embeddings
                if 'all_embeddings' in source_data and source_data['all_embeddings']:
                    # Compare with each embedding
                    similarities = []
                    for idx, emb in enumerate(source_data['all_embeddings']):
                        source_embedding = self.preprocess_embedding(emb)
                        similarity = float(np.dot(target_embedding, source_embedding))
                        l2_dist = np.linalg.norm(target_embedding - source_embedding)
                        adjusted_similarity = (1.0 - l2_dist/2.0) * similarity
                        similarities.append((adjusted_similarity, idx))
                    
                    max_similarity, best_idx = max(similarities)

                    if max_similarity > best_similarity:
                        best_similarity = max_similarity
                        best_match = {
                            'mapping_id': mapping_id,
                            'source_face': source_data['all_faces'][best_idx],
                            'similarity': max_similarity
                        }
                else:
                    # Fall back to single embedding comparison
                    if 'embedding' not in source_data:
                        continue
                        
                    source_embedding = self.preprocess_embedding(source_data['embedding'])
                    similarity = float(np.dot(target_embedding, source_embedding))
                    l2_dist = np.linalg.norm(target_embedding - source_embedding)
                    adjusted_similarity = (1.0 - l2_dist/2.0) * similarity
                    
                    if adjusted_similarity > best_similarity:
                        best_similarity = adjusted_similarity
                        best_match = {
                            'mapping_id': mapping_id,
                            'source_face': source_data['face'],
                            'similarity': adjusted_similarity
                        }
            
            if best_match:
                print(f"\nFound match with similarity: {best_similarity:.3f}")
            else:
                print(f"\nNo match found above threshold ({self.similarity_threshold})")
            
            return best_match
            
        except Exception as e:
            print(f"Error in find_best_match: {str(e)}")
            import traceback
            traceback.print_exc()
            return None

    def _get_models_dir(self) -> str:
        """Get the appropriate models directory based on environment"""
        if getattr(sys, 'frozen', False):
            # Running in a bundle
            return os.path.join(sys._MEIPASS, 'models')
        else:
            # Running in development
            return os.path.join(os.path.dirname(os.path.dirname(
                os.path.dirname(__file__))), 'models')

    def _get_execution_provider(self) -> str:
        """Determine the best execution provider for the current system"""
        if platform.processor() == 'arm':
            return 'CoreMLExecutionProvider'
        return 'CPUExecutionProvider'

    def process_frame(self, frame):
        if frame is None:
            return frame
            
        try:
            result = frame.copy()
            current_faces = self.detect_faces(frame)
            
            if not current_faces:
                return frame
                
            swapped = result.copy()
            swap_successful = False
            
            # Properly indented for loop block
            for face in current_faces:
                # Apply position smoothing
                smoothed_bbox = self.smooth_face_position(face['bbox'])
                face['bbox'] = smoothed_bbox
                
                match = self.find_best_match(face['embedding'])
                if match and match['similarity'] > self.similarity_threshold:
                    try:
                        # Apply face swap with enhanced settings and smoothed position
                        swapped = self.face_swapper.get(
                            swapped,
                            face['face'],
                            match['source_face'],
                            paste_back=True
                        )
                        
                        # Apply additional stabilization if enabled
                        if self.use_face_enhancement:
                            swapped = self.enhance_face_region(
                                swapped, 
                                smoothed_bbox,
                                self.enhancement_level
                            )
                            
                        swap_successful = True
                        
                    except Exception as e:
                        print(f"Error in face swap: {e}")
                        continue
                        
            return swapped if swap_successful else result
            
        except Exception as e:
            print(f"Error in process_frame: {e}")
            return frame

    def extract_face(self, frame: np.ndarray, bbox) -> Optional[np.ndarray]:
        """Extract face region from frame"""
        try:
            x1, y1, x2, y2 = map(int, bbox)
            return frame[y1:y2, x1:x2]
        except Exception as e:
            print(f"Error extracting face: {str(e)}")
            return None
        
    def analyze_face(self, frame: np.ndarray) -> Optional[Dict[str, Any]]:
        """Analyze a face in an image with detailed debugging"""
        print("\nAnalyzing source face image...")
        
        faces = self.detect_faces(frame)
        if not faces:
            print("No faces detected in source image")
            return None
        
        print(f"Detected {len(faces)} faces in source image")
        face_data = faces[0]  # Get the first detected face
        
        # Debug face data
        print("\nFace data details:")
        print(f"- Bounding box: {face_data['bbox']}")
        print(f"- Embedding shape: {face_data['embedding'].shape}")
        print(f"- Embedding norm: {np.linalg.norm(face_data['embedding'])}")
        print(f"- Embedding min/max: {face_data['embedding'].min():.3f}/{face_data['embedding'].max():.3f}")
        
        # Extract face region
        face_img = self.extract_face(frame, face_data['bbox'])
        
        if face_img is not None:
            result = {
                'face': face_data['face'],
                'embedding': face_data['embedding'],
                'image': face_img
            }
            print("Face analysis complete - data extracted successfully")
            return result
        else:
            print("Failed to extract face image")
            return None

    def set_source_face(self, image: np.ndarray) -> bool:
        """Set the source face for swapping"""
        if image is None:
            print("No image provided")
            return False
        
        try:
            faces = self.face_analyzer.get(image)
            if not faces:
                print("No faces detected in source image")
                return False
            
            # Get the most prominent face
            self.source_face = min(faces, key=lambda x: x.bbox[0])
            self.source_embedding = self.source_face.normed_embedding
            return True
        
        except Exception as e:
            print(f"Error setting source face: {e}")
            return False

    def get_face_preview(self, face) -> Optional[np.ndarray]:
        """Extract face region for preview"""
        if face is None:
            return None
        
        try:
            if not hasattr(face, 'bbox'):
                return None
            
            x1, y1, x2, y2 = map(int, face.bbox)
            if not hasattr(face, 'img') or face.img is None:
                return None
            
            return face.img[y1:y2, x1:x2]
        
        except Exception as e:
            print(f"Error getting face preview: {e}")
            return None

    def draw_debug_info(self, frame: np.ndarray, faces: List[Dict[str, Any]]) -> np.ndarray:
        """Draw debug information on frame"""
        debug_frame = frame.copy()
        for face in faces:
            bbox = face['bbox']
            x1, y1, x2, y2 = map(int, bbox)
            
            # Draw bounding box
            cv2.rectangle(debug_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            # Draw landmarks
            if 'landmarks' in face:
                for point in face['landmarks']:
                    x, y = map(int, point)
                    cv2.circle(debug_frame, (x, y), 1, (0, 0, 255), -1)
            
            # Add text for face information
            text = "Target Face"
            cv2.putText(debug_frame, text, (x1, y1 - 10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        return debug_frame

    def set_debug_mode(self, enabled: bool) -> None:
        """Enable or disable debug visualization"""
        self.debug_mode = enabled
        print(f"Debug mode {'enabled' if enabled else 'disabled'}")

    def preprocess_embedding(self, embedding: np.ndarray) -> np.ndarray:
        """Preprocess face embedding for better matching"""
        # Ensure embedding is float32
        embedding = embedding.astype(np.float32)
        
        # L2 normalization
        norm = np.linalg.norm(embedding)
        if norm > 0:
            embedding = embedding / norm
            
        # Optional: Zero mean
        embedding = embedding - np.mean(embedding)
        
        return embedding

    def _match_faces_between_frames(self, current_faces, previous_faces):
        """Check if faces in current frame match previous frame"""
        if not current_faces or not previous_faces:
            return False
        
        try:
            # Check if number of faces matches
            if len(current_faces) != len(previous_faces):
                return False
            
            # Check each face position
            for curr, prev in zip(current_faces, previous_faces):
                curr_center = self._get_face_center(curr['bbox'])
                prev_center = self._get_face_center(prev['bbox'])
                
                # Calculate position shift
                shift = np.sqrt(
                    (curr_center[0] - prev_center[0])**2 +
                    (curr_center[1] - prev_center[1])**2
                )
                
                # If shift is too large, faces don't match
                if shift > self.max_position_shift:
                    return False
                
            return True
        
        except Exception as e:
            print(f"Error matching faces: {e}")
            return False

    def _get_face_center(self, bbox):
        """Calculate center point of face bounding box"""
        x1, y1, x2, y2 = bbox
        return ((x1 + x2) / 2, (y1 + y2) / 2)

    def reset_face_cache(self):
        """Reset the face caching"""
        self.last_successful_faces = None

    def verify_face_objects(self, source_face, target_face) -> bool:
        """Verify face objects have required attributes"""
        try:
            # Check source face
            if source_face is None:
                print("Source face is None")
                return False
            
            # Check target face
            if target_face is None:
                print("Target face is None")
                return False
            
            # Check required attributes
            required_attrs = ['bbox', 'landmark_2d_106', 'embedding']
            
            for attr in required_attrs:
                if not hasattr(source_face, attr):
                    print(f"Source face missing {attr}")
                    return False
                if not hasattr(target_face, attr):
                    print(f"Target face missing {attr}")
                    return False
                
            return True
        
        except Exception as e:
            print(f"Error verifying face objects: {str(e)}")
            return False

    def test_face_swapper(self):
        """Test face swapper functionality"""
        try:
            print("\nTesting face swapper...")
            # Create a simple test image
            test_img = np.zeros((128, 128, 3), dtype=np.uint8)
            test_img = cv2.rectangle(test_img, (30, 30), (98, 98), (255, 255, 255), -1)
            
            # Test if the model is responsive
            print("Testing model response...")
            result = self.face_swapper.get_input_shape()
            print(f"Model input shape: {result}")
            
            print("Face swapper test complete")
            return True
            
        except Exception as e:
            print(f"Face swapper test failed: {str(e)}")
            return False

    def enhance_face_region(self, image, bbox, strength=1.0):
        """Apply enhancement to the face region"""
        try:
            x1, y1, x2, y2 = map(int, bbox)
            face_region = image[y1:y2, x1:x2]
            
            # Apply subtle sharpening
            kernel = np.array([[-1,-1,-1],
                             [-1, 9,-1],
                             [-1,-1,-1]]) * strength
            sharpened = cv2.filter2D(face_region, -1, kernel)
            
            # Blend the sharpened region with original
            enhanced = cv2.addWeighted(face_region, 0.7, sharpened, 0.3, 0)
            
            # Place enhanced region back
            result = image.copy()
            result[y1:y2, x1:x2] = enhanced
            return result
            
        except Exception as e:
            print(f"Error enhancing face region: {e}")
            return image

def preprocess_celebrities(face_processor, images_dir, max_images_per_celebrity=3):
    """Preprocess celebrity images and return mappings for the gallery."""
    import os
    import cv2
    import numpy as np
    import random

    def load_celebrity_images(images_dir, max_images):
        """Load a limited number of celebrity images from the specified directory."""
        celebrities = {}
        images_dir = get_resource_path('images')
        for celebrity in os.listdir(images_dir):
            celebrity_dir = os.path.join(images_dir, celebrity)
            if os.path.isdir(celebrity_dir):
                # Collect all images in the celebrity's directory
                all_images = [
                    os.path.join(celebrity_dir, file)
                    for file in os.listdir(celebrity_dir)
                    if file.lower().endswith(('.png', '.jpg', '.jpeg'))
                ]
                if all_images:
                    # Randomly select up to max_images
                    selected_images = random.sample(all_images, min(max_images, len(all_images)))
                    celebrities[celebrity] = selected_images
        return celebrities

    print("\nLoading celebrity images...")
    celebrity_images = load_celebrity_images(images_dir, max_images_per_celebrity)
    predefined_faces = {}

    for celebrity, images in celebrity_images.items():
        print(f"\nProcessing {celebrity}...")
        embeddings = []
        valid_faces = []
        preview_image = None

        # Process each image for the celebrity
        for img_path in images:
            try:
                image = cv2.imread(img_path)
                if image is not None:
                    face_data = face_processor.analyze_face(image)
                    if face_data:
                        embeddings.append(face_data['embedding'])
                        valid_faces.append(face_data['face'])
                        if preview_image is None:
                            preview_image = img_path  # Store the first successful image path
            except Exception as e:
                print(f"Error processing {img_path}: {str(e)}")

        if embeddings and preview_image:
            # Create an average embedding from all valid faces
            avg_embedding = np.mean(embeddings, axis=0)
            # Normalize the average embedding
            avg_embedding = avg_embedding / np.linalg.norm(avg_embedding)
            
            predefined_faces[celebrity] = {
                "preview_image": preview_image,  # Store the image path
                "embedding": avg_embedding,
                "all_embeddings": embeddings,
                "all_faces": valid_faces
            }
            print(f"Processed {len(embeddings)} faces for {celebrity}")

    return predefined_faces

```

# src/core/image_loader.py

```py
# src/core/image_loader.py

import os
import cv2

def load_celebrity_images(images_dir):
    """Load celebrity images from the specified directory."""
    celebrities = {}
    for celebrity in os.listdir(images_dir):
        celebrity_dir = os.path.join(images_dir, celebrity)
        if os.path.isdir(celebrity_dir):
            # Collect all images in the celebrity's directory
            images = [
                os.path.join(celebrity_dir, file)
                for file in os.listdir(celebrity_dir)
                if file.lower().endswith(('.png', '.jpg', '.jpeg'))
            ]
            if images:
                celebrities[celebrity] = images
    return celebrities

```

# src/core/video_handler.py

```py
# src/core/video_handler.py

import cv2
import numpy as np
from typing import Optional, Tuple, Callable, List, Dict
from threading import Thread, Lock
import time
import platform
import signal
import subprocess
import sys

class VideoHandler:
    def __init__(self):
        self.camera = None
        self.is_running = False
        self.frame_lock = Lock()
        self.current_frame = None
        self.processing_callback = None
        self.frame_size = (1280, 720)
        self.fps_stats = {'last_time': time.time(), 'frames': 0, 'fps': 0}
        self.process_every_n_frames = 2
        self.frame_count = 0
        self.show_fps = False
        self.capture_thread = None
        
        # Frame caching for smooth transitions
        self.last_processed_frames = []
        self.max_cache_frames = 3
        self.last_successful_swap = None
        self.last_face_positions = None
        
        # Set up signal handler for segfault protection
        if platform.system() == 'Darwin':
            signal.signal(signal.SIGSEGV, self._handle_segfault)
            
    def _handle_segfault(self, signum, frame):
        """Handle segmentation faults gracefully"""
        print("Caught segmentation fault - cleaning up...")
        self.stop_camera()
        # Restart the application
        os.execv(sys.executable, ['python'] + sys.argv)
        
    def _init_camera_backend(self):
        """Initialize appropriate camera backend for the platform"""
        # if platform.system() == 'Darwin':
        #     # Try to use AVFoundation backend on macOS
        #     self.camera_backend = cv2.CAP_AVFOUNDATION
        # else:
        #     self.camera_backend = cv2.CAP_ANY

        self.camera_backend = cv2.CAP_QT

    def _safe_camera_open(self, camera_id: int, backend=None) -> Optional[cv2.VideoCapture]:
        """Safely try to open a camera with timeout"""
        try:
            if backend is not None:
                cap = cv2.VideoCapture(camera_id, backend)
            else:
                cap = cv2.VideoCapture(camera_id)
                
            if not cap.isOpened():
                return None
                
            # Try to read a test frame with timeout
            cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
            start_time = time.time()
            while time.time() - start_time < 2.0:  # 2 second timeout
                ret, frame = cap.read()
                if ret and frame is not None:
                    return cap
                time.sleep(0.1)
                
            # If we couldn't get a frame, release and return None
            cap.release()
            return None
            
        except Exception as e:
            print(f"Error opening camera {camera_id}: {str(e)}")
            return None
            
    def _create_capture(self, camera_id: int) -> cv2.VideoCapture:
        """Create camera capture with appropriate settings"""
        if platform.system() == 'Darwin':
            capture = cv2.VideoCapture(camera_id, cv2.CAP_AVFOUNDATION)
        else:
            capture = cv2.VideoCapture(camera_id)
            
        if capture.isOpened():
            capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_size[0])
            capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_size[1])
            capture.set(cv2.CAP_PROP_FPS, 30)
            capture.set(cv2.CAP_PROP_BUFFERSIZE, 1)
            
        return capture
        
    def start_camera(self, camera_id: int = 0) -> bool:
        self.stop_camera()
        time.sleep(0.5)
        
        try:
            self.camera = cv2.VideoCapture(camera_id)
            
            if not self.camera.isOpened():
                if platform.system() == 'Darwin':
                    self.camera = cv2.VideoCapture(camera_id, cv2.CAP_AVFOUNDATION)
                    
            if not self.camera.isOpened():
                return False
            
            # Force specific frame size
            self.frame_size = (1280, 720)  # Fixed size
            self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_size[0])
            self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_size[1])
            
            # Verify size was set
            actual_width = self.camera.get(cv2.CAP_PROP_FRAME_WIDTH)
            actual_height = self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
            print(f"Camera resolution: {actual_width}x{actual_height}")
            
            self.is_running = True
            self.capture_thread = Thread(target=self._protected_capture_loop, daemon=True)
            self.capture_thread.start()
            return True
            
        except Exception as e:
            print(f"Error starting camera: {e}")
            self.stop_camera()
            return False

    def _protected_capture_loop(self):
        """Protected version of capture loop"""
        try:
            self._capture_loop()
        except Exception as e:
            print(f"Error in capture loop: {str(e)}")
            self.stop_camera()
            
    def stop_camera(self):
        """Stop camera and clear cache"""
        self.is_running = False
        if self.capture_thread:
            self.capture_thread.join(timeout=1.0)
        if self.camera:
            self.camera.release()
            self.camera = None
        time.sleep(0.5)  # Allow camera to fully release
        with self.frame_lock:
            self.current_frame = None

    def _capture_loop(self):
        """Main capture loop running in separate thread"""
        frame_counter = 0
        while self.is_running and self.camera and self.camera.isOpened():
            ret, frame = self.camera.read()
            if not ret or frame is None:
                continue
                
            frame_counter += 1
            if frame_counter % self.process_every_n_frames != 0:
                continue
                
            processed_frame = frame.copy()
            
            if self.processing_callback:
                try:
                    result = self.processing_callback(processed_frame)
                    if result is not None:
                        processed_frame = result
                except Exception as e:
                    print(f"Error in frame processing: {e}")
            
            # Thread-safe frame update
            with self.frame_lock:
                self.current_frame = processed_frame
        
    def _update_fps(self):
        """Update FPS calculation"""
        current_time = time.time()
        delta_time = current_time - self.fps_stats['last_time']
        
        if delta_time >= 1.0:
            self.fps_stats['fps'] = self.fps_stats['frames'] / delta_time
            self.fps_stats['frames'] = 0
            self.fps_stats['last_time'] = current_time
        else:
            self.fps_stats['frames'] += 1
            
    def get_camera_list(self) -> List[dict]:
        """Get list of available cameras"""
        cameras = []
        # Only check first few indices on macOS
        max_cameras = 3 if platform.system() == 'Darwin' else 5
        
        for i in range(max_cameras):
            try:
                print(f"Checking camera {i}...")
                cap = cv2.VideoCapture(i)
                if cap.isOpened():
                    ret, test_frame = cap.read()
                    if ret and test_frame is not None:
                        cameras.append({
                            'id': i,
                            'name': f'Camera {i}'
                        })
                        print(f"Found working camera {i}")
                cap.release()
            except Exception as e:
                print(f"Error checking camera {i}: {str(e)}")
                
        return cameras
        
    def get_latest_frame(self) -> Optional[np.ndarray]:
        """Thread-safe method to get the latest frame"""
        with self.frame_lock:
            if self.current_frame is None:
                return None
            return self.current_frame.copy()

    def set_frame_size(self, width: int, height: int):
        """Set capture frame size"""
        self.frame_size = (width, height)
        if self.camera and self.camera.isOpened():
            self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
            self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
            
    def set_processing_callback(self, callback: Callable):
        """Set callback for frame processing"""
        self.processing_callback = callback

    def set_frame_processing_rate(self, process_every_n: int):
        """Set how often frames should be processed"""
        self.process_every_n_frames = max(1, process_every_n)
        print(f"Processing every {self.process_every_n_frames} frames")

    def clear_cache(self):
        """Clear the frame cache"""
        self.last_processed_frames = []
        self.last_successful_swap = None
        self.last_face_positions = None
```

# src/main.py

```py
# src/main.py

import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from src.ui.main_window import MainWindow  # Updated import

def main():
    # Enable high DPI scaling
    if hasattr(Qt, 'AA_EnableHighDpiScaling'):
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    
    # Create application
    app = QApplication(sys.argv)
    
    # Create and show main window
    window = MainWindow()
    window.show()
    
    # Start event loop
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
```

# src/ui/__init__.py

```py

```

# src/ui/camera_view.py

```py

```

# src/ui/face_gallery.py

```py
# src/ui/face_gallery.py

from PyQt6.QtWidgets import QDialog, QVBoxLayout, QGridLayout, QPushButton, QLabel, QScrollArea, QWidget
from PyQt6.QtGui import QPixmap, QImage, QIcon
from PyQt6.QtCore import Qt
import cv2

class FaceGallery(QDialog):
    def __init__(self, predefined_faces, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select a Face")
        self.setMinimumSize(800, 600)
        self.predefined_faces = predefined_faces
        self.selected_face = None
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        
        # Add scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        layout.addWidget(scroll)
        
        # Create container widget for scroll area
        container = QWidget()
        grid_layout = QGridLayout(container)
        scroll.setWidget(container)

        # Add faces to grid
        row, col = 0, 0
        for name, data in self.predefined_faces.items():
            try:
                # Create frame for each celebrity
                frame = QWidget()
                frame_layout = QVBoxLayout(frame)
                
                # Create image button
                button = QPushButton()
                button.setFixedSize(150, 150)
                
                # Load and set image
                if 'preview_image' in data:
                    image = cv2.imread(data['preview_image'])
                    if image is not None:
                        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                        h, w = image.shape[:2]
                        q_image = QImage(image.data, w, h, w * 3, QImage.Format.Format_RGB888)
                        pixmap = QPixmap.fromImage(q_image)
                        scaled_pixmap = pixmap.scaled(
                            150, 150,
                            Qt.AspectRatioMode.KeepAspectRatio,
                            Qt.TransformationMode.SmoothTransformation
                        )
                        button.setIcon(QIcon(scaled_pixmap))
                        button.setIconSize(button.size())
                
                button.clicked.connect(lambda checked, n=name: self.select_face(n))
                frame_layout.addWidget(button)
                
                # Add name label
                label = QLabel(name)
                label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                frame_layout.addWidget(label)
                
                grid_layout.addWidget(frame, row, col)
                
                # Update grid position
                col += 1
                if col > 3:
                    col = 0
                    row += 1
                    
            except Exception as e:
                print(f"Error adding {name} to gallery: {str(e)}")

    def select_face(self, name):
        self.selected_face = name
        self.accept()
```

# src/ui/face_mapping.py

```py
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
```

# src/ui/main_window.py

```py
# src/ui/main_window.py

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
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(33)
        # Load celebrity images
        images_dir = "images"  # Path to your images directory
        self.predefined_faces = preprocess_celebrities(self.face_processor, images_dir)
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
        self.threshold_slider.setValue(int(self.face_processor.similarity_threshold * 100))
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
        """Open the gallery pop-out window."""
        try:
            from src.ui.face_gallery import FaceGallery
            
            if not self.predefined_faces:
                print("No predefined faces available")
                QMessageBox.warning(self, "Error", "No predefined faces available")
                return
                
            print(f"Opening gallery with {len(self.predefined_faces)} faces")
            gallery = FaceGallery(self.predefined_faces, self)
            
            if gallery.exec():  # Modal dialog
                selected_face = gallery.selected_face
                if selected_face and selected_face in self.predefined_faces:
                    face_data = self.predefined_faces[selected_face]
                    image = cv2.imread(face_data['preview_image'])
                    if image is not None:
                        self.set_source_face(image, face_data)
                        print(f"Selected face: {selected_face}")
                    else:
                        print(f"Failed to load image for {selected_face}")
                        QMessageBox.warning(self, "Error", f"Failed to load image for {selected_face}")
                
        except Exception as e:
            print(f"Error opening face gallery: {str(e)}")
            QMessageBox.warning(self, "Error", f"Error opening face gallery: {str(e)}")

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

    def update_frame(self):
        frame = self.video_handler.get_latest_frame()
        if frame is None:
            return

        if self.face_processor and hasattr(self.face_processor, 'process_frame'):
            processed_frame = self.face_processor.process_frame(frame)
            if processed_frame is not None:
                frame = processed_frame

        if not self.show_face_brackets:
            # Clear face brackets if the toggle is off
            frame = self.clear_brackets(frame)

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w = frame.shape[:2]
        bytes_per_line = 3 * w
        qt_image = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(qt_image).scaled(
            640, 480, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation
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
        """Set up frame processing based on current source face"""
        if self.source_face:
            print("\nSetting up face processor with source face...")
            print("Source face information:")
            print(f" - Face object present: {self.source_face['face'] is not None}")
            print(f" - Embedding shape: {self.source_face['embedding'].shape}")
            
            # Create a simple mapping with the current source face
            self.face_processor.set_face_mappings({
                'default': {
                    'source_face': {
                        'face': self.source_face['face'],
                        'embedding': self.source_face['embedding']
                    },
                    'target_face': None
                }
            })
            
            # Ensure the video handler is using the face processor
            self.video_handler.set_processing_callback(self.face_processor.process_frame)
            print("Face processor connected to video stream")
        else:
            print("Clearing face processor")
            self.video_handler.set_processing_callback(None)

    def toggle_debug(self, checked):
        """Toggle debug visualization"""
        self.debug_toggle.setText("Debug: On" if checked else "Debug: Off")
        if hasattr(self, 'face_processor'):
            self.face_processor.set_debug_mode(checked)

    def update_threshold(self, value):
        """Update similarity threshold"""
        threshold = value / 100.0
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
        """Toggle the video window"""
        try:
            if self.video_window is None:
                from src.ui.video_window import VideoWindow
                self.video_window = VideoWindow(self)  # Set parent to main window
                self.video_window.closed.connect(self.on_video_window_closed)
                self.video_window.show()
                self.popout_button.setText("Close Video Window")

                # Route video frames to the popout window
                self.video_handler.set_processing_callback(self.video_window.update_frame)
            else:
                self.video_window.close()
                self.video_window = None
                self.popout_button.setText("Popout Video")
                self.video_handler.set_processing_callback(self.update_frame)
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
        """Set the source face and update the UI."""
        if image is None:
            QMessageBox.warning(self, "Error", "No valid image provided")
            return

        if data is None:
            # Single image processing
            face_data = self.face_processor.analyze_face(image)
            if not face_data:
                QMessageBox.warning(self, "Error", "No face detected in the image")
                return
                
            self.source_face = {
                'face': face_data['face'],
                'embedding': face_data['embedding'],
                'image': face_data['image']
            }
        else:
            # Celebrity with multiple faces
            self.source_face = {
                'face': data.get('all_faces', [None])[0],  # First face for preview
                'embedding': data['embedding'],  # Average embedding
                'all_faces': data['all_faces'],  # All face objects
                'all_embeddings': data['all_embeddings'],  # All embeddings
                'image': cv2.imread(data['preview_image'])  # Preview image
            }
            
        # Update the preview with the first/main image
        self.update_preview(self.source_face['image'])
        self.set_frame_processor()
        print("Source face updated successfully")

    def toggle_enhancement(self, state):
        """Toggle face enhancement"""
        self.face_processor.use_face_enhancement = bool(state)

    def update_enhancement(self, value):
        """Update enhancement strength"""
        self.face_processor.enhancement_level = value / 50.0  # Scale to 0-2 range

```

# src/ui/video_window.py

```py
# src/ui/video_window.py

import cv2
import numpy as np
from PyQt6.QtWidgets import QMainWindow, QLabel, QMenuBar, QMenu, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QImage, QPixmap, QAction

class VideoWindow(QMainWindow):
    closed = pyqtSignal()  # Signal emitted when window is closed

    def __init__(self, parent=None):
        super().__init__(parent)
        self.last_size = None  # Store last valid size
        self.init_ui()

    def init_ui(self):
        """Initialize the UI"""
        self.setWindowTitle("Video Feed")
        self.setMinimumSize(640, 480)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)

        # Create video display label
        self.video_label = QLabel()
        self.video_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.video_label.setMinimumSize(640, 480)
        self.video_label.setStyleSheet("""
            QLabel {
                background-color: #222;
                border: 1px solid #666;
            }
        """)
        layout.addWidget(self.video_label)

        # Create menu bar
        menubar = QMenuBar()
        self.setMenuBar(menubar)

        # View menu
        view_menu = QMenu("View", self)
        menubar.addMenu(view_menu)

        # Size presets
        self.add_size_presets(view_menu)

    def add_size_presets(self, menu):
        """Add size preset options to menu"""
        sizes = {
            "640x480": (640, 480),
            "800x600": (800, 600),
            "1280x720": (1280, 720),
            "1920x1080": (1920, 1080)
        }

        size_menu = menu.addMenu("Window Size")
        for name, (width, height) in sizes.items():
            action = QAction(name, self)
            action.triggered.connect(lambda checked, w=width, h=height: self.resize(w, h))
            size_menu.addAction(action)

    def update_frame(self, frame):
        """Update the video frame displayed in the QLabel"""
        if frame is None:
            return
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_frame.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(qt_image)
        self.video_label.setPixmap(pixmap)

    def resizeEvent(self, event):
        """Handle resize events"""
        try:
            super().resizeEvent(event)
            current_pixmap = self.video_label.pixmap()
            if current_pixmap and not current_pixmap.isNull():
                scaled_pixmap = current_pixmap.scaled(
                    self.video_label.size(),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                )
                self.video_label.setPixmap(scaled_pixmap)
                self.last_size = self.size()
            elif self.last_size:
                # Restore last valid size if current resize fails
                self.resize(self.last_size)
                
        except Exception as e:
            print(f"Error handling resize: {str(e)}")

    def closeEvent(self, event):
        """Handle window close event"""
        try:
            self.closed.emit()
            super().closeEvent(event)
        except Exception as e:
            print(f"Error closing video window: {str(e)}")
            event.accept()
```

