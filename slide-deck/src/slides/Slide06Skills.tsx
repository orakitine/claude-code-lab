import { Slide, Heading, Text, CodePane, UnorderedList, ListItem } from 'spectacle';

export function Slide06Skills() {
  const powerPair = `project-context skill → generates .project-context.md
            ↓
/prime command → reads it for instant understanding`;

  return (
    <Slide>
      <Heading fontSize="h2" color="primary" margin="0 0 30px 0">
        Level 2: Skills Collection
      </Heading>
      <Text fontSize="text" color="secondary" margin="0 0 30px 0">
        Next Step: Multi-Step Workflows
      </Text>
      <UnorderedList fontSize="text">
        <ListItem>project-context - Project analysis (pairs with /prime!)</ListItem>
        <ListItem>quality-gate - Lint, test, build verification</ListItem>
        <ListItem>doc-vault - Auto-activating documentation cache</ListItem>
        <ListItem>fork-terminal - Context handoff to new terminals</ListItem>
      </UnorderedList>
      <Text fontSize="text" margin="30px 0 20px 0" color="secondary">
        Highlight: The Power Pair
      </Text>
      <CodePane language="text">
        {powerPair}
      </CodePane>
    </Slide>
  );
}
