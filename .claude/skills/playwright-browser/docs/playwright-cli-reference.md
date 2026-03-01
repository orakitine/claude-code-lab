# Playwright CLI Quick Reference

Generated from `playwright-cli --help`. Use `playwright-cli --help <command>` for detailed usage.

## Session Pattern

All commands use `-s=<session-name>` for named sessions:
```bash
playwright-cli -s=<name> <command> [args] [options]
```

## Core Commands

| Command | Description | Example |
|---------|-------------|---------|
| `open [url]` | Launch browser | `playwright-cli -s=test open https://example.com --persistent` |
| `close` | Close browser session | `playwright-cli -s=test close` |
| `goto <url>` | Navigate to URL | `playwright-cli -s=test goto https://example.com/page2` |
| `snapshot` | Get element refs | `playwright-cli -s=test snapshot` |
| `screenshot` | Capture page image | `playwright-cli -s=test screenshot --filename=out.png` |
| `click <ref>` | Click element | `playwright-cli -s=test click e12` |
| `fill <ref> <text>` | Fill input field | `playwright-cli -s=test fill e15 "hello"` |
| `type <text>` | Type into focused element | `playwright-cli -s=test type "search"` |
| `press <key>` | Press keyboard key | `playwright-cli -s=test press Enter` |
| `hover <ref>` | Hover over element | `playwright-cli -s=test hover e20` |
| `select <ref> <val>` | Select dropdown option | `playwright-cli -s=test select e30 "option1"` |

## Environment Variables

| Variable | Purpose | Default |
|----------|---------|---------|
| `PLAYWRIGHT_MCP_VIEWPORT_SIZE` | Set viewport (WxH) | `1280x720` |
| `PLAYWRIGHT_MCP_CAPS` | Set to `vision` for image responses | unset |

## Session Management

```bash
playwright-cli list                    # List active sessions
playwright-cli close-all               # Close all sessions
playwright-cli -s=<name> close         # Close specific session
playwright-cli -s=<name> delete-data   # Wipe session profile
```

## Common Flags

- `--persistent` — preserve cookies/localStorage (use with `open`)
- `--headed` — show browser window (use with `open`)
- `--browser=chrome` — use Chrome instead of Chromium (use with `open`)
- `--filename=<path>` — save screenshot to specific path
