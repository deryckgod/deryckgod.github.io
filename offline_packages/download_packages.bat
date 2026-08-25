@echo off
chcp 65001 > nul
title 離線 Python 套件包下載器

echo 正在檢查 Python 環境...
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [錯誤] 系統未安裝 Python，或未將其加入環境變數 PATH 中。
    echo 請安裝 Python 3.13 並勾選 "Add Python to PATH" 再次執行。
    pause
    exit /b 1
)

echo Python 環境正常，開始執行下載腳本...
python download_packages.py

echo.
echo 下載任務已結束。
pause
