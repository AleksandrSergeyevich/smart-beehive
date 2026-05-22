# Stage 1: Install dependencies
FROM python:3.11-slim AS builder

WORKDIR /app

RUN pip install --no-cache-dir poetry==1.7.1

COPY pyproject.toml ./

RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --only main 2>/dev/null || \
    pip install --no-cache-dir fastapi uvicorn pydantic influxdb-client asyncpg "sqlalchemy[asyncio]"

# Stage 2: Runtime image
FROM python:3.11-slim AS runtime

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev curl \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin/uvicorn /usr/local/bin/uvicorn

COPY src/ ./src/

RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]
