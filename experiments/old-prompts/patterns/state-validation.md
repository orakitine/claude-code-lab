# State Validation Pattern

## Purpose
Validates task states and manages state transitions across the workflow pipeline.

## Usage
Include this pattern with expected state parameter: `@.claude/patterns/state-validation.md`

Replace `$EXPECTED_STATE` with target state: `toRefine`, `toImplement`, `toReview`, or `done`

## Validation Logic

1. **Current state validation**:
   - Extract state from filename: `[currentState]`
   - Compare with `$EXPECTED_STATE`
   - Validate against workflow progression rules

2. **State transition rules**:
   - `toRefine` → `toImplement` ✅ (refinement complete)
   - `toImplement` → `toReview` ✅ (implementation complete)  
   - `toReview` → `done` ✅ (review approved)
   - **Invalid transitions**: Provide guidance on proper sequence

3. **State-specific actions**:

   **If state matches expected**:
   - Proceed with command execution
   - Prepare for next state transition

   **If state is ahead** (already processed):
   - `toRefine` command on `[toImplement]`: Offer to re-refine or skip
   - `toImplement` command on `[toReview]`: Warn already coded, offer review
   - `toRefine/toImplement` on `[done]`: Warn complete, offer to reopen

   **If state is behind** (prerequisites missing):
   - `toImplement` command on `[toRefine]`: Error - requires refinement first
   - `toReview` command on `[toRefine]`: Error - requires implementation first
   - Suggest running prerequisite commands

4. **State transition preparation**:
   - Plan filename rename for successful completion
   - Create backup of current state file
   - Document transition for rollback if needed

## State Workflow Reference
```
[toRefine] → [toImplement] → [toReview] → [done]
    ↑             ↑             ↑           ↑
 define-task   refine-task  implement-task  review-task
```

## Error Handling
- **Multiple files same state**: List options for selection
- **State parsing failure**: Manual state entry option
- **Missing prerequisite**: Clear guidance on required steps
- **File system errors**: Fallback to manual file selection