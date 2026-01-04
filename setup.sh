#!/bin/bash
# Setup script for Econometrics Portable Agent
# Creates virtual environment and installs all dependencies

set -e  # Exit on error

echo "======================================"
echo "Econometrics Portable Agent Setup"
echo "======================================"
echo ""

# Check Python version
echo "Checking Python version..."
python3 --version

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
REQUIRED_VERSION="3.10"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
    echo "Error: Python 3.10 or higher required. Found Python $PYTHON_VERSION"
    exit 1
fi

echo "✓ Python $PYTHON_VERSION detected"
echo ""

# Create virtual environment
echo "Creating virtual environment..."
if [ -d "venv" ]; then
    echo "Warning: venv directory already exists. Remove it? (y/n)"
    read -r response
    if [ "$response" = "y" ]; then
        rm -rf venv
        python3 -m venv venv
        echo "✓ Virtual environment created"
    else
        echo "Using existing venv"
    fi
else
    python3 -m venv venv
    echo "✓ Virtual environment created"
fi
echo ""

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo "✓ Virtual environment activated"
echo ""

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip --quiet
echo "✓ pip upgraded"
echo ""

# Install requirements
echo "Installing requirements from requirements.txt..."
pip install -r requirements.txt --quiet
echo "✓ Requirements installed"
echo ""

# Install package in editable mode
echo "Installing package in editable mode..."
pip install -e . --quiet
echo "✓ Package installed"
echo ""

# Install test dependencies
echo "Installing test dependencies..."
pip install pytest pytest-cov --quiet
echo "✓ Test dependencies installed"
echo ""

echo "======================================"
echo "Setup Complete!"
echo "======================================"
echo ""
echo "To activate the virtual environment:"
echo "  source venv/bin/activate"
echo ""
echo "To deactivate:"
echo "  deactivate"
echo ""
echo "To run tests:"
echo "  pytest tests/"
echo ""
echo "To verify installation:"
echo "  python -c 'import src; print(\"Package imported successfully!\")'"
echo ""
