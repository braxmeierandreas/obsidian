@echo off
setlocal

set "VENV_DIR=venv"
set "REQ_FILE=requirements.txt"
set "MAIN_SCRIPT=main.py"

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python ist nicht installiert oder nicht im PATH.
    pause
    exit /b
)

if not exist "%VENV_DIR%" (
    echo Erstelle virtuelle Umgebung...
    python -m venv %VENV_DIR%
)

call "%VENV_DIR%\Scripts\activate"

echo Installiere/Pruefe Abhaengigkeiten...
pip install pygame >nul

echo Starte Snake...
python "%MAIN_SCRIPT%"

deactivate
