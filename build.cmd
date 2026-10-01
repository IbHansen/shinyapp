@echo off
REM Export the app as a static Shinylive site into site\ (the same as the GitHub action).
setlocal
call "%USERPROFILE%\miniforge3\Scripts\activate.bat" shinyapp
if errorlevel 1 exit /b 1
call "%~dp0sync_modules.cmd"
cd /d "%~dp0"
shinylive export app site
endlocal
