# MCP Servers - External Tool Providers

## What is MCP?

**Model Context Protocol (MCP)** is a standard for connecting external tools and data sources to Claude.

Think of MCP servers as **plugin systems** that extend Claude's capabilities.

## Key Characteristics

- **External processes**: Run separately from Claude
- **Standard protocol**: Works across different AI tools
- **Tool providers**: Expose new capabilities to Claude
- **Context providers**: Can also provide data/knowledge

## How MCP Works

```
Claude Code
     ↓
  [MCP Client]
     ↓
  [MCP Server] ← External process (Node.js, Python, etc.)
     ↓
  [External Service] ← Database, API, filesystem, etc.
```

Claude calls MCP tools → MCP server handles request → Returns results

## Configuration

MCP servers are configured in `.claude/settings.json`:

```json
{
  "mcpServers": {
    "server-name": {
      "command": "executable",
      "args": ["arg1", "arg2"],
      "env": {
        "ENV_VAR": "value"
      }
    }
  }
}
```

## Real Examples

### PostgreSQL Database Access
```json
{
  "mcpServers": {
    "postgres": {
      "command": "uvx",
      "args": ["mcp-server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://user:pass@localhost/dbname"
      }
    }
  }
}
```

**Gives Claude:**
- `query_database(sql)` - Run SQL queries
- `list_tables()` - See database schema
- `describe_table(name)` - Get table details

### GitHub Integration
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_..."
      }
    }
  }
}
```

**Gives Claude:**
- `get_issue(repo, number)` - Fetch issue details
- `create_pr(repo, title, body)` - Create pull requests
- `list_repos()` - List repositories

### Brave Search
```json
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "BSA..."
      }
    }
  }
}
```

**Gives Claude:**
- `web_search(query)` - Search the web
- Better than built-in search for some use cases

### SQLite
```json
{
  "mcpServers": {
    "sqlite": {
      "command": "uvx",
      "args": ["mcp-server-sqlite", "--db-path", "./data.db"]
    }
  }
}
```

**Gives Claude:**
- `query(sql)` - Query local SQLite databases
- `list_tables()` - Explore schema

## Popular MCP Servers

| Server | Purpose | Command |
|--------|---------|---------|
| **PostgreSQL** | Database queries | `mcp-server-postgres` |
| **SQLite** | Local databases | `mcp-server-sqlite` |
| **GitHub** | GitHub integration | `@modelcontextprotocol/server-github` |
| **Google Drive** | File access | `@modelcontextprotocol/server-gdrive` |
| **Slack** | Slack messaging | `@modelcontextprotocol/server-slack` |
| **Brave Search** | Web search | `@modelcontextprotocol/server-brave-search` |
| **Filesystem** | Extended file ops | `@modelcontextprotocol/server-filesystem` |
| **Memory** | Persistent memory | `@modelcontextprotocol/server-memory` |

Full list: https://github.com/modelcontextprotocol/servers

## MCP vs Custom Tools

| Aspect | Custom Tools | MCP Servers |
|--------|--------------|-------------|
| **Scope** | Single function | Multiple related tools |
| **Process** | Runs in Claude | Separate process |
| **Language** | Python (usually) | Any language |
| **State** | Stateless | Can maintain state |
| **Complexity** | Simple scripts | Full applications |
| **Reusability** | Project-specific | Cross-tool compatible |

**When to use MCP:**
- Need multiple related tools (database: query, schema, insert)
- External service integration (GitHub, Slack, Google)
- Want to maintain state between calls
- Building for multiple AI tools (not just Claude)

**When to use Custom Tools:**
- Single, simple function
- Project-specific logic
- Quick prototypes

## Creating Your Own MCP Server

### Basic Structure (Python)

```python
# my-mcp-server.py
from mcp.server import Server
from mcp.server.stdio import stdio_server

app = Server("my-server")

@app.tool()
def my_tool(param: str) -> str:
    """Description of what this tool does."""
    return f"Result: {param}"

@app.tool()
def another_tool(value: int) -> dict:
    """Another capability."""
    return {"doubled": value * 2}

if __name__ == "__main__":
    stdio_server(app)
```

### Configuration
```json
{
  "mcpServers": {
    "my-server": {
      "command": "python",
      "args": ["my-mcp-server.py"]
    }
  }
}
```

### Basic Structure (Node.js)

```javascript
// my-mcp-server.js
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';

const server = new Server({
  name: 'my-server',
  version: '1.0.0'
});

server.setRequestHandler('tools/list', async () => ({
  tools: [
    {
      name: 'my_tool',
      description: 'Does something useful',
      inputSchema: {
        type: 'object',
        properties: {
          param: { type: 'string' }
        }
      }
    }
  ]
}));

server.setRequestHandler('tools/call', async (request) => {
  if (request.params.name === 'my_tool') {
    return {
      content: [
        {
          type: 'text',
          text: `Result: ${request.params.arguments.param}`
        }
      ]
    };
  }
});

