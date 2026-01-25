@echo off
REM --- MASTER LAUNCHER: EVERYTHING ---
setlocal

set "SCRIPTS_DIR=%~dp0"
set "HABITS_SCRIPT=%SCRIPTS_DIR%..\17_HABITS\RUN_HABITS.bat"

echo ========================================================
echo      MASTER SYNC: FINANCE + MORNING ROUTINE
echo ========================================================
echo.

echo [STEP 1/3] Updating Trading and Finance...
call "%SCRIPTS_DIR%UPDATE_TRADING.bat"

echo.
echo [STEP 2/3] Starting Morning Routine...
call "%SCRIPTS_DIR%START_MY_DAY.bat"

echo.
echo [STEP 3/3] Habit ^& Addiction Check-in...
call "%HABITS_SCRIPT%"

echo.
echo ========================================================
echo      ALL SYSTEMS UPDATED AND READY!
echo ========================================================
echo Druecke eine Taste, um dieses Fenster zu schliessen.
pause >nul

endlocal