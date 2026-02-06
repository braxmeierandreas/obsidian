@echo off
title OpenClaw Agent Installation
echo ========================================================
echo   INSTALLATION: OpenClaw AI Agent (Global)
echo ========================================================
echo.
echo Pruefe Node.js Version...
node -v
echo.
echo Installiere OpenClaw via npm...
echo.
call npm install -g openclaw@latest
echo.
echo ========================================================
echo   Installation abgeschlossen.
echo   Bitte jetzt '01_START_WIZARD.bat' ausfuehren.
echo ========================================================
pause
