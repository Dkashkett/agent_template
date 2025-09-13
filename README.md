## Setup Instructions

Follow these steps after cloning the repository:

```bash
# Sync dependencies exactly as specified in pyproject.toml and uv.lock
uv sync

# Install pre-commit hooks (Ruff runs automatically before commits)
pre-commit install
