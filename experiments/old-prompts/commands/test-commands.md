---
description: "Test if custom commands are working properly"
args: []
allowed_tools: ["Read", "Glob", "LS"]
---

# COMMAND TEST VERIFICATION

Testing if Claude Code slash commands are properly configured and executable.

## TEST 1: File Discovery
Let me verify the tasks directory structure and find available tasks:

!ls tasks/

## TEST 2: Task Pattern Matching
Search for tasks in different states:

!find tasks/ -name "*toReview*"
!find tasks/ -name "*done*" | head -5

## TEST 3: Command Integration Check
This command should be executable if slash commands are working properly.

Command execution successful! ✅