@echo off
setlocal
set "VENV_DIR=venv"
set "MAIN_SCRIPT=main.py"
python --version >nul 2>&1
if %errorlevel% neq 0 (echo Python nicht gefunden. & pause & exit /b)
if not exist "%VENV_DIR%" (python -m venv %VENV_DIR%)
call "%VENV_DIR%\Scripts\activate"
pip install pygame >nul
python "%MAIN_SCRIPT%"
deactivate
