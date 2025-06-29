from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="Math")


@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Use this tool to add two integer number

    Args:
        a: first integer number
        b: second integer number

    Returns:
        integer number: the addition result of this two input integer numbers
    """
    return a + b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """
    Use this tool to multiply two integer number

    Args:
        a: first integer number
        b: second integer number

    Returns:
        integer number: the multiplication result of this two input integer numbers
    """
    return a * b


if __name__ == "__main__":
    mcp.run(transport="stdio")
