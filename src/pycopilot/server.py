#!/usr/bin/env python3
"""
PyCopilot MCP Server - Main server implementation
"""
import asyncio
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent
from .tools import get_all_tools, get_tool_by_name


# Create MCP server instance
app = Server("pycopilot")


@app.list_tools()
async def list_tools() -> list[Tool]:
    """
    List available tools.
    Tools are automatically loaded from the tools package.
    """
    tools = get_all_tools()
    return [tool.to_tool() for tool in tools]


@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """
    Handle tool calls.
    Automatically routes to the appropriate tool based on name.
    """
    tool = get_tool_by_name(name)
    if tool is None:
        raise ValueError(f"Unknown tool: {name}")

    return await tool.execute(arguments)


async def main():
    """Main entry point for the MCP server"""
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )


def run():
    """Synchronous entry point for command-line script"""
    asyncio.run(main())
