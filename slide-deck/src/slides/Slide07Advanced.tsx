import { Slide, Heading, Text, CodePane } from 'spectacle';

export function Slide07Advanced() {
  const taskWorkflowStructure = `.claude/skills/task-workflow/
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
└── SKILL_CREATION_PRINCIPLES.md  # ⭐ Secret weapon`;

  return (
    <Slide>
      <Heading fontSize="h2" color="primary" margin="0 0 30px 0">
        Level 3: Framework-Aware Workflows
      </Heading>
      <Text fontSize="text" color="secondary" margin="0 0 30px 0">
        Current Level: Advanced Skills
      </Text>
      <CodePane language="bash">
        {taskWorkflowStructure}
      </CodePane>
    </Slide>
  );
}
