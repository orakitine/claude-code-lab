# Purpose

Create a new Claude code agent to execute the command.

## Variables

DEFAULT_MODEL: opus
HEAVY_MODEL: opus
BASE_MODEL: sonnet
FAST_MODEL: haiku

## Instructions

- Before executing the command, run `claude --help` to understand the command and its options.
- Extract the user's task from their request and pass it using the `-p` flag so it executes automatically
- For the --model argument, use the DEFAULT_MODEL if not specified. If 'fast' is requested, use the FAST_MODEL. If 'heavy' is requested, use the HEAVY_MODEL.
- Always run with `--dangerously-skip-permissions`
