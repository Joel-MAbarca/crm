FROM python:3.11-slim

WORKDIR /app

COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ .

RUN python manage.py collectstatic --noinput

CMD ["/bin/sh", "-c", "python manage.py migrate && gunicorn crm.wsgi:application --bind 0.0.0.0:${PORT:-8000}"]

