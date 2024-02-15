@echo off

:: Travar windows

set contador=0
:start

set /a contador=%contador%+1
start chrome.exe
if %contador% lss 100 goto start


set /a contador=%contador%+1
start "" "C:\Program Files\Autodesk\AutoCAD 2024\acad.exe"
if %contador% lss 130 goto start

echo HEHE
start chrome.exe

start winword.exe

start calc


echo de novo
taskmgr

exit