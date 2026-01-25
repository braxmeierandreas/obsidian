@echo off
REM --- HABIT TRACKER LAUNCHER ---
setlocal

set "SCRIPT_DIR=%~dp0"
set "ROOT_DIR=%SCRIPT_DIR%.."
set "PYTHON_EXE=%ROOT_DIR%\15_GOOGLE\.venv\Scripts\python.exe"
set "TRACKER_SCRIPT=%SCRIPT_DIR%habit_tracker.py"

echo.
echo ========================================
echo      HABIT ^& ADDICTION TRACKER
echo ========================================
echo.

"%PYTHON_EXE%" "%TRACKER_SCRIPT%"

echo.
endlocal