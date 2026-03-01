# Parallel UI Review

## Purpose

Discover user stories from YAML files, fan out parallel `@browser-qa-agent` instances to validate each story, then aggregate and report pass/fail results with screenshots.

## Variables

HEADED: false                              # Show browser windows. Pass "headed" as argument to enable
VISION: false                              # Screenshot-as-image validation. Pass "vision" as argument to enable
STORIES_DIR: ai_review/user_stories        # Directory containing YAML story files
AGENT_TIMEOUT: 300                         # Seconds before agent timeout
FILENAME_FILTER: ""                        # Restrict discovery to matching YAML filenames

## Workflow

1. **Parse Arguments**
   - Scan $ARGUMENTS for keywords (case-insensitive)
   - IF: "headed" found → set HEADED=true
   - IF: "vision" found → set VISION=true
   - Remaining text → set FILENAME_FILTER
   - Example: `/ui-review headed hackernews` → HEADED=true, FILENAME_FILTER="hackernews"
   - Example: `/ui-review` → all defaults (headless, no vision, all stories)

2. **Discover Stories**
   - Glob: `<STORIES_DIR>/*.yaml`
   - IF: FILENAME_FILTER is set → only include files matching filter
   - Parse each YAML file → extract `stories` array
   - Count total stories across all files
   - Create timestamped run directory: `screenshots/browser-qa/<YYYY-MM-DD>_<HH-MM-SS>_<8-char-uuid>/`
   - Example: found `hackernews.yaml` with 3 stories → 3 agents needed
   - Tool: Glob, Bash (for parsing YAML), Bash (for mkdir)

3. **Spawn Parallel Agents**
   - For each story, spawn a `@browser-qa-agent` using the Agent tool with `run_in_background: true`
   - Each agent gets a prompt containing:
     ```
     Execute this user story:

     **Story:** <story-name>
     **URL:** <story-url>
     **Headed:** <HEADED>
     **Vision:** <VISION>
     **Screenshots Directory:** <run-dir>/<source-file>/<story-slug>/

     **Workflow:**
     <story-workflow>
     ```
   - Launch ALL agents in a single message (parallel execution)
   - Example: 3 stories → 3 parallel Agent tool calls, each with `subagent_type: "general-purpose"` and the browser-qa-agent prompt

4. **Collect Results**
   - Wait for all agents to complete (use TaskOutput for each)
   - Parse each agent's report for: PASS/FAIL status, step count, screenshot directory
   - Example: Agent 1 returns "PASS 3/3 steps", Agent 2 returns "FAIL 2/4 steps"

5. **Generate Summary Report**
   - Format results into summary table:
     ```
     UI REVIEW SUMMARY
     Run: <timestamp>
     Stories: <total> | Passed: <pass-count> | Failed: <fail-count>

     | # | Story | Source | Status | Steps | Screenshots |
     |---|-------|--------|--------|-------|-------------|
     | 1 | Front page loads | hackernews.yaml | PASS | 3/3 | ./screenshots/browser-qa/.../ |
     | 2 | View comments | hackernews.yaml | FAIL | 2/3 | ./screenshots/browser-qa/.../ |
     ```
   - IF: any failures → include full failure reports below the table
   - Report screenshot root directory for easy browsing
