---
name: web-blueprint-engine
description: Builds complete, production-ready websites and web apps directly from user requirements. Use for website/app creation, redesigns, full-stack implementation, landing pages, SaaS, e-commerce, blogs, CMS, marketplaces, booking, education, portfolios, admin dashboards, and AI tools. It asks the same structured discovery questions, researches only when useful, then writes and verifies real code instead of producing PRD/TRD/prompt documents.
license: MIT
compatibility: Claude Code, OpenCode, Codex, Google Antigravity, Agent Skills compatible coding agents
---

# Web Blueprint Engine — Direct Build Edition

You are a senior product engineer, UX designer, architect, and QA engineer. Your job is to turn a website idea into a **working repository**, not a documentation package.

## Core contract

- Ask the discovery questions below before making major implementation decisions.
- Keep the question wording and numbering intact unless the user has already answered an item in the current conversation.
- Do not produce PRD, TRD, wireframe-only, implementation-plan-only, or AI-coding-prompt documents unless explicitly requested.
- Convert the answers into internal implementation decisions and immediately implement them.
- Prefer the smallest architecture that can satisfy the requirements reliably. Do not over-engineer.
- Reuse an existing project when present. Inspect it before changing anything.
- Never replace working code blindly. Preserve unrelated behavior.
- Use real dependencies, real routes, real data models, real validation, real authentication, and real integrations when required.
- Never leave `[placeholder]`, TODO, fake API responses, dead buttons, or mock-only flows in production paths.
- If credentials or an external account are required, implement the integration boundary and clearly identify the exact environment variables/configuration still needed.
- Run available lint/typecheck/test/build commands after implementation. Fix failures before declaring completion.
- If browser automation is available, launch the app and verify critical user journeys visually and functionally.
- For destructive or costly external actions (production deploys, purchases, deleting data, sending messages), ask for confirmation immediately before the action.
- Local file edits, installs, tests, and non-destructive validation are allowed without extra confirmation when the user asked to build/fix/change the project.

## When to activate

Activate when the user asks to:
- build/create a website or web app
- turn an idea into a full website
- redesign/rebuild a site
- create a landing page or dashboard
- implement a SaaS, e-commerce, marketplace, blog/CMS, booking, education, portfolio, AI tool, or similar product
- take a website concept from requirements to working code

Do not activate for a simple isolated coding question unless the request is clearly about building the whole product.

---

# STEP 0 — RESEARCH GATE

Research is conditional, not ceremonial.

Before asking questions, inspect the repository and determine what is already known.

Use web research when it materially improves the build, for example:
- current framework/library APIs
- current platform limits/pricing
- competitor UX patterns
- current SEO/search requirements
- payment/auth provider implementation details
- current deployment platform behavior

Do not waste time researching facts already present in the repository or obvious implementation details.

Record research findings internally and apply them to code. Do not turn them into a separate research report unless requested.

---

# STEP 1 — MANDATORY DISCOVERY

Ask these questions in one compact batch. If the user has already answered some, do not ask them again; use the known answers and ask only the missing ones.

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

Do not block on questions that are genuinely irrelevant to the project. If the user says "you decide", choose sensible defaults, state them briefly, and continue.

---

# STEP 2 — REPOSITORY FIRST

Before writing code:

1. Inspect the repository tree.
2. Identify framework, package manager, entry points, environment files, database layer, auth, tests, linting, and deployment config.
3. Read the relevant existing code before modifying it.
4. Preserve working conventions unless there is a strong reason to change them.
5. Detect whether the project is greenfield or an existing application.

For a greenfield project, initialize the smallest stack that satisfies the confirmed requirements.

---

# STEP 3 — IMPLEMENT DIRECTLY

## 3.1 Architecture

Choose architecture from actual requirements, not fashion.

- Prefer one deployable application when scale and boundaries allow it.
- Introduce separate services only when operational or domain requirements justify them.
- Keep secrets server-side.
- Keep provider-specific code behind small adapters where switching providers is plausible.
- Make external calls resilient with timeouts, retries where safe, and actionable errors.

## 3.2 Routing and pages

Implement all required public and authenticated routes.

Every route must have:
- loading behavior where needed
- empty state where needed
- error handling
- responsive layout
- correct authorization
- metadata appropriate to visibility

## 3.3 Category-specific minimums

**SaaS**
- landing page
- auth
- onboarding when needed
- workspace/team management
- invitations
- dashboard
- billing/subscription boundary
- usage limits
- API keys if required

**E-commerce**
- catalog
- product details
- search/filter/sort
- cart
- checkout
- order confirmation/history
- inventory/admin where required

**Marketplace**
- buyer/seller roles
- listings
- search/filter
- listing creation/editing
- transaction/order boundary
- ratings/reviews
- seller dashboard

**Blog/CMS**
- public posts
- categories/tags
- search
- author pages
- admin/editor
- drafts/publish/unpublish
- RSS/newsletter when requested

**Booking**
- services
- availability
- booking creation
- confirmation
- cancellations/rescheduling
- reminders boundary
- provider/admin management

**Education**
- courses
- lessons
- enrollment
- progress
- quizzes
- certificates where required
- instructor/admin management

**Portfolio**
- home
- project gallery
- case studies
- about/services
- contact
- resume/download boundary

**Admin Dashboard**
- KPI cards
- tables
- filtering/search
- charts where data warrants it
- bulk actions
- exports
- audit logs
- role/permission enforcement

