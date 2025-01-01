#!/bin/bash
# run.sh

# Add the project root to PYTHONPATH
export PYTHONPATH="$PYTHONPATH:$(pwd)"

# Run the application
python src/main.py
