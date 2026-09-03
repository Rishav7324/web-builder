# Web Blueprint Engine References

These references are intentionally modular. `SKILL.md` is the operating contract; references provide deeper implementation guidance without bloating the always-loaded skill.

## Reference map

| File | Use when |
|---|---|
| `architecture.md` | architecture, boundaries, caching, jobs, services |
| `frontend-ui.md` | UI, components, responsive behavior, forms, interactions |
| `accessibility.md` | keyboard, screen readers, semantic HTML, accessible forms |
| `backend-data.md` | database schemas, migrations, APIs, queries, concurrency |
| `auth-security.md` | auth, RBAC, sessions, uploads, webhooks, privacy |
| `seo-performance.md` | SEO, metadata, performance, caching, observability |
| `testing-qa.md` | tests, browser verification, regression checks |
| `project-patterns.md` | SaaS, commerce, marketplace, CMS, booking, education, AI |
| `integrations.md` | payments, email, storage, search, analytics, AI, OAuth |
| `cicd-hosting.md` | CI/CD, environments, deployment, releases |
| `framework-next-react.md` | Next.js and React implementation decisions |
| `framework-vue-nuxt.md` | Vue and Nuxt implementation decisions |
| `backend-platforms.md` | Supabase, Firebase, FastAPI, PostgreSQL |
| `styling-ui.md` | Tailwind, shadcn/ui, themes, component systems |
| `stack-selection.md` | greenfield stack selection, versions, dependencies |
| `documents.md` | compatibility with the original blueprint document model |
| `sections.md` | compatibility with the original blueprint section model |

## Loading rule

Do not read every reference for every task. Load the smallest relevant set based on the detected stack and feature. If a framework/provider API is version-sensitive, inspect the installed version and consult current official documentation before implementation.

## Precedence

If a reference conflicts with the core skill or explicit user requirement:
1. explicit user requirement
2. `SKILL.md`
3. project conventions/contracts
4. relevant reference
5. generic defaults

References are guidance, not permission to add features the user did not request.
