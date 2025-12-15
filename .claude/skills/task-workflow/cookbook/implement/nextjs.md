# Implement Task Workflow (Next.js)

Execute Next.js task implementation with framework-specific patterns, App Router conventions, and Next.js quality gates.

## Workflow

1. **Discover and Load Task**

   - Use task discovery pattern to find target task file
   - Tool: Glob to search TASK_DIR with user's identifier
   - Support all formats: full ID, short ID, keywords, category, "latest"
   - Example: User says "implement BROOKLY-042" → Find BROOKLY-042 [toImplement] (api): add-user-profile-endpoint.md

2. **Validate Task State**

   - Tool: Read task file and extract [state] from filename
   - Verify state is [toImplement] (expected for implement workflow)
   - IF: state is [toRefine] → Error "Task needs refinement first. Run refine workflow."
   - IF: state is [toImplement] → Proceed with implementation
   - IF: state is [toReview] or [done] → Warn "Already implemented"
   - Example: BROOKLY-042 [toImplement] found → State valid, proceed

3. **Load and Parse Specification**

   - Tool: Read entire task specification file
   - Extract key information: Requirements (Must/Should/Could), Files to modify/create, Architecture changes, Integration points, Acceptance criteria, Testing strategy
   - Validate specification completeness (all sections present and filled)
   - Example: Loaded BROOKLY-042 spec: API route, Server Components, 2 route handlers, 4 acceptance criteria

4. **Detect Next.js Architecture**

   - Tool: Glob to check for Next.js structure indicators
   - Check for App Router: Look for `app/` directory with `layout.tsx` or `page.tsx`
   - Check for Pages Router: Look for `pages/` directory with `_app.tsx` or `index.tsx`
   - Identify Next.js version: Tool: Read `package.json` and check `next` version
   - Set architecture context for implementation decisions
   - Example: Found `app/layout.tsx` → App Router detected, Next.js 14.x → Use Server Components by default

5. **Pre-Implementation Safety Checks**

   - IF: ENABLE_LINT → Tool: Bash to run `npm run lint` (Next.js ESLint config)
   - IF: ENABLE_TYPECHECK → Tool: Bash to run `npm run typecheck` or `tsc --noEmit`
   - IF: ENABLE_BUILD → Tool: Bash to run `npm run build` (next build)
   - IF: ENABLE_TESTS → Tool: Bash to run test command
   - Verify all checks pass before starting implementation
   - Example: Run `npm run lint && tsc --noEmit && npm run build` → All pass ✓

6. **Plan Implementation Phases (Next.js-Aware)**

   - Break implementation into logical phases based on complexity
   - LOW complexity: Single phase (e.g., add single Server Component)
   - MEDIUM complexity: 2-3 phases (e.g., API route → data layer → UI component)
   - HIGH complexity: 4+ phases (e.g., auth system with middleware → protected routes → UI → API)
   - Consider Next.js-specific ordering:
     - Phase 1: Server-side (API routes, Server Components, Server Actions)
     - Phase 2: Client-side (Client Components with 'use client')
     - Phase 3: Integration and middleware
   - Example: MEDIUM → Phase 1: Create API route handler, Phase 2: Add Server Component, Phase 3: Client interaction

7. **Execute Implementation Phases (Next.js Patterns)**

   For each phase, follow Next.js conventions:

   **App Router Patterns:**
   - **Server Components** (default): Place in `app/` directory, no 'use client' directive
     - Example: `app/dashboard/profile/page.tsx` exports async function with server-side data fetching
   - **Client Components**: Add 'use client' directive at top, use hooks and interactivity
     - Example: `app/components/ProfileForm.tsx` starts with 'use client', uses useState/useEffect
   - **API Routes**: Create `route.ts` in `app/api/` with named exports (GET, POST, etc.)
     - Example: `app/api/profile/route.ts` exports `export async function GET(request: Request) {...}`
   - **Layouts**: Use `layout.tsx` for shared UI wrapping multiple pages
     - Example: `app/dashboard/layout.tsx` exports default function with children prop
   - **Metadata**: Export `metadata` object or `generateMetadata` function for SEO
     - Example: `export const metadata = { title: 'User Profile', description: '...' }`
   - **Loading States**: Create `loading.tsx` for automatic loading UI
     - Example: `app/dashboard/loading.tsx` exports loading skeleton component
   - **Error Handling**: Create `error.tsx` for error boundaries
     - Example: `app/dashboard/error.tsx` exports error component with reset function

   **Pages Router Patterns (if detected):**
   - **Pages**: Create files in `pages/` directory, export default React component
     - Example: `pages/profile.tsx` exports default ProfilePage component
   - **API Routes**: Create files in `pages/api/` with default export handler
     - Example: `pages/api/profile.ts` exports `export default function handler(req, res) {...}`
   - **getServerSideProps**: Export for server-side data fetching on each request
     - Example: `export async function getServerSideProps(context) { return { props: {...} } }`
   - **getStaticProps**: Export for static generation at build time
     - Example: `export async function getStaticProps() { return { props: {...}, revalidate: 60 } }`

   **Common Patterns:**
   - **Image Optimization**: Use `next/image` component, not `<img>`
     - Example: `<Image src="/profile.jpg" alt="Profile" width={200} height={200} />`
   - **Link Navigation**: Use `next/link` component, not `<a>`
     - Example: `<Link href="/dashboard">Dashboard</Link>`
   - **Environment Variables**: Use `process.env.NEXT_PUBLIC_*` for client-side, plain `process.env.*` for server
     - Example: `const apiKey = process.env.STRIPE_SECRET_KEY // Server-only`
   - **Middleware**: Create `middleware.ts` at root for request interception
     - Example: `export function middleware(request: NextRequest) { /* auth check */ }`

   Implementation execution:
   - Announce phase: "Phase X of Y: {phase description}"
   - Implement changes: Tool: Write for new files, Tool: Edit for modifications
   - Follow Next.js conventions precisely: correct file locations, proper directives
   - Validate phase completion: run relevant quality gates
   - Example: Phase 1 complete → Created `app/api/profile/route.ts` (API route), Added `lib/profile-service.ts` (data layer)

