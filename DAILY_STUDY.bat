@echo off
setlocal enabledelayedexpansion

set "SCRIPTS_DIR=%~dp000_SCRIPTS"
set "PYTHON_EXE=%~dp030_TECH_GOOGLE\.venv\Scripts\python.exe"

:MENU
cls
echo ========================================================
echo             DAILY STUDY SELECTOR
echo ========================================================
echo.
echo  [0]  ZUFAELLIG (Default)
echo  [1]  Public Health
echo  [2]  Health Promotion
echo  [3]  Artificial Intelligence
echo  [4]  Large Language Models
echo  [5]  Clinical Psychology
echo  [6]  Exercise Physiology
echo  [7]  Behavioral Economics
echo  [8]  Sleep Science
echo  [9]  Nutrition Science
echo  [10] Eigene Suche...
echo.
set "SELECTION=0"
set /p "SELECTION=Deine Wahl (0-10): "

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

REM Falls ungültige Eingabe
GOTO MENU

:CUSTOM_SEARCH
echo.
set /p "TOPIC=Gib dein Suchthema ein: "
if "%TOPIC%"=="" goto MENU
GOTO RUN_TOPIC

:RUN_RANDOM
echo.
echo [INFO] Starte Zufallsmodus...
"%PYTHON_EXE%" "%SCRIPTS_DIR%\routine_daily_study.py"
GOTO END

:RUN_TOPIC
echo.
echo [INFO] Suche nach Thema: "%TOPIC%"
"%PYTHON_EXE%" "%SCRIPTS_DIR%\routine_daily_study.py" "%TOPIC%"
GOTO END

:END
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Fehler beim Abrufen der Studie.
) else (
    echo.
    echo [SUCCESS] Vorgang abgeschlossen.
)

echo.
pause
endlocal