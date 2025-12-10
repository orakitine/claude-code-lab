# Hooks - Event-Driven Automation

## What Are Hooks?

Hooks are **shell commands that automatically execute in response to events** during your Claude Code session.

Think of them as GitHub Actions, but for your coding workflow.

## Key Characteristics

- **Event-driven**: Triggered by specific actions
- **Shell commands**: Run any CLI command
- **Invisible**: Execute silently in background
- **Powerful**: Can modify behavior, notify, validate, etc.

## How Hooks Work

```
Event occurs (e.g., user submits prompt)
         ↓
Hook command executes (e.g., notify-send "Working!")
         ↓
Event continues normally
```

Hooks run **synchronously** - the event waits for the hook to complete.

## Configuration

Hooks are defined in `.claude/settings.json`:

```json
{
  "hooks": {
    "user-prompt-submit": "echo 'User said: $PROMPT'",
    "before-tool-call": "echo 'About to call: $TOOL_NAME'",
    "after-tool-call": "echo 'Just called: $TOOL_NAME'",
    "on-error": "notify-send 'Error occurred!'"
  }
}
```

## Available Hook Events

### `user-prompt-submit`
Fires when user submits a prompt

**Available variables:**
- `$PROMPT` - The user's prompt text

**Example:**
```json
{
  "hooks": {
    "user-prompt-submit": "echo \"User asked: $PROMPT\" >> ~/claude-log.txt"
  }
}
```

### `before-tool-call`
Fires before Claude calls any tool

**Available variables:**
- `$TOOL_NAME` - Name of tool being called
- `$TOOL_PARAMS` - JSON parameters
- `$FILE_PATH` - If tool operates on files

**Example:**
```json
{
  "hooks": {
    "before-tool-call": "if [[ $TOOL_NAME == 'Write' ]]; then echo 'Creating: $FILE_PATH'; fi"
  }
}
```

### `after-tool-call`
Fires after Claude calls a tool

**Available variables:**
- `$TOOL_NAME` - Name of tool that was called
- `$RESULT` - Tool's return value
- `$SUCCESS` - true/false

**Example:**
```json
{
  "hooks": {
    "after-tool-call": "if [[ $TOOL_NAME == 'Bash' && $SUCCESS == 'true' ]]; then say 'Command succeeded'; fi"
  }
}
```

### `on-error`
Fires when an error occurs

**Available variables:**
- `$ERROR_MESSAGE` - The error message
- `$TOOL_NAME` - Tool that errored (if applicable)

**Example:**
```json
{
  "hooks": {
    "on-error": "osascript -e 'display notification \"$ERROR_MESSAGE\" with title \"Claude Error\"'"
  }
}
```

## Common Use Cases

### Auto-Linting Before Write
```json
{
  "hooks": {
    "before-tool-call": "if [[ $TOOL_NAME == 'Write' && $FILE_PATH == *.js ]]; then eslint $FILE_PATH || exit 1; fi"
  }
}
```

If linter fails, hook returns non-zero, blocking the write!

### Auto-Format After Edit
```json
{
  "hooks": {
    "after-tool-call": "if [[ $TOOL_NAME == 'Edit' ]]; then prettier --write $FILE_PATH; fi"
  }
}
```

### Notification System
```json
{
  "hooks": {
    "user-prompt-submit": "osascript -e 'display notification \"Thinking...\" with title \"Claude\"'",
    "on-error": "osascript -e 'display notification \"Error!\" with title \"Claude\"'"
  }
}
```

### Session Logging
```json
{
  "hooks": {
    "user-prompt-submit": "echo \"[$(date)] USER: $PROMPT\" >> ~/claude-session.log",
    "after-tool-call": "echo \"[$(date)] TOOL: $TOOL_NAME\" >> ~/claude-session.log"
  }
}
```

### Auto-Commit
```json
{
  "hooks": {
    "after-tool-call": "if [[ $TOOL_NAME == 'Write' || $TOOL_NAME == 'Edit' ]]; then git add $FILE_PATH && git commit -m 'Auto-commit: $FILE_PATH'; fi"
  }
}
```

### Security Validation
```json
{
  "hooks": {
    "before-tool-call": "if [[ $TOOL_NAME == 'Bash' && $TOOL_PARAMS == *rm* ]]; then echo 'Blocked dangerous command' && exit 1; fi"
  }
}
```

## Hook Blocking

Hooks can **block operations** by exiting with non-zero status:

```bash
# This hook blocks all Write operations to production files
if [[ $TOOL_NAME == 'Write' && $FILE_PATH == */production/* ]]; then
  echo "Cannot write to production!"
  exit 1  # Non-zero = block operation
fi
```

When blocked, Claude sees the error and can adjust behavior or ask user.

## Multi-Command Hooks

Use shell scripting for complex logic:

```json
{
  "hooks": {
    "after-tool-call": "~/.claude/hooks/after-tool.sh"
  }
}
```

