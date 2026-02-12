# Tools Package

This package contains all MCP tools for PyCopilot. The architecture is designed for easy extensibility.

## Architecture

- **`base.py`**: Defines `BaseTool` abstract base class that all tools must inherit from
- **`__init__.py`**: Tool registry that manages all available tools
- **Individual tool files**: Each tool is implemented in its own file (e.g., `add.py`)

## Adding a New Tool

To add a new tool to PyCopilot, follow these steps:

### 1. Create a new tool file

Create a new Python file in the `tools` directory (e.g., `multiply.py`):

```python
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
```

### 2. Register the tool

Open `__init__.py` and add your tool class to the `TOOL_CLASSES` list:

```python
from .add import AddTool
from .multiply import MultiplyTool  # Import your new tool

TOOL_CLASSES = [
    AddTool,
    MultiplyTool,  # Add your tool here
]
```

### 3. That's it!

No changes to `server.py` are needed. The server will automatically:
- List your tool when clients request available tools
- Route calls to your tool when the tool name matches

## Tool Implementation Requirements

Every tool must:

1. **Inherit from `BaseTool`**
2. **Implement required properties and methods**:
   - `name`: Unique identifier for the tool
   - `description`: Human-readable description
   - `get_input_schema()`: JSON Schema for input validation
   - `execute()`: Async method that performs the tool's operation

3. **Use Pydantic for input validation** (recommended)
4. **Return a list of `TextContent`** from the `execute()` method

## Benefits of This Architecture

- **Separation of Concerns**: Each tool is self-contained in its own file
- **Easy to Extend**: Add new tools without modifying `server.py`
- **Type Safety**: Pydantic models provide runtime validation
- **Maintainable**: Clear structure makes it easy to find and update tools
- **Testable**: Each tool can be tested independently
