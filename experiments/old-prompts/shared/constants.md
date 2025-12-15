# Shared Command Constants

## File Patterns
- **Task Directory**: `/tasks/`
- **Task Filename Format**: `BROOKLY-### [state] (category): task-name.md`
- **State Indicators**: `[toRefine]`, `[toImplement]`, `[toReview]`, `[done]`

## State Workflow
```
[toRefine] → [toImplement] → [toReview] → [done]
    ↑             ↑             ↑           ↑
 define-task   refine-task  implement-task  review-task
```

## State Definitions
- **toRefine**: Task created but needs requirements clarification
- **toImplement**: Requirements refined and ready for coding
- **toReview**: Implementation complete, needs code review
- **done**: Fully complete and approved

## Category Classifications
Common categories that map to conventional commit types:
- `(feat)` - New features
- `(fix)` - Bug fixes  
- `(design)` - UI/UX changes
- `(refactor)` - Code restructuring
- `(docs)` - Documentation updates
- `(test)` - Testing improvements
- `(chore)` - Maintenance tasks

## Quality Gates
Standard checks for implementation and review commands:
```bash
npm run lint      # Code style validation
npm run typecheck # TypeScript validation  
npm run build     # Build verification
npm run test      # Test suite execution
```

## Common Response Templates

### Task Selection Menu
```
Found multiple matching tasks:
1. BROOKLY-006 [toRefine] (design): implement-new-color-theme.md
2. BROOKLY-007 [toRefine] (feat): add-user-authentication.md
3. BROOKLY-008 [toImplement] (fix): resolve-mobile-layout-issue.md

Please select (1-3) or type 'cancel':
```

### State Transition Confirmation
```
✅ Task ready for next stage:
   Current: BROOKLY-006 [currentState] (category): task-name.md
   Next: BROOKLY-006 [nextState] (category): task-name.md

Proceeding with [command-action]...
```

### Error Messages
```
❌ Invalid state transition:
   Task is currently [currentState] but expected [expectedState]
   Run '/prerequisite-command BROOKLY-006' first.
```

## Alternative Command Phrases
Patterns for natural language command triggers:
- **Define**: "Let's create", "New task", "Define task"
- **Refine**: "Let's refine", "Interview for", "Clarify requirements"
- **Implement**: "Let's code", "Build this", "Implement task"
- **Review**: "Let's review", "Check the code", "Review implementation"