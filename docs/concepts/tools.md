# Tools - Custom Capabilities

## What Are Tools?

Tools are **executable functions** that give Claude new capabilities. They're actual code that runs and returns results.

## Key Characteristics

- **Capability-focused**: Add WHAT Claude can do
- **Code-based**: Python scripts, not instructions
- **Invoked by Claude**: Called automatically during task execution
- **Return values**: Provide data/results back to Claude

## Types of Tools

### 1. Built-in Tools
Claude Code includes these by default:

**File Operations**
- `Read` - Read file contents
- `Write` - Create new files
- `Edit` - Modify existing files
- `Glob` - Find files by pattern
- `Grep` - Search file contents

**Web Access**
- `WebFetch` - Retrieve and process URLs
- `WebSearch` - Search the web

**Execution**
- `Bash` - Run shell commands
- `Task` - Spawn sub-agents

**Code Analysis**
- `mcp__ide__getDiagnostics` - Get VS Code errors
- `mcp__ide__executeCode` - Run Jupyter code

**Notebooks**
- `NotebookEdit` - Edit Jupyter cells

### 2. Custom Tools
You create these in `.claude/skills/*/tools/`

**Example: Fork Terminal**
```python
#!/usr/bin/env -S uv run
"""Fork a new terminal window with a command."""

import os
import platform
import subprocess

def fork_terminal(command: str) -> str:
    """Open a new Terminal window and run the specified command."""
    system = platform.system()
    cwd = os.getcwd()

    if system == "Darwin":  # macOS
        shell_command = f"cd '{cwd}' && {command}"
        escaped_shell_command = shell_command.replace("\\", "\\\\").replace('"', '\\"')

        result = subprocess.run(
            ["osascript", "-e", f'tell application "Terminal" to do script "{escaped_shell_command}"'],
            capture_output=True,
            text=True,
        )
        return f"stdout: {result.stdout.strip()}\\nstderr: {result.stderr.strip()}\\nreturn_code: {result.returncode}"

    elif system == "Windows":
        full_command = f'cd /d "{cwd}" && {command}'
        subprocess.Popen(["cmd", "/c", "start", "cmd", "/k", full_command], shell=True)
        return "Windows terminal launched"

    else:
        raise NotImplementedError(f"Platform {system} not supported")
```

### 3. MCP Tools
Provided by external MCP servers (covered in [MCP Servers](mcp-servers.md))

## Creating Custom Tools

### Tool File Structure

```python
#!/usr/bin/env -S uv run
"""Tool description for Claude to understand what it does."""

import required_modules

def tool_function(param1: str, param2: int) -> str:
    """
    Function docstring - Claude sees this!

    Args:
        param1: Description of first parameter
        param2: Description of second parameter

    Returns:
        Description of return value
    """
    # Implementation
    result = do_something(param1, param2)
    return result

if __name__ == "__main__":
    # CLI interface (optional)
    import sys
    if len(sys.argv) > 1:
        output = tool_function(sys.argv[1], int(sys.argv[2]))
        print(output)
```

### Key Elements

1. **Shebang**: `#!/usr/bin/env -S uv run` - Makes it executable
2. **Module docstring**: Describes overall purpose
3. **Function signature**: Clear parameter types
4. **Function docstring**: What it does, params, returns
5. **Implementation**: Actual logic
6. **CLI interface**: Optional, for manual testing

### Tool Discovery

Claude automatically discovers tools in:
- `.claude/skills/*/tools/*.py`
- `~/.claude/skills/*/tools/*.py`

The tool becomes available by its **function name**.

## Tool Design Principles

### ✅ DO

- **Single responsibility**: One tool, one capability
- **Clear interface**: Well-typed parameters
- **Good docstrings**: Claude reads these!
- **Error handling**: Return meaningful error messages
- **Cross-platform**: Support macOS, Windows, Linux when possible

### ❌ DON'T

- **Duplicate built-ins**: Check if capability already exists
- **Side effects without returns**: Always return results
- **Unclear parameters**: Use type hints
- **Poor error messages**: Help Claude debug

## Common Tool Patterns

### Pattern: External Command Wrapper
```python
def run_linter(file_path: str) -> str:
    """Run ESLint on a file and return results."""
    result = subprocess.run(
        ["eslint", file_path, "--format", "json"],
        capture_output=True,
        text=True
    )
    return result.stdout
```

### Pattern: API Integration
```python
def fetch_github_issue(repo: str, issue_num: int) -> dict:
    """Fetch GitHub issue details."""
    import requests

    url = f"https://api.github.com/repos/{repo}/issues/{issue_num}"
    response = requests.get(url)
    return response.json()
```

### Pattern: Data Processing
```python
def parse_csv(file_path: str) -> str:
    """Parse CSV and return summary statistics."""
    import pandas as pd

    df = pd.read_csv(file_path)
    summary = {
        "rows": len(df),
        "columns": list(df.columns),
        "types": df.dtypes.to_dict()
    }
    return str(summary)
```

### Pattern: File System Operations
```python
def find_large_files(directory: str, min_size_mb: int = 10) -> list:
    """Find files larger than specified size."""
    import os

    large_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            size_mb = os.path.getsize(path) / (1024 * 1024)
            if size_mb >= min_size_mb:
                large_files.append({"path": path, "size_mb": size_mb})

    return large_files
```

## Tool Return Values

Tools should return **serializable data**:

**✅ Good return types:**
- `str` - Text output
- `dict` - Structured data
- `list` - Collections
- `int`, `float`, `bool` - Simple values

**❌ Avoid:**
- Complex objects
- File handles
- Connections

## Testing Tools

### Manual Testing
```bash
# Test from command line
.claude/skills/my-skill/tools/my_tool.py "arg1" "arg2"
```

### In Claude Code
```python
# Claude can call it directly
my_tool(param1="value", param2=123)
```

### Unit Tests
```python
# tests/test_my_tool.py
from claude.skills.my_skill.tools.my_tool import my_function

def test_my_function():
    result = my_function("input")
    assert result == "expected output"
```

## Tool Examples

### Database Query Tool
```python
def query_sqlite(db_path: str, query: str) -> list:
    """Execute SQLite query and return results."""
    import sqlite3

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()

    return [dict(row) for row in results]
```

### Image Analysis Tool
```python
def analyze_image(image_path: str) -> dict:
    """Analyze image and return metadata."""
    from PIL import Image

    img = Image.open(image_path)
    return {
        "dimensions": img.size,
        "format": img.format,
        "mode": img.mode,
        "file_size": os.path.getsize(image_path)
    }
```

### Code Metrics Tool
```python
def calculate_complexity(file_path: str) -> dict:
    """Calculate cyclomatic complexity of Python file."""
    import radon.complexity as radon

    with open(file_path) as f:
        code = f.read()

    results = radon.cc_visit(code)
    return {
        "average": radon.average_complexity(results),
        "functions": [{"name": r.name, "complexity": r.complexity} for r in results]
    }
```

## Dependencies

Tools can use external packages:

```python
#!/usr/bin/env -S uv run
# /// script
# dependencies = ["requests", "pandas"]
# ///

import requests
import pandas as pd

def fetch_and_analyze(url: str) -> dict:
    """Fetch CSV from URL and analyze."""
    response = requests.get(url)
    df = pd.read_csv(io.StringIO(response.text))
    return {"rows": len(df), "columns": list(df.columns)}
```

The `/// script` section tells `uv` which dependencies to install.

## Tool vs Bash Command

**Use a Tool when:**
- Need structured output
- Complex logic required
- Want type safety
- Reusable across skills

**Use Bash when:**
- Simple command execution
- Standard CLI tools
- One-off operations
- No processing needed

## Security Considerations

### Input Validation
```python
def safe_tool(user_input: str) -> str:
    """Tool with input validation."""
    # Validate input
    if not user_input.isalnum():
        return "Error: Invalid input"

    # Safe to use
    return process(user_input)
```

### Sandbox Awareness
```python
def file_tool(path: str) -> str:
    """Tool that respects sandbox boundaries."""
    # Ensure path is within allowed directory
    safe_path = os.path.abspath(path)
    if not safe_path.startswith(os.getcwd()):
        return "Error: Path outside project"

    # Safe to proceed
    return read_file(safe_path)
```

## Your Current Tools

From this project:
- `fork_terminal.py` - Spawns new terminal windows

## Next Steps

- Create a simple tool for a repeated task
- Add error handling and type hints
- Test tool manually and in Claude
- Build a skill that uses your tool

## Related Concepts

- [Skills](skills.md) - Workflows that use tools
- [MCP Servers](mcp-servers.md) - External tool providers
- [Bash Tool](../quick-reference/cheatsheet.md#bash) - Built-in command execution
