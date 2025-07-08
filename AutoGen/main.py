from autogen_agentchat.ui import Console

from agents.search_assistant import search_assistant_agent
from utils.logger import logger

import asyncio


async def main() -> None:
    agent = search_assistant_agent()

    stream = agent.run_stream(task="Find information on AutoGen")
    await Console(stream)


if __name__ == "__main__":
    try:
        asyncio.run(main=main())
    except Exception as e:
        logger.error(f"❌ Error occurred: {e}")
