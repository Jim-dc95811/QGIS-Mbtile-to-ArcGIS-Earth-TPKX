@echo off
setlocal
cd /d "%~dp0"
title mb2tpkx 2.0 - MBTiles to TPKX
echo Starting Ready to Fly - on an older PC this first step can take a few minutes, please wait...
echo (Windows Defender may check the files first and slow the PC. That is normal - do not close this window.)
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0System Files\Ready_To_Fly.ps1" -Folder "%~dp0System Files" -Tool "mb2tpkx" -Packages "Pillow" -Imports "PIL"
if errorlevel 1 goto rtf_stopped
set "PYEXE="
set /p PYEXE=<"%~dp0System Files\python_path.txt"
if not defined PYEXE goto rtf_stopped
if "%~1"=="" (
    set /p "input=Enter the full path to your MBTiles file: "
) else (
    set "input=%~1"
)
set "input=%input:"=%"
if not exist "%input%" (
    echo MBTiles file not found: "%input%"
    pause
    exit /b 1
)
"%PYEXE%" "%~dp0System Files\mb2tpkx.py" "%input%"
if errorlevel 1 (
    echo Conversion failed. Check the error above.
) else (
    echo Conversion complete.
)
pause
exit /b 0

:rtf_stopped
echo.
echo mb2tpkx did not start - read the message above.
echo A log is in System Files\Ready_To_Fly_log.txt
pause
exit /b 1
