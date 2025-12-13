# JavaScript/TypeScript Project Analysis

Comprehensive analysis workflow for JavaScript and TypeScript projects. Uses parallel agent execution for faster analysis.

## Variables

ENABLE_PARALLEL_EXECUTION: true       # Use parallel agent swarm for faster analysis
MAX_PARALLEL_AGENTS: 3                # Maximum agents to run simultaneously

## Workflow

1. **Detect Framework**
   - Tool: Run `tools/detect_framework.py` on project root
   - Checks for: Next.js, React+Vite, Vue, Svelte, Express, Nest.js, vanilla TS/JS
   - Indicators: package.json dependencies, config files (next.config.js, vite.config.ts), directory structures
   - Example: package.json has "vite" + "react" → {type: "nodejs", framework: "react-vite", language: "typescript"}

2. **Launch Parallel Analysis Swarm**
   - IF: ENABLE_PARALLEL_EXECUTION is true → Launch all analysis tasks as parallel background agents
   - Tool: Task with run_in_background: true for each analysis task
   - Agents to spawn:
     - Agent "DependencyAnalyzer": Run `tools/analyze_dependencies.py` on project root
     - Agent "StructureMapper": Run `tools/analyze_structure.py` on project root
     - Agent "EntryPointFinder": Run `tools/find_entry_points.py` with detected framework
   - Each agent runs independently and returns analysis results
   - Example: 3 agents launch simultaneously → All complete in ~4s (vs ~9s sequential)

3. **Collect Swarm Results**
   - Tool: TaskOutput for each agent to retrieve results
   - Wait for all agents to complete (block: true)
   - Parse each agent's output:
     - DependencyAnalyzer: {runtime: [...], dev: [...], scripts: {...}, metadata: {...}}
     - StructureMapper: {src: {...}, tests: {...}, config: [...], docs: [...]}
     - EntryPointFinder: ["src/main.tsx", "src/App.tsx", "index.html"]
   - Example: All agents complete → Combined data ready for pattern detection

4. **Detect Patterns**
   - Analyze collected structure and dependencies to identify architecture patterns
   - Frontend: Component frameworks (React/Vue/Svelte), state management (Redux/Zustand/Context), styling (CSS-in-JS/Tailwind/Modules), routing
   - Backend: API type (REST/GraphQL/tRPC), server framework (Express/Fastify/Nest.js/Hono), database (Prisma/TypeORM/Mongoose), auth (JWT/sessions)
   - Testing: Framework (Vitest/Jest/Mocha), testing library (React Testing Library), E2E (Playwright/Cypress)
   - Build: Bundler (Vite/Webpack/Rollup), package manager (npm/yarn/pnpm), monorepo (Turborepo/Nx)
   - Example: Vite + React + TypeScript + Vitest detected → Modern React SPA pattern

5. **Generate Report**
   - Tool: Run `tools/generate_report.py` with all collected data
   - Report sections: project overview, tech stack, directory structure, entry points, key dependencies, available scripts, detected patterns, dev workflow
   - Output mode: IF user requested "save" → Write to OUTPUT_FILE, ELSE → Display in chat
   - Show execution time comparison if parallel execution was used
   - Example report shows: "Analysis completed in 6s (29% faster than sequential 9s execution)"

## Tool Sequence Example

```
detect_framework(".")
  → {type: "nodejs", framework: "react-vite", language: "typescript"}

PARALLEL SWARM:
├─ analyze_dependencies(".")      → {runtime: [...], dev: [...], scripts: {...}}
├─ analyze_structure(".")         → {src: {...}, tests: {...}, config: {...}}
└─ find_entry_points(".", "react-vite")  → ["src/main.tsx", "src/App.tsx"]

collect_results()
  → {dependencies: {...}, structure: {...}, entry_points: [...]}

detect_patterns({...all_data...})
  → {frontend: "React SPA", testing: "Vitest", build: "Vite"}

generate_report({...all_data...}, "display")
  → [formatted markdown report with performance metrics]
```
