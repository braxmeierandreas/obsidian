@echo off
REM --- Trading Update Script ---
setlocal

set "SCRIPTS_DIR=%~dp0"
set "VAULT_ROOT=%~dp0.."
set "PYTHON_EXE=%VAULT_ROOT%\15_GOOGLE\.venv\Scripts\python.exe"
set "SCRIPT_PATH=%VAULT_ROOT%\14_TRADING\03_SCRIPTS\update_all.py"

echo ========================================================
echo      UPDATING TRADING 212 AND FINANCE DASHBOARDS
echo ========================================================
echo.

if not exist "%PYTHON_EXE%" (
    echo [ERROR] Python Environment not found: %PYTHON_EXE%
    pause
    exit /b
)

if not exist "%SCRIPT_PATH%" (
    echo [ERROR] Update Script not found: %SCRIPT_PATH%
    pause
    exit /b
)

echo Starting Update...
"%PYTHON_EXE%" "%SCRIPT_PATH%"

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Update failed with error level %errorlevel%
) else (
    echo.
    echo [SUCCESS] Update complete!
)

endlocal
