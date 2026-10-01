@echo off
REM Run the app with normal Python and open it in the browser.
REM Double-click this file. Close the window (or press Ctrl+C) to stop the app.
setlocal
title Pakistan carbon tax app
call "%USERPROFILE%\miniforge3\Scripts\activate.bat" shinyapp
if errorlevel 1 goto failed
cd /d "%~dp0app"
echo.
echo The app opens in your browser at http://127.0.0.1:8000
echo Close this window to stop it.
echo.
shiny run --launch-browser --port 8000 app.py
if errorlevel 1 goto failed
endlocal
exit /b 0

:failed
echo.
echo The app did not start, see the messages above.
pause
endlocal
exit /b 1
