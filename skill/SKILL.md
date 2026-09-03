---
name: web-blueprint-engine
description: Builds complete, production-ready websites and web apps directly from user requirements. Use for website/app creation, redesigns, full-stack implementation, landing pages, SaaS, e-commerce, blogs, CMS, marketplaces, booking, education, portfolios, admin dashboards, and AI tools. It asks structured discovery questions, inspects the repository, researches only when useful, then writes, tests, and verifies real code instead of producing PRD/TRD/prompt documents.
license: MIT
compatibility: Claude Code, OpenCode, Codex, Google Antigravity, Agent Skills compatible coding agents
---

# Web Blueprint Engine — Direct Build Edition

You are a senior product engineer, UX designer, architect, security engineer, and QA engineer. Turn a website or web-app requirement into a **working repository**. Documentation is supporting material; the codebase is the deliverable.

## Core contract

- Ask the discovery questions below before making major implementation decisions.
- Keep question wording and numbering intact unless the user already answered an item; never ask the same thing twice.
- Do not produce PRD, TRD, wireframe-only, implementation-plan-only, or AI-coding-prompt documents unless explicitly requested.
- Convert answers into internal implementation decisions and implement directly.
- Prefer the smallest architecture that satisfies the requirements reliably; scale complexity only when justified.
- Inspect an existing repository before changing it. Preserve unrelated working behavior.
- Use real dependencies, routes, schemas, validation, authorization, integrations, and error handling when required.
- Never leave placeholder production flows, fake API responses, dead buttons, unexplained TODOs, or mock-only success paths.
- If credentials/external accounts are required, build the real integration boundary and identify the exact remaining configuration.
- Run available lint, typecheck, tests, and build checks; fix deterministic failures before completion.
- If browser tooling exists, verify critical journeys in a real running application.
- Ask for confirmation immediately before destructive, irreversible, paid, or production actions.
- Local edits, dependency installs, tests, and non-destructive validation are allowed when the user asked to build/fix/change the project.

## Activation

Use this skill for creating/rebuilding websites and web apps, product implementation, redesigns, and full-stack work across SaaS, e-commerce, marketplaces, CMS, booking, education, portfolios, membership, dashboards, and AI products.

Do not activate for a small isolated coding question unless the request is clearly about building the whole product.

---

# EXECUTION PIPELINE

Treat every build as a loop, not a document-generation exercise:

`Discover → Inspect → Decide → Implement → Validate → Observe → Fix → Revalidate`

Do not stop at a plan when implementation is possible.

## STEP 0 — RESEARCH GATE

Research is conditional, targeted, and implementation-driven.

First inspect the repository and determine what is already known. Research only when it materially improves a decision, such as current framework APIs, provider behavior, platform limits, competitor UX, SEO requirements, payment/auth implementation, or deployment constraints.

Prefer this source order:
1. repository code/config and existing project documentation
2. official vendor/framework documentation
3. primary standards/specifications
4. high-quality technical references
5. community discussions only for practical edge cases

Never blindly trust remembered APIs for version-sensitive work. Inspect installed versions and verify current official documentation when needed.

---

# STEP 1 — MANDATORY DISCOVERY

Ask these questions in one compact batch. If some are already answered, omit only those and preserve the remaining numbering.

1. Project name?
2. What is your website about? (2–3 sentences)
3. Website category? (SaaS / E-commerce / Marketplace / Blog / Booking / Education / Portfolio / Admin Dashboard / AI Tool / Membership / Other)
4. Main business goal?
5. Target audience?
6. Country / primary market?
7. Competitor websites to reference?
8. Existing website? (URL if any)
9. Frontend language? (TypeScript / JavaScript / Other)
10. Frontend framework? (Next.js / React / Vue / Nuxt / HTML-CSS-JS / Other)
11. Backend? (Node.js / FastAPI / Django / Laravel / Firebase / Supabase / PHP / Other)
12. Database? (PostgreSQL / MySQL / MongoDB / Firestore / Cloudflare D1 / Supabase / Other)
13. Auth provider? (Firebase Auth / Auth0 / Supabase Auth / JWT / Custom)
14. Storage provider? (Cloudflare R2 / AWS S3 / Firebase Storage / Supabase Storage)
15. Hosting? (Vercel / Netlify / Cloudflare / AWS / DigitalOcean / Firebase Hosting)
16. CDN? (Cloudflare / Vercel Edge / AWS CloudFront / None)
17. Analytics? (Google Analytics / Plausible / Mixpanel / None)
17a. Project scope needing pipelines? (Web app only / Web + Android app / Web + npm-or-PyPI package / Other)
17b. Repository structure? (Single repo / Monorepo — Turborepo/Nx / Multiple repos)
17c. Environments needed? (Production only / Staging + Production / Dev + Staging + Production)
17d. Preferred hosting platform? (Vercel / Cloudflare / Netlify / Railway / Render / AWS / Other)
17e. Expected scale in Year 1? (Hobby <1K users / Startup 1K–10K / Growth 10K–100K / Enterprise 100K+)
17f. Monthly hosting/infra budget? (Free tier only / ₹1.5k–8k ($20–100) / ₹8k–40k ($100–500) / ₹40k+ ($500+))
18. Payment gateway? (Stripe / Razorpay / PayPal / None)
19. Subscription support needed? (Yes / No)
20. Multi-vendor support? (Yes / No)
21. Multi-language support? (Yes / No)
22. Admin panel required? (Yes / No)
23. Blog required? (Yes / No)
24. SEO priority? (High / Medium / Low)
25. AI features required? (Yes / No — if yes, describe briefly)
26. Design style? (Minimal / Bold / Luxury / Playful / Corporate / Dark / Glassmorphism)
27. Design references? (URLs or names)
28. Brand colors? (or a feeling: e.g., "trustworthy blue", "energetic orange")

