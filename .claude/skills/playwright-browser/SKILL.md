---
name: Playwright Browser
description: Headless browser automation using Playwright CLI. Use for browser testing, screenshots, scraping, and parallel browser sessions. Token-efficient CLI — no MCP overhead.
trigger: manual
allowed-tools:
  - Bash
  - Read
  - Write
---

# Purpose

Automate browsers using `playwright-cli`, a token-efficient CLI for Playwright. Runs headless by default, supports parallel sessions via named sessions (`-s=`), and persistent profiles for cookies/state. Use when you need headless browsing, UI testing, screenshots, web scraping, or any browser automation that can run in the background.

## Variables

HEADED: false                              # Show browser window. Options: true, false
VISION: false                              # Return screenshots as images in context (higher token cost)
VIEWPORT_SIZE: 1440x900                    # Browser viewport dimensions (WxH)
SCREENSHOTS_DIR: ./screenshots             # Where screenshots are saved

## Workflow

1. **Open Session**
   - Derive a short kebab-case session name from the user's prompt
   - Open with `--persistent` to preserve cookies/localStorage across commands
   - Example: "test checkout on mystore.com" → `-s=mystore-checkout`
   - Example: "scrape pricing from competitor.com" → `-s=competitor-pricing`
   - IF: HEADED is true → add `--headed` flag
   - IF: VISION is true → prefix with `PLAYWRIGHT_MCP_CAPS=vision`
   - Tool: Bash
     ```
     PLAYWRIGHT_MCP_VIEWPORT_SIZE=<VIEWPORT_SIZE> playwright-cli -s=<session-name> open <url> --persistent
     ```
   - Headed example:
     ```
     PLAYWRIGHT_MCP_VIEWPORT_SIZE=1440x900 playwright-cli -s=mystore-checkout open https://mystore.com --persistent --headed
     ```

2. **Snapshot Page**
   - Capture element references to identify interactive elements
   - Returns a list of refs (e.g., `e12`, `e45`) you can click, fill, etc.
   - Example: `playwright-cli -s=mystore-checkout snapshot` → returns element tree with refs
   - Tool: Bash `playwright-cli -s=<session-name> snapshot`

3. **Interact with Elements**
   - Use refs from snapshot to click, fill, type, select, hover
   - Example: `playwright-cli -s=mystore-checkout click e12` → clicks element ref e12
   - Example: `playwright-cli -s=mystore-checkout fill e15 "test@example.com"` → fills input
   - Example: `playwright-cli -s=mystore-checkout type "search query"` → types into focused element
   - Example: `playwright-cli -s=mystore-checkout press Enter` → presses keyboard key
   - Navigate: `goto <url>`, `go-back`, `go-forward`, `reload`
   - Tool: Bash `playwright-cli -s=<session-name> <command> <args>`

4. **Take Screenshots**
   - Capture current page state as PNG
   - IF: specific filename needed → use `--filename=<path>`
   - Example: `playwright-cli -s=mystore-checkout screenshot` → saves to default location
   - Example: `playwright-cli -s=mystore-checkout screenshot --filename=./screenshots/checkout-step1.png`
   - Tool: Bash `playwright-cli -s=<session-name> screenshot [--filename=<path>]`

5. **Close Session**
   - ALWAYS close the session when done — this is not optional
   - Example: `playwright-cli -s=mystore-checkout close`
   - To close ALL sessions: `playwright-cli close-all`
   - To wipe session data: `playwright-cli -s=<name> delete-data`
   - Tool: Bash `playwright-cli -s=<session-name> close`

## Additional Commands Reference

Available commands (use `playwright-cli --help <command>` for details):

- **Navigation**: `open [url]`, `goto <url>`, `go-back`, `go-forward`, `reload`
- **Input**: `click <ref>`, `dblclick <ref>`, `fill <ref> <text>`, `type <text>`, `press <key>`, `select <ref> <val>`, `check <ref>`, `uncheck <ref>`, `hover <ref>`
- **Capture**: `snapshot`, `screenshot [--filename=<f>]`, `pdf`
- **Tabs**: `tab-list`, `tab-new [url]`, `tab-close [index]`, `tab-select <index>`
- **Storage**: `state-save`, `state-load`, `cookie-get`, `cookie-clear`
- **DevTools**: `console`, `run-code <js>`, `network`
- **Sessions**: `list`, `close-all`, `kill-all`
- **Config**: `open --headed`, `open --browser=chrome`, `resize <w> <h>`
