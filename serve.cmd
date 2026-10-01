@echo off
REM Serve the exported site\ on http://localhost:8008/ (Ctrl+C to stop).
setlocal
call "%USERPROFILE%\miniforge3\Scripts\activate.bat" shinyapp
if errorlevel 1 exit /b 1
python "%~dp0serve.py"
endlocal