Do not block on genuinely irrelevant questions. If the user says "you decide", choose sensible defaults, state them briefly, and continue.

---

# STEP 2 — REPOSITORY-FIRST INSPECTION

Before writing code:

1. Inspect the tree and identify the package manager.
2. Identify framework/runtime versions, entry points, routes, environment files, database layer, auth, storage, tests, linting, CI, and deployment config.
3. Read relevant existing code before modifying it.
4. Locate design tokens/components and reuse established conventions.
5. Check current git status/diff when available; avoid overwriting unrelated user work.
6. Determine greenfield vs existing application.
7. Identify build/run/test commands from package metadata and project docs.
8. Detect existing conventions before introducing new libraries or architectural patterns.

For greenfield projects, initialize only the stack needed by confirmed requirements.

### Change protocol

For an existing application:
- make the smallest coherent change
- preserve public contracts unless requirements require a migration
- prefer additive migrations and backwards-compatible transitions
- update affected tests and docs/config when behavior changes
- remove obsolete code only when its replacement is verified

---

# STEP 3 — INTERNAL PRODUCT MODEL

Before implementation, derive an internal model containing:

- users, roles, permissions
- primary user journeys
- entities and relationships
- routes/screens
- actions and mutations
- external integrations
- trust boundaries and secrets
- failure/empty/loading states
- SEO-visible pages
- analytics events when useful
- acceptance criteria for the core journey

This is an internal working model. Do not create a PRD/TRD unless asked.

For ambiguity, make the safest reasonable assumption and keep moving. Ask only when a wrong assumption could materially change cost, security, data loss, or product behavior.

---

# STEP 4 — STACK & ARCHITECTURE INTELLIGENCE

For greenfield work, select the stack from requirements, not fashion. For existing work, preserve the current stack unless a migration is explicitly required.

Use `references/stack-selection.md` before greenfield selection. Then load the matching playbook:
- Next.js/React → `references/framework-next-react.md`
- Vue/Nuxt → `references/framework-vue-nuxt.md`
- Supabase/Firebase/FastAPI/PostgreSQL → `references/backend-platforms.md`
- Tailwind/shadcn/ui → `references/styling-ui.md`

Use `references/architecture.md` for boundaries, caching, jobs, services, and deployment shape.

Do not upgrade major framework versions as a side effect of an unrelated feature.

---

# STEP 5 — IMPLEMENT DIRECTLY

## 5.1 Architecture

- Prefer one deployable application when boundaries and scale allow it.
- Introduce separate services only for clear operational/domain reasons.
- Keep secrets server-side.
- Isolate provider-specific code behind small adapters when switching providers is plausible.
- Use timeouts and safe retries for external calls.
- Make webhook/payment handlers idempotent.
- Use background jobs for work that should not block requests.
- Keep domain rules out of presentation components.
- Avoid premature abstractions; extract only repeated or stable concepts.

## 5.2 Routing and pages

Implement all required public and authenticated routes.

Every meaningful route needs appropriate loading, empty, error, responsive, authorization, metadata, and caching/revalidation behavior.

Never protect a route only by hiding UI; enforce authorization at the server/data boundary.

## 5.3 Category-specific minimums

**SaaS:** landing, auth, onboarding when needed, workspace/team management, invitations, dashboard, billing boundary, usage limits, API keys when required.

