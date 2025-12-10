# Commands - User-Invoked Prompt Shortcuts

## What Are Commands?

Slash commands are **text expansion macros** - shortcuts for complex prompts you type frequently.

## Key Characteristics

- **User-invoked**: You type `/command` explicitly
- **Text expansion**: The command file content becomes the prompt
- **Visible**: User knows they're running a command
- **Simple**: Just markdown files with prompt text

## How They Work

```
User types:    /review-pr
               ↓
Claude sees:   [entire contents of .claude/commands/review-pr.md]
               ↓
Claude acts:   As if user typed that full prompt
```

It's literally find-and-replace!

## Creating a Command

### 1. Create the file
```bash
.claude/commands/my-command.md
```

### 2. Write the prompt
```markdown
Review the current PR changes and provide a detailed code review.

Focus on:
- Logic errors
- Security vulnerabilities
- Test coverage
- Performance issues
- Code style consistency

Format the output as a markdown report with severity levels.
```

### 3. Use it
```
User: /my-command
```

That's it!

## Command Structure

Commands are **just markdown files**. No frontmatter, no special syntax.

```markdown
This is what Claude will see when you type /mycommand.

You can include:
- Multiple paragraphs
- Bullet lists
- Specific instructions
- Context requirements
- Output format requests

Everything in this file becomes the prompt.
```

## Parameterized Commands

Commands can accept arguments:

```markdown
<!-- .claude/commands/fix-issue.md -->
Find and fix the bug described in GitHub issue #{{ARG1}}.

Steps:
1. Fetch issue details
2. Locate relevant code
3. Fix the bug
4. Run tests
5. Commit with message "fix: resolve issue #{{ARG1}}"
```

Usage:
```
/fix-issue 123
```

Claude sees:
```
Find and fix the bug described in GitHub issue #123...
```

## Common Use Cases

### Development Workflow
```markdown
<!-- /commit -->
Create a git commit with a conventional commit message.

1. Run git status and git diff
2. Analyze the changes
3. Write a concise commit message following conventional commits
4. Stage relevant files
5. Create the commit
```

### Testing
```markdown
<!-- /test -->
Run the test suite and fix any failures.

1. Run all tests
2. If failures: analyze and fix
3. Re-run tests to verify
4. Report results
```

### Documentation
```markdown
<!-- /docs -->
Generate documentation for recent changes.

1. Review git log for recent commits
2. Identify changed files
3. Update relevant documentation
4. Ensure examples are current
```

### Code Review
```markdown
<!-- /review -->
Perform a thorough code review of current changes.

Check for:
- Logic correctness
- Security issues
- Performance concerns
- Test coverage
- Documentation updates needed

Provide actionable feedback with severity ratings.
```

## Commands vs Skills

| Aspect | Commands | Skills |
|--------|----------|--------|
| **Invoked** | User types `/cmd` | Claude auto-detects |
| **Visibility** | Explicit | Invisible |
| **Purpose** | Shortcut for typing | Workflow automation |
| **When to use** | Repeated requests | Contextual patterns |

## Global vs Project Commands

**Global Commands**: `~/.claude/commands/`
- Available everywhere
- Good for: Personal workflow, general tasks
- Example: `/commit`, `/review`, `/test`

**Project Commands**: `.claude/commands/`
- Only in this project
- Good for: Project-specific tasks
- Example: `/deploy`, `/build-docker`, `/run-migrations`

## Best Practices

### ✅ DO

- Keep commands focused on single tasks
- Use clear, descriptive names
- Include step-by-step instructions
- Specify output format
- Document parameters if used

### ❌ DON'T

- Create overly complex multi-step workflows (use skills instead)
- Use vague instructions
- Duplicate built-in functionality
- Create one-off commands (just type the prompt)

## Advanced Patterns

### Conditional Logic
```markdown
<!-- /review-changes -->
Review the current changes.

IF changes include tests:
  - Verify test coverage is adequate

IF changes include API endpoints:
  - Check security implications
  - Verify input validation

IF changes include database:
  - Review migrations
  - Check for breaking changes
```

### Chained Actions
```markdown
<!-- /ship -->
Prepare changes for production.

1. Run full test suite
2. If tests pass: generate changelog
3. Create git commit
4. Create GitHub PR
5. Report PR URL
```

### Integration with Skills
```markdown
<!-- /parallel-research -->
Fork terminal use claude code to research the latest React patterns
and fork terminal use claude code to review our current React usage.

Combine findings into a migration plan.
```

This command triggers the fork-terminal skill twice!

## Your Current Commands

From `.claude/commands/`:
- `/prime` - Understand codebase and report
- `/load_ai_docs` - Load documentation from websites
- `/convert_paths_absolute` - Convert relative paths to absolute

## Command Organization

For many commands, organize by category:

```
.claude/commands/
├── dev-commit.md
├── dev-test.md
├── dev-build.md
├── review-pr.md
├── review-security.md
├── docs-generate.md
└── docs-update.md
```

Or use prefixes:
- `dev-*` for development
- `review-*` for code review
- `docs-*` for documentation
- `deploy-*` for deployment

## Testing Commands

1. Type the command
2. Verify expansion happened (you'll see Claude respond to full prompt)
3. Check results match expectations
4. Refine prompt if needed

## Command Templates

### Starter Template
```markdown
[Clear, concise description of what to do]

Steps:
1. [First action]
2. [Second action]
3. [Third action]

Output format:
[How to present results]
```

### Research Template
```markdown
Research [TOPIC] and provide a summary.

Focus on:
- [Aspect 1]
- [Aspect 2]
- [Aspect 3]

Sources to check:
- Official documentation
- Recent blog posts
- Community discussions

Format: Markdown with sections and bullet points
```

### Fix Template
```markdown
Fix [PROBLEM].

1. Identify root cause
2. Implement fix
3. Add test to prevent regression
4. Verify fix works
5. Report what was changed and why
```

## Next Steps

- Create a few commands for your common workflows
- Try parameterized commands
- Combine commands with skills
- Build a personal command library

## Related Concepts

- [Skills](skills.md) - Auto-invoked workflows (vs manual commands)
- [CLAUDE.md](configuration.md#claudemd) - Persistent instructions
- [Hooks](hooks.md) - Event-driven automation
