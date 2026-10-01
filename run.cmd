@echo off
REM Run the app with normal Python (fast, for developing). Opens the browser.
setlocal
call "%USERPROFILE%\miniforge3\Scripts\activate.bat" shinyapp
if errorlevel 1 exit /b 1
call "%~dp0sync_modules.cmd"
cd /d "%~dp0app"
shiny run --launch-browser app.py
endlocal
