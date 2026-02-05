@echo off
title OpenClaw Update
echo ========================================================
echo   UPDATE: OpenClaw AI Agent
echo ========================================================
echo.
echo Aktualisiere OpenClaw auf die neueste Version...
echo.
call npm update -g openclaw
echo.
echo Checke Status...
call openclaw --version
echo.
pause