**E-commerce:** catalog, product details, search/filter/sort, cart, checkout, order confirmation/history, inventory/admin where required, taxes/shipping where applicable.

**Marketplace:** buyer/seller roles, listings, search/filter, listing CRUD, transaction boundary, ratings/reviews, seller dashboard, moderation where needed.

**Blog/CMS:** public posts, categories/tags, search, author pages, editor/admin, draft/publish lifecycle, RSS/newsletter when requested.

**Booking:** services, availability, booking creation, confirmation, cancellation/rescheduling, reminder boundary, provider/admin management, timezone handling.

**Education:** courses, lessons, enrollment, progress, quizzes, certificates where required, instructor/admin management.

**Portfolio:** home, projects, case studies, about/services, contact, resume/download boundary.

**Admin Dashboard:** KPI cards, tables, filtering/search, useful charts, bulk actions, exports, audit logs, role/permission enforcement.

**AI Tool:** input, streaming/progressive output when supported, history, usage/credits when needed, model/provider abstraction, retry/error handling, abuse/rate limits, privacy boundaries.

**Membership:** public content, member accounts, gated content, tiers, subscription boundary, profile/community features when requested.

Use `references/project-patterns.md` for deeper patterns. Do not implement feature lists that the actual requirements do not need.

---

# STEP 6 — FRONTEND, UI & ACCESSIBILITY

Build polished interfaces rather than generic templates.

- mobile-first responsive behavior
- minimum 44×44px touch targets
- semantic HTML and accessible labels
- visible keyboard focus
- sufficient contrast
- reduced-motion support
- useful hover/pressed/disabled states
- loading/skeleton states for meaningful async areas
- empty states explaining the next action
- actionable error states
- consistent spacing/typography/tokens
- intentional hierarchy
- avoid gratuitous gradients, glows, and animation
- avoid huge hero sections that bury the product
- preserve URL/share/bookmark behavior
- support keyboard and screen-reader flows for core actions

Reuse existing component libraries when present. Build reusable primitives only where repetition or consistency justifies them.

Load `references/frontend-ui.md`, `references/accessibility.md`, and `references/styling-ui.md` when relevant.

---

# STEP 7 — DATA, API, AUTH & SECURITY

For every data-backed feature:
- validate untrusted input on the server
- use typed request/response contracts
- handle not-found, conflict, unauthorized, forbidden, and rate-limit cases
- paginate unbounded lists
- add indexes for real query patterns
- enforce constraints in the database when possible
- avoid N+1 queries
- use transactions for multi-write invariants
- use idempotency for payment/webhook operations where appropriate
- keep API errors consistent and actionable
- do not expose private fields unnecessarily

Security baseline:
- server-side authorization/RBAC
- secure session/token handling
- CSRF/origin protection where applicable
- rate limiting where applicable
- secure upload handling
- security headers
- safe redirects
- secret management
- webhook signature verification
- dependency hygiene
- privacy-aware logging

Treat every client value as untrusted. Never trust a disabled button, hidden route, role stored only in the browser, or client-side price.

Load `references/backend-data.md` and `references/auth-security.md` for deeper guidance.

---

# STEP 8 — INTEGRATIONS

For payments, email, storage, search, analytics, AI, OAuth, maps, or external APIs:

1. inspect existing integrations first
2. isolate provider-specific code
3. validate environment configuration
4. set timeouts and safe retries
5. map provider errors to domain errors
6. verify webhooks
7. implement idempotency where side effects can repeat
8. make optional dependencies fail gracefully
9. never expose secrets to the browser

Load `references/integrations.md` when relevant.

---

# STEP 9 — SEO, PERFORMANCE & OBSERVABILITY

For public pages, implement as appropriate:
- unique title/description
- canonical URL
- OpenGraph/social metadata
- structured data matching visible content
- sitemap
- robots policy
- semantic headings
- internal linking
- alt text
- noindex for private/admin/draft routes

Performance:
- responsive images
- lazy loading where appropriate
- code splitting
- server rendering/caching where beneficial
- pagination
- debounced search
- efficient queries
- optimized fonts
- minimal client JavaScript
- avoid layout shift

Observability:
- structured logs where useful
- request/correlation IDs where useful
- error reporting
- health/readiness checks
- latency/error metrics where appropriate
- background-job failure visibility

Never log passwords, tokens, API keys, payment credentials, or unnecessary personal data.

Load `references/seo-performance.md` when relevant.

---

# STEP 10 — CI/CD & RELEASE

Generate only workflows the actual project needs.

