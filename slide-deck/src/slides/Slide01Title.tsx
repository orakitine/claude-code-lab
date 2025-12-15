import { Slide, Heading, Text, FlexBox } from 'spectacle';

export function Slide01Title() {
  return (
    <Slide>
      <FlexBox height="100%" flexDirection="column" justifyContent="center" alignItems="center">
        <Heading fontSize="h1" color="primary">
          Claude Code Tips & Tricks
        </Heading>
        <Heading fontSize="h2" color="secondary" margin="40px 0 0 0">
          My Journey from Commands to Universal Task Workflows
        </Heading>
        <Text fontSize="text" margin="60px 0 0 0">
          What I learned in 2 weeks of deep diving
        </Text>
        <Text fontSize="text" margin="20px 0 0 0" color="secondary">
          And what I want to learn from YOU
        </Text>
        <Text fontSize="text" margin="60px 0 0 0" color="tertiary">
          github.com/orakitine/claude-code-lab
        </Text>
      </FlexBox>
    </Slide>
  );
}
