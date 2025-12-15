import { Slide, Heading, Text, UnorderedList, ListItem } from 'spectacle';

export function Slide13Final() {
  return (
    <Slide>
      <Heading fontSize="h2" color="primary" margin="0 0 60px 0">
        What's the ONE workflow you wish Claude Code could automate for you?
      </Heading>
      <Text fontSize="text" margin="60px 0 40px 0" color="secondary">
        Next steps:
      </Text>
      <UnorderedList fontSize="text">
        <ListItem>Share session notes</ListItem>
        <ListItem>Create team channel for sharing</ListItem>
        <ListItem>Build requested skills together</ListItem>
      </UnorderedList>
    </Slide>
  );
}
