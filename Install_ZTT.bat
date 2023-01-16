@echo off
Powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "& './Install_ZTT.ps1'"
rem PowerShell.exe -NoProfile -Command "& {Start-Process PowerShell.exe -ArgumentList '-NoProfile -ExecutionPolicy Bypass -File ""./Install_ZTT.ps1""' -Verb RunAs}"
TIMEOUT /T 10