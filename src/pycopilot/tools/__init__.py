#!/usr/bin/env python3
"""
Tools package - Manages all available MCP tools

To add a new tool:
1. Create a new file in this package (e.g., my_tool.py)
2. Implement a class that inherits from BaseTool
3. Add the class to the TOOL_CLASSES list below
"""
from typing import Optional
from .base import BaseTool
from .add import AddTool
from .multiply import MultiplyTool

# Registry of all available tool classes
# Add new tool classes here when implementing new tools
TOOL_CLASSES = [
    AddTool,
    MultiplyTool
]


def get_all_tools() -> list[BaseTool]:
    """
    Get instances of all registered tools.

    Returns:
        List of BaseTool instances for all available tools
    """
    return [tool_class() for tool_class in TOOL_CLASSES]


def get_tool_by_name(name: str) -> Optional[BaseTool]:
    """
    Get a tool instance by its name.

    Args:
        name: The name of the tool to retrieve

    Returns:
        BaseTool instance if found, None otherwise
    """
    tools = get_all_tools()
    for tool in tools:
        if tool.name == name:
            return tool
    return None


# Export public API
__all__ = [
    "BaseTool",
    "AddTool",
    "get_all_tools",
    "get_tool_by_name",
    "TOOL_CLASSES",
]
