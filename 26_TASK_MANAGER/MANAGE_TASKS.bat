@echo off
chcp 65001 > nul
setlocal

set "SCRIPTS_DIR=%~dp0"
set "VAULT_ROOT=%~dp0.."
set "PYTHON_EXE=%VAULT_ROOT%\15_GOOGLE\.venv\Scripts\python.exe"

REM Fallback if venv python doesn't exist
if not exist "%PYTHON_EXE%" set "PYTHON_EXE=python"

cls
echo ==========================================
echo      ANDREAS' TASK MANAGER v2.0 (Pro)
echo ==========================================
echo.
echo [1/3] Lese Kanban Board...
echo [2/3] Bi-Directional Sync mit Google Tasks...
echo.

"%PYTHON_EXE%" "%~dp0sync_and_manage.py"

echo.
echo ==========================================
echo.
echo Druecke eine Taste, um das Board zu oeffnen...
pause > nul

start "" "obsidian://open?file=26_TASK_MANAGER/KANBAN_BOARD"
endlocal