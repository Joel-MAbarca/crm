# backend/start.sh
#!/bin/sh
set -e

python manage.py migrate
exec gunicorn crm.wsgi:application --bind 0.0.0.0:$PORT