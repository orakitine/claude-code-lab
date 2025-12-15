import { Deck, Progress, FullScreen } from 'spectacle';
import { theme } from './theme/spectacleTheme';

// Import all slide components
import { Slide01Title } from './slides/Slide01Title';
import { Slide02ThreeAudiences } from './slides/Slide02ThreeAudiences';
import { Slide03ClaudePrimer } from './slides/Slide03ClaudePrimer';
import { Slide04WhenToUse } from './slides/Slide04WhenToUse';
import { Slide05Commands } from './slides/Slide05Commands';
import { Slide06Skills } from './slides/Slide06Skills';
import { Slide07Advanced } from './slides/Slide07Advanced';
import { Slide08Principles } from './slides/Slide08Principles';
import { Slide09Lifecycle } from './slides/Slide09Lifecycle';
import { Slide10Result } from './slides/Slide10Result';
import { Slide11YourTurn } from './slides/Slide11YourTurn';
import { Slide12Resources } from './slides/Slide12Resources';
import { Slide13Final } from './slides/Slide13Final';

function App() {
  return (
    <Deck theme={theme}>
      <Slide01Title />
      <Slide02ThreeAudiences />
      <Slide03ClaudePrimer />
      <Slide04WhenToUse />
      <Slide05Commands />
      <Slide06Skills />
      <Slide07Advanced />
      <Slide08Principles />
      <Slide09Lifecycle />
      <Slide10Result />
      <Slide11YourTurn />
      <Slide12Resources />
      <Slide13Final />

      {/* Slide controls */}
      <FullScreen />
      <Progress color="#8B5CF6" />
    </Deck>
  );
}

export default App;
