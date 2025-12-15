# Claude Code Tips & Tricks - Slideshow

Interactive presentation built with React and Spectacle for sharing Claude Code knowledge with coworkers.

## Setup

```bash
npm install
```

## Usage

### Development

```bash
npm run dev
```

Open your browser to the URL shown (typically http://localhost:5173)

### Build

```bash
npm run build
```

Creates optimized production bundle in `dist/` directory.

### Preview Production Build

```bash
npm run preview
```

## Keyboard Navigation

- **Arrow Keys**: Navigate between slides (← → or ↑ ↓)
- **Space**: Advance to next slide
- **Home**: Go to first slide
- **End**: Go to last slide
- **F**: Toggle fullscreen mode

## Slide Content

The presentation contains 12 slides covering:

1. **Title Slide** - Introduction and journey theme
2. **.claude Primer** - Directory structure overview
3. **When to Use What** - Decision table for Commands/Skills/Tools
4. **Level 1: Commands** - Simple command shortcuts (/commit, /prime, etc.)
5. **Level 2: Skills** - Multi-step workflows and the "power pair"
6. **Level 3: Advanced** - Framework-aware task-workflow structure
7. **SKILL_CREATION_PRINCIPLES** - The "linter for skills"
8. **Task Lifecycle** - task-workflow in action
9. **Results** - TASK-001 completion showcase
10. **Your Turn** - Interactive questions for the audience
11. **Resources** - Repository link and what's inside
12. **Final Question** - Open discussion and next steps

## Tech Stack

- **React 19** - UI library
- **Vite 7** - Build tool and dev server
- **TypeScript** - Type safety
- **Spectacle 10** - Presentation framework
  - Built-in CodePane for syntax highlighting
  - Keyboard navigation
  - Progress indicator
  - Fullscreen mode

## Theme

- **Primary**: #8B5CF6 (Claude purple)
- **Secondary**: #A78BFA (Light purple)
- **Background**: #1a1a1a (Dark)
- **Text**: #f5f5f5 (Light)

## Notes

- Presentation designed for 20-25 minute session
- Code examples use Spectacle's built-in syntax highlighting
- Directory trees displayed as ASCII in monospace font
- No deployment infrastructure (local development only)
