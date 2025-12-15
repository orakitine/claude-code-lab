# Example: Context Handoff in Action

## Scenario

You're working on a TypeScript project and want to:
1. Analyze code quality
2. Hand off to a specialist to fix issues

## Step-by-Step Example

### Main Session (Terminal 1)

```
You: "Analyze src/ for code quality issues"

Me (Analyzer):
"I found the following issues:

FILES ANALYZED:
- src/auth/login.ts
- src/auth/validators.ts
- src/utils/helpers.ts

ISSUES:
1. src/auth/login.ts:42 - Unused variable 'foo'
2. src/auth/validators.ts:15 - Missing return type annotation
3. src/utils/helpers.ts:23 - console.log in production code

RECOMMENDATIONS:
1. Remove unused variable
2. Add explicit return type: Promise<boolean>
3. Replace console.log with proper logger

Would you like me to fork a fixer agent to resolve these?"

You: "Yes, fork and fix them"

Me:
"Creating context handoff..."
[Generates handoff file]:

---HANDOFF FILE CONTENT---
# Code Fix Task - Context Handoff

## Analysis Summary

**Files Analyzed:**
- src/auth/login.ts (authentication logic)
- src/auth/validators.ts (input validation)
- src/utils/helpers.ts (utility functions)

**Issues Found:**
1. **src/auth/login.ts:42**
   - Type: Unused variable
   - Detail: Variable 'foo' declared but never used
   - Severity: Warning

2. **src/auth/validators.ts:15**
   - Type: Missing type annotation
   - Detail: Function validatePassword missing return type
   - Severity: Error
   - Recommended fix: Add `: Promise<boolean>`

3. **src/utils/helpers.ts:23**
   - Type: Production console.log
   - Detail: console.log should not be in production
   - Severity: Warning
   - Recommended fix: Replace with logger.debug()

**Recommended Fixes:**
- Remove unused 'foo' variable
- Add return type annotation: Promise<boolean>
- Import logger and replace console.log

## Context from Original Conversation

User asked to analyze src/ for code quality issues. This is a TypeScript
project using standard linting rules. User wants automated fixes applied.

## Your Mission

You are a code-fixing specialist. Apply all recommended fixes above.
Work methodically through each issue. Test after fixing.

## Execute Now

Begin fixing the issues listed above.
---END HANDOFF FILE---

"Forking terminal with context..."
[Runs: fork_terminal("claude --model sonnet -p \"$(cat /tmp/handoff.md)\"")]
```

### Forked Session (Terminal 2)

```
[New terminal opens]

Me (Fixer):
"I've received a context handoff. Let me review...

From the analysis:
- 3 files analyzed
- 3 issues to fix
- Clear recommendations provided

Starting fixes:

1. src/auth/login.ts:42 - Removing unused variable 'foo'
   [Reads file, removes line 42]
   ✓ Fixed

2. src/auth/validators.ts:15 - Adding return type annotation
   [Reads file, adds ': Promise<boolean>']
   ✓ Fixed

3. src/utils/helpers.ts:23 - Replacing console.log with logger
   [Imports logger, replaces console.log]
   ✓ Fixed

All issues resolved! Running quick test...
[Runs: npm run type-check]
✓ All tests pass!

Summary:
- 3 issues fixed
- 0 issues remaining
- Type checking passes
- Ready for review"
```

## Key Points

### What Got Handed Off:
1. ✅ **File list** - Fixer knows which files were analyzed
2. ✅ **Issue details** - Exact locations and problems
3. ✅ **Recommendations** - How to fix each issue
4. ✅ **Original intent** - Why the user requested this
5. ✅ **Project context** - TypeScript project, linting rules

### What Made It Work:
- **Structured format** - Easy for fixer to parse
- **Complete context** - No guessing needed
- **Clear mission** - Fixer knows exactly what to do
- **Background preserved** - Fixer understands user's goals

### Without Context Handoff:
```
Forked Session:
"I don't know what to fix. What files? What issues?
 Starting from scratch..."
```

### With Context Handoff:
```
Forked Session:
"I have complete context. Fixing 3 issues systematically..."
```

## The Magic 🎭

The fixer agent didn't just get a task like "fix the code" - it got:
- **What** was analyzed
- **What** issues were found
- **Where** they're located
- **How** to fix them
- **Why** this matters

That's the power of context handoff!
