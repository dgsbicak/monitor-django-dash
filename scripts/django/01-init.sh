#!/bin/bash


#python manage.py makemigrations
python manage.py migrate
python manage.py wait_db --nsleep 2
python manage.py collectstatic --no-input
#python manage.py test -v2
#gunicorn system_monitor.wsgi -b 0.0.0.0:8000 -w $(nproc)
python manage.py runserver 0.0.0.0:8000