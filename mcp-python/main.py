"""
FastMCP quickstart example.

cd to the `examples/snippets/clients` directory and run:
    uv run server fastmcp_quickstart stdio
"""

from mcp.server.fastmcp import FastMCP
from sqliteDB import DBAccess

# Create an MCP server
mcp = FastMCP("Demo")

dbAccess = DBAccess("mwreqservices_default.db")

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def count_reqsets() -> int:
    """Count the number reqset in the database"""
    return dbAccess.count_reqsets()

@mcp.tool()
def list_reqsets() -> list:
    """List all reqsets in the database"""
    return dbAccess.list_reqsets()

@mcp.tool()
def count_linkset() -> int:
    """Count the number of link sets in the database"""
    return dbAccess.count_linkset()

@mcp.tool()
def list_linkset() -> list:
    """List all link sets in the database"""
    return dbAccess.list_linkset()

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    print(name)
    return f"Hello, {name}!"


# Add a prompt
@mcp.prompt()
def greet_user(name: str, style: str = "friendly") -> str:
    """Generate a greeting prompt"""
    styles = {
        "friendly": "Please write a warm, friendly greeting",
        "formal": "Please write a formal, professional greeting",
        "casual": "Please write a casual, relaxed greeting",
    }

    return f"{styles.get(style, styles['friendly'])} for someone named {name}."

if __name__ == "__main__":
    mcp.run(transport="sse")