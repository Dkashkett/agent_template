FROM python:3.13-slim

COPY . /app

WORKDIR /app

#RUN apt-get update && apt-get install -y --no-install-recommends \
#    curl \
# && rm -rf /var/lib/apt/lists/*

RUN pip install uv

RUN uv sync --frozen --no-cache
#RUN uv venv .venv \
#    && .venv/bin/uv pip install --upgrade pip \
#    && .venv/bin/pip install uv \
#    && .venv/bin/uv sync --frozen --no-cache

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

RUN useradd -m appuser
USER appuser

EXPOSE 8000

CMD ["uv", "run", "app/main.py", "--port", "80", "--host", "0.0.0.0"]