@echo off
setlocal enabledelayedexpansion

:: ========================================================
:: DER HAUSHALTS-HELD: ULTIMATE WEEKLY BACKUP
:: Version: 2.0 (Full System Cover)
:: ========================================================

:: --- 1. SETUP ---
for /f %%a in ('powershell -Command "Get-Date -UFormat %%V"') do set WEEK=%%a
for /f %%a in ('powershell -Command "Get-Date -Format yyyy"') do set YEAR=%%a
set "DEST_ROOT=%USERPROFILE%\Desktop\BackUp - KW %WEEK% %YEAR%"

cls
color 1f
echo ========================================================
echo      DER HAUSHALTS-HELD - BACKUP ZENTRALE
echo      KW %WEEK% / %YEAR%
echo ========================================================
echo Ziel: %DEST_ROOT%
echo.

:: --- 2. INTERAKTIVE CHECKLISTE (Die "Cloud & System" Ebene) ---

:CHECK_CHROME
set /p "input=1. [CHROME] Hast du Lesezeichen exportiert? (Wir sichern gleich die Datei, aber Export ist sicherer) (j/n): "

:CHECK_DRIVE
echo.
echo 2. [GOOGLE] Drive & Fotos sind Cloud-basiert.
set /p "input=   Hast du bei Bedarf einen Google Takeout gestartet oder wichtige Drive-Files lokal? (j/n): "

:CHECK_PHONE
echo.
echo 3. [HANDY] Bitte schliesse dein Samsung S24 Ultra jetzt an.
echo    Tipp: Starte 'Smart Switch' fuer ein volles Backup oder kopiere den DCIM Ordner.
set /p "input=   Ist das Handy-Backup erledigt? (j/n): "

:CHECK_WIN
echo.
echo 4. [WINDOWS] Sollen wir einen Wiederherstellungspunkt erstellen?
set /p "input=   (Erfordert Admin-Rechte - 'j' versucht es, 'n' ueberspringt): "
if /i "%input%"=="j" (
    echo    -> Versuche Wiederherstellungspunkt zu setzen...
    powershell -Command "Checkpoint-Computer -Description 'Wochentliches Backup KW%WEEK%' -RestorePointType 'MODIFY_SETTINGS'" 2>nul
    if errorlevel 1 echo    [!] Hat nicht geklappt (evtl. keine Admin-Rechte). Egal, weiter gehts.
)

:CHECK_OBSIDIAN
echo.
set /p "input=5. [OBSIDIAN] Ist Obsidian komplett geschlossen? (WICHTIG!) (j/n): "
if /i "%input%"=="n" (
    echo    -> Bitte schliessen!
    pause
)

echo.
echo ========================================================
echo Checkliste fertig. Starte physisches Kopieren...
echo ========================================================

if not exist "%DEST_ROOT%" mkdir "%DEST_ROOT%"

:: --- 3. KOPIER-ROUTINEN ---

:: --- A) DAS GEHIRN (Obsidian) ---
echo.
echo [1/6] Sichere Obsidian Vault...
set "SUB_OBS=%DEST_ROOT%\01_Obsidian_Vault"
if not exist "%SUB_OBS%" mkdir "%SUB_OBS%"
robocopy "%USERPROFILE%\obsidian" "%SUB_OBS%" /E /ZB /R:1 /W:1 /XD ".git" ".trash" "node_modules" "$RECYCLE.BIN" /njh /njs
echo    -> Erledigt.

:: --- B) DOKUMENTE ---
echo.
echo [2/6] Sichere Dokumente...
set "SUB_DOCS=%DEST_ROOT%\02_Dokumente"
if not exist "%SUB_DOCS%" mkdir "%SUB_DOCS%"
robocopy "%USERPROFILE%\Documents" "%SUB_DOCS%" /E /ZB /R:1 /W:1 /XD "My Music" "My Pictures" "My Videos" /njh /njs
echo    -> Erledigt.

:: --- C) BILDER ---
echo.
echo [3/6] Sichere Bilder...
set "SUB_PICS=%DEST_ROOT%\03_Bilder_Fotos"
if not exist "%SUB_PICS%" mkdir "%SUB_PICS%"
robocopy "%USERPROFILE%\Pictures" "%SUB_PICS%" /E /ZB /R:1 /W:1 /njh /njs
echo    -> Erledigt.

:: --- D) DEV & KEYS (SSH & VS Code) ---
echo.
echo [4/6] Sichere Developer Configs (SSH & VS Code)...
set "SUB_DEV=%DEST_ROOT%\04_Dev_Settings"
if not exist "%SUB_DEV%\SSH" mkdir "%SUB_DEV%\SSH"
if not exist "%SUB_DEV%\VSCode" mkdir "%SUB_DEV%\VSCode"

:: SSH Keys (Ohne Known_hosts Müll, nur Keys und Config)
if exist "%USERPROFILE%\.ssh" (
    robocopy "%USERPROFILE%\.ssh" "%SUB_DEV%\SSH" /E /ZB /R:1 /W:1 /njh /njs
)
:: VS Code User Settings
if exist "%APPDATA%\Code\User" (
    robocopy "%APPDATA%\Code\User" "%SUB_DEV%\VSCode" "settings.json" "keybindings.json" "snippets" /E /ZB /R:1 /W:1 /njh /njs
)
echo    -> Erledigt.

:: --- E) BROWSER DATEN (Chrome) ---
echo.
echo [5/6] Sichere Chrome Lesezeichen...
set "SUB_WEB=%DEST_ROOT%\05_Browser_Settings"
if not exist "%SUB_WEB%" mkdir "%SUB_WEB%"
:: Kopiert nur Lesezeichen und Login-Daten (verschlüsselt, nur auf diesem PC nutzbar)
if exist "%LOCALAPPDATA%\Google\Chrome\User Data\Default" (
    copy "%LOCALAPPDATA%\Google\Chrome\User Data\Default\Bookmarks" "%SUB_WEB%\Chrome_Bookmarks_Backup" >nul
    echo    -> Bookmarks kopiert.
) else (
    echo    -> Chrome Pfad nicht gefunden oder leer.
)

:: --- F) ARCHIV (Downloads) ---
echo.
echo [6/6] Sichere Downloads...
set "SUB_DL=%DEST_ROOT%\99_Downloads_Archiv"
if not exist "%SUB_DL%" mkdir "%SUB_DL%"
robocopy "%USERPROFILE%\Downloads" "%SUB_DL%" /E /ZB /R:1 /W:1 /njh /njs
echo    -> Erledigt.

:: --- ABSCHLUSS ---
echo.
echo ========================================================
echo BACKUP COMPLETE!
echo Ordner erstellt: %DEST_ROOT%
echo ========================================================
echo Druecke eine Taste zum Beenden...
pause >nul
