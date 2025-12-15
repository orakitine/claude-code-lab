# Claude Code Tips & Tricks - Slide Outline

> **Total**: 10-12 slides | **Duration**: 20-25 min
> **Vibe**: Casual show-and-tell, not formal training

---

## Slide Breakdown

### Slide 1: Title
**"Claude Code Tips & Tricks: My Journey from Commands to Universal Task Workflows"**

- Your name
- "What I learned in 2 weeks of deep diving"
- "And what I want to learn from YOU"
- Repo link: https://github.com/orakitine/claude-code-lab

**Visual**: Simple, clean title slide

---

### Slide 2: Quick .claude Primer

**"How Claude Code Extensibility Works"**

```
~/.claude/                    # Global (99% of my stuff)
├── CLAUDE.md                 # Personal instructions
├── settings.json             # Hooks, MCP, permissions
├── skills/                   # Reusable workflows
│   ├── task-workflow/
│   ├── quality-gate/
│   └── doc-vault/
└── commands/                 # Prompt shortcuts

./.claude/                    # Project (rare)
└── CLAUDE.md                 # Project context only
```

**Key Point**: Global first, project-specific rarely

**Visual**: Directory tree with annotations

---

### Slide 3: When to Use What

**"Three Tools in Your Toolbox"**

```
┌─────────────────────────────────────────────┐
│  SITUATION              →  SOLUTION         │
├─────────────────────────────────────────────┤
│  Same prompt 3+ times   →  COMMAND         │
│  Multi-step workflow    →  SKILL           │
│  Custom logic needed    →  TOOL            │
│  Automate on events     →  HOOK            │
│  External integration   →  MCP SERVER      │
└─────────────────────────────────────────────┘
```

**Visual**: Decision table with examples

---

### Slide 4: Level 1 - Simple Commands

**"Where I Started: Just Shortcuts"**

**My command collection:**
- `/all_skills` - List available skills
- `/commit` - Smart git commits (with optional message)
- `/prime` - Understand codebase (pairs with project-context!)
- `/toggle-hooks` - Enable/disable hooks

**Example: /commit**
```markdown
# Variables: COMMIT_MESSAGE
# Workflow:
- Review changes
- Write appropriate message
- Commit the code
```

**When**: You type the same thing 3+ times

**Visual**: List of commands with /commit example highlighted

---

### Slide 5: Level 2 - Skills Collection

**"Next Step: Multi-Step Workflows"**

**My skill collection:**
- `project-context` - Project analysis (pairs with `/prime`!)
- `quality-gate` - Lint, test, build verification
- `doc-vault` - Auto-activating documentation cache
- `fork-terminal` - Context handoff to new terminals

**Highlight: The Power Pair**
```
project-context skill → generates .project-context.md
            ↓
/prime command → reads it for instant understanding
```

**When**: Multi-step process you repeat often

**Visual**: List of skills with "power pair" diagram highlighted

---

### Slide 6: Level 3 - Advanced Skills

**"Current Level: Framework-Aware Workflows"**

```
.claude/skills/task-workflow/
├── SKILL.md                  # Main orchestrator
├── cookbook/
│   ├── define.md             # Create spec
│   ├── refine.md             # Interview
│   ├── implement/
│   │   ├── generic.md        # Default
│   │   └── nextjs.md         # Next.js specific
│   └── review/
│       ├── generic.md
│       └── nextjs.md
└── SKILL_CREATION_PRINCIPLES.md  # ⭐ Secret weapon
```

**Visual**: Directory tree highlighting SKILL_CREATION_PRINCIPLES

---

### Slide 7: The Secret Weapon

**"SKILL_CREATION_PRINCIPLES: My 'Linter for Skills'"**

**Key Principles:**
- Single source of truth (no duplication)
- Inline examples (variables show format)
- Framework detection and routing
- Cookbook pattern for variants
- Quality gates integration

**Example**: Variables section shows format inline:
```
TASK_ID_PREFIX: TASK        # Not "prefix for task IDs"
TASK_DIR: ./tasks           # Shows exact format
```

**Visual**: Screenshot of actual SKILL_CREATION_PRINCIPLES sections

---

### Slide 8: Real Example - Task Lifecycle

