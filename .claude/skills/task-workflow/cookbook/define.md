# Define Task Workflow

Create comprehensive task specifications with intelligent codebase analysis and structured documentation.

## Workflow

1. **Generate Task ID**

   - Tool: Glob to scan TASK_DIR for existing task files
   - Find highest task number with pattern: `{TASK_ID_PREFIX}-*`
   - Increment by 1 and zero-pad to TASK_ID_PADDING digits
   - Example: Existing TASK-005 found → Generate TASK-006 (with padding=3)

2. **Analyze Task Description**

   - Parse user's task description for key information
   - Extract primary goal, domain area, and work type
   - Identify relevant keywords (authentication, modal, API, bug, design, etc.)
   - Example: "add user authentication" → Goal: add, Domain: user management, Type: feature

3. **Determine Task Category**

   - Map task description to conventional commit category
   - IF: "add", "create", "new" → Category: feat
   - IF: "fix", "bug", "error", "issue", "repair" → Category: fix
   - IF: "design", "style", "theme", "UI", "UX", "color" → Category: design
   - IF: "refactor", "restructure", "clean", "improve code" → Category: refactor
   - IF: "test", "testing", "coverage" → Category: test
   - IF: "docs", "documentation", "readme" → Category: docs
   - IF: "optimize", "performance", "speed" → Category: perf
   - ELSE: Category: chore
   - Example: "add user authentication" → Category: feat

4. **Generate Task Slug**

   - Convert task description to lowercase kebab-case
   - Remove special characters, keep letters/numbers/hyphens
   - Limit to reasonable length (max 60 characters)
   - Example: "Add User Authentication with JWT" → slug: "add-user-authentication-with-jwt"

5. **Analyze Existing Codebase**

   - Tool: Glob to find relevant existing files based on task domain
   - IF: UI/component task → Check src/components/, src/app/
   - IF: API/backend task → Check src/lib/, src/api/, backend/
   - IF: Styling task → Check stylesheets, theme files
   - IF: Test task → Check test directories
   - Tool: Read relevant files to understand current implementation
   - Example: Authentication task → Read src/app/login, src/lib/auth files

6. **Identify Dependencies and Integration Points**

   - Analyze which existing systems will be affected
   - Check for: database schemas, API endpoints, components, utilities
   - Determine what needs modification vs creation
   - Identify potential conflicts or breaking changes
   - Example: Auth task → Affects: login component, API routes, session management, database user table

7. **Create Task Specification**

   - Tool: Use templates/task-template.md as base structure
   - Fill in all sections with analyzed information:
     - Task ID: {TASK_ID_PREFIX}-{id} ({category})
     - Current State Analysis (from codebase analysis)
     - Gap Analysis (what exists vs what's needed)
     - Technical Requirements (based on findings)
     - Implementation Approach (files to modify/create)
     - Integration Points (connections to existing systems)
     - Acceptance Criteria (testable, specific)
     - Testing Strategy (appropriate for change type)
   - Example: Complete TASK-006 spec with all sections populated

8. **Generate Filename**

   - Format: {TASK_ID_PREFIX}-{id} [{STATE_INITIAL}] ({category}): {slug}.md
   - Use Variables: TASK_ID_PREFIX, STATE_INITIAL from SKILL.md
   - Example: TASK-006 [toRefine] (feat): add-user-authentication-with-jwt.md

9. **Save Task File**

   - Tool: Write task specification to TASK_DIR with generated filename
   - Ensure TASK_DIR exists (create if needed)
   - Full path: {TASK_DIR}/{filename}
   - Example: Write to ./tasks/TASK-006 [toRefine] (feat): add-user-authentication-with-jwt.md

10. **Confirm Creation**

    - Display task summary: ID, category, state, filename
    - Show file location and size
    - List key sections included in specification
    - Provide next step guidance: "Run refine workflow to clarify requirements"
    - Example: "✓ Created TASK-006 in ./tasks/ (4.2 KB). State: toRefine. Next: Run refine workflow to interview for requirements."

## Task Discovery Pattern

When user provides partial task identifier:

1. **Parse Input**
   - Full ID: TASK-006 → Direct match
   - Short ID: 6, 006 → Expand to TASK-006
   - Keywords: auth, login → Search filenames
   - Category: (feat), feat → Filter by category
   - Special: "latest" → Most recently created

2. **Search TASK_DIR**
   - Tool: Glob with pattern matching
   - Match filename components: ID, state, category, slug
   - Rank matches by relevance (exact > partial > fuzzy)
   - Example: "auth" finds TASK-006 [toRefine] (feat): add-user-authentication-with-jwt.md

3. **Handle Results**
   - IF: Single match → Auto-select and proceed
   - IF: Multiple matches → Display numbered list with details, prompt user selection
   - IF: No matches → Suggest similar tasks, check for typos, list available tasks
   - Example: 3 matches found → Show list "1. TASK-006 (feat) 2. TASK-012 (fix) 3. TASK-015 (design)"

4. **Validate Selection**
   - Confirm task exists and is readable
   - Extract state from filename
   - Verify state matches expected workflow phase
   - Example: Selected TASK-006, confirmed state [toRefine], ready for refine workflow

## State Transition Rules

Task states follow strict workflow progression:

```
[toRefine] → [toImplement] → [toReview] → [done]
    ↑             ↑               ↑          ↑
  define        refine         implement   review
```

**Valid transitions:**
- Define workflow → Creates [toRefine] state (initial)
- Refine workflow → Transitions [toRefine] to [toImplement]
- Implement workflow → Transitions [toImplement] to [toReview]
- Review workflow → Transitions [toReview] to [done]

**Invalid transitions:**
- Cannot skip states (e.g., [toRefine] directly to [done])
- Cannot go backwards (unless explicitly requested for rework)
- Must complete current phase before advancing

**Example:**
- Task created with define → TASK-006 [toRefine]
- Cannot implement until refined → Must run refine workflow first
- After refine → TASK-006 [toImplement] → Ready for implement workflow
