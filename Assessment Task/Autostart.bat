@echo off
db_create.sql postgres
echo Once the PostgrSQL server is running, press any key to continue
pause >nul
cls
echo Following this next step, make your way back to the folder containing this batch file and run the batch file titled 'migrate.bat'
pause >nul
python manage.py runserver
pause