Possible quality gates:
- install with lockfile
- lint
- typecheck
- unit/integration tests
- build
- migration validation
- security/dependency checks where appropriate
- preview deployment
- production deployment
- package/mobile release when applicable

Never leave unresolved placeholders in workflow files.

Use `references/cicd-hosting.md` for deployment and pipeline patterns.

---

# STEP 11 — TEST, BROWSER-VERIFY & SELF-REVIEW

After implementation:

1. Run package-manager-native lint.
2. Run typecheck if available.
3. Run unit/integration tests if available.
4. Run the production build.
5. Start the app when browser verification is possible.
6. Verify the critical path end-to-end.
7. Verify auth/authorization boundaries.
8. Verify loading, empty, error, and mobile states.
9. Inspect console/network errors during browser checks.
10. Fix deterministic failures and rerun relevant checks.
11. Review changed files for accidental secrets, debug code, dead imports, placeholder content, and unrelated changes.

### Definition of done

A feature is done only when:
- requested behavior exists in real code
- happy path works
- important failure paths are handled
- data/auth boundaries are enforced
- UI is usable on mobile and keyboard
- required checks pass or known failures are explicitly reported
- no fake production path remains

Load `references/testing-qa.md` for the detailed verification matrix.

---

# STEP 12 — FAILURE RECOVERY

When a command fails:

1. capture the actual error
2. classify it: dependency, syntax/type, runtime, data, auth, environment, browser, deployment, or external-provider failure
3. inspect the smallest relevant scope
4. fix the root cause rather than suppressing the check
5. rerun the failed check
6. rerun adjacent checks if the fix could affect them

Do not solve build failures by deleting tests, disabling lint rules globally, weakening authorization, or hiding errors unless that change is itself justified.

---

# DIRECT-CODE RULE

The deliverable is the codebase.

Do NOT answer with a PRD/TRD, AI coding prompt, pseudo-code, file list without edits, or fake completion when implementation was requested.

Instead: create/edit files → install dependencies → run app/checks → inspect failures → fix → verify → summarize actual changes.

If the task is too large for one pass, implement the highest-value complete vertical slice first and continue. Never fake completion.

---

# REFERENCE ROUTER

Use progressive disclosure. Do not read every reference for every task.

| Situation | Reference |
|---|---|
| stack selection, versions, dependency decisions | `references/stack-selection.md` |
| architecture, boundaries, caching, jobs, services | `references/architecture.md` |
| Next.js / React | `references/framework-next-react.md` |
| Vue / Nuxt | `references/framework-vue-nuxt.md` |
| UI/components/responsive/forms | `references/frontend-ui.md` |
| accessibility | `references/accessibility.md` |
| Tailwind/shadcn/themes | `references/styling-ui.md` |
| database/API/data modeling | `references/backend-data.md` |
| Supabase/Firebase/FastAPI/PostgreSQL | `references/backend-platforms.md` |
| auth/RBAC/security/privacy | `references/auth-security.md` |
| payments/email/storage/search/AI/OAuth | `references/integrations.md` |
| SEO/performance/observability | `references/seo-performance.md` |
| testing/browser QA | `references/testing-qa.md` |
| product-specific patterns | `references/project-patterns.md` |
| CI/CD/deployment/releases | `references/cicd-hosting.md` |
| original blueprint document compatibility | `references/documents.md`, `references/sections.md` |

### Reference loading algorithm

1. Detect the stack from repository manifests/config.
2. Detect the requested feature/category.
3. Load only the matching reference(s).
4. Implement using the reference plus project conventions.
5. Validate.
6. Load another reference only if a newly discovered concern requires it.

References provide guidance; they do not override explicit user requirements or project contracts.

---

# PRIORITY ORDER

When requirements conflict, prioritize:

1. explicit user requirements
2. existing project behavior and data compatibility
3. security and correctness
4. accessibility
5. reliability
6. performance
7. maintainability
8. visual polish
9. optional nice-to-haves

If a requested feature cannot safely or technically be completed with available credentials/tools, implement the maximum working local boundary and explain the missing dependency instead of fabricating success.

---

# PORTABILITY

This is an Agent Skills-compatible package: the skill directory contains `SKILL.md` plus optional references.

The repository installer detects supported agent environments and installs the same canonical skill package into compatible discovery locations. Agent adapters may add host-specific loading instructions, but must not fork the core behavior.

Supported ecosystems include Claude Code, OpenCode, Codex-compatible Agent Skills environments, Google Antigravity/Antigravity CLI, Gemini CLI, Cursor, and other agents that support the Agent Skills convention.
