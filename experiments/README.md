# Experiments Directory

This is your playground for hands-on learning! Experiment freely here without worrying about breaking anything.

## Structure

```
experiments/
├── commands/       # Your custom slash commands
├── skills/         # Skills you're building
├── tools/          # Custom tools you write
├── notes/          # Your learning notes
└── README.md       # This file
```

## How to Use

### Testing Commands
1. Create a command file: `commands/mytest.md`
2. Copy to Claude: `cp commands/mytest.md ../.claude/commands/`
3. Test it: `/mytest`
4. Iterate and improve!

### Building Skills
1. Create skill directory: `skills/my-skill/`
2. Add SKILL.md and any tools/prompts
3. Copy to Claude: `cp -r skills/my-skill ../.claude/skills/`
4. Test with trigger phrases
5. Debug and refine!

### Writing Tools
1. Create tool: `tools/my_tool.py`
2. Make it executable: `chmod +x tools/my_tool.py`
3. Test standalone: `./tools/my_tool.py args`
4. Add to a skill in `tools/` subdirectory
5. Let Claude use it!

### Taking Notes
Use `notes/` to document:
- What you learned
- Patterns that worked
- Ideas for future experiments
- Debugging insights
- "Aha!" moments

## Workflow Tips

### Safe Experimentation
- Keep working versions in `.claude/`
- Experiment with copies in `experiments/`
- When satisfied, move experiments to `.claude/`

### Learning Cycle
1. **Read** a concept in `docs/concepts/`
2. **Plan** what to build
3. **Create** in `experiments/`
4. **Test** by copying to `.claude/`
5. **Iterate** based on results
6. **Document** learnings in `notes/`

### Example: Creating a Command

```bash
# 1. Create experimental command
cat > experiments/commands/review.md << 'EOF'
Review my recent code changes.

Focus on:
- Logic correctness
- Security issues
- Test coverage
- Code style

Format as markdown with severity levels.
EOF

# 2. Test it
cp experiments/commands/review.md .claude/commands/
# Then use: /review

# 3. Iterate if needed
vim experiments/commands/review.md

# 4. Update when satisfied
cp experiments/commands/review.md .claude/commands/
```

## Current Experiments

Document what you're working on:

### Active
- *Nothing yet - start your first experiment!*

### Completed
- *Your completed experiments will be listed here*

### Ideas
- Create `/commit` command for smart commits
- Build a code formatter skill
- Write a database query tool
- Set up auto-format hook
- Create a research orchestration skill

## Resources

- [Commands Guide](../docs/concepts/commands.md)
- [Skills Guide](../docs/concepts/skills.md)
- [Tools Guide](../docs/concepts/tools.md)
- [Skill Patterns](../docs/examples/skill-patterns.md)
- [Cheat Sheet](../docs/quick-reference/cheatsheet.md)

## Tips

1. **Start simple** - Get one thing working before adding complexity
2. **Test frequently** - Copy to `.claude/` and test after each change
3. **Read error messages** - They tell you what's wrong!
4. **Study examples** - The fork-terminal skill is your reference
5. **Document everything** - Future you will thank present you

Happy experimenting! 🧪
