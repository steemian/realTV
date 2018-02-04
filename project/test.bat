@echo off


set PY="D:\usr\bin\python3\python.exe"

:INFINITE
    cls
    %PY% -u test.py
    pause
    goto INFINITE
    