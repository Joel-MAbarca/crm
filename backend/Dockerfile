# backend/Dockerfile
FROM python:3.10-slim

WORKDIR /app/backend

COPY requirements.txt /app/backend/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/backend/

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && gunicorn crm.wsgi:application --bind 0.0.0.0:$PORT"]