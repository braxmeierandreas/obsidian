@echo off
echo ==========================================
echo      OBSIDIAN VAULT CLEANUP CREW
echo ==========================================
echo.

cd /d "%~dp0"

echo [1/3] Suche nach Sync-Konflikten...
python "CHECK_SYNC_CONFLICTS.py"
echo.

echo [2/3] Strukturiere Ordner neu...
python "AUTO_RENAME_FOLDERS.py"
echo.

echo [3/3] Raeume Root-Verzeichnis auf...
python "AUTO_MOVE_ROOT_FILES.py"
echo.

echo ==========================================
echo      WARTUNG ABGESCHLOSSEN
echo ==========================================
pause
