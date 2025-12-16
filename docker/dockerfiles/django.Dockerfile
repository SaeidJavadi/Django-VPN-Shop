# Base Image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libjpeg-dev \
    zlib1g-dev \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set workdir
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY backend /app

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port for Gunicorn
EXPOSE 8000

# Command to run
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "vpnShop.wsgi:application", "--workers", "3"]
