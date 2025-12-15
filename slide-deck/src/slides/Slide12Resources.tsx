import { Slide, Heading, Text, UnorderedList, ListItem, Link } from 'spectacle';

export function Slide12Resources() {
  return (
    <Slide>
      <Heading fontSize="h2" color="primary" margin="0 0 40px 0">
        Clone This Repository
      </Heading>
      <Link
        href="https://github.com/orakitine/claude-code-lab"
        target="_blank"
        fontSize="h3"
        color="secondary"
        margin="0 0 40px 0"
      >
        github.com/orakitine/claude-code-lab
      </Link>
      <Text fontSize="text" margin="40px 0 20px 0">
        What's inside:
      </Text>
      <UnorderedList fontSize="text">
        <ListItem>Complete task-workflow skill</ListItem>
        <ListItem>SKILL_CREATION_PRINCIPLES (the "linter")</ListItem>
        <ListItem>My learning journey (Phases 1-5)</ListItem>
        <ListItem>Real example (TASK-001 from define to done)</ListItem>
        <ListItem>Documentation and patterns</ListItem>
      </UnorderedList>
    </Slide>
  );
}
