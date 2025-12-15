# Task Specification: Create Spectacle-Based React Slideshow App

## Metadata

- **Task ID**: TASK-001 (feat)
- **State**: [toImplement]
- **Created**: 2025-12-15
- **Refined**: 2025-12-15
- **Priority**: HIGH
- **Estimated Complexity**: LOW-MEDIUM (simplified after refinement)
- **Framework**: React (Vite + Spectacle)

## Current State Analysis

### Existing Implementation

*What currently exists in the codebase related to this task*

- **Current files involved**:
  - `../docs/TIPS_AND_TRICKS_SLIDES.md` - Complete slide content and structure (12 slides)
  - `../docs/TIPS_AND_TRICKS_SESSION.md` - Detailed session guide with talking points
  - `../.claude/skills/` - Skills to showcase (task-workflow, quality-gate, project-context, doc-vault, fork-terminal)
  - `../.claude/commands/` - Commands to showcase (all_skills, commit, prime, toggle-hooks)
  - `../todo-app/` - Example Next.js project with TASK-001 completed workflow
- **Current functionality**: Documentation exists but no interactive presentation tool
- **Current structure**: Markdown-based slide outline with visual design notes
- **Existing patterns used**: Claude purple theme (#8B5CF6), code syntax highlighting, directory trees

### Gap Analysis

*Comparison between current state and desired state*

- **What works well**:
  - Complete slide content already written and structured
  - Clear visual design guidelines (colors, typography, layout)
  - Real examples from working skills and commands
  - Well-organized 12-slide progression

- **What needs improvement**:
  - Content is static markdown, not interactive presentation
  - No way to present slides in professional format
  - Code examples not syntax-highlighted in presentation
  - No keyboard navigation for live presentation

- **What's missing**:
  - React application infrastructure (Vite setup)
  - Spectacle integration for presentation framework
  - Tailwind CSS configuration with Claude purple theme
  - Slide components implementing the 12 slides
  - Code syntax highlighting for live demos
  - Keyboard navigation (arrow keys, spacebar)
  - Progress indicator
  - Presentation mode features

- **Technical debt**: N/A (greenfield project)

## Overview

### Description

Create a professional, interactive slideshow application using React and Spectacle for presenting Claude Code tips and tricks to coworkers. The app will implement 12 slides covering the journey from basic commands to advanced task-workflow skill, with code syntax highlighting, keyboard navigation, and Claude purple theme branding. Content is based on existing TIPS_AND_TRICKS_SLIDES.md documentation.

### User Story

As a presenter sharing Claude Code knowledge with coworkers, I want an interactive slideshow application so that I can deliver a professional 20-25 minute tips and tricks session with live code examples, smooth navigation, and engaging visuals.

### Business Value

*Why this task matters to users or the business*

- **Problem solved**: No interactive way to present Claude Code patterns to team
- **User benefit**: Professional presentation tool for knowledge sharing sessions
- **Business impact**: Faster team onboarding, shared Claude Code patterns, community building

## Technical Requirements

### Must Have

*Core requirements that define task completion*

- React application created with Vite
- Spectacle library integrated for presentation framework
- Tailwind CSS configured with Claude purple theme (#8B5CF6)
- All 12 slides implemented based on TIPS_AND_TRICKS_SLIDES.md:
  1. Title slide with journey theme
  2. .claude primer (directory structure)
  3. When to use what (decision table)
  4. Level 1 - Simple commands collection
  5. Level 2 - Skills collection (with power pair)
  6. Level 3 - Advanced task-workflow structure
  7. SKILL_CREATION_PRINCIPLES (the secret weapon)
  8. Task lifecycle flowchart
  9. TASK-001 result showcase
  10. Interactive questions (Your Turn)
  11. Repository resources
  12. Final question and next steps
- Code syntax highlighting for markdown/bash/typescript examples
- Keyboard navigation (arrow keys, spacebar, home, end)
- Progress indicator showing current slide position
- Responsive design (works on laptop presentation screen)

### Should Have

*Important enhancements that add significant value*

- ✅ **Fade transitions** (decided: use fade for smooth, professional flow)
- Dark theme with purple accents throughout
- Slide numbers display (1/12 format)
- Print-to-PDF capability for handouts (if Spectacle supports it easily)

### Could Have

*Nice-to-have features if time permits*

- Timer/elapsed time display
- Presenter mode with next slide preview
- Fullscreen mode toggle

### Won't Have (Refined)

*Explicitly out of scope based on refinement decisions*

- ❌ **QR code on resources slide** (decided: clickable link sufficient)
- ❌ **Speaker notes view** (decided: skip for MVP)
- ❌ **Tailwind CSS** (decided: Spectacle theme only)
- ❌ **Deployment infrastructure** (decided: local dev only)

### Won't Have

*Explicitly out of scope to set clear boundaries*

- Real-time collaboration features
- Slide editing within app
- Video/animation embedding
- Live polling or audience interaction
- Multi-language support
- Authentication or user accounts

## Implementation Approach

### Files to Modify

*Existing files that need changes*

- None (greenfield project in new slide-deck directory)

### Files to Create

*New files to add*

Project structure:
```
slide-deck/
├── package.json                    # Vite + React + Spectacle
├── vite.config.ts                  # Vite configuration
├── tsconfig.json                   # TypeScript config
├── index.html                      # Entry HTML
├── src/
│   ├── main.tsx                    # App entry point
│   ├── App.tsx                     # Main Spectacle deck component
│   ├── slides/
│   │   ├── Slide01Title.tsx        # Title slide
│   │   ├── Slide02ClaudePrimer.tsx # .claude structure (ASCII tree in <pre>)
│   │   ├── Slide03WhenToUse.tsx    # Decision table
│   │   ├── Slide04Commands.tsx     # Commands collection
│   │   ├── Slide05Skills.tsx       # Skills collection (with power pair)
│   │   ├── Slide06Advanced.tsx     # task-workflow structure (ASCII tree in <pre>)
│   │   ├── Slide07Principles.tsx   # SKILL_CREATION_PRINCIPLES
│   │   ├── Slide08Lifecycle.tsx    # Task lifecycle (simple flowchart)
│   │   ├── Slide09Result.tsx       # TASK-001 showcase
│   │   ├── Slide10YourTurn.tsx     # Interactive questions
│   │   ├── Slide11Resources.tsx    # Repo link (clickable, no QR code)
│   │   └── Slide12Final.tsx        # Final question
│   └── theme/
│       └── spectacleTheme.ts       # Spectacle theme with purple (#8B5CF6)
└── README.md                       # Setup and usage instructions
```

### Architecture Changes

*Structural or design pattern changes*

- **Component-based architecture**: Each slide as separate React component
- **Spectacle Deck pattern**: Main App wraps slides in Spectacle Deck
- **Theme system**: Spectacle theme configured with Claude purple (#8B5CF6) - no Tailwind needed
- **Code highlighting**: Spectacle's built-in `CodePane` component for all code examples
- **Directory trees**: Simple monospace `<pre>` blocks with ASCII tree characters
- **Slide transitions**: Fade transitions for smooth, professional flow
- **Navigation**: Spectacle's built-in keyboard navigation (arrows, spacebar, home, end)
- **Deployment**: Local development only (`npm run dev`), no deployment infrastructure

### Integration Points

*How this connects to existing systems*

- **Content source**: TIPS_AND_TRICKS_SLIDES.md provides slide content
- **Code examples**: References to actual skills/commands in ../.claude/
- **Real examples**: Links to ../todo-app/tasks/TASK-001 for live demo
- **Repository link**: https://github.com/orakitine/claude-code-lab
- **No backend**: Fully static frontend application

## Dependencies

### Internal Dependencies

*Other parts of codebase this relies on*

- `../docs/TIPS_AND_TRICKS_SLIDES.md` - Content source
- `../.claude/skills/` - Skills to showcase
- `../.claude/commands/` - Commands to showcase
- `../todo-app/tasks/TASK-001` - Real workflow example

### External Dependencies

*Third-party libraries or services needed*

- **spectacle** (^11.0.0) - Presentation framework (includes built-in CodePane for syntax highlighting)
- **react** (^18.0.0) - UI library
- **react-dom** (^18.0.0) - React DOM rendering
- **vite** (^5.0.0) - Build tool and dev server
- **typescript** (~5.9.0) - Type safety

**Note:** Tailwind CSS not needed - using Spectacle's theming system configured with purple colors (#8B5CF6)

### Blocking Dependencies

*Must be completed before this task*

- None (independent greenfield project)

## Acceptance Criteria

*Testable conditions that define "done"*

- [ ] Vite + React + TypeScript project successfully initialized
- [ ] Spectacle library integrated and basic deck renders
- [ ] Tailwind CSS configured with Claude purple (#8B5CF6) primary color
- [ ] All 12 slides implemented with content from TIPS_AND_TRICKS_SLIDES.md
- [ ] Code syntax highlighting works for bash/typescript/markdown examples
- [ ] Keyboard navigation functional (arrow keys advance/go back, spacebar advances)
- [ ] Directory tree visualizations render correctly (Slide 2, 6)
- [ ] Decision table displays properly (Slide 3)
- [ ] Command/skill collections formatted clearly (Slides 4-5)
- [ ] Power pair diagram visible (Slide 5)
- [ ] Task lifecycle flowchart readable (Slide 8)
- [ ] Progress indicator shows current slide number (e.g., "3/12")
- [ ] Responsive layout works on 1920x1080 and 1366x768 screens
- [ ] npm run dev starts development server successfully
- [ ] npm run build creates production bundle without errors
- [ ] Presentation flows smoothly through all slides in order
- [ ] Professional appearance matches visual design notes
- [ ] README.md includes setup and usage instructions

## Testing Strategy

### Unit Tests

*Component-level testing approach*

- Test individual slide components render without errors
- Verify CodeBlock component highlights syntax correctly
- Confirm DirectoryTree component renders tree structure
- Validate theme configuration applies purple colors

### Integration Tests

*System-level testing approach*

- Test full deck navigation (forward/backward through all slides)
- Verify keyboard shortcuts work across all slides
- Confirm slide transitions are smooth
- Test that code examples display correctly in presentation

### Manual Testing

*User-facing testing checklist*

- [ ] Run presentation end-to-end on laptop screen
- [ ] Test keyboard navigation (arrows, spacebar, home, end)
- [ ] Verify all code examples are readable and properly highlighted
- [ ] Check purple theme consistency across all slides
- [ ] Confirm directory trees and diagrams render correctly
- [ ] Test on different screen resolutions (1920x1080, 1366x768)
- [ ] Verify presentation timing (should support 20-25 min session)
- [ ] Check that slide content matches TIPS_AND_TRICKS_SLIDES.md

### Regression Testing

*Ensure existing functionality still works*

- N/A (new project, no existing functionality)

## Migration Strategy

*How to transition from current to new state without breaking things*

- **Step 1**: Create slide-deck directory and initialize Vite project
- **Step 2**: Install Spectacle and create basic 1-slide deck (proof of concept)
- **Step 3**: Configure Tailwind with purple theme
- **Step 4**: Implement slides incrementally (1-3 at a time)
- **Step 5**: Add code highlighting and visual components
- **Step 6**: Polish transitions, navigation, and styling
- **Rollback plan**: Keep TIPS_AND_TRICKS_SLIDES.md as fallback (can present from markdown if app breaks)

## Potential Challenges

*Known risks and mitigation strategies*

- **Challenge 1**: Spectacle learning curve (unfamiliar library) → **Mitigation**: Review Spectacle docs and examples first, start with simple slides
- **Challenge 2**: Code syntax highlighting performance → **Mitigation**: Use Spectacle's built-in CodePane if available, or lightweight highlighter
- **Challenge 3**: Directory tree visualization complexity → **Mitigation**: Use simple monospace pre-formatted text initially, enhance with ASCII art or component later
- **Challenge 4**: Responsive layout for different screens → **Mitigation**: Use Spectacle's built-in responsive features, test early on target screens
- **Challenge 5**: Balancing content density vs readability → **Mitigation**: Follow visual design notes (minimal text, large fonts)

## Performance Considerations

*Impact on speed, memory, or resources*

- **Expected impact**: Lightweight React SPA, should load quickly
- **Optimization opportunities**:
  - Code-split slides (lazy load)
  - Optimize images if used
  - Minify production bundle
- **Monitoring needs**: Build size should stay under 500KB for fast loading

## Security Considerations

*Security implications and safeguards*

- **Data sensitivity**: No sensitive data (public presentation)
- **Authentication/Authorization**: None needed (static site)
- **Input validation**: N/A (no user input)
- **Vulnerability risks**: Minimal (no backend, no user data, standard React dependencies)

## Accessibility Considerations

*Ensuring usability for all users*

- **Keyboard navigation**: Full keyboard support via Spectacle (arrows, spacebar)
- **Screen reader support**: Use semantic HTML in slide content, ARIA labels where needed
- **Color contrast**: Ensure purple theme maintains WCAG AA contrast ratios for text
- **Focus management**: Spectacle handles focus management for slides

## Documentation Needs

*What documentation must be updated or created*

- [ ] **README.md**: Setup instructions (npm install, npm run dev, npm run build)
- [ ] **README.md**: Usage instructions (keyboard shortcuts, navigation)
- [ ] **README.md**: Slide content overview (what each slide covers)
- [ ] **Code comments**: Complex slide components (directory trees, flowcharts)
- [ ] **Package.json scripts**: Document available npm commands

## References

*Links to relevant documentation, designs, or related tasks*

- **Content source**: `../docs/TIPS_AND_TRICKS_SLIDES.md`
- **Session guide**: `../docs/TIPS_AND_TRICKS_SESSION.md`
- **Spectacle docs**: https://formidable.com/open-source/spectacle/
- **Spectacle GitHub**: https://github.com/FormidableLabs/spectacle
- **Tailwind docs**: https://tailwindcss.com/docs
- **Vite docs**: https://vitejs.dev/
- **Claude purple color**: #8B5CF6 (from TIPS_AND_TRICKS_SLIDES.md)
- **Presentation duration**: 20-25 minutes (from slide outline)
- **Example project**: `../todo-app/` (Next.js project with task-workflow example)

## Notes

*Additional context, decisions, or clarifications*

- This is TASK-001 for the slide-deck project (separate from todo-app's TASK-001)
- Using task-workflow skill to build this app (dogfooding!)
- Will serve as real example for Slide 8-9 (task lifecycle demonstration)
- Can be used for future presentations beyond initial tips session
- Consider deploying to GitHub Pages or Vercel for easy sharing
- Purple theme (#8B5CF6) matches Claude branding for cohesive look
- Focus on clarity and readability over fancy animations
- Slides are conversation starters, not comprehensive documentation
- Total slide count: 12 slides for 20-25 minute session

---

## Workflow State History

- [toRefine] - 2025-12-15 - Task created by define workflow
- [toImplement] - 2025-12-15 - Task refined with key decisions:
  - ✅ Code highlighting: Spectacle's built-in CodePane
  - ✅ Styling: Spectacle theme with purple (#8B5CF6), no Tailwind
  - ✅ Transitions: Fade transitions
  - ✅ Directory trees: Simple ASCII in `<pre>` blocks
  - ✅ Resources slide: Clickable link, no QR code
  - ✅ Deployment: Local development only (`npm run dev`)
  - **Result**: Simplified implementation, reduced dependencies, faster development
- [toReview] - 2025-12-15 - Task implemented successfully:
  - **Files Created**: 18 files
    - package.json, tsconfig.json, vite.config.ts, index.html
    - src/theme/spectacleTheme.ts
    - src/App.tsx (Spectacle Deck with 12 slides)
    - 12 slide components (Slide01Title.tsx through Slide12Final.tsx)
    - README.md with setup and usage instructions
  - **Dependencies Installed**: React 19, Vite 7, TypeScript 5.9, Spectacle 10
  - **Build Status**: ✅ Successful (dist: 1.5MB, includes Spectacle framework)
  - **Implementation Notes**:
    - Used Spectacle v10.1.8 (v11 not available)
    - Removed Tailwind CSS (not needed with Spectacle theme)
    - CodePane component doesn't support `fontSize` or custom `theme` props
    - Deck component doesn't support `transition="fade"` (uses default transitions)
    - All 12 slides implemented with content from TIPS_AND_TRICKS_SLIDES.md
    - Purple theme (#8B5CF6) configured in spectacleTheme.ts
    - Build produces single-bundle SPA (1.5MB due to Spectacle dependencies)
  - **Complexity Assessment**: Actual complexity was **LOW** (simpler than estimated)
  - **All Acceptance Criteria**: Ready for manual validation
