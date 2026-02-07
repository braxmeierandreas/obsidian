@echo off
setlocal enabledelayedexpansion

echo ===================================================
echo      Wahrheit oder Pflicht - ANDROID BUILDER (V4)
echo ===================================================
echo.

wsl --status >nul 2>&1
if %errorlevel% neq 0 (
    echo [FEHLER] WSL ist nicht installiert.
    pause
    exit /b
)

echo [1/2] Pruefe/Installiere Buildozer und Cython...
wsl sudo apt update >nul
wsl sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses-dev cmake libffi-dev libssl-dev python3-dev >nul
wsl pip3 install --user --upgrade buildozer cython --break-system-packages >nul

echo [2/2] Starte Build-Prozess...
echo.

REM Fix: Laufwerkbuchstabe zu Kleinbuchstabe konvertieren fuer WSL
set "DRIVE=%CD:~0,1%"
for %%i in (a b c d e f g h i j k l m n o p q r s t u v w x y z) do (
    set "TEMP_DRIVE=%%i"
    if /I "!DRIVE!"=="!TEMP_DRIVE!" set "DRIVE_LOWER=%%i"
)
set "REST_PATH=%CD:~3%"
set "REST_PATH=%REST_PATH:\=/%"
set "WSL_DIR=/mnt/%DRIVE_LOWER%/%REST_PATH%"

echo Linux-Pfad: %WSL_DIR%
echo.
echo Der erste Build dauert ca. 15-30 Minuten.
echo Wenn du gefragt wirst: "Do you want to continue?", tippe 'y' und Enter.
echo.

wsl bash -c "cd '%WSL_DIR%' && ~/.local/bin/buildozer android debug"

echo.
echo ===================================================
if exist "bin\*.apk" (
    echo [ERFOLG] APK wurde erstellt! Schau in den Ordner 'bin'.
) else (
    echo [FEHLER] APK wurde nicht erzeugt. 
    echo Bitte scrolle im Fenster hoch, um den Fehler zu finden.
)
pause