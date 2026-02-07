@echo off
setlocal

echo ===================================================
echo      Wahrheit oder Pflicht - APP BUILDER (FINAL)
echo ===================================================
echo.

:: Wir nutzen PowerShell um den Pfad absolut sicher fuer WSL zu konvertieren
for /f "usebackq tokens=*" %%i in (`powershell -command "$p = (Get-Location).Path; $p = '/mnt/' + $p.Substring(0,1).ToLower() + $p.Substring(2).Replace('\','/'); Write-Output $p"`) do set "WSL_DIR=%%i"

echo Dein Pfad wird vorbereitet...
echo Linux-Verzeichnis: %WSL_DIR%
echo.
echo Der Prozess startet jetzt. Bitte hab ca. 20-30 Min Geduld.
echo Lizenzen werden automatisch akzeptiert.
echo.

wsl bash -c "export PATH=$PATH:~/.local/bin && cd '%WSL_DIR%' && yes | buildozer android debug"

if exist "bin\*.apk" (
    echo.
    echo [ERFOLG] Die APK liegt im Ordner 'bin'!
) else (
    echo.
    echo [FEHLER] Bau fehlgeschlagen. Pruefe die Meldungen oben.
)
pause
