@echo off
title MAESTER CONTROL SYSTEM
color 0A

echo ====================================================
echo   LAUNCHING EDUWERKS DUAL-CORE SYSTEM
echo ====================================================
echo.

:: 1. Launch Code Architect (Port 8501)
echo [1/2] Initializing Code Architect (Port 8501)...
start "Architect Bot" cmd /k "python -m streamlit run ml_bot.py --server.port 8501 --server.enableCORS false --server.enableXsrfProtection false --server.address localhost --browser.gatherUsageStats false"

:: 2. Launch Study Scribe (Port 8502)
echo [2/2] Initializing Study Scribe (Port 8502)...
start "Scribe Bot" cmd /k "python -m streamlit run study_bot.py --server.port 8502 --server.enableCORS false --server.enableXsrfProtection false --server.address localhost --browser.gatherUsageStats false"

echo.
echo ====================================================
echo   SYSTEMS ONLINE. 
echo   DO NOT CLOSE THE BLACK WINDOWS.
echo ====================================================
pause