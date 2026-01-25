@echo off
echo Starte Anki-Synchronisation...

REM %~dp0 steht für den Ordner, in dem diese .bat Datei liegt.
REM So wird das Python-Skript immer gefunden, egal von wo aus die .bat gestartet wird.
python "%~dp0\..\03_UNIVERSITY\03_AGF2\07_REVIEW_PROCESS\ELABORATION\SKRIPTE\anki_import.py"

echo.
echo Fertig.
pause
