---
name: Fork Terminal Skill
description: Fork a terminal session to a new terminal window. Use this when the user requests 'fork terminal' or 'create a new terminal' or 'new terminal: <command>' or 'fork session: <command>'.
trigger: manual
allowed-tools:
  - Bash
  - Read
---

# Purpose

Fork a terminal session to a new terminal window using agentic coding tools (Claude Code, Codex CLI, Gemini CLI) or raw CLI commands. Supports context handoff with conversation summary for agentic tools.

## Variables

ENABLE_RAW_CLI_COMMANDS: true    # Allow forking with raw CLI commands (ffmpeg, curl, python, etc.)
ENABLE_GEMINI_CLI: true           # Enable Gemini CLI agent forking
ENABLE_CODEX_CLI: true            # Enable Codex CLI agent forking
ENABLE_CLAUDE_CODE: true          # Enable Claude Code agent forking
AGENTIC_CODING_TOOLS: claude-code, codex-cli, gemini-cli  # List of supported agentic tools

## Workflow

1. **Parse User Request**
   - Extract: tool type (agentic vs raw CLI), tool name, command/task
   - Check for "summary" keyword (context handoff for agentic tools)
   - Example: "fork terminal use claude code to fix tests" → Tool: claude-code, Task: "fix tests", Summary: no

2. **Read Fork Tool**
   - Tool: Read `.claude/skills/fork-terminal/tools/fork_terminal.py`
   - Understand forking mechanism and parameters
   - Example: fork_terminal(command: str) → Spawns new terminal with command

3. **Handle Summary Context (Agentic Tools Only)**
   - IF: User requested summary (keywords: "summarize", "summary", "include context")
   - AND: Tool is in AGENTIC_CODING_TOOLS (claude-code, codex-cli, gemini-cli)
   - AND: Tool is enabled via ENABLE flag
   - THEN: Apply summary workflow:
     - Read `.claude/skills/fork-terminal/prompts/fork_summary_user_prompt.md` template
     - Fill template IN MEMORY (IMPORTANT: don't update the file, fill it in memory only)
     - Replace XML tags: <fill in the history here> with conversation history between you and user
     - Replace XML tags: <fill in the next user request here> with the user's task
     - This filled prompt will be passed to the PROMPT parameter (-p flag) of the agentic coding tool
     - Template structure: Provides context handoff so new agent has conversation history
   - ELSE: Use task as-is without summary (for raw CLI or when summary not requested)
   - Summary examples:
     - "fork terminal use claude code to fix tests summarize work so far"
     - "spin up new terminal with codex include summary for refactoring"
     - "create terminal with gemini with context to implement feature"
   - Non-summary example: "fork terminal use claude code to run tests" → Direct task, no summary

4. **Route to Cookbook**
   - Determine scenario based on tool type and enabled flags
   - Options: Raw CLI, Claude Code, Codex CLI, Gemini CLI
   - Example: "claude code" requested + ENABLE_CLAUDE_CODE=true → Claude Code scenario

5. **Execute Cookbook Scenario**
   - Read and follow appropriate cookbook file
   - Cookbook will construct the fork command
   - Example: claude-code.md → Builds claude command with flags

6. **Fork Terminal**
   - Tool: Execute fork_terminal(command)
   - Spawns new terminal window with constructed command
   - Example: fork_terminal("claude --model sonnet -p 'fix tests'")

## Cookbook

### Raw CLI Commands

- IF: The user requests a non-agentic coding tool AND `ENABLE_RAW_CLI_COMMANDS` is true.
- THEN: Read and execute: `.claude/skills/fork-terminal/cookbook/cli-command.md` 
- EXAMPLES:
  - "Create a new terminal to <xyz> with ffmpeg"
  - "Create a new terminal to <xyz> with curl"
  - "Create a new terminal to <xyz> with python"

### Claude Code

- IF: The user requests a claude code agent to execute the command AND `ENABLE_CLAUDE_CODE` is true.
- THEN: Read and execute: `.claude/skills/fork-terminal/cookbook/claude-code.md`
- EXAMPLES:
  - "fork terminal use claude code to <xyz>"
  - "spin up a new terminal request <xyz> using claude code"
  - "create a new terminal to <xyz> with claude code"

### Codex CLI

- IF: The user requests a codex CLI agent to execute the command AND `ENABLE_CODEX_CLI` is true.
- THEN: Read and execute: `.claude/skills/fork-terminal/cookbook/codex-cli.md`
- EXAMPLES:
  - "fork terminal use codex to <xyz>"
  - "spin up a new terminal request <xyz> using codex"
  - "create a new terminal to <xyz> with codex"

### Gemini CLI

- IF: The user requests a gemini CLI agent to execute the command AND `ENABLE_GEMINI_CLI` is true.
- THEN: Read and execute: `.claude/skills/fork-terminal/cookbook/gemini-cli.md`
- EXAMPLES:
  - "fork terminal use gemini to <xyz>"
  - "spin up a new terminal request <xyz> with gemini"
  - "create a new terminal to <xyz> using gemini"
