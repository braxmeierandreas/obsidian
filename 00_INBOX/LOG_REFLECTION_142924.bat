@echo off
echo Starte Reflexions-System...
python "00_SCRIPTS\create_reflection_entry.py"

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ❌ Es gab einen Fehler!
    echo Bitte überprüfe die Fehlermeldung oben.
    pause
) else (
    echo.
    echo ✅ Fertig! Das Fenster kann geschlossen werden.
    timeout /t 3 >nul
)
