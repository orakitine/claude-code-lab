import { Slide, Heading, Text, CodePane } from 'spectacle';

export function Slide03ClaudePrimer() {
  const codeExample = `~/.claude/                    # Global (99% of my stuff)
├── CLAUDE.md                 # Personal instructions
├── settings.json             # Hooks, MCP, permissions
├── skills/                   # Reusable workflows
│   ├── task-workflow/
│   ├── quality-gate/
│   └── doc-vault/
└── commands/                 # Prompt shortcuts

./.claude/                    # Project (rare)
└── CLAUDE.md                 # Project context only`;

  return (
    <Slide>
      <Heading fontSize="h2" color="primary" margin="0 0 40px 0">
        How Claude Code Extensibility Works
      </Heading>
      <CodePane language="bash">
        {codeExample}
      </CodePane>
      <Text fontSize="text" margin="40px 0 0 0" color="secondary">
        Key Point: Global first, project-specific rarely
      </Text>
    </Slide>
  );
}
