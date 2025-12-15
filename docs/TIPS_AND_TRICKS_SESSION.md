# Claude Code Tips & Tricks: My Journey

> **Format**: Casual show-and-tell (20-25 min)
> **Vibe**: Personal sharing, not formal training
> **Goal**: Spark conversation, learn from each other

---

## Session Flow

### 1. Quick .claude Primer (3-5 min)

**"Here's how Claude Code extensibility works"**

Show your actual directory structure:

```
~/.claude/                    # Global (99% of my stuff lives here)
├── CLAUDE.md                 # Personal instructions for Claude
├── settings.json             # Hooks, MCP servers, permissions
├── skills/                   # Reusable workflows
│   ├── task-workflow/        # Universal task management
│   ├── quality-gate/         # Code quality checks
│   ├── project-context/      # Project analysis
│   └── doc-vault/            # Documentation cache
└── commands/                 # Quick prompt shortcuts

./.claude/                    # Project-specific (rare)
└── CLAUDE.md                 # Project context only
```

**Key Point**: Global first, project-specific only when truly unique.

---

### 2. Decision Making: When to Use What (2-3 min)

**"Three tools in your toolbox - here's when I use each"**

```
┌─────────────────────────────────────────────────────────┐
│  QUESTION                    →  ANSWER                  │
├─────────────────────────────────────────────────────────┤
│  Same prompt repeatedly?     →  COMMAND                 │
│  Multi-step workflow?        →  SKILL                   │
│  Need custom logic?          →  TOOL (inside skill)     │
│  Automate on events?         →  HOOK                    │
│  External integrations?      →  MCP SERVER              │
└─────────────────────────────────────────────────────────┘
```

**Real examples from my work:**
- **Commands** (repetitive prompts):
  - `/commit` - Smart git commits
  - `/prime` - Understand codebase instantly
  - `/toggle-hooks` - Enable/disable automation
  - `/all_skills` - Discover available workflows

- **Skills** (multi-step workflows):
  - `project-context` + `/prime` - The power pair for codebase understanding
  - `quality-gate` - Automated code quality verification
  - `doc-vault` - Auto-activating documentation cache
  - `fork-terminal` - Context handoff to new terminals
  - `task-workflow` - Universal task lifecycle management (the masterpiece!)

- **Integrations**:
  - Brave Search MCP - Web search capabilities
  - Memory MCP - Knowledge graph persistence

---

### 3. My Evolution: Basic → Advanced (10-12 min)

**"Let me show you what I actually built, from simple to complex"**

#### Level 1: Simple Commands

**Started here** - Just shortcuts for repetitive prompts:

**My actual commands:**

1. **`/all_skills`** - List all available skills
   ```markdown
   List all available skills from your system prompt.
   ```

2. **`/commit`** - Smart git commits
   ```markdown
   # Variables: COMMIT_MESSAGE
   # Workflow:
   - IF message provided → use it
   - ELSE: review changes, write appropriate message
   - Commit the code
   ```

3. **`/prime`** - Understand codebase quickly
   ```markdown
   # Workflow:
   1. Read README.md and .project-context.md
   2. Find all README files in repo
   3. Ask user which ones to read
   ```
   **Pro tip**: Pairs with `project-context` skill!

4. **`/toggle-hooks`** - Enable/disable notification hooks
   ```markdown
   # Workflow:
   - Parse: on/off/toggle
   - Create or remove .claude/.enable-hooks file
   ```

**When to create**: You type the same thing 3+ times

---

#### Level 2: Basic Skills

**Graduated to** - Multi-step workflows with framework awareness:

**My actual skills:**

1. **`project-context`** - Project analysis (pairs with `/prime`!)
   ```markdown
   ---
   name: Project Context Analyzer
   trigger: manual
   ---
   Workflow:
   1. Detect project type (JS, Python, Go)
   2. Analyze dependencies and structure
   3. Generate comprehensive report
   4. Save to .project-context.md or display
   ```

2. **`quality-gate`** - Code quality verification
   ```markdown
   ---
   name: Quality Gate
   trigger: manual
   ---
   Workflow:
   1. Run linter
   2. Run type checker
   3. Run tests
   4. Run build
   5. Report results
   ```

3. **`doc-vault`** - Auto-activating documentation cache
   ```markdown
   ---
   name: Doc Vault
   trigger: auto
   ---
   Workflow:
   - Auto-loads on first technical trigger
   - Fetches fresh docs via WebFetch
   - Caches for session use
   - Auto-consults when relevant
   ```

4. **`fork-terminal`** - Context handoff to new terminals
   ```markdown
   ---
   name: Fork Terminal
   trigger: manual
   ---
   Workflow:
   - Spawn new terminal window
   - Run Claude Code, Codex, or Gemini
   - Pass conversation context (optional)
   - Cross-platform (macOS/Windows)
   ```

**When to create**: Multi-step process you repeat often

---

#### Level 3: Advanced Skills with Variants

**Current level** - Framework-aware workflows with specialized variants:

```
.claude/skills/task-workflow/
├── SKILL.md                  # Main orchestrator
├── cookbook/
│   ├── define.md             # Create task spec
│   ├── refine.md             # Interview/clarify
│   ├── implement/
│   │   ├── generic.md        # Default implementation
│   │   └── nextjs.md         # Next.js patterns
│   └── review/
│       ├── generic.md        # Default review
│       └── nextjs.md         # Next.js validation
└── SKILL_CREATION_PRINCIPLES.md  # ⭐ The secret weapon
```

**Key Innovation**: SKILL_CREATION_PRINCIPLES

Think of it as your **linter for skills**:
- Single source of truth (no duplication)
- Inline examples (variables show format)
- Framework detection and routing
- Quality gates integration

