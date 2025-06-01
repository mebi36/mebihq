FROM node:16 as frontend

RUN npm install -g npm@8.19.2

WORKDIR /frontend

# Install frontend dependencies
COPY frontend/package*.json ./
RUN npm install

# Copy Vue source files and build
COPY frontend/ ./
RUN npm run build


FROM python:3.8-slim


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy the backend subdir into app/backend
COPY backend /app/backend

# Set working directory to where manage.py is
WORKDIR /app/backend

RUN python manage.py makemigrations
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000"]