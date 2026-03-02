# 4-Layer Agentic Browser Automation
# Adapted from github.com/disler/bowser for claude-code-lab

model := "opus"

default_prompt := "Go to https://news.ycombinator.com/, take a screenshot of the front page, summarize the top 3 stories, close the browser."

default_qa_prompt := "Navigate to https://news.ycombinator.com/. Verify the front page loads with at least 10 posts. Click 'More' to go to the next page. Verify page 2 loads with new posts. Go back to page 1. Click into the first post's comments link. Verify comments are visible."

# List available commands
default:
    @just --list

# ─── Layer 1: Skill (Capability) ─────────────────────────────

# Test the raw Playwright skill directly
test-skill headed="false" prompt=default_prompt:
    claude --dangerously-skip-permissions --model {{model}} "/playwright-browser (headed: {{headed}}) {{prompt}}"

# ─── Layer 2: Subagent (Scale) ───────────────────────────────

# Test the Playwright browser agent (isolated session)
test-agent headed="false" prompt=default_prompt:
    claude --dangerously-skip-permissions --model {{model}} "Use @playwright-browser-agent to do this: (headed: {{headed}}) {{prompt}}"

# Test the QA agent with a structured user story
test-qa headed="false" prompt=default_qa_prompt:
    claude --dangerously-skip-permissions --model {{model}} "Use @browser-qa-agent: (headed: {{headed}}) {{prompt}}"

# ─── Layer 3: Command (Orchestration) ────────────────────────

# Run parallel UI review across all YAML user stories
ui-review *flags="":
    claude --dangerously-skip-permissions --model {{model}} "/browser:ui-review {{flags}}"

# Run a saved browser automation workflow
run-workflow workflow="blog-summarizer" *args="":
    claude --dangerously-skip-permissions --model {{model}} "/browser:run-workflow {{workflow}} {{args}}"

# ─── Layer 4: Just (Reusability) ─────────────────────────────

# Summarize a blog (headless, no auth needed)
summarize-blog url="https://simonwillison.net/":
    just run-workflow blog-summarizer "{{url}} headless"

# Run UI review in headed mode (watch the browsers)
ui-review-headed:
    just ui-review headed

# Quick smoke test — skill + screenshot
smoke-test:
    claude --dangerously-skip-permissions --model {{model}} "/playwright-browser Go to https://example.com, take a screenshot, close the browser."
