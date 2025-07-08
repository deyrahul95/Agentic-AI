from agents.search_assistant import search_assistant_agent
from utils.logger import logger

import asyncio


async def main() -> None:
    agent = search_assistant_agent()

    result = await agent.run(task="Find information on AutoGen")
    print(result.messages)


if __name__ == "__main__":
    try:
        asyncio.run(main=main())
    except Exception as e:
        logger.error(f"❌ Error occurred: {e}")
