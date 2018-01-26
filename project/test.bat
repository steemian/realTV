@echo off


:INFINITE
    cls
    python test.py > test.log
    pause
    goto INFINITE
    