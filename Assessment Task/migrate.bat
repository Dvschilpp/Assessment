@echo off
python manage.py migrate
cls
python manage.py syncdb
start http://127.0.0.1:8000