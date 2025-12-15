import { Slide, Heading, OrderedList, ListItem } from 'spectacle';

export function Slide11YourTurn() {
  return (
    <Slide>
      <Heading fontSize="h2" color="primary" margin="0 0 60px 0">
        What Are YOU Doing?
      </Heading>
      <OrderedList fontSize="text">
        <ListItem>What commands have you created?</ListItem>
        <ListItem>What skills do you use?</ListItem>
        <ListItem>How do you structure .claude/?</ListItem>
        <ListItem>What's your approach to working with Claude?</ListItem>
        <ListItem>What workflows would you automate?</ListItem>
      </OrderedList>
    </Slide>
  );
}
