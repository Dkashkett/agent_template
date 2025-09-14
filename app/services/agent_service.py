from agents import Agent, Runner

from app.config.openai import OpenAIConfig

config = OpenAIConfig()

comedian_agent = Agent(
    name="Comedian",
    instructions="You are a comedian. Make the user laugh with a joke or witty remark.",
)


async def process_user_message(message: str) -> str:
    """
    Calls the OpenAI Agent workflow and returns the response.
    """
    result = await Runner.run(comedian_agent, message)

    return result.final_output
