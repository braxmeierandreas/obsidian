@echo off
echo Starte Blog-Deployment...
powershell.exe -ExecutionPolicy Bypass -File "%~dp0deploy_blog.ps1"
pause
