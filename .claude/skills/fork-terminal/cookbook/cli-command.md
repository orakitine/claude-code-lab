# Raw CLI Command Fork

Execute a raw CLI command in a forked terminal (non-agentic tools like ffmpeg, curl, python, etc.).

## Workflow

1. **Identify Command**
   - Extract the CLI tool from user's request
   - Common tools: ffmpeg, curl, python, node, npm, git, docker, etc.
   - Example: "fork terminal with ffmpeg to convert video" → Command: ffmpeg

2. **Check Command Help**
   - Tool: Run `<command> --help` to understand available options
   - Verify command is installed and accessible
   - Example: `ffmpeg --help` → Shows ffmpeg usage and options

3. **Extract Arguments**
   - Parse user's request for command arguments and options
   - Build complete command with flags and parameters
   - Example: "fork ffmpeg to convert input.mp4 to output.webm" → Args: -i input.mp4 output.webm

4. **Construct Full Command**
   - Format: `<command> <arguments>`
   - Example: `ffmpeg -i input.mp4 -c:v libvpx-vp9 output.webm`

5. **Execute Fork**
   - Tool: Call fork_terminal(command) with constructed command
   - Spawns new terminal running the raw CLI command
   - Example: fork_terminal("python -m http.server 8000")
