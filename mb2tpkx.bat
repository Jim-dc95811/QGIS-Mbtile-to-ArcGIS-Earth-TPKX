@echo off
setlocal
cd /d "%~dp0"
rem --- Find Python 3 (py launcher first, then python) ---
set "PYEXE=py -3"
where py >nul 2>nul || set "PYEXE=python"
%PYEXE% --version >nul 2>nul
if errorlevel 1 (
    echo Python 3 was not found. Install it from https://www.python.org/downloads/windows/
    echo using the default options, then run this again.
    pause
    exit /b 1
)
rem --- Pillow: install it once if it is missing ---
%PYEXE% -c "import PIL" >nul 2>nul
if errorlevel 1 (
    echo Pillow is not installed yet. Installing it now - one time only...
    echo.
    %PYEXE% -m pip install Pillow
    %PYEXE% -c "import PIL" >nul 2>nul
    if errorlevel 1 (
        echo.
        echo Pillow could not be installed automatically.
        echo Open Command Prompt and run:  py -3 -m pip install Pillow
        echo If your network blocks downloads, ask IT to install Pillow for Python 3.
        pause
        exit /b 1
    )
    echo.
    echo Pillow installed.
    echo.
)
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
%PYEXE% "%~dp0System Files\mb2tpkx.py" "%input%"
if errorlevel 1 (
    echo Conversion failed. Check the error above.
) else (
    echo Conversion complete.
)
pause
