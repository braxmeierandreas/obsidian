@echo off
REM --- HABIT STREAK SETUP LAUNCHER ---
setlocal

set "SCRIPT_DIR=%~dp0"
set "SETUP_SCRIPT=%SCRIPT_DIR%setup_streaks.py"

echo.
echo ========================================
echo      HABIT STREAK SETUP (INITIAL)
echo ========================================
echo.

python "%SETUP_SCRIPT%"

echo.
endlocal