import { Slide, Heading, CodePane } from 'spectacle';

export function Slide09Lifecycle() {
  const lifecycleFlow = `"define task: make app more visually appealing"
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
Validates criteria → [done]`;

  return (
    <Slide>
      <Heading fontSize="h2" color="primary" margin="0 0 40px 0">
        task-workflow in Action
      </Heading>
      <CodePane language="text">
        {lifecycleFlow}
      </CodePane>
    </Slide>
  );
}