**Show the file** - Walk through key sections:
- Variables pattern (extensibility)
- Cookbook pattern (framework variants)
- Workflow-first structure
- No duplication rule

**Real example**: "When I create TASK-001 in a Next.js project, it auto-detects the framework and routes to `cookbook/implement/nextjs.md` which knows about App Router vs Pages Router, Server Components, API route patterns, etc."

---

#### Level 4: The Complete Workflow

**task-workflow skill in action** (live demo or walkthrough):

```bash
# In todo-app directory
"define task: make app more visually appealing"

# Creates: TASK-001 [toRefine] (design): make-app-more-pretty.md
# - Gap analysis (what's missing)
# - Technical requirements
# - Acceptance criteria
# - Testing strategy

"refine task 001"

# Systematic interview (8 questions)
# Updates spec with decisions
# Transitions: [toRefine] → [toImplement]

"implement task 001"

# Detects Next.js framework
# Routes to cookbook/implement/nextjs.md
# Runs quality gates
# Implements in phases
# Transitions: [toImplement] → [toReview]

"review task 001"

# Validates against acceptance criteria
# Runs final quality checks
# Transitions: [toReview] → [done]
```

**Show the completed task file**: `tasks/TASK-001 [done] (design): make-app-more-pretty.md`

**Highlight**: Complete workflow history, all decisions documented, quality gates passed.

---

### 4. Your Turn: Show & Tell (5-10 min)

**"Now I want to learn from YOU"**

**Questions to spark discussion:**

1. **What commands have you created?**
   - Share your most-used shortcuts
   - Any clever prompt patterns?

2. **What skills do you use?**
   - Built your own or using others?
   - What workflows would you automate?

3. **How do you structure your .claude/ directory?**
   - Global vs project-specific split?
   - Any organizational tips?

4. **What's your approach to working with Claude?**
   - Project context in CLAUDE.md?
   - Hooks for automation?
   - MCP servers installed?

5. **What problems are you facing?**
   - Context loss?
   - Repetitive tasks?
   - Quality consistency?

**Collection Template** (optional - share async):

```markdown
## My Tip: [Name]

**What**: Command/Skill/Pattern I use
**Why**: Problem it solves
**How**: Quick example
**Impact**: Time saved / quality improved

[Code snippet or link]
```

---

## Talking Points & Tips

### Opening Hook

*"I spent the last 2 weeks going deep on Claude Code extensibility, and I want to share what I learned - but more importantly, I want to see what YOU'RE doing that I might be missing."*

### Transition to SKILL_CREATION_PRINCIPLES

*"The breakthrough moment for me was realizing I needed a 'linter for skills' - a set of principles to keep things maintainable. Let me show you what I mean..."*

**Open the file, highlight:**
- Variables section (see the format inline)
- No duplication rule
- Cookbook pattern explanation
- Framework detection logic

*"This is what lets me create universal workflows that adapt to different frameworks automatically."*

### Transition to Your Turn

*"Okay, I've talked for [X] minutes. Now it's your turn - what are YOU doing with Claude Code that's working well?"*

**Techniques:**
- Go around the room
- Popcorn sharing (voluntary)
- Pair up and share, then report back
- Async collection via Slack/wiki

---

## Demo Tips

### Option A: Live Demo (Risky but engaging)
- Have task-workflow already set up
- Define a simple task live
- Show the generated file
- Explain the workflow

### Option B: Walkthrough (Safe)
- Show completed TASK-001 file
- Walk through each section
- Explain the lifecycle
- Show framework-specific routing

### Option C: Hybrid (Recommended)
- Quick live: "define task: add dark mode toggle"
- Pre-completed: Walk through TASK-001 implementation
- Show: Actual code changes in todo-app

---

## Resources to Share

**This Repository**: https://github.com/orakitine/claude-code-lab

**What's inside:**
- `.claude/skills/task-workflow/` - Complete skill with principles
- `docs/` - Learning resources I created
- `tasks/TASK-001` - Real example from define to done
- `README.md` - My learning journey (Phases 1-5)

**Key files to highlight:**
- `.claude/skills/SKILL_CREATION_PRINCIPLES.md` - The "linter"
- `.claude/skills/task-workflow/SKILL.md` - Main orchestrator
- `.claude/skills/task-workflow/cookbook/implement/nextjs.md` - Framework variant example

---

## Wrap-Up

**Share these takeaways:**

1. **Start simple**: Commands are easy wins
2. **Graduate to skills**: When you need multi-step workflows
3. **Use principles**: Maintainability matters (SKILL_CREATION_PRINCIPLES)
4. **Share patterns**: We all benefit from each other's discoveries

**Call to action:**
- Clone the repo: `git clone https://github.com/orakitine/claude-code-lab.git`
- Try creating your first command
- Share what you build (GitHub issues, Slack, wiki)
- Let's build a team library together

**Final question:**
*"What's the ONE workflow you wish Claude Code could automate for you?"*

(Collect answers - these are your next skills to build!)

---

## Post-Session Follow-Up

**Within 24 hours:**
- [ ] Share session notes
- [ ] Create team Slack/wiki for sharing patterns
- [ ] Start collecting tips from the team

**Within 1 week:**
- [ ] Compile team submissions
- [ ] Build 1-2 team-requested skills together
- [ ] Document team best practices

**Ongoing:**
- [ ] Regular show-and-tell sessions
- [ ] Build shared skill library
- [ ] Cross-pollinate patterns

---

**Remember**: This is a conversation, not a presentation. Your goal is to spark ideas and learn from others, not to lecture. Keep it casual, show real examples, and make space for their stories.

Good luck, and may your coworkers have fascinating workflows to share! 🎤
