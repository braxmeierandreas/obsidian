@echo off
echo ==========================================
echo      🧹 OBSIDIAN VAULT CLEANUP CREW
echo ==========================================
echo.

cd /d "%~dp0"

echo [1/2] Suche nach Sync-Konflikten...
python "CHECK_SYNC_CONFLICTS.py"
echo.

echo [2/2] Raeume Root-Verzeichnis auf...
python "AUTO_MOVE_ROOT_FILES.py"
echo.

echo ==========================================
echo      ✅ Wartung abgeschlossen
echo ==========================================
pause