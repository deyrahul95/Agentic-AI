from utils.logger import logger


def web_search_tool(query: str) -> str:
    """Find information on the web"""
    logger.info(f"Query => {query}")
    return "AutoGen is a programming framework for building multi-agent applications."
