# Codex CLI Agent Fork

Create a new Codex CLI agent in a forked terminal to execute the task.

## Variables

DEFAULT_MODEL: gpt-5.1-codex-max     # Default model if not specified by user
HEAVY_MODEL: gpt-5.1-codex-max       # Model for "heavy" tasks
BASE_MODEL: gpt-5.1-codex-max        # Base/standard model
FAST_MODEL: gpt-5.1-codex-mini       # Model for "fast" tasks

## Workflow

1. **Check Codex CLI**
   - Tool: Run `codex --help` to understand available options
   - Verify Codex CLI is installed and accessible
   - Example: `codex --help` → Shows available flags and usage

2. **Extract Task**
   - Parse user's request for the task/prompt
   - Will be passed as positional prompt (interactive mode, no -p flag)
   - Example: "fork codex to refactor module" → Task: "refactor module"

3. **Determine Model**
   - IF: User specifies "fast" → Use FAST_MODEL (gpt-5.1-codex-mini)
   - IF: User specifies "heavy" → Use HEAVY_MODEL (gpt-5.1-codex-max)
   - ELSE: Use DEFAULT_MODEL (gpt-5.1-codex-max)
   - Example: "fork with codex fast to check syntax" → Model: gpt-5.1-codex-mini

4. **Construct Command**
   - Format: `codex -m <model> --dangerously-bypass-approvals-and-sandbox "<task>"`
   - Use `-m` for model selection (not --model)
   - Always use interactive mode (positional prompt, no -p flag)
   - Always include `--dangerously-bypass-approvals-and-sandbox` flag
   - Example: `codex -m gpt-5.1-codex-mini --dangerously-bypass-approvals-and-sandbox "optimize queries"`

5. **Execute Fork**
   - Tool: Call fork_terminal(command) with constructed command
   - Spawns new terminal with Codex CLI agent in interactive mode
   - Example: fork_terminal("codex -m gpt-5.1-codex-max --dangerously-bypass-approvals-and-sandbox 'implement caching'")
