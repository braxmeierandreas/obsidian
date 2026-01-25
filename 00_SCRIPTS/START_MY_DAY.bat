@echo off
REM --- Morning Routine Script ---
setlocal

set "SCRIPTS_DIR=%~dp0"
set "VAULT_ROOT=%~dp0.."
set "PYTHON_EXE=%VAULT_ROOT%\15_GOOGLE\.venv\Scripts\python.exe"
set "VAULT_NAME=Obsidian"

echo ========================================================
echo      STARTING DAY FOR ANDREAS BRAXMEIER
echo ========================================================
echo.

echo [1/4] Syncing Sparkasse...
"%PYTHON_EXE%" "%SCRIPTS_DIR%BANKING\bank_sync_sparkasse.py"

echo [2/4] Updating Dashboard Data...
"%PYTHON_EXE%" "%SCRIPTS_DIR%routine_dashboard_update.py"

echo [3/4] Updating Google Data and YouTube...
"%PYTHON_EXE%" "%SCRIPTS_DIR%GOOGLE\google_contacts.py"
"%PYTHON_EXE%" "%SCRIPTS_DIR%GOOGLE\google_youtube_assistant.py"

echo [4/4] Generating Morning Briefing...
"%PYTHON_EXE%" "%SCRIPTS_DIR%routine_daily_briefing.py"

if %errorlevel% neq 0 (
    echo [ERROR] Error generating briefing.
) else (
    echo [SUCCESS] Briefing created successfully.
)

echo.
echo Opening Obsidian Vault...
for /f %%I in ('powershell -NoProfile -Command "Get-Date -Format 'yyyy-MM-dd'"') do set TODAY=%%I

set "URI=obsidian://open?vault=%VAULT_NAME%&file=02_JOURNAL%%2F08_BRIEFING%%2FBRIEFING_%TODAY%"
start "" "%URI%"

echo.
echo ========================================================
echo      HAVE A PRODUCTIVE DAY!
echo ========================================================

endlocal