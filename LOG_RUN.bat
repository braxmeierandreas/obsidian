@echo off
chcp 65001 > nul
cls
color 0B

echo.
echo  =============================================================
echo         TRACK YOUR PROGRESS - BECOME A LEGEND
echo  =============================================================
echo.
echo  Run Logger v1.0
echo.

set /p dist="Runner Distance (km)   : "
set /p time="Time (mm:ss)           : "
set /p hr="Avg Heart Rate         : "
set /p spm="Cadence (SPM)          : "
set /p note="Note (Optional)        : "

if "%note%"=="" set note="-"

echo.
echo  Processing run data...
echo.

python "C:\Users\braxm\obsidian\00_SCRIPTS\FIT\log_run.py" %dist% %time% %hr% %spm% %note%

pause