const transport = new StdioServerTransport();
await server.connect(transport);
```

## Advanced MCP Features

### Resource Providers
MCP servers can provide **context** (not just tools):

```python
@app.resource("project://readme")
def get_readme() -> str:
    """Provides project README as context."""
    with open("README.md") as f:
        return f.read()
```

Claude can then access this as context automatically!

### Prompts
MCP servers can provide **prompt templates**:

```python
@app.prompt("code-review")
def code_review_prompt(file_path: str) -> str:
    """Returns code review prompt."""
    return f"Review {file_path} for security and performance issues."
```

### State Management
```python
class StatefulServer:
    def __init__(self):
        self.cache = {}

    @app.tool()
    def store(self, key: str, value: str) -> str:
        """Store value in server memory."""
        self.cache[key] = value
        return f"Stored {key}"

    @app.tool()
    def retrieve(self, key: str) -> str:
        """Retrieve value from server memory."""
        return self.cache.get(key, "Not found")
```

## Testing MCP Servers

### Test Locally
```bash
# Run server directly
python my-mcp-server.py

# Test with MCP inspector
npx @modelcontextprotocol/inspector my-mcp-server.py
```

### Test in Claude
```json
// Add to settings.json
{
  "mcpServers": {
    "test": {
      "command": "python",
      "args": ["my-mcp-server.py"]
    }
  }
}
```

Then ask Claude to use the tools!

## Use Cases

### Database Access
```
You: "Query our users table and show me the most recent 10 signups"
Claude: [Uses MCP postgres tool to query database]
```

### External APIs
```
You: "Create a GitHub issue for the bug we just found"
Claude: [Uses MCP github tool to create issue]
```

### Custom Integrations
```
You: "Check our Stripe dashboard for today's revenue"
Claude: [Uses custom MCP stripe-server tool]
```

### Knowledge Bases
```
You: "What does our internal wiki say about deployment?"
Claude: [Uses MCP server that queries company wiki]
```

## Security Considerations

### Environment Variables
```json
{
  "mcpServers": {
    "secure": {
      "command": "my-server",
      "env": {
        "API_KEY": "${API_KEY}",  // Read from shell environment
        "SECRET": "${SECRET}"
      }
    }
  }
}
```

Never hardcode secrets in settings.json!

### Permissions
MCP servers run with your user permissions, so:
- ✅ Can access your files
- ✅ Can make network requests
- ⚠️ Only use trusted MCP servers!

## Debugging MCP Servers

### Enable Logging
```json
{
  "mcpServers": {
    "debug": {
      "command": "python",
      "args": ["server.py", "--log-level", "DEBUG"]
    }
  }
}
```

### Check Server Output
```bash
# MCP servers write to stderr
python server.py 2> debug.log
```

### Use MCP Inspector
```bash
npx @modelcontextprotocol/inspector python server.py
```

Opens interactive UI to test tools!

## Global vs Project MCP Servers

**Global**: `~/.claude/settings.json`
- Available in all projects
- Good for: Personal databases, general APIs

**Project**: `.claude/settings.json`
- Only in this project
- Good for: Project-specific databases, APIs

## Best Practices

### ✅ DO

- Use MCP for external service integration
- Keep servers focused (one service per server)
- Document tools well (Claude reads descriptions!)
- Handle errors gracefully
- Use environment variables for secrets

### ❌ DON'T

- Hardcode secrets in settings.json
- Make servers too complex
- Duplicate built-in capabilities
- Forget error handling
- Skip testing

## Example: Custom API Server

```python
# company-api-server.py
from mcp.server import Server
import requests

app = Server("company-api")

@app.tool()
def get_employee(email: str) -> dict:
    """Fetch employee details from company API."""
    response = requests.get(
        f"https://api.company.com/employees/{email}",
        headers={"Authorization": f"Bearer {os.getenv('COMPANY_API_KEY')}"}
    )
    return response.json()

@app.tool()
def create_ticket(title: str, description: str) -> dict:
    """Create support ticket in company system."""
    response = requests.post(
        "https://api.company.com/tickets",
        json={"title": title, "description": description},
        headers={"Authorization": f"Bearer {os.getenv('COMPANY_API_KEY')}"}
    )
    return response.json()
```

Configuration:
```json
{
  "mcpServers": {
    "company": {
      "command": "python",
      "args": ["company-api-server.py"],
      "env": {
        "COMPANY_API_KEY": "${COMPANY_API_KEY}"
      }
    }
  }
}
```

## Next Steps

- Install a popular MCP server (sqlite, github)
- Try using its tools
- Build a simple custom MCP server
- Integrate with your existing services

## Resources

- MCP Specification: https://spec.modelcontextprotocol.io
- Official Servers: https://github.com/modelcontextprotocol/servers
- Python SDK: https://github.com/modelcontextprotocol/python-sdk
- TypeScript SDK: https://github.com/modelcontextprotocol/typescript-sdk

## Related Concepts

- [Tools](tools.md) - Custom Python tools (simpler alternative)
- [Configuration](configuration.md) - Where MCP servers are configured
- [Skills](skills.md) - Can use MCP tools in workflows
