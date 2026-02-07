@echo off
setlocal

:: Define paths
set "VENV_DIR=venv"
set "REQ_FILE=requirements.txt"
set "MAIN_SCRIPT=main.py"

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH. Please install Python.
    pause
    exit /b
)

:: Create Virtual Environment if it doesn't exist
if not exist "%VENV_DIR%" (
    echo Creating virtual environment...
    python -m venv %VENV_DIR%
)

:: Activate Virtual Environment
call "%VENV_DIR%\Scripts\activate"

:: Install Requirements
echo Checking dependencies...
pip install pygame chess >nul

:: Run the Game
echo Starting Chess...
python "%MAIN_SCRIPT%"

:: Deactivate (optional, script ends anyway)
deactivate
