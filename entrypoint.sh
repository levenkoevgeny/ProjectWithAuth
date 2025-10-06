#!/bin/bash

echo "Collect static files"
python manage.py collectstatic --noinput

echo "Apply database migrations"
python manage.py migrate --settings=ProjectWithAuth.settings

echo "Starting server"
gunicorn --bind 0.0.0.0:8000 --workers 3 ProjectWithAuth.wsgi:application
