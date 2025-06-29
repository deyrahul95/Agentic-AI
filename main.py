from langchain.chat_models import init_chat_model
from langchain_core.language_models import BaseChatModel

from dotenv import load_dotenv

import os

load_dotenv()


def get_ollama_model() -> BaseChatModel:
    """
    Create an instance of local ollama model

    Returns:
        An instance of 'BaseChatModel'
    """
    base_url: str = str(os.getenv("OLLAMA_URL"))

    model = init_chat_model("llama3.2:1b", model_provider="ollama", base_url=base_url)
    return model


def main():
    model = get_ollama_model()

    while True:
        query: str = input("Please enter your query (or '/bye' to end this chat) => ")

        if query.lower() == "/bye":
            return

        response = model.invoke([{"role": "user", "content": query}])
        print(response.text())


if __name__ == "__main__":
    main()
