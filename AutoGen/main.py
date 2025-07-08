from autogen_core.models import UserMessage
from autogen_core import EVENT_LOGGER_NAME

from utils.ollama_client import get_ollama_client

import asyncio
import logging


logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(EVENT_LOGGER_NAME)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


async def main() -> None:
    print("⚒️ Creating Ollama model client...")
    ollama_model_client = get_ollama_client()

    user_message = UserMessage(content="What is the capital of France?", source="user")

    print("⚙️ Getting response from AI....")
    response = await ollama_model_client.create([user_message])
    print(response)
    await ollama_model_client.close()
    print("🛑 Ollama model client closed")


if __name__ == "__main__":
    try:
        asyncio.run(main=main())
    except Exception as e:
        print(f"❌ Error occurred: {e}")
