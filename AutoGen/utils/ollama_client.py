from configs.settings import DEFAULT_OLLAMA_MODEL

from autogen_ext.models.ollama import OllamaChatCompletionClient

from dotenv import load_dotenv
import os


def get_ollama_client(model_name=DEFAULT_OLLAMA_MODEL) -> OllamaChatCompletionClient:
    load_dotenv()
    host_url = os.getenv("OLLAMA_URL")

    if host_url is None:
        raise Exception("Please set up ollama url environment variable!")

    ollama_client = OllamaChatCompletionClient(model=model_name, host=host_url)
    return ollama_client
