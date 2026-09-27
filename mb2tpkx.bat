@echo off
setlocal
cd /d "%~dp0"
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
py -3 "%~dp0mb2tpkx.py" "%input%"
if errorlevel 1 (
    echo Conversion failed. Check the error above.
) else (
    echo Conversion complete.
)
pause
