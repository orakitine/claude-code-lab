import { Slide, Heading, Text, CodePane, UnorderedList, ListItem } from 'spectacle';

export function Slide08Principles() {
  const variablesExample = `TASK_ID_PREFIX: TASK        # Not "prefix for task IDs"
TASK_DIR: ./tasks           # Shows exact format`;

  return (
    <Slide>
      <Heading fontSize="h2" color="primary" margin="0 0 30px 0">
        SKILL_CREATION_PRINCIPLES
      </Heading>
      <Text fontSize="text" color="secondary" margin="0 0 30px 0">
        My "Linter for Skills"
      </Text>
      <UnorderedList fontSize="text">
        <ListItem>Single source of truth (no duplication)</ListItem>
        <ListItem>Inline examples (variables show format)</ListItem>
        <ListItem>Framework detection and routing</ListItem>
        <ListItem>Cookbook pattern for variants</ListItem>
        <ListItem>Quality gates integration</ListItem>
      </UnorderedList>
      <Text fontSize="text" margin="30px 0 20px 0" color="secondary">
        Example: Variables section shows format inline
      </Text>
      <CodePane language="text">
        {variablesExample}
      </CodePane>
    </Slide>
  );
}
