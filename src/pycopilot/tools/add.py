#!/usr/bin/env python3
"""
Add tool - Adds two numbers together
"""
from typing import Any
from mcp.types import TextContent
from pydantic import BaseModel
from .base import BaseTool


class AddInput(BaseModel):
    """Input schema for the add tool"""
    a: float
    b: float


class AddTool(BaseTool):
    """Tool for adding two numbers together"""

    @property
    def name(self) -> str:
        return "add"

    @property
    def description(self) -> str:
        return "Add two numbers together. Returns the sum of a and b."

    def get_input_schema(self) -> dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "a": {
                    "type": "number",
                    "description": "The first number"
                },
                "b": {
                    "type": "number",
                    "description": "The second number"
                }
            },
            "required": ["a", "b"]
        }

    async def execute(self, arguments: dict) -> list[TextContent]:
        """Execute the add operation"""
        # Validate input using pydantic model
        input_data = AddInput(**arguments)
        result = input_data.a + input_data.b

        return [
            TextContent(
                type="text",
                text=f"The sum of {input_data.a} and {input_data.b} is {result}"
            )
        ]
