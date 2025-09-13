from pydantic import BaseSettings


class Config(BaseSettings):
    openai_api_key: str
    agent_workflow_id: str

    class Config:
        env_file = ".env"
