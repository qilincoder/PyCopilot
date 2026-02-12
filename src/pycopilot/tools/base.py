#!/usr/bin/env python3
"""
Base class for all MCP tools
"""
from abc import ABC, abstractmethod
from typing import Any
from mcp.types import Tool, TextContent
from pydantic import BaseModel


class BaseTool(ABC):
    """
    Abstract base class for all tools.
    Each tool should inherit from this class and implement the required methods.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Return the name of the tool"""
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """Return the description of the tool"""
        pass

    @abstractmethod
    def get_input_schema(self) -> dict[str, Any]:
        """
        Return the JSON schema for the tool's input parameters.
        Should follow the format:
        {
            "type": "object",
            "properties": {...},
            "required": [...]
        }
        """
        pass

    @abstractmethod
    async def execute(self, arguments: dict) -> list[TextContent]:
        """
        Execute the tool with the given arguments.

        Args:
            arguments: Dictionary of input arguments

        Returns:
            List of TextContent objects containing the results
        """
        pass

    def to_tool(self) -> Tool:
        """
        Convert this tool to an MCP Tool object.
        This method is used by the server to list available tools.
        """
        return Tool(
            name=self.name,
            description=self.description,
            inputSchema=self.get_input_schema()
        )
