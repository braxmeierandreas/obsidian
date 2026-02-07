@echo off
setlocal enabledelayedexpansion

REM Get ESC character for colors
for /F "delims=#" %%a in ('"prompt #$E# & for %%b in (1) do rem"') do set "ESC=%%a"

set "RESET=%ESC%[0m"
set "BOLD=%ESC%[1m"
set "CYAN=%ESC%[36m"
set "GREEN=%ESC%[32m"
set "YELLOW=%ESC%[33m"
set "BLUE=%ESC%[34m"
set "MAGENTA=%ESC%[35m"
set "RED=%ESC%[31m"
set "WHITE=%ESC%[97m"

set "SCRIPTS_DIR=%~dp000_SCRIPTS"
set "PYTHON_EXE=%~dp030_TECH_GOOGLE\.venv\Scripts\python.exe"

:MENU
cls
echo %BOLD%%CYAN%
echo   **********************************************************
echo   *                                                        *
echo   *    [STUDY]  D A I L Y   A C A D E M I C   S T U D Y    *
echo   *                                                        *
echo   **********************************************************
echo %RESET%
echo %WHITE%   Datum: %BOLD%%YELLOW%%DATE%%RESET%
echo %BOLD%%BLUE%   ----------------------------------------------------------%RESET%
echo.
echo    %GREEN%[0]%RESET%  %BOLD%RANDOM TOPIC (Surprise Me)%RESET%
echo.
echo    %CYAN%[1]%RESET%  Public Health         %CYAN%[11]%RESET% Longevity
echo    %CYAN%[2]%RESET%  Health Promotion      %CYAN%[12]%RESET% Biohacking
echo    %CYAN%[3]%RESET%  Artificial Intelligence%CYAN%[13]%RESET% Neuroscience
echo    %CYAN%[4]%RESET%  LLMs                  %CYAN%[14]%RESET% Microbiome
echo    %CYAN%[5]%RESET%  Clinical Psychology   %CYAN%[15]%RESET% Intermittent Fasting
echo    %CYAN%[6]%RESET%  Exercise Physiology   %CYAN%[16]%RESET% Cybersecurity
echo    %CYAN%[7]%RESET%  Behavioral Economics  %CYAN%[17]%RESET% Software Engineering
echo    %CYAN%[8]%RESET%  Sleep Science         %CYAN%[18]%RESET% Blockchain/Health
echo    %CYAN%[9]%RESET%  Nutrition Science     %CYAN%[19]%RESET% Stress Management
echo    %CYAN%[10]%RESET% Mental Health         %CYAN%[20]%RESET% Yoga ^& Meditation
echo.
echo    %MAGENTA%[S]%RESET% %BOLD%CUSTOM SEARCH (Free Text)%RESET%
echo    %RED%[X]%RESET% Exit
echo.
echo %BOLD%%BLUE%   ----------------------------------------------------------%RESET%
set "SELECTION="
set /p "SELECTION=%BOLD%%YELLOW%   Select Option: %RESET%"

if /I "%SELECTION%"=="X" exit
if /I "%SELECTION%"=="S" goto CUSTOM_SEARCH
if "%SELECTION%"=="0" goto RUN_RANDOM
if "%SELECTION%"=="" goto RUN_RANDOM

set "TOPIC="
if "%SELECTION%"=="1" set "TOPIC=Public Health"
if "%SELECTION%"=="2" set "TOPIC=Health Promotion"
if "%SELECTION%"=="3" set "TOPIC=Artificial Intelligence"
if "%SELECTION%"=="4" set "TOPIC=Large Language Models"
if "%SELECTION%"=="5" set "TOPIC=Clinical Psychology"
if "%SELECTION%"=="6" set "TOPIC=Exercise Physiology"
if "%SELECTION%"=="7" set "TOPIC=Behavioral Economics"
if "%SELECTION%"=="8" set "TOPIC=Sleep Science"
if "%SELECTION%"=="9" set "TOPIC=Nutrition Science"
if "%SELECTION%"=="10" set "TOPIC=Mental Health"
if "%SELECTION%"=="11" set "TOPIC=Longevity"
if "%SELECTION%"=="12" set "TOPIC=Biohacking"
if "%SELECTION%"=="13" set "TOPIC=Neuroscience"
if "%SELECTION%"=="14" set "TOPIC=Microbiome"
if "%SELECTION%"=="15" set "TOPIC=Intermittent Fasting"
if "%SELECTION%"=="16" set "TOPIC=Cybersecurity"
if "%SELECTION%"=="17" set "TOPIC=Software Engineering"
if "%SELECTION%"=="18" set "TOPIC=Blockchain in Healthcare"
if "%SELECTION%"=="19" set "TOPIC=Stress Management"
if "%SELECTION%"=="20" set "TOPIC=Yoga & Meditation Science"

if defined TOPIC goto RUN_TOPIC

goto MENU

:CUSTOM_SEARCH
echo.
echo %BOLD%%MAGENTA%   --- CUSTOM SEARCH ---%RESET%
set /p "TOPIC=   Enter your topic: "
if "%TOPIC%"=="" goto MENU
goto RUN_TOPIC

:RUN_RANDOM
echo.
echo %BLUE%   [INFO] Starting random discovery...%RESET%
"%PYTHON_EXE%" "%SCRIPTS_DIR%\routine_daily_study.py"
goto END

:RUN_TOPIC
echo.
echo %BLUE%   [INFO] Researching topic: %BOLD%"%TOPIC%"%RESET%
"%PYTHON_EXE%" "%SCRIPTS_DIR%\routine_daily_study.py" "%TOPIC%"
goto END

:END
set "RET=%ERRORLEVEL%"
if %RET% neq 0 (
    echo.
    echo %RED%   [ERROR]   %RESET% %BOLD%Failed to fetch or summarize the study (Exit Code: %RET%).%RESET%
) else (
    echo.
    echo %GREEN%   [SUCCESS] %RESET% %BOLD%Study saved to 33_STUDIES and opened.%RESET%
)

echo.
echo %YELLOW%   Press any key to return to menu...%RESET%
pause > nul
goto MENU