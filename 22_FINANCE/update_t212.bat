@echo off
echo ---------------------------------------------------
echo  MASTER SYNC: Alle Finanz-Daten werden aktualisiert
echo ---------------------------------------------------
set "TRADING_ROOT=%~dp0"
set "VAULT_ROOT=%TRADING_ROOT%..\"
set "PYTHON_EXE=%VAULT_ROOT%15_GOOGLE\.venv\Scripts\python.exe"

"%PYTHON_EXE%" "%TRADING_ROOT%03_SCRIPTS\update_all.py"
echo.

echo ---------------------------------------------------
pause
