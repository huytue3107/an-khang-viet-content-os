@echo off
setlocal

set "ROOT=%~dp0"
cd /d "%ROOT%"

python scripts\generate-all-visuals.py

pause
