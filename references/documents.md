# Document Content Specifications — V4 (Preserved Reference)

This reference is retained from the original Web Blueprint Engine package. It contains the detailed Foundation and Advanced document specifications that informed the Direct Build edition.

## How V6 uses this reference

The current canonical `skill/SKILL.md` supersedes the original requirement to generate PRD/TRD documents. Agents should use the specifications below as **internal implementation checklists** and implement the corresponding product behavior directly.

## Foundation areas

### Product requirements
Implement the equivalent of:
- executive product context
- problem/user analysis
- personas and anti-personas where relevant
- jobs-to-be-done
- user stories
- goals and non-goals
- measurable success metrics
- risks and assumptions

Do not generate a PRD unless the user explicitly asks for one.

### Technical requirements
Implement the equivalent of:
- concrete technology stack
- architecture and data flow
- security requirements
- performance targets
- accessibility/WCAG requirements
- applicable privacy/payment compliance
- third-party integrations
- operational constraints

Do not generate a TRD unless explicitly requested.

## Product-flow areas

Translate the original blueprint's app-flow concepts into actual routes, states, permissions, transitions, and user journeys.

For each important journey implement:
1. entry point
2. authentication/authorization requirements
3. validation
4. happy path
5. loading state
6. empty state
7. failure state
8. success confirmation
9. persistence
10. recovery/back navigation

## Data and API requirements

For every persistent feature:
- define entities and relationships
- add database constraints and useful indexes
- validate server-side
- enforce authorization at the data boundary
- paginate unbounded lists
- use transactions for multi-write invariants
- use idempotency for payments/webhooks where appropriate
- return consistent typed errors

## Security requirements

Apply least privilege, secure secret handling, input validation, authentication, authorization/RBAC, rate limiting where applicable, secure uploads, security headers, audit logging for privileged operations, and OWASP-aligned mitigations.

## Accessibility requirements

Use semantic HTML, keyboard access, visible focus, labels, sufficient contrast, reduced-motion support, meaningful error messaging, and accessible touch targets.

## SEO requirements

For public pages implement unique metadata, canonical URLs, Open Graph metadata, structured data when appropriate, sitemap, robots rules, semantic headings, internal linking, image alt text, and noindex for private/admin/draft content.

## Business and growth requirements

When relevant, implement analytics events, conversion points, onboarding, retention hooks, subscription boundaries, referral/invite mechanics, and measurable business KPIs.

## Original package compatibility

This file intentionally remains as a reference so agents upgrading an existing V4 project do not lose the detailed requirement categories. The canonical V6 skill decides whether each item becomes code, configuration, tests, or internal reasoning.
