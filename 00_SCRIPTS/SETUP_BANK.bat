@echo off
cd /d "%~dp0"
echo.
echo ========================================================
echo   COMDIRECT SETUP - EINMALIGE AKTIVIERUNG
echo ========================================================
echo.
echo 1. Das Skript startet gleich.
echo 2. Du bekommst eine Push-Nachricht auf dein Handy.
echo 3. Bestaetige sie.
echo 4. WICHTIG: Tippe die TAN, die in der App steht, hier ein!
echo.
pause
python bank_sync_comdirect.py
echo.
echo Falls erfolgreich: Das Fenster schliesst sich gleich.
echo Falls Fehler: Bitte Screenshot machen oder Fehler lesen.
pause
