from autogen_agentchat.agents import AssistantAgent

from utils.ollama_client import get_ollama_client
from tools.web_search import web_search_tool


def search_assistant_agent() -> AssistantAgent:
    ollama_client = get_ollama_client()

    agent = AssistantAgent(
        name="assistant",
        model_client=ollama_client,
        tools=[web_search_tool],
        system_message="Use tools to solve tasks.",
    )

    return agent
