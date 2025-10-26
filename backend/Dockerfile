FROM python:3.11-slim

WORKDIR /app

COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ .

RUN python manage.py collectstatic --noinput

# ← COPIA EL SCRIPT
COPY backend/start.sh /start.sh
RUN chmod +x /start.sh

# ← USA EL SCRIPT
CMD ["/start.sh"]