FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install poetry
RUN pip install poetry

# Copy project files
COPY pyproject.toml poetry.lock* README.md ./

# Configure poetry to not create a virtual environment inside the container
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --no-interaction --no-ansi --only main

# Copy application code
COPY app/ ./app/

# Expose Public, Parcel Internal, and Party Internal ports
EXPOSE 8080 8081 8082

# Healthcheck for all three apps
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080/health && \
        curl -f http://localhost:8081/health && \
        curl -f http://localhost:8082/health || exit 1

# Command to run the application (runs both servers concurrently via app/main.py)
CMD ["python", "-m", "app.main"]