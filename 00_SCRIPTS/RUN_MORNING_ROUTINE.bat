@echo off
chcp 65001 >nul
:: Use dynamic path for robustness
set "SCRIPT_ROOT=%~dp0"
set "VAULT_ROOT=%SCRIPT_ROOT%.."
set "PYTHON_EXE=%VAULT_ROOT%\15_GOOGLE\.venv\Scripts\python.exe"

echo --- Starte Morning Routine (Andreas Braxmeier) ---

echo [1/3] Aktualisiere Live-Metriken im Dashboard...
"%PYTHON_EXE%" "%SCRIPT_ROOT%\routine_dashboard_update.py"

echo [2/3] Generiere neues Morning Briefing...
"%PYTHON_EXE%" "%SCRIPT_ROOT%\routine_daily_briefing.py"

echo [3/3] Öffne Obsidian...
:: Obsidian URI (Generic Vault Name lookup or hardcoded if stable)
set "TODAY=%DATE:~-4%-%DATE:~-7,2%-%DATE:~-10,2%"
start "" "obsidian://open?vault=Obsidian&file=02_JOURNAL%%2F08_BRIEFING%%2FBRIEFING_%TODAY%"

echo --- Fertig! Viel Erfolg heute, Andreas. ---
timeout /t 5 >nul