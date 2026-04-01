# Use official slim Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Prevent Python from writing .pyc files & enable stdout logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies (needed for some Python packages)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project code
COPY api/ api/
COPY config/ config/
COPY db/ db/

# Set default Railway PORT (Railway injects PORT automatically)
ENV PORT=8000
EXPOSE 8000

# Production-ready command using Gunicorn + Uvicorn workers
# CMD ["sh", "-c", "gunicorn api.app:app -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT"]
CMD ["gunicorn", "api.app:app", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:$PORT", "--workers", "1", "--timeout", "120"]