**"task-workflow in Action"**

```
"define task: make app more visually appealing"
   ↓
TASK-001 [toRefine] created with:
- Gap analysis
- Requirements
- Acceptance criteria

"refine task 001"
   ↓
Interview (8 questions) → [toImplement]

"implement task 001"
   ↓
Detects Next.js → Routes to nextjs.md → [toReview]

"review task 001"
   ↓
Validates criteria → [done]
```

**Visual**: Flowchart or step-by-step with state transitions

---

### Slide 9: The Result

**"TASK-001: Complete Workflow History"**

**Show**: Screenshot of completed task file

**Highlight:**
- All decisions documented
- Quality gates passed
- Code changes linked
- Acceptance criteria validated

**Key Point**: "Everything from thought to production is tracked"

**Visual**: Actual task file with annotations

---

### Slide 10: Your Turn

**"What Are YOU Doing?"**

**Questions for the group:**

1. What commands have you created?
2. What skills do you use?
3. How do you structure .claude/?
4. What's your approach to working with Claude?
5. What workflows would you automate?

**Visual**: Questions as bullet list, inviting discussion

---

### Slide 11: Resources

**"Clone This Repository"**

**https://github.com/orakitine/claude-code-lab**

**What's inside:**
- Complete task-workflow skill
- SKILL_CREATION_PRINCIPLES (the "linter")
- My learning journey (Phases 1-5)
- Real example (TASK-001 from define to done)
- Documentation and patterns

**Call to action:**
- Try creating your first command
- Share what you build
- Let's build a team library

**Visual**: Repo structure or QR code

---

### Slide 12: Final Question

**"What's the ONE workflow you wish Claude Code could automate for you?"**

(Open floor for answers)

**Next steps:**
- Share session notes
- Create team channel for sharing
- Build requested skills together

**Visual**: Big question, open space for discussion

---

## Visual Design Notes

### Keep It Simple
- Minimal text (you'll elaborate verbally)
- Code blocks with syntax highlighting
- Directory trees for structure
- Flowcharts for processes
- Screenshots of real examples

### Color Scheme
- **Primary**: Claude purple (#8B5CF6)
- **Code blocks**: Dark background
- **Highlights**: Light purple (#A78BFA)
- Keep it clean and professional

### Typography
- **Titles**: 48-54pt, bold
- **Body**: 24-28pt
- **Code**: 20-22pt, monospace
- Plenty of whitespace

---

## Presentation Tips

### Opening (Slide 1-2)
*"I went deep on Claude Code for 2 weeks. Built commands, skills, even a universal task management system. I want to show you what I learned, but honestly, I'm MORE curious about what YOU'RE doing."*

### Transition to Principles (Slide 7)
*"The breakthrough was creating SKILL_CREATION_PRINCIPLES. Think of it as a linter for skills - it keeps everything maintainable and prevents chaos."*

### Demo Approach (Slide 8-9)
- **Option A**: Quick live demo of "define task"
- **Option B**: Walk through completed TASK-001
- **Option C**: Show video/recording

Pick based on your comfort level and time available.

### Engagement (Slide 10)
*"Okay, enough about me. Let's go around - who's built something cool? Or who has a workflow they WISH they could automate?"*

### Closing (Slide 12)
*"My goal isn't to teach you - it's to start a conversation. Let's share patterns and build a team library together."*

---

## Time Allocation

- Slides 1-3 (Context): ~3-5 min
- Slides 4-6 (Evolution): ~5-7 min
- Slides 7-9 (Advanced): ~5-7 min
- Slides 10-12 (Discussion): ~5-10 min

**Total**: 20-25 minutes + organic discussion

---

## Backup Plans

### If Running Long
- Skip Slide 5 (basic skills), jump straight to advanced
- Shorten demo (just show completed task file)

### If Running Short
- Deeper dive into SKILL_CREATION_PRINCIPLES
- Live demo of creating a simple command
- More time for discussion

### If Demo Fails
- Have screenshots ready
- Walk through completed task file instead
- Show code changes in todo-app

---

**Remember**: This is show-and-tell, not a lecture. Your slides are conversation starters, not the full story. Keep it casual, be ready to go off-script, and make space for others to share.
