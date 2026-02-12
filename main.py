#!/usr/bin/env python3
"""
PyCopilot - Backwards compatibility entry point

This file is kept for backwards compatibility with existing configurations
that use 'uv run main.py'. For new usage, prefer:
- uvx pycopilot
- uv run pycopilot
- python -m pycopilot
"""
from pycopilot.server import run

if __name__ == "__main__":
    run()