Then in `~/.claude/hooks/after-tool.sh`:
```bash
#!/bin/bash

case $TOOL_NAME in
  Write)
    echo "File created: $FILE_PATH"
    prettier --write "$FILE_PATH"
    ;;
  Edit)
    echo "File edited: $FILE_PATH"
    git add "$FILE_PATH"
    ;;
  Bash)
    echo "Command ran: $TOOL_PARAMS"
    ;;
esac
```

## Platform-Specific Hooks

### macOS Notifications
```json
{
  "hooks": {
    "on-error": "osascript -e 'display notification \"$ERROR_MESSAGE\"'"
  }
}
```

### Linux Notifications
```json
{
  "hooks": {
    "on-error": "notify-send 'Claude Error' \"$ERROR_MESSAGE\""
  }
}
```

### Windows Notifications
```json
{
  "hooks": {
    "on-error": "powershell -Command \"New-BurntToastNotification -Text 'Error: $ERROR_MESSAGE'\""
  }
}
```

## Debugging Hooks

### Log Everything
```json
{
  "hooks": {
    "user-prompt-submit": "echo \"PROMPT: $PROMPT\" >> /tmp/claude-debug.log",
    "before-tool-call": "echo \"BEFORE: $TOOL_NAME\" >> /tmp/claude-debug.log",
    "after-tool-call": "echo \"AFTER: $TOOL_NAME\" >> /tmp/claude-debug.log"
  }
}
```

### Visual Feedback
```bash
# Flash terminal title
echo -ne "\\033]0;Claude: $TOOL_NAME\\007"
```

## Best Practices

### ✅ DO

- Keep hooks fast (they block execution)
- Log for debugging
- Use exit codes to communicate success/failure
- Test hooks thoroughly
- Document complex hook logic

### ❌ DON'T

- Run slow operations (blocks Claude)
- Forget error handling
- Make hooks overly complex
- Block legitimate operations
- Ignore hook failures

## Hook Recipes

### Code Quality Gate
```bash
# .claude/hooks/quality-gate.sh
#!/bin/bash

if [[ $TOOL_NAME != "Write" && $TOOL_NAME != "Edit" ]]; then
  exit 0  # Only check file operations
fi

# Run linter
eslint "$FILE_PATH" || exit 1

# Run type checker
tsc --noEmit "$FILE_PATH" || exit 1

# Run tests
npm test || exit 1

exit 0  # All checks passed
```

### Backup Before Edit
```bash
if [[ $TOOL_NAME == "Edit" ]]; then
  cp "$FILE_PATH" "$FILE_PATH.backup.$(date +%s)"
fi
```

### Smart Auto-Commit
```bash
if [[ $TOOL_NAME == "Write" || $TOOL_NAME == "Edit" ]]; then
  # Only auto-commit for certain file types
  case $FILE_PATH in
    *.md|*.txt|*.json)
      git add "$FILE_PATH"
      git commit -m "docs: update $(basename $FILE_PATH)"
      ;;
    *.js|*.ts|*.py)
      git add "$FILE_PATH"
      git commit -m "feat: modify $(basename $FILE_PATH)"
      ;;
  esac
fi
```

## Hook Environment

Hooks execute with:
- Current working directory = project root
- Access to all environment variables
- Access to Claude-provided variables (`$TOOL_NAME`, etc.)

## Conditional Hooks

Use shell scripting for conditional execution:

```json
{
  "hooks": {
    "before-tool-call": "[ -f .enable-hooks ] && ~/.claude/hooks/validate.sh || true"
  }
}
```

Only runs hook if `.enable-hooks` file exists!

## Global vs Project Hooks

**Global Hooks**: `~/.claude/settings.json`
- Active in ALL projects
- Good for: Personal workflow, universal checks

**Project Hooks**: `.claude/settings.json`
- Active only in this project
- Good for: Project-specific requirements

**Precedence**: Project hooks override global hooks

## Performance Considerations

Hooks run **synchronously**, so:

```json
{
  "hooks": {
    // ❌ BAD - Blocks for 5 seconds
    "after-tool-call": "sleep 5 && echo 'done'"

    // ✅ GOOD - Fast check
    "after-tool-call": "git add $FILE_PATH"

    // ✅ GOOD - Background if needed
    "after-tool-call": "slow-operation.sh &"
  }
}
```

## Integration with Skills

Skills can be designed to work WITH hooks:

**Skill workflow:**
1. Create `.pre-commit-check` file
2. Make code changes
3. Hook reads `.pre-commit-check` and validates
4. Remove marker file

**Hook:**
```bash
if [[ -f .pre-commit-check && $TOOL_NAME == "Write" ]]; then
  npm test || exit 1
fi
```

## Next Steps

- Add a simple logging hook
- Experiment with notification hooks
- Create a code quality gate
- Build project-specific validation hooks

## Related Concepts

- [Configuration](configuration.md) - Where hooks are defined
- [Tools](tools.md) - What hooks can respond to
- [Skills](skills.md) - Can coordinate with hooks
