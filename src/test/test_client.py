#!/usr/bin/env python3
"""
Test client for PyCopilot MCP server
"""
import asyncio
import json
import sys
from typing import Any


async def send_request(writer: asyncio.StreamWriter, reader: asyncio.StreamReader, request: dict) -> dict:
    """Send a JSON-RPC request and get the response"""
    # Send request
    request_str = json.dumps(request) + "\n"
    print(f">>> Sending: {request_str.strip()}")
    writer.write(request_str.encode())
    await writer.drain()

    # Read response
    response_line = await reader.readline()
    if not response_line:
        raise Exception("No response received")

    response = json.loads(response_line.decode())
    print(f"<<< Received: {json.dumps(response, indent=2)}\n")
    return response


async def test_mcp_server():
    """Test the MCP server"""
    # Start the server process
    process = await asyncio.create_subprocess_exec(
        sys.executable, "../../main.py",
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    reader = process.stdout
    writer = process.stdin

    try:
        print("=" * 60)
        print("Testing PyCopilot MCP Server")
        print("=" * 60 + "\n")

        # Step 1: Initialize
        print("Step 1: Initialize the server")
        init_request = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {
                    "name": "test-client",
                    "version": "1.0.0"
                }
            }
        }
        await send_request(writer, reader, init_request)

        # Step 2: List tools
        print("Step 2: List available tools")
        list_tools_request = {
            "jsonrpc": "2.0",
            "id": 2,
            "method": "tools/list",
            "params": {}
        }
        await send_request(writer, reader, list_tools_request)

        # Step 3: Call add tool
        print("Step 3: Call the 'add' tool with a=10, b=25")
        call_tool_request = {
            "jsonrpc": "2.0",
            "id": 3,
            "method": "tools/call",
            "params": {
                "name": "add",
                "arguments": {
                    "a": 10,
                    "b": 25
                }
            }
        }
        await send_request(writer, reader, call_tool_request)

        # Step 4: Test with decimal numbers
        print("Step 4: Call the 'add' tool with a=3.14, b=2.86")
        call_tool_request2 = {
            "jsonrpc": "2.0",
            "id": 4,
            "method": "tools/call",
            "params": {
                "name": "add",
                "arguments": {
                    "a": 3.14,
                    "b": 2.86
                }
            }
        }
        await send_request(writer, reader, call_tool_request2)

        print("=" * 60)
        print("All tests completed successfully!")
        print("=" * 60)

    except Exception as e:
        print(f"\n❌ Error: {e}")
        # Print stderr if there's an error
        stderr = await process.stderr.read()
        if stderr:
            print(f"\nServer stderr:\n{stderr.decode()}")
    finally:
        # Close the server
        writer.close()
        await writer.wait_closed()
        process.terminate()
        await process.wait()


if __name__ == "__main__":
    asyncio.run(test_mcp_server())
