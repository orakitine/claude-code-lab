import { Slide, Heading, Text, UnorderedList, ListItem } from 'spectacle';

export function Slide10Result() {
  return (
    <Slide>
      <Heading fontSize="h2" color="primary" margin="0 0 40px 0">
        TASK-001: Complete Workflow History
      </Heading>
      <UnorderedList fontSize="text">
        <ListItem>All decisions documented</ListItem>
        <ListItem>Quality gates passed</ListItem>
        <ListItem>Code changes linked</ListItem>
        <ListItem>Acceptance criteria validated</ListItem>
      </UnorderedList>
      <Text fontSize="h3" margin="60px 0 0 0" color="secondary">
        "Everything from thought to production is tracked"
      </Text>
    </Slide>
  );
}
