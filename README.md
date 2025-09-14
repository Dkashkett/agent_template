## Setup Instructions

Follow these steps after cloning the repository:

```bash
# Create and activate a new virtual environment
python -m venv .venv
source .venv/bin/activate

# Sync dependencies exactly as specified in pyproject.toml and uv.lock
uv sync

# Install pre-commit hooks (Ruff runs automatically before commits)
pre-commit install
```

Docker

```bash
docker build -t agent-template .

docker run --env-file .env.local -p 8000:8000 agent-template

# Optional:
docker run -p 8000:8000 -v $(pwd):/app agent-template
```
