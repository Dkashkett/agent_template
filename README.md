## Setup Instructions

Follow these steps after cloning the repository:

```bash
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