8. **Continuous Validation**

   - After each significant change or phase:
     - IF: ENABLE_TYPECHECK → Run `tsc --noEmit` to check types
     - Check for Next.js-specific issues: 'use client' placement, async Server Components
     - Fix issues before proceeding to next change
   - Example: After creating API route → Run `tsc --noEmit` → Fix Response type → Proceed

9. **Integration and Testing**

   - After all phases complete:
     - Verify all Must Have requirements implemented
     - Check Should Have requirements (implement if time permits)
     - Test each acceptance criterion:
       - Server-side: Verify API routes work (curl/fetch tests)
       - Client-side: Verify UI renders and interacts correctly
       - Integration: Verify data flows from server to client
     - Check Next.js-specific functionality:
       - Metadata renders correctly (check page source)
       - Images optimized (check Network tab)
       - Navigation works with next/link
   - Example: Test profile API endpoint, Server Component data fetch, Client Component form submission → All criteria met ✓

10. **Final Quality Gates**

    - Run complete Next.js quality gate suite:
      - IF: ENABLE_LINT → Tool: Bash run `npm run lint` (Next.js ESLint rules)
      - IF: ENABLE_TYPECHECK → Tool: Bash run `tsc --noEmit`
      - IF: ENABLE_BUILD → Tool: Bash run `npm run build` (Verify production build succeeds)
      - IF: ENABLE_TESTS → Tool: Bash run test command
    - Verify no errors or warnings
    - Check build output for bundle size, route generation
    - Example: Build output shows static routes generated, bundle sizes acceptable → ✓

11. **Document Implementation**

    - Tool: Edit task file to add implementation notes to Workflow State History
    - Document: Phases completed, Files created/modified, Next.js patterns used (App Router, Server Components, etc.), Quality gates results, Any deviations from spec
    - Note Next.js-specific decisions: Server vs Client Component choices, data fetching strategy
    - Example: "Used Server Components for dashboard (app/dashboard/page.tsx), Client Component for form (ProfileForm.tsx with 'use client'), API route at app/api/profile/route.ts"

12. **Transition State to [toReview]**

    - Tool: Bash (mv command) to rename task file
    - Change state from [toImplement] to [toReview]
    - Preserves all other filename components (ID, category, slug)
    - Example: `mv "BROOKLY-042 [toImplement] (api): add-user-profile-endpoint.md" "BROOKLY-042 [toReview] (api): add-user-profile-endpoint.md"`

13. **Generate Implementation Summary**

    - Output to user: Summary of what was implemented
    - Include: Phases executed, Files changed (created/modified/deleted), Quality gates status, Next.js patterns applied, Next steps (ready for review)
    - Example: "✅ Implementation complete! Created API route (app/api/profile/route.ts), Server Component (app/dashboard/profile/page.tsx), Client form (ProfileForm.tsx). All quality gates passing. Ready for review."

## Next.js-Specific Checklist

Before marking implementation complete, verify:

- [ ] **Correct Router Pattern**: App Router or Pages Router conventions followed
- [ ] **Server vs Client**: Components marked with 'use client' only when needed (interactivity, hooks)
- [ ] **File Locations**: Files in correct directories (app/, pages/, lib/, components/)
- [ ] **Naming Conventions**: route.ts for API routes (App Router), handler for pages/api (Pages Router)
- [ ] **Metadata**: SEO metadata exported where appropriate
- [ ] **Image Optimization**: All images use next/image component
- [ ] **Link Navigation**: All navigation uses next/link component
- [ ] **Environment Variables**: Correct NEXT_PUBLIC_ prefix for client-side vars
- [ ] **TypeScript**: All Next.js types used correctly (NextRequest, NextResponse, Metadata, etc.)
- [ ] **Build Success**: `npm run build` completes without errors
- [ ] **No Console Warnings**: No Next.js warnings in dev server or build output

## Framework Detection Example

```typescript
// Detected App Router structure:
// ✓ app/layout.tsx exists
// ✓ app/page.tsx exists
// ✓ next.config.js uses appDir
// → Use App Router patterns (Server Components by default)

// Detected Pages Router structure:
// ✓ pages/_app.tsx exists
// ✓ pages/index.tsx exists
// ✗ No app/ directory
// → Use Pages Router patterns (getServerSideProps, getStaticProps)
```
