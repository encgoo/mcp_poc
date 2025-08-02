# MCP server type
## studio
This means the VS Code needs to start up the MCP server. 

## sse
```json
{
	"servers": {
		"my-mcp-server-a578ccdf": {
			"type": "studio",
			"command": "uv",
			"args": [
				"run",
				"mcp",
				"dev",
				".\\main.py"
			],
			"cwd": "D:\\Development\\git\\mcp_poc\\mcp-python"
		},
		"my-mcp-server-12345678": {
			"type": "sse",
			"url": "http://localhost:8000/sse",
			"headers": {
				"mcp-server": "my-mcp-server-a578ccdf"
			}	
		}
	},
	"inputs": []
}
```
This means the MCP server can be started outside VS Code, by terminal for example. 
```bash
uv run main.py
```
It will output the port being used. This can then be put into the mcp.json above.

Then we just need to enter the server URL to the mcp.json. 

This one is easier, we can make sure that the server is running.

# Usage
For this particular example, we can just type in Copilot
```
add two number 1,2
```