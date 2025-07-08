from autogen_core.models import UserMessage

from utils.ollama_client import get_ollama_client
from utils.logger import logger

import asyncio


async def main() -> None:
    logger.info("⚒️ Creating Ollama model client...")
    ollama_model_client = get_ollama_client()

    user_message = UserMessage(content="What is the capital of France?", source="user")

    logger.info("⚙️ Getting response from AI....")
    response = await ollama_model_client.create([user_message])
    logger.info(f"AI Response => {response.content}")

    await ollama_model_client.close()
    logger.info("🛑 Ollama model client closed")


if __name__ == "__main__":
    try:
        asyncio.run(main=main())
    except Exception as e:
        logger.error(f"❌ Error occurred: {e}")
