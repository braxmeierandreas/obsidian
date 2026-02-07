@echo off
setlocal
set "VENV_DIR=venv"
set "MAIN_SCRIPT=main.py"

echo === Muehle Ultimate Starter ===
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python wurde nicht gefunden! Bitte installiere Python.
    pause
    exit /b
)

if not exist "%VENV_DIR%" (
    echo Erstelle virtuelle Umgebung...
    python -m venv %VENV_DIR%
)

call "%VENV_DIR%\Scripts\activate"

echo Installiere Abhaengigkeiten...
pip install pygame

echo Starte das Spiel...
python "%MAIN_SCRIPT%"

if %errorlevel% neq 0 (
    echo.
    echo Das Spiel wurde mit einem Fehler beendet (Code: %errorlevel%).
    if exist crash_log.txt (
        echo Fehlerdetails in crash_log.txt gespeichert:
        type crash_log.txt
    )
    pause
)

deactivate