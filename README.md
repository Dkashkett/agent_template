## Setup Instructions

Follow these steps after cloning the repository:

First, ensure you have `uv` installed. https://docs.astral.sh/uv/getting-started/installation/

Next, run the following commands:

```bash
# Create and activate a new virtual environment with uv
uv venv .venv
source .venv/bin/activate
pip install uv

# Sync dependencies exactly as specified in pyproject.toml and uv.lock
uv sync --all-extras

# Install pre-commit hooks (Ruff runs automatically before commits)
pre-commit install
```

Docker (Optional)

```bash
docker build -t agent-template .

docker run --env-file .env.local -p 8000:8000 agent-template

# Optional:
docker run -p 8000:8000 -v $(pwd):/app agent-template
```
