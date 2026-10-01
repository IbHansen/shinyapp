@echo off
REM Run the test app (sumslide, sheet, viewer options) with normal Python.
REM It uses the modules from the repo (editable install), not the copies in app\.
setlocal
call "%USERPROFILE%\miniforge3\Scripts\activate.bat" shinyapp
if errorlevel 1 exit /b 1
cd /d "%~dp0test_app"
shiny run --launch-browser --port 8001 app.py
endlocal
