@echo off
setlocal

:: Pfad zum Skript
set "SCRIPT_PATH=%~dp000_SYSTEM_REFLECTION\create_log.py"

if exist "%SCRIPT_PATH%" (
    python "%SCRIPT_PATH%"
) else (
    echo ❌ FEHLER: Skript nicht gefunden unter %SCRIPT_PATH%
)

:: Warten, damit man das Ergebnis sieht
echo.
echo Druecke eine Taste zum Schliessen...
pause >nul
