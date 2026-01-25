@echo off
echo ==========================================
echo      Finance App Enterprise Launcher
echo ==========================================

set "TRADING_ROOT=%~dp0"
set "VAULT_ROOT=%TRADING_ROOT%..\"
set "PYTHON_EXE=%VAULT_ROOT%15_GOOGLE\.venv\Scripts\python.exe"

echo [1/3] Checking Dependencies (Skipping auto-install for speed)...
:: "%PYTHON_EXE%" -m pip install -r requirements.txt

echo [2/3] Running Logic Tests...
"%PYTHON_EXE%" -m unittest discover tests
if %errorlevel% neq 0 (
    echo TESTS FAILED! Fix issues before running UI.
    pause
    exit /b %errorlevel%
)

echo [3/3] Starting App...
"%PYTHON_EXE%" finance_app.py

pause