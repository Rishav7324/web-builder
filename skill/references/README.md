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
| `documents.md` | compatibility with the original blueprint document model |
| `sections.md` | compatibility with the original blueprint section model |

## Loading rule

Do not read every reference for every task. Load the smallest relevant set, implement, then return to the core verification loop.

## Precedence

If a reference conflicts with the core skill or explicit user requirement:
1. explicit user requirement
2. `SKILL.md`
3. project conventions/contracts
4. relevant reference
5. generic defaults

References are guidance, not permission to add features the user did not request.
