@echo off

::dependency files for speech translator

:: pip install commands

::pip command for speechRecognisation
@echo " installing speechRecognisation package"
pip install SpeechRecognition
@echo " COMPLETED ...... "
::pip command for googleTrans package 
@echo " installing googleTrans package"
pip install googletrans==4.0.0-rc1
@echo " COMPLETED ...... "
::exit command

pause
