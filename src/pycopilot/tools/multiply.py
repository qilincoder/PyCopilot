#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025-12-19 17:24
# @Author  : Jack
# @File    : multiply.py

"""
multiply
"""
from typing import Any
from mcp.types import TextContent
from pydantic import BaseModel
from .base import BaseTool


class MultiplyInput(BaseModel):
    """Input schema for the multiply tool"""
    a: float
    b: float


class MultiplyTool(BaseTool):
    """Tool for multiplying two numbers"""

    @property
    def name(self) -> str:
        return "multiply"

    @property
    def description(self) -> str:
        return "Multiply two numbers together."

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
        """Execute the multiply operation"""
        input_data = MultiplyInput(**arguments)
        result = input_data.a * input_data.b

        return [
            TextContent(
                type="text",
                text=f"{input_data.a} × {input_data.b} = {result}"
            )
        ]