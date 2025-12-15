# Task Discovery Pattern

## Purpose
Universal task file discovery and validation logic used across all workflow commands.

## Usage
Include this pattern in commands that need to locate task files: `@.claude/patterns/task-discovery.md`

## Discovery Logic

1. **Parse user input** for task identification:
   - Full filename: `BROOKLY-006 [expectedState] (category): task-name.md`
   - Partial ID: `BROOKLY-006`, `006`, `6`
   - Keywords: `design`, `theme`, `color`
   - Category: `(design)`, `design`

2. **Scan `/tasks` folder** and find matches:
   - Exact filename match (highest priority)
   - ID number match (e.g., 006 → BROOKLY-006)
   - Keyword match in filename
   - Category match

3. **Present results**:
   - If **single match**: Auto-select and proceed
   - If **multiple matches**: List options for user to choose with:
     - Full filename
     - Current state
     - Category and description
     - Last modified date
   - If **no matches**: Suggest alternatives based on:
     - Similar keywords
     - Available states in `/tasks` folder
     - Recent tasks that might be related

4. **Confirm selection**:
   - Display selected task details
   - Show current state and target state
   - Confirm correct file before proceeding

## Output Variables
After successful discovery, these should be available:
- `$TASK_FILE` - Full path to selected task file
- `$TASK_ID` - Task ID (e.g., BROOKLY-006)  
- `$CURRENT_STATE` - Current state from filename
- `$CATEGORY` - Task category
- `$TASK_NAME` - Human readable task name