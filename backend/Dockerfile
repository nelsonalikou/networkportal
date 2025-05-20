FROM python:3.11-slim-buster

WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential curl && \
    rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry

# Tell Poetry to skip creating a virtualenv
ENV POETRY_VIRTUALENVS_CREATE=false

# Copy project metadata
COPY pyproject.toml poetry.lock ./

# Install dependencies globally in container
RUN poetry install --no-root --no-interaction --no-ansi

# Copy app code
COPY . .

# Expose app port
EXPOSE 8000
