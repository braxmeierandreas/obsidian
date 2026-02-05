@echo off
chcp 65001 > nul
cls
echo ==========================================
echo      ANDREAS' TASK MANAGER v1.0
echo ==========================================
echo.
echo [1/3] Lese Kanban Board...
echo [2/3] Verbinde mit Google Tasks...
echo.

python "%~dp0sync_and_manage.py"

echo.
echo ==========================================
echo.
echo Druecke eine Taste, um das Board zu oeffnen...
pause > nul

start "" "obsidian://open?file=26_TASK_MANAGER/KANBAN_BOARD"
