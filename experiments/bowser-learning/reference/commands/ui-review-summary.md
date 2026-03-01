# /ui-review Command (Summary from Bowser)

## Purpose

Discovers user stories from YAML files, fans out parallel `bowser-qa-agent` instances to validate each story, then aggregates and reports pass/fail results with screenshots.

## Variables

- HEADED: false (default) — set to "headed" to show browsers
- VISION: false — set to "vision" for screenshot-as-image validation
- FILENAME_FILTER: "" — restrict discovery to matching YAML filenames
- AGENT_TIMEOUT: 300 seconds per agent

## Directory Structure

- Stories: `ai_review/user_stories/*.yaml`
- Screenshots: `screenshots/bowser-qa/{timestamp}_{uuid}/{source-file}/{story-slug}/`

## 4-Phase Workflow

### Phase 1: Discover
- Glob YAML files from `ai_review/user_stories/`
- Parse story arrays from each file
- Generate timestamped run directory
- Compute screenshot paths for each story

### Phase 2: Spawn
- Create team via TeamCreate
- Establish tasks per story
- Launch all agents simultaneously with explicit prompts
- Each prompt includes: story details, screenshot paths, headed/vision config

### Phase 3: Collect
- Capture agent outputs
- Parse results for pass/fail status and step counts
- Update task completion

### Phase 4: Cleanup
- Send shutdown requests
- Delete team
- Generate aggregated summary report table

## Report Format

Summary table with overall pass/fail, failure details, and screenshot directory location.
