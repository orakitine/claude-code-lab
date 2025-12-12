# JavaScript/TypeScript Project Analysis

Comprehensive analysis workflow for JavaScript and TypeScript projects.

## Workflow

1. **Detect Framework**
   - Tool: Run `tools/detect_framework.py` on project root
   - Checks for: Next.js, React+Vite, Vue, Svelte, Express, Nest.js, vanilla TS/JS
   - Indicators: package.json dependencies, config files (next.config.js, vite.config.ts), directory structures
   - Example: package.json has "vite" + "react" → {type: "nodejs", framework: "react-vite", language: "typescript"}

2. **Analyze Dependencies**
   - Tool: Run `tools/analyze_dependencies.py` on project root
   - Extracts from package.json: runtime deps, dev deps, npm scripts, Node.js version
   - Record: Key dependencies and purposes, available scripts (dev, build, test), notable packages
   - Example: {runtime: ["react", "react-dom"], dev: ["vite", "typescript"], scripts: {dev: "vite", build: "vite build"}}

3. **Map Directory Structure**
   - Tool: Run `tools/analyze_structure.py` on project root
   - Categorizes directories: source (src/, app/, components/), tests (__tests__, *.test.ts), config, docs, assets, build output
   - Ignore: node_modules/, dist/, build/, .next/, .git/, hidden files (except .env.example)
   - Example: {src: {file_count: 15, subdirs: ["components", "hooks"]}, tests: {file_count: 8}}

4. **Find Entry Points**
   - Tool: Run `tools/find_entry_points.py` with detected framework
   - Checks: package.json "main" field, common entries (main.ts, index.ts, app.ts), framework-specific (pages/_app.tsx for Next.js, src/App.tsx for React)
   - Record: application entry, server entry (if backend), test entries, framework special files
   - Example: ["src/main.tsx", "src/App.tsx", "index.html"]

5. **Detect Patterns**
   - Analyze structure and dependencies to identify architecture patterns
   - Frontend: Component frameworks (React/Vue/Svelte), state management (Redux/Zustand/Context), styling (CSS-in-JS/Tailwind/Modules), routing
   - Backend: API type (REST/GraphQL/tRPC), server framework (Express/Fastify/Nest.js/Hono), database (Prisma/TypeORM/Mongoose), auth (JWT/sessions)
   - Testing: Framework (Vitest/Jest/Mocha), testing library (React Testing Library), E2E (Playwright/Cypress)
   - Build: Bundler (Vite/Webpack/Rollup), package manager (npm/yarn/pnpm), monorepo (Turborepo/Nx)
   - Example: Vite + React + TypeScript + Vitest detected → Modern React SPA pattern

6. **Generate Report**
   - Tool: Run `tools/generate_report.py` with all collected data
   - Report sections: project overview, tech stack, directory structure, entry points, key dependencies, available scripts, detected patterns, dev workflow
   - Output mode: IF user requested "save" → Write to .project-context.md, ELSE → Display in chat
   - Example: Complete markdown report with all sections formatted

## Tool Sequence Example

```
detect_framework(".")
  → {type: "nodejs", framework: "react-vite", language: "typescript"}

analyze_dependencies(".")
  → {runtime: [...], dev: [...], scripts: {...}}

analyze_structure(".")
  → {src: {...}, tests: {...}, config: {...}}

find_entry_points(".", "react-vite")
  → ["src/main.tsx", "src/App.tsx"]

generate_report({...all_data...}, "display")
  → [formatted markdown report]
```
