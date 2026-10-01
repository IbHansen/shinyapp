@echo off
REM Create the conda env "shinyapp": Shiny, Shinylive and ModelFlow installed
REM editable from the local repo C:\modelflow2\modelflow. Run once.
setlocal
call "%USERPROFILE%\miniforge3\Scripts\activate.bat" base
if errorlevel 1 exit /b 1
call conda create -y -n shinyapp python=3.12 pip
if errorlevel 1 exit /b 1
call conda activate shinyapp
python -m pip install -r "%~dp0requirements.txt"
if errorlevel 1 exit /b 1
python -m pip install -e C:\modelflow2\modelflow
endlocal
