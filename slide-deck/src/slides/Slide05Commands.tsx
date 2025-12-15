import { Slide, Heading, Text, CodePane, UnorderedList, ListItem } from 'spectacle';

export function Slide05Commands() {
  const commitExample = `# Variables: COMMIT_MESSAGE
# Workflow:
- Review changes
- Write appropriate message
- Commit the code`;

  return (
    <Slide>
      <Heading fontSize="h2" color="primary" margin="0 0 30px 0">
        Level 1: Simple Commands
      </Heading>
      <Text fontSize="text" color="secondary" margin="0 0 30px 0">
        Where I Started: Just Shortcuts
      </Text>
      <UnorderedList fontSize="text">
        <ListItem>/all_skills - List available skills</ListItem>
        <ListItem>/commit - Smart git commits (with optional message)</ListItem>
        <ListItem>/prime - Understand codebase (pairs with project-context!)</ListItem>
        <ListItem>/toggle-hooks - Enable/disable hooks</ListItem>
      </UnorderedList>
      <Text fontSize="text" margin="30px 0 20px 0" color="secondary">
        Example: /commit
      </Text>
      <CodePane language="markdown">
        {commitExample}
      </CodePane>
    </Slide>
  );
}
