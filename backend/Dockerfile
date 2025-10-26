FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ .

RUN python manage.py collectstatic --noinput

COPY backend/start.sh /start.sh

RUN apt-get update && apt-get install -y dos2unix && \
    dos2unix /start.sh

RUN chmod +x /start.sh

# USA EL SCRIPT
CMD ["/start.sh"]
