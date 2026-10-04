@echo off
cd /d "%~dp0"
py -3 Master4_Grid_Maker.py
if errorlevel 1 echo.
echo.
echo Press any key to close...
pause >nul