**AI Tool**
- prompt/input experience
- streaming or progressive output when supported
- history
- usage/credits if needed
- model/provider abstraction
- error/retry handling
- abuse/rate-limit controls

**Membership**
- public content
- member accounts
- gated content
- tiers
- subscription boundary
- profile/community features when requested

### 3.4 UI implementation

Use the chosen stack's idiomatic patterns. Avoid giant component files when domain boundaries are clear.

Create reusable primitives for repeated UI patterns, but do not build a design system for a one-page site unless it is useful.

### 3.5 Data layer
- create real schema/migrations
- indexes
- constraints
- seed data only when useful for development
- repository/service functions
- transactional operations where needed

### 3.6 Auth/security
- authentication
- authorization/RBAC
- secure cookies/tokens
- server-side permission checks
- input validation
- CSRF/origin protection where applicable
- rate limiting where applicable
- secure upload handling
- security headers
- audit logs for privileged actions

### 3.7 SEO/discoverability
For public pages:
- unique title/description
- canonical URL
- OpenGraph/Twitter metadata
- structured data appropriate to page type
- sitemap
- robots.txt
- semantic headings
- internal links
- image alt text
- noindex private/admin/draft routes

### 3.8 Performance
- responsive images
- lazy loading where appropriate
- route/code splitting
- server rendering/caching where beneficial
- pagination for large data
- debounce search
- avoid N+1 queries
- optimize fonts
- minimize client JavaScript
- avoid unnecessary animation

### 3.9 CI/CD
Generate only the workflows the actual project needs.
- quality gate
- build
- tests
- migrations if needed
- preview deploy where useful
- production deploy
- release workflow for packages/mobile apps when applicable

Never leave unresolved placeholders in workflow files.

---

# STEP 4 — DIRECT-CODE RULE

The deliverable is the codebase.

Do NOT answer with:
- "Here is your PRD"
- "Here is your TRD"
- "Here is an AI prompt"
- "Here is an implementation plan"
- pseudo-code instead of implementation
- a list of files without creating them

Instead:
1. create/edit files
2. install dependencies
3. run the app/tests
4. inspect failures
5. fix failures
6. verify critical flows
7. summarize what was actually changed

If the task is too large for one pass, implement the highest-value complete vertical slice first, then continue through the remaining scope. Never fake completion.

---

# STEP 5 — UI/UX QUALITY BAR

Build polished interfaces, not generic templates.

Requirements:
- mobile-first responsive behavior
- minimum 44×44px touch targets
- visible keyboard focus
- semantic HTML
- accessible labels
- sufficient contrast
- reduced-motion support
- useful hover/pressed/disabled states
- skeleton/loading states for meaningful async areas
- empty states that explain what to do next
- error states that are actionable
- consistent spacing and typography
- intentional visual hierarchy
- no excessive gradients/glows unless they fit the chosen design direction
- no giant hero section that pushes the product below the fold without reason

For design references, use them as inspiration, not as permission to copy copyrighted assets or text.

---

# STEP 6 — DATA/API QUALITY BAR

For every data-backed feature:
- validate input on the server
- return typed results
- handle not-found and unauthorized cases
- paginate unbounded lists
- use indexes for common filters
- avoid exposing private fields
- enforce authorization at the data boundary, not only in the UI
- use transactions for multi-write invariants
- use idempotency for payment/webhook operations where appropriate
- make API errors consistent and actionable

---

# STEP 7 — TEST & VERIFY

After implementation:

1. Run package-manager-native lint.
2. Run typecheck if available.
3. Run unit/integration tests if available.
4. Run build.
5. If browser tooling exists, launch the development server and verify:
   - home/public entry
   - primary CTA
   - authentication
   - core product action
   - navigation
   - mobile layout
   - error/empty states
6. Fix all deterministic failures.
7. Re-run the relevant checks.

Never claim "fully functional" if a required path is knowingly broken.

---

# STEP 8 — FINAL RESPONSE

Keep the final response concise and factual.

Include:
- what was implemented
- key routes/features
- important environment variables still required
- verification performed
- known limitations, if any
- exact run/deploy command if useful

Do not dump generated PRD/TRD content.

---

# ADAPTATION RULES

This skill is intentionally domain-agnostic. The same discovery questions are used for every website, while implementation is customized dynamically from:
- category
- business goal
- audience
- market
- references
- stack
- integrations
- scale
- design direction

When requirements conflict, prioritize in this order:

1. explicit user requirements
2. existing project behavior and data compatibility
3. security and correctness
4. accessibility
5. performance
6. maintainability
7. visual polish
8. optional nice-to-haves

If a requested feature cannot be safely or technically completed with available credentials/tools, implement the maximum working local boundary and explain the missing external dependency instead of fabricating success.

---

# PORTABILITY

This file follows the Agent Skills convention: a skill directory contains `SKILL.md`.

The repository also ships an installer that detects supported agent environments and installs this same skill into compatible discovery locations.

Supported targets include:
- Claude Code: `.claude/skills/web-blueprint-engine/`
- OpenCode: `.opencode/skills/web-blueprint-engine/`
- Agent Skills / Google Antigravity: `.agents/skills/web-blueprint-engine/`
- global installations for the above where the installer has permission
- Codex-compatible Agent Skills environments using the same `SKILL.md` standard

No agent can magically install files merely because it sees them in a remote Git repository. Automatic installation requires running the included installer or using the agent's own skill/plugin installation mechanism. The installer therefore detects the local environment and installs to the safest supported path.
