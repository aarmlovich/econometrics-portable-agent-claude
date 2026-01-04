@echo off
REM Setup script for Econometrics Portable Agent (Windows)
REM Creates virtual environment and installs all dependencies

echo ======================================
echo Econometrics Portable Agent Setup
echo ======================================
echo.

REM Check Python version
echo Checking Python version...
python --version
if %errorlevel% neq 0 (
    echo Error: Python not found. Please install Python 3.10 or higher.
    exit /b 1
)
echo.

REM Create virtual environment
echo Creating virtual environment...
if exist venv (
    echo Warning: venv directory already exists.
    set /p response="Remove it? (y/n): "
    if /i "%response%"=="y" (
        rmdir /s /q venv
        python -m venv venv
        echo Virtual environment created
    ) else (
        echo Using existing venv
    )
) else (
    python -m venv venv
    echo Virtual environment created
)
echo.

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo Error: Failed to activate virtual environment
    exit /b 1
)
echo Virtual environment activated
echo.

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip --quiet
echo pip upgraded
echo.

REM Install requirements
echo Installing requirements from requirements.txt...
pip install -r requirements.txt --quiet
echo Requirements installed
echo.

REM Install package in editable mode
echo Installing package in editable mode...
pip install -e . --quiet
echo Package installed
echo.

REM Install test dependencies
echo Installing test dependencies...
pip install pytest pytest-cov --quiet
echo Test dependencies installed
echo.

echo ======================================
echo Setup Complete!
echo ======================================
echo.
echo To activate the virtual environment:
echo   venv\Scripts\activate
echo.
echo To deactivate:
echo   deactivate
echo.
echo To run tests:
echo   pytest tests/
echo.
echo To verify installation:
echo   python -c "import src; print('Package imported successfully!')"
echo.
pause
