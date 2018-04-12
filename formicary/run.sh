#!/bin/sh
pip install -r requirements.txt

python manage.py migrate
python manage.py collectstatic -v0 --noinput
python manage.py runserver 0.0.0.0:8080