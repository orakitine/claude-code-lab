# Claude Code Agent Fork

Create a new Claude Code agent in a forked terminal to execute the task.

## Variables

DEFAULT_MODEL: opus       # Default model if not specified by user
HEAVY_MODEL: opus         # Model for "heavy" tasks
BASE_MODEL: sonnet        # Base/standard model
FAST_MODEL: haiku         # Model for "fast" tasks

## Workflow

1. **Check Claude CLI**
   - Tool: Run `claude --help` to understand available options
   - Verify Claude Code is installed and accessible
   - Example: `claude --help` → Shows available flags and usage

2. **Extract Task**
   - Parse user's request for the task/prompt
   - This will be passed via `-p` flag for automatic execution
   - Example: "fork claude code to fix tests" → Task: "fix tests"

3. **Determine Model**
   - IF: User specifies "fast" → Use FAST_MODEL (haiku)
   - IF: User specifies "heavy" → Use HEAVY_MODEL (opus)
   - ELSE: Use DEFAULT_MODEL (opus)
   - Example: "fork with claude fast to lint code" → Model: haiku

4. **Construct Command**
   - Format: `claude --model <model> -p "<task>" --dangerously-skip-permissions`
   - Always include `--dangerously-skip-permissions` flag
   - Example: `claude --model haiku -p "fix linting errors" --dangerously-skip-permissions`

5. **Execute Fork**
   - Tool: Call fork_terminal(command) with constructed command
   - Spawns new terminal with Claude Code agent running the task
   - Example: fork_terminal("claude --model opus -p 'implement feature X' --dangerously-skip-permissions")
