@echo off
REM Until modelflowib 2.84 is on PyPI, the browser app needs the two new modules
REM next to app.py. Copies them from the local repo. When 2.84 is released, delete
REM app\modelwidget_core.py and app\modelinput_shiny.py and stop calling this.
copy /y C:\modelflow2\modelflow\modelwidget_core.py "%~dp0app\" >nul
copy /y C:\modelflow2\modelflow\modelinput_shiny.py "%~dp0app\" >nul
