from agents import Agent, Runner

from app.config.openai import OpenAIConfig


class AgentService:
    def __init__(self, config: OpenAIConfig = None, agent: Agent = None):
        self.config = config
        self.agent = agent

    async def handle_message(self, message: str) -> str:
        result = await Runner.run(self.agent, message)
        return result.final_output


def get_agent_service() -> AgentService:
    return AgentService(
        config=OpenAIConfig(),
        agent=Agent(
            name="Comedian",
            instructions="You are a comedian. Make the user laugh with a joke or witty remark.",
        ),
    )
