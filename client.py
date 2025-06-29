from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain.chat_models import init_chat_model
from langchain_core.language_models import BaseChatModel

from dotenv import load_dotenv

import os
import asyncio

load_dotenv()


def get_ollama_model() -> BaseChatModel:
    """
    Create an instance of local ollama model

    Returns:
        An instance of 'BaseChatModel'
    """
    base_url: str = str(os.getenv("OLLAMA_URL"))

    model = init_chat_model("llama3.2", model_provider="ollama", base_url=base_url)
    return model


def create_user_query(query: str) -> dict:
    """
    Create user query with required format

    Returns:
        An dict with formatted user message
    """
    return {"messages": [{"role": "user", "content": query}]}


def get_response_content(response: dict) -> str:
    """
    Print response last message content

    Returns:
        The last message content in string
    """
    return response["messages"][-1].content


async def main():
    client = MultiServerMCPClient(
        connections={
            "math": {
                "command": "python",
                "args": ["math_server.py"],  ## Ensure correct absolute path is given
                "transport": "stdio",
            },
            "weather": {
                "url": "http://localhost:8000/mcp",  ## Ensure server is running here
                "transport": "streamable_http",
            },
        }  # type: ignore
    )

    tools = await client.get_tools()
    model = get_ollama_model()
    agent = create_react_agent(model=model, tools=tools)

    math_response = await agent.ainvoke(create_user_query("what's (3 + 5) * 12?"))
    print("Math response: ", get_response_content(math_response))

    weather_response = await agent.ainvoke(create_user_query("what is the weather in Kolkata?"))
    print("Weather response: ", get_response_content(weather_response))

asyncio.run(main())
