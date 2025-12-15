import { Slide, Heading, Text, UnorderedList, ListItem } from 'spectacle';

export function Slide02ThreeAudiences() {
  return (
    <Slide>
      <Heading fontSize="h2" color="primary" margin="0 0 40px 0">
        Designing for Three Audiences
      </Heading>
      <UnorderedList fontSize="text">
        <ListItem>
          <Text color="secondary">YOU (Me)</Text> - The developer creating workflows
        </ListItem>
        <ListItem>
          <Text color="secondary">CLAUDE (AI)</Text> - The agent executing tasks
        </ListItem>
        <ListItem>
          <Text color="secondary">OTHER DEVS (Team)</Text> - Teammates using/maintaining skills
        </ListItem>
      </UnorderedList>
      <Text fontSize="h3" margin="60px 0 30px 0" color="primary">
        Why SKILL_CREATION_PRINCIPLES?
      </Text>
      <Text fontSize="text">
        A "linter for skills" that helps all three audiences:
      </Text>
      <UnorderedList fontSize="text" margin="20px 0 0 0">
        <ListItem>Ensures clarity for YOU when designing</ListItem>
        <ListItem>Provides structure for CLAUDE to execute</ListItem>
        <ListItem>Maintains consistency for OTHER DEVS to understand</ListItem>
      </UnorderedList>
    </Slide>
  );
}
