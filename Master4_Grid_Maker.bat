@echo off
setlocal
cd /d "%~dp0"
title Master 4 Grid Maker 2.0
echo Starting Ready to Fly - on an older PC this first step can take a few minutes, please wait...
echo (Windows Defender may check the files first and slow the PC. That is normal - do not close this window.)
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0System Files\Ready_To_Fly.ps1" -Folder "%~dp0System Files" -Tool "Master 4 Grid Maker" -Packages "Pillow" -Imports "PIL"
if errorlevel 1 goto rtf_stopped
set "PYEXE="
set /p PYEXE=<"%~dp0System Files\python_path.txt"
if not defined PYEXE goto rtf_stopped
"%PYEXE%" "System Files\Master4_Grid_Maker.py"
if errorlevel 1 echo.
echo.
echo Press any key to close...
pause >nul
exit /b 0

:rtf_stopped
echo.
echo Master 4 Grid Maker did not start - read the message above.
echo A log is in System Files\Ready_To_Fly_log.txt
pause
exit /b 1
