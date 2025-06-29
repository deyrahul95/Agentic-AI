from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="Weather")


@mcp.tool()
async def get_weather(location:str) -> str:
    """
    Use this tool to get the weather information for specific location

    Args:
        location: location string

    Returns:
        str: the current weather for this location
    """
    return f"Hey, {location} is cloudy all day. It may rain today also."

if __name__ == "__main__":
    mcp.run(transport="streamable-http")