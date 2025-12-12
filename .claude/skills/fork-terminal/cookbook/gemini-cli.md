# Gemini CLI Agent Fork

Create a new Gemini CLI agent in a forked terminal to execute the task.

## Variables

DEFAULT_MODEL: gemini-2.5-pro          # Default model if not specified by user
HEAVY_MODEL: gemini-3-pro-preview      # Model for "heavy" tasks
BASE_MODEL: gemini-2.5-pro             # Base/standard model
FAST_MODEL: gemini-2.5-flash           # Model for "fast" tasks

## Workflow

1. **Check Gemini CLI**
   - Tool: Run `gemini --help` to understand available options
   - Verify Gemini CLI is installed and accessible
   - Example: `gemini --help` → Shows available flags and usage

2. **Extract Task**
   - Parse user's request for the task/prompt
   - Will be passed after `-i` flag (interactive mode)
   - Example: "fork gemini to analyze code" → Task: "analyze code"

3. **Determine Model**
   - IF: User specifies "fast" → Use FAST_MODEL (gemini-2.5-flash)
   - IF: User specifies "heavy" → Use HEAVY_MODEL (gemini-3-pro-preview)
   - ELSE: Use DEFAULT_MODEL (gemini-2.5-pro)
   - Example: "fork with gemini fast to review PR" → Model: gemini-2.5-flash

4. **Construct Command**
   - Format: `gemini --model <model> --yolo -i "<task>"`
   - OR short form: `gemini --model <model> -y -i "<task>"`
   - `-i` flag MUST be last flag before the prompt (interactive mode)
   - Always include `--yolo` (or `-y`) flag
   - Example: `gemini --model gemini-2.5-flash -y -i "implement authentication"`

5. **Execute Fork**
   - Tool: Call fork_terminal(command) with constructed command
   - Spawns new terminal with Gemini CLI agent in interactive mode
   - Example: fork_terminal("gemini --model gemini-2.5-pro --yolo -i 'add error handling'")
