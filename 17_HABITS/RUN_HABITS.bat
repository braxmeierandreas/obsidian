@echo off
REM --- HABIT TRACKER LAUNCHER ---
setlocal

set "SCRIPT_DIR=%~dp0"
set "TRACKER_SCRIPT=%SCRIPT_DIR%habit_tracker.py"

echo.
echo ========================================
echo      HABIT ^& ADDICTION TRACKER
echo ========================================
echo.

python "%TRACKER_SCRIPT%"

echo.
pause
endlocal