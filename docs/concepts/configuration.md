# Configuration - Settings & Customization

## Configuration Locations

Claude Code has **two-tier configuration**:

```
~/.claude/                    # Global (all projects)
├── settings.json
├── CLAUDE.md
├── commands/
└── skills/

project/.claude/              # Project-specific
├── settings.json
├── CLAUDE.md
├── commands/
└── skills/
```

**Precedence**: Project settings override global settings

## settings.json

Main configuration file for Claude Code behavior.

### Structure

```json
{
  "dangerouslySkipPermissions": [],
  "hooks": {},
  "mcpServers": {},
  "commands": {}
}
```

### Permission Configuration

Control which tools can run without asking permission:

```json
{
  "dangerouslySkipPermissions": [
    "Read",
    "Grep",
    "Glob"
  ]
}
```

**Options:**
- `["*"]` - Skip all permissions (dangerous!)
- `["Read", "Bash"]` - Skip specific tools
- `[]` - Ask for everything (safest)

### Hooks

Event-driven automation (see [Hooks](hooks.md)):

```json
{
  "hooks": {
    "user-prompt-submit": "echo 'User said something' >> ~/log.txt",
    "before-tool-call": "~/.claude/hooks/before.sh",
    "after-tool-call": "~/.claude/hooks/after.sh",
    "on-error": "notify-send 'Error!'"
  }
}
```

### MCP Servers

External tool providers (see [MCP Servers](mcp-servers.md)):

```json
{
  "mcpServers": {
    "postgres": {
      "command": "uvx",
      "args": ["mcp-server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://..."
      }
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

### Command Metadata

Optional metadata for commands:

```json
{
  "commands": {
    "review": {
      "description": "Review code changes",
      "category": "code-quality"
    },
    "test": {
      "description": "Run test suite",
      "category": "testing"
    }
  }
}
```

## CLAUDE.md

**Persistent instructions** that Claude reads every session.

### Global CLAUDE.md

`~/.claude/CLAUDE.md` - Applies to all projects

**Example: Personal Coding Style**
```markdown
# My Coding Standards

## Language Preferences
- Always use TypeScript over JavaScript
- Prefer functional programming patterns
- Use const/let, never var

## Code Quality
- Write tests for all new functions
- Use descriptive variable names
- Add JSDoc comments for public APIs

## Git Workflow
- Use conventional commits
- Always run tests before committing
- Keep commits atomic and focused

## Communication Style
- Be concise in explanations
- Show code examples
- Explain tradeoffs when making decisions
```

### Project CLAUDE.md

`.claude/CLAUDE.md` - Applies only to this project

**Example: Project-Specific**
```markdown
# Project: E-Commerce Platform

## Architecture
- This is a Next.js application
- Uses PostgreSQL database
- Tailwind CSS for styling
- Deployed on Vercel

## Important Files
- `/src/app` - App router pages
- `/src/components` - React components
- `/prisma/schema.prisma` - Database schema
- `/tests` - Jest test files

## Workflow
- Always update Prisma schema before modifying database
- Run `npm run db:migrate` after schema changes
- Test with `npm run test:integration`

## Code Standards
- Use server components by default
- Client components only when needed
- Follow existing component patterns in `/src/components`

## Deployment
- Main branch auto-deploys to production
- Staging branch deploys to staging environment
- Always test on staging first
```

### CLAUDE.md Best Practices

✅ **DO:**
- Document project architecture
- Specify coding standards
- List important file locations
- Define workflow procedures
- Include domain knowledge

❌ **DON'T:**
- Make it too long (Claude will summarize)
- Include sensitive information
- Duplicate what's in README.md
- Make overly strict rules

## Directory Structure

### Complete Setup

```
~/.claude/                              # Global configuration
├── settings.json                       # Global settings
├── CLAUDE.md                           # Global instructions
├── commands/                           # Global commands
│   ├── commit.md
│   ├── test.md
│   └── review.md
├── skills/                             # Global skills
│   ├── my-skill/
│   │   ├── SKILL.md
│   │   └── tools/
│   └── another-skill/
└── hooks/                              # Hook scripts (optional)
    ├── before-tool.sh
    └── after-tool.sh

project/.claude/                        # Project configuration
├── settings.json                       # Project settings
├── CLAUDE.md                           # Project instructions
├── commands/                           # Project commands
│   ├── deploy.md
│   └── build.md
└── skills/                             # Project skills
    └── project-specific-skill/
        ├── SKILL.md
        ├── cookbook/
        ├── prompts/
        └── tools/
```

## Environment Variables

### In MCP Servers

Use `${VAR_NAME}` to reference environment variables:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"  // Read from shell
      }
    }
  }
}
```

### Setting Environment Variables

```bash
# In ~/.bashrc or ~/.zshrc
export GITHUB_TOKEN="ghp_..."
export DATABASE_URL="postgresql://..."
export API_KEY="sk_..."
```

Then restart shell or `source ~/.bashrc`

## Configuration Precedence

When same setting exists in both global and project config:

```
Project .claude/settings.json
         ↓ (overrides)
Global ~/.claude/settings.json
         ↓ (fallback)
Claude Code defaults
```

**Example:**
```json
// ~/.claude/settings.json
{
  "dangerouslySkipPermissions": ["Read"]
}

// project/.claude/settings.json
{
  "dangerouslySkipPermissions": ["Read", "Write", "Bash"]
}

// Result: ["Read", "Write", "Bash"] (project wins)
```

## Common Configurations

### Minimal Setup
```json
{
  "dangerouslySkipPermissions": ["Read", "Grep", "Glob"]
}
```

### Development Setup
```json
{
  "dangerouslySkipPermissions": ["Read", "Grep", "Glob", "Bash"],
  "hooks": {
    "after-tool-call": "if [[ $TOOL_NAME == 'Write' ]]; then prettier --write $FILE_PATH; fi"
  }
}
```

### Full-Featured Setup
```json
{
  "dangerouslySkipPermissions": ["Read", "Grep", "Glob"],
  "hooks": {
    "before-tool-call": "~/.claude/hooks/before.sh",
    "after-tool-call": "~/.claude/hooks/after.sh",
    "on-error": "osascript -e 'display notification \"Error: $ERROR_MESSAGE\"'"
  },
  "mcpServers": {
    "postgres": {
      "command": "uvx",
      "args": ["mcp-server-postgres"],
      "env": {
        "DATABASE_URL": "${DATABASE_URL}"
      }
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

## Debugging Configuration

### Check Current Settings
```bash
# View global settings
cat ~/.claude/settings.json

# View project settings
cat .claude/settings.json

# View global instructions
cat ~/.claude/CLAUDE.md

# View project instructions
cat .claude/CLAUDE.md
```

### Test Hooks
```bash
# Run hook manually
TOOL_NAME="Write" FILE_PATH="test.js" bash -c "$(jq -r '.hooks["after-tool-call"]' .claude/settings.json)"
```

### Verify MCP Servers
```bash
# Test MCP server directly
uvx mcp-server-postgres
```

## Security Best Practices

### ✅ DO

- Use environment variables for secrets
- Keep settings.json in version control (without secrets)
- Use project-specific configs for project secrets
- Review hook scripts before adding

### ❌ DON'T

- Hardcode API keys in settings.json
- Commit sensitive data
- Use `dangerouslySkipPermissions: ["*"]` in shared projects
- Run untrusted hook scripts

## Migration and Portability

### Share Configuration (Safe)
```bash
# Share global config (remove secrets first!)
cp ~/.claude/settings.json ~/.claude/settings.example.json
# Edit and remove all env values
# Share settings.example.json
```

### Setup New Machine
```bash
# Copy config
cp settings.example.json ~/.claude/settings.json

# Set environment variables
echo 'export GITHUB_TOKEN="ghp_..."' >> ~/.bashrc

# Install MCP servers
npm install -g @modelcontextprotocol/server-github
```

## Configuration Tips

### Organized Global Skills
```
~/.claude/skills/
├── code-quality/
│   ├── SKILL.md (thorough code review)
├── documentation/
│   ├── SKILL.md (auto-generate docs)
└── testing/
    ├── SKILL.md (comprehensive testing)
```

### Project Templates
Create reusable project configs:

```
~/claude-templates/
├── nextjs/.claude/
├── python/.claude/
└── rust/.claude/
```

Then:
```bash
cp -r ~/claude-templates/nextjs/.claude ./
```

## Your Current Setup

From this project:

**Project Settings**: `.claude/settings.json` (if exists)
**Project Commands**: `.claude/commands/`
- `/prime`
- `/load_ai_docs`
- `/convert_paths_absolute`

**Project Skills**: `.claude/skills/`
- `fork-terminal/`

**Global Settings**: `~/.claude/CLAUDE.md`
- Skippy Protocol (awesome!)

## Next Steps

- Review your global CLAUDE.md
- Set up project-specific CLAUDE.md
- Configure helpful hooks
- Add MCP servers for services you use
- Organize skills by category

## Related Concepts

- [Hooks](hooks.md) - Configured in settings.json
- [MCP Servers](mcp-servers.md) - Configured in settings.json
- [Skills](skills.md) - Located in .claude/skills/
- [Commands](commands.md) - Located in .claude/commands/
