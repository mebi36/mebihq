# Dockerfile
FROM node:16 AS frontend-builder

RUN npm install -g npm@8.19.4

WORKDIR /app/frontend

COPY frontend/package*.json ./
RUN npm install

COPY frontend/ ./
RUN npm run build


FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libpq-dev curl \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY backend /app/backend
COPY --from=frontend-builder /app/frontend/dist /app/backend/static/vue/dist

WORKDIR /app/backend

RUN python manage.py collectstatic --noinput

CMD python manage.py migrate --noinput && \
    gunicorn backend.wsgi:application --bind 0.0.0.0:8000
    # python manage.py runserver 0.0.0.0:8000
