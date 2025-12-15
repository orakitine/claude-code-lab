# Analyze and Fix Pattern - Context Handoff Example

## Pattern Overview

This demonstrates a two-agent workflow with context handoff:
1. **Agent 1 (Analyzer)**: Analyzes code and finds issues
2. **Agent 2 (Fixer)**: Receives context and fixes issues

## Workflow

### Phase 1: Analysis (Current Agent)

1. **Analyze Code**
   - Scan files for issues (linting, type errors, security issues)
   - Document findings in structured format
   - Example: Found 5 issues across 3 files

2. **Prepare Context Handoff**
   - Read template: `fix_handoff_template.md`
   - Fill in placeholders:
     - `<files_list>`: List of analyzed files
     - `<issues_list>`: Structured list of issues with file:line
     - `<recommendations>`: Specific fix suggestions
     - `<conversation_context>`: Summary of user conversation
   - Save as temporary handoff file

3. **Fork to Fixer Agent**
   - Use fork-terminal or background Task agent
   - Pass handoff file as context
   - Command: `claude -p "$(cat /tmp/handoff_context.md)"`

### Phase 2: Fixing (Forked Agent)

1. **Receive Context**
   - Read handoff prompt with all context
   - Understand: files, issues, recommendations, original conversation

2. **Execute Fixes**
   - Fix each issue systematically
   - Follow recommended approaches
   - Test fixes as you go

3. **Report Back**
   - Summary of fixes applied
   - Any issues that couldn't be auto-fixed
   - Recommendations for user review

## Example Flow

```
Main Session:
User: "Analyze src/ for issues and fix them"
Agent 1: [Analyzes code]
         "Found 5 linting errors, 2 type errors"
         [Prepares handoff with context]
         [Forks new terminal]

Forked Session:
Agent 2: [Reads handoff context]
         "I see 7 issues to fix from the analysis..."
         [Fixes each issue]
         "All fixed! Summary: ..."
```

## Benefits

- **Separation of Concerns**: Analysis and fixing are separate
- **Context Preserved**: Fixer knows everything analyzer found
- **Parallel Work**: Could fork multiple fixers for different file types
- **Audit Trail**: Handoff file documents what was passed

## Try It

1. Analyze some code and find issues
2. Fill in the handoff template with findings
3. Fork a new terminal with the handoff as prompt
4. Watch the fixer work with full context!
