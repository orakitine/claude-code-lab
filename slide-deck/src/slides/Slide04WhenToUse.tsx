import { Slide, Heading, CodePane } from 'spectacle';

export function Slide04WhenToUse() {
  const decisionTable = `┌────────────────────────────────────────────────────────┐
│  SITUATION            →  SOLUTION     │  WHO EXECUTES  │
├────────────────────────────────────────────────────────┤
│  Same prompt 3+ times →  COMMAND     │  YOU type it   │
│  Multi-step workflow  →  SKILL       │  CLAUDE calls  │
│  Custom logic needed  →  TOOL        │  CLAUDE calls  │
│  Automate on events   →  HOOK        │  System runs   │
│  External integration →  MCP SERVER  │  CLAUDE calls  │
└────────────────────────────────────────────────────────┘`;

  return (
    <Slide>
      <Heading fontSize="h2" color="primary" margin="0 0 40px 0">
        Three Tools in Your Toolbox
      </Heading>
      <CodePane language="text">
        {decisionTable}
      </CodePane>
    </Slide>
  );
}
