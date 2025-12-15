# Refine Task Workflow

Conduct systematic requirements interviews to clarify specifications and prepare tasks for implementation.

## Workflow

1. **Discover and Load Task**

   - Use task discovery pattern to find target task file
   - Tool: Glob to search TASK_DIR with user's identifier
   - Support formats: full ID (TASK-006), short ID (6, 006), keywords (auth), category (feat)
   - Example: User says "refine 006" → Find TASK-006 [toRefine] (feat): add-user-authentication-with-jwt.md

2. **Validate Task State**

   - Tool: Read task file and extract [state] from filename
   - Verify state is [toRefine] (expected for refine workflow)
   - IF: state is [toRefine] → Proceed with refinement
   - IF: state is [toImplement] → Warn "Already refined, offer to re-refine or skip"
   - IF: state is [toReview] or [done] → Warn "Already past refinement stage"
   - Example: TASK-006 [toRefine] found → State valid, proceed

3. **Analyze Specification Completeness**

   - Tool: Read entire task specification file
   - Parse all sections: Overview, Requirements, Implementation, Acceptance Criteria, Testing
   - Identify gaps, ambiguities, and missing information
   - Categorize issues by severity: Critical (blocks implementation), Important (affects quality), Nice-to-have (optional clarifications)
   - Example: Found 3 critical gaps (authentication method unclear, storage undefined, error handling missing), 2 important (UI design vague, performance targets not set)

4. **Prioritize Questions**

   - Order questions by implementation impact: Critical → Important → Optional
   - Group related questions together (all auth questions, all UI questions)
   - Estimate question count and inform user
   - Example: "I have 8 questions about this task. 3 are critical for implementation, 5 are important for quality. Let's go through them systematically."

5. **Conduct Systematic Interview**

   - Present questions ONE at a time to avoid overwhelming user
   - For each question:
     - Explain WHY the question is important
     - Provide context from current specification
     - Suggest options if applicable
     - Show progress: "Question X of Y"
     - Allow user to skip non-critical questions
   - Tool: Write answers directly into task specification as received
   - Example: "Question 1 of 8 (Critical): Which authentication method should we use? This affects the entire security architecture. Options: JWT tokens (stateless), Session cookies (stateful), OAuth (third-party). Why it matters: [explanation]"

6. **Update Specification**

   - Tool: Edit task file to incorporate answers
   - Update relevant sections: Technical Requirements, Implementation Approach, Acceptance Criteria
   - Add new sections if answers reveal additional considerations
   - Ensure consistency across all sections (if auth method changed, update related sections)
   - Example: User chose JWT → Update: Technical Requirements (add JWT lib), Implementation (add token generation/validation), Testing (add token expiry tests)

7. **Validate Completeness**

   - After all questions answered, review entire specification
   - Check that: All Must Have requirements are clear, Implementation approach is actionable, Acceptance criteria are testable, Dependencies are identified
   - IF: Still has critical gaps → Generate follow-up questions
   - IF: Complete → Confirm readiness for implementation
   - Example: All sections complete, no blockers, ready to transition

8. **Generate Transition Summary**

   - Compile list of all clarifications made
   - Highlight key decisions and their implications
   - Identify any risks or challenges uncovered during refinement
   - Estimate implementation complexity (LOW/MEDIUM/HIGH) based on refined understanding
   - Example: "Clarified 8 points: Auth method (JWT), Storage (PostgreSQL), Error handling (custom middleware). Complexity: MEDIUM. Risk: Token refresh complexity."

9. **Transition State**

   - Tool: Rename file from [toRefine] to [toImplement]
   - Old: TASK-006 [toRefine] (feat): add-user-authentication-with-jwt.md
   - New: TASK-006 [toImplement] (feat): add-user-authentication-with-jwt.md
   - Example: mv "./tasks/TASK-006 [toRefine] (feat): add-user-authentication-with-jwt.md" "./tasks/TASK-006 [toImplement] (feat): add-user-authentication-with-jwt.md"

10. **Confirm Next Steps**

    - Display updated task summary with new state
    - Show file location and updated size
    - Provide guidance: "Task ready for implementation. Run implement workflow when ready to code."
    - Example: "✓ TASK-006 refined and ready. State: [toImplement]. File: ./tasks/TASK-006 [toImplement] (feat): add-user-authentication-with-jwt.md (6.8 KB). Next: Run implement workflow."

