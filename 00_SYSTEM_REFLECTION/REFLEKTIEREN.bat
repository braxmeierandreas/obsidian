@echo off
setlocal
echo 🧠 Starte Reflexions-System...

:: Absoluter Pfad zum Skript basierend auf dem Speicherort dieser BAT
set "SCRIPT_PATH=%~dp000_SYSTEM_REFLECTION\create_log.py"

if exist "%SCRIPT_PATH%" (
    python "%SCRIPT_PATH%"
) else (
    echo ❌ FEHLER: Skript nicht gefunden unter %SCRIPT_PATH%
    pause
)

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ❌ Es gab ein Problem beim Ausfuehren des Skripts.
    pause
) else (
    timeout /t 2 >nul
)
