@echo off
echo Starte Anki-Synchronisation...

REM %~dp0 steht für den Ordner, in dem diese .bat Datei liegt.
python "%~dp0anki_import.py"

echo.
echo Fertig.