## Question Categories

Questions organized by priority and type:

### Critical (Must answer before implementation)

- **Technical decisions**: Core architectural choices, framework selections, API designs
- **Integration requirements**: How this connects to existing systems, dependencies
- **Data models**: Database schemas, data structures, storage requirements
- **Security requirements**: Authentication, authorization, data protection
- **Example**: "Which database will store user credentials? This determines our ORM choice and migration strategy."

### Important (Affects quality and maintainability)

- **User experience**: UI/UX expectations, interaction patterns, accessibility
- **Performance targets**: Response times, load capacity, optimization goals
- **Error handling**: Expected error scenarios, user feedback, recovery strategies
- **Testing approach**: Coverage requirements, testing tools, CI/CD integration
- **Example**: "What should happen if login fails 3 times? Lock account? Show CAPTCHA? This affects both UX and security."

### Nice-to-have (Optional enhancements)

- **Future extensibility**: Potential future features, scalability considerations
- **Advanced features**: Optional enhancements, power-user capabilities
- **Documentation preferences**: Code comment style, API doc format
- **Example**: "Should we support social login (Google, GitHub) in addition to email/password? Nice to have but not required for MVP."

## Interactive Features

Enhance user experience during refinement:

1. **Progress Tracking**
   - Show current question number and total
   - Display category (Critical/Important/Nice-to-have)
   - Visual progress: "█████░░░░░ 50% (5/10 questions)"
   - Example: "Question 5 of 10 (Important) - 50% complete"

2. **Skip Options**
   - Allow skipping Nice-to-have questions: "Type 'skip' to defer this question"
   - Defer to later: "We can revisit this during implementation if needed"
   - Mark deferred items in spec for follow-up
   - Example: User skips social login question → Add note in spec: "TODO: Decide on social login during implementation"

3. **Context Preservation**
   - Reference previous answers when relevant
   - Show how current question relates to earlier decisions
   - Maintain consistency across related questions
   - Example: "Earlier you chose JWT for auth. This question is about JWT token expiry duration..."

4. **Answer Validation**
   - Check if answers make sense in context
   - Flag potential conflicts with previous answers
   - Suggest implications of choices
   - Example: User chooses "Store passwords in plain text" → "⚠️ Security risk! Strongly recommend bcrypt hashing instead."

## State Validation

Ensure proper workflow progression:

**Valid state: [toRefine]**
- Task is in correct state for refinement
- Proceed with interview process
- Example: TASK-006 [toRefine] → Refinement proceeds normally

**Invalid state: [toImplement]**
- Task already refined
- Options: Re-refine (update existing answers), Skip (move to implement), Cancel
- Example: TASK-006 [toImplement] → "This task was already refined. Re-refine to update requirements?"

**Invalid state: [toReview] or [done]**
- Task is past refinement stage
- Inform user and suggest appropriate action
- Example: TASK-006 [toReview] → "This task is under review. Cannot refine after implementation. Create new task if requirements changed."

## Error Handling

Handle common issues gracefully:

**Task not found**
- Search TASK_DIR for similar tasks
- Suggest available tasks in toRefine state
- Offer to list all tasks
- Example: "TASK-007 not found. Did you mean TASK-006? Available tasks in toRefine state: TASK-006, TASK-009, TASK-012"

**Multiple matches**
- Display numbered list with task details: ID, state, category, title
- Prompt user to select by number
- Show last modified date to help decision
- Example: "3 tasks match 'auth': 1. TASK-006 [toRefine] (feat): add-auth | 2. TASK-009 [toImplement] (fix): fix-auth-bug | Select 1-3:"

**File read/write errors**
- Check TASK_DIR exists and is writable
- Verify file permissions
- Suggest fixes: create directory, check permissions
- Example: "Cannot write to ./tasks/. Directory doesn't exist. Create it? (yes/no)"

**Specification parse errors**
- Attempt to load file despite format issues
- Note sections that couldn't be parsed
- Proceed with refinement where possible
- Example: "⚠️ Specification format irregular, but proceeding with refinement. Some sections may need manual cleanup."
