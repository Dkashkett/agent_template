from app.config import Config
from openai import OpenAI

config = Config()
client = OpenAI(api_key=config.openai_api_key)


def process_user_message(message: str) -> str:
    """
    Calls the OpenAI Agent workflow and returns the response.
    """
    response = client.agents.run(
        agent_id=config.agent_workflow_id, input={"user_message": message}
    )
    return response.output_text if hasattr(response, "output_text") else str(response)
