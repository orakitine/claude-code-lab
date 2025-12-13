# Purpose

Toggle notification hooks on or off by creating or removing `.claude/.enable-hooks` file.

## Workflow

- Parse the user's request to determine if they want hooks enabled or disabled:

  - "on", "true", "enable", "yes" → Enable hooks
  - "off", "false", "disable", "no" → Disable hooks
  - No parameter → Check current state and toggle to opposite

- IF: no parameter (toggle):

  - Use Bash to check: `[ -f .claude/.enable-hooks ] && echo "enabled" || echo "disabled"`
  - If currently enabled → Disable (remove file)
  - If currently disabled → Enable (create file)

- IF: enabling:

  - Use Write tool to create empty `.claude/.enable-hooks` file
  - Confirm: "✓ Notification hooks enabled"

- IF: disabling:
  - Use Bash to run: `rm -f .claude/.enable-hooks`
  - Confirm: "✓ Notification hooks disabled"
