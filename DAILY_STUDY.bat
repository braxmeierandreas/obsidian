@echo off
setlocal enabledelayedexpansion

REM ANSI Color Codes
set "ESC="
set "RESET=%ESC%[0m"
set "BOLD=%ESC%[1m"
set "CYAN=%ESC%[36m"
set "GREEN=%ESC%[32m"
set "YELLOW=%ESC%[33m"
set "BLUE=%ESC%[34m"
set "MAGENTA=%ESC%[35m"

set "SCRIPTS_DIR=%~dp000_SCRIPTS"
set "PYTHON_EXE=%~dp030_TECH_GOOGLE\.venv\Scripts\python.exe"

:MENU
cls
echo %BOLD%%CYAN%
echo   ____   _    ___ _  __   __  ____ _____ _   _ ______   __
echo  ^|  _ \ / \  ^|_ _^| ^| \ \ / / / ___^|_   _^| ^| ^| ^|  _ \ \ / /
echo  ^| ^| ^| / _ \  ^| ^| ^| ^|  \ V /  \___ \ ^| ^| ^| ^| ^| ^| ^| ^| \ V / 
echo  ^| ^|_^| / ___ \ ^| ^| ^| ^|___^| ^|    ___) ^| ^| ^| ^| ^|_^| ^| ^|_^| ^| ^| ^|  
echo  ^|____/_/   \_\___^|_____^|_^|   ^|____/  ^|_^|  \___/^|____/  ^|_^|  
echo %RESET%
echo %BOLD%%YELLOW%  ========================================================%RESET%
echo %BOLD%               WISSENSCHAFTS-DASHBOARD v2.0%RESET%
echo %BOLD%%YELLOW%  ========================================================%RESET%
echo.
echo  %GREEN%[0]%RESET%  %BOLD%ZUFAELLIG (Überraschung!)%RESET%
echo  %CYAN%[1]%RESET%  Public Health
echo  %CYAN%[2]%RESET%  Health Promotion
echo  %CYAN%[3]%RESET%  Artificial Intelligence
echo  %CYAN%[4]%RESET%  Large Language Models
echo  %CYAN%[5]%RESET%  Clinical Psychology
echo  %CYAN%[6]%RESET%  Exercise Physiology
echo  %CYAN%[7]%RESET%  Behavioral Economics
echo  %CYAN%[8]%RESET%  Sleep Science
echo  %CYAN%[9]%RESET%  Nutrition Science
echo  %MAGENTA%[10]%RESET% %BOLD%Eigene Suche...%RESET%
echo.
set "SELECTION=0"
set /p "SELECTION=%BOLD%%YELLOW%Deine Wahl (0-10): %RESET%"

IF "%SELECTION%"=="0" GOTO RUN_RANDOM
IF "%SELECTION%"=="" GOTO RUN_RANDOM
IF "%SELECTION%"=="1" SET "TOPIC=Public Health" & GOTO RUN_TOPIC
IF "%SELECTION%"=="2" SET "TOPIC=Health Promotion" & GOTO RUN_TOPIC
IF "%SELECTION%"=="3" SET "TOPIC=Artificial Intelligence" & GOTO RUN_TOPIC
IF "%SELECTION%"=="4" SET "TOPIC=Large Language Models" & GOTO RUN_TOPIC
IF "%SELECTION%"=="5" SET "TOPIC=Clinical Psychology" & GOTO RUN_TOPIC
IF "%SELECTION%"=="6" SET "TOPIC=Exercise Physiology" & GOTO RUN_TOPIC
IF "%SELECTION%"=="7" SET "TOPIC=Behavioral Economics" & GOTO RUN_TOPIC
IF "%SELECTION%"=="8" SET "TOPIC=Sleep Science" & GOTO RUN_TOPIC
IF "%SELECTION%"=="9" SET "TOPIC=Nutrition Science" & GOTO RUN_TOPIC
IF "%SELECTION%"=="10" GOTO CUSTOM_SEARCH

GOTO MENU

:CUSTOM_SEARCH
echo.
echo %BOLD%%MAGENTA%--- MANUELLE SUCHE ---%RESET%
set /p "TOPIC=Gib dein Suchthema ein: "
if "%TOPIC%"=="" goto MENU
GOTO RUN_TOPIC

:RUN_RANDOM
echo.
echo %BLUE%[INFO] Starte Zufallsmodus...%RESET%
"%PYTHON_EXE%" "%SCRIPTS_DIR%\routine_daily_study.py"
GOTO END

:RUN_TOPIC
echo.
echo %BLUE%[INFO] Suche nach Thema: %BOLD%"%TOPIC%"%RESET%
"%PYTHON_EXE%" "%SCRIPTS_DIR%\routine_daily_study.py" "%TOPIC%"
GOTO END

:END
if %errorlevel% neq 0 (
    echo.
    echo %ESC%[41m[ERROR]%RESET% %BOLD%Fehler beim Abrufen der Studie.%RESET%
) else (
    echo.
    echo %ESC%[42m[SUCCESS]%RESET% %BOLD%Vorgang abgeschlossen. Datei in Obsidian gespeichert.%RESET%
)

echo.
echo %YELLOW%Druecke eine Taste, um zurück zum Menü zu gelangen...%RESET%
pause > nul
GOTO MENU