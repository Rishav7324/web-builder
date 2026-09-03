# Architecture & Engineering Decisions

Use this reference when choosing application boundaries, folders, runtime responsibilities, caching, jobs, or service architecture.

## Decision hierarchy

Choose the least complex architecture that satisfies:
1. product requirements
2. security boundaries
3. expected traffic/data volume
4. deployment constraints
5. team/maintenance reality

Do not introduce microservices because they sound advanced. A modular monolith is the default for most early products.

## Architecture checklist

- Identify public, authenticated, privileged, and internal routes.
- Identify trusted vs untrusted boundaries.
- Keep business rules independent from UI components.
- Keep database access behind a predictable data/service boundary.
- Keep provider SDK usage behind adapters when replacement is plausible.
- Keep secrets and privileged operations server-side.
- Define ownership for each domain entity.
- Define transaction boundaries for multi-write operations.
- Define asynchronous work and retry policy.
- Define cache ownership and invalidation rules.

## Common shapes

### Small website
Prefer a single frontend application with static/server-rendered pages and a small server boundary only when forms, email, CMS, or protected operations require it.

### Full-stack SaaS
Typical boundaries:
- presentation/routes
- application/service layer
- domain rules
- persistence/repositories
- integrations
- background jobs

Do not create separate deployables unless there is a concrete need.

### Monorepo
Use packages for genuinely shared code:
- UI primitives
- schemas/types
- configuration
- SDK/client
- domain utilities

Avoid a giant shared package that becomes a dumping ground.

## Server/client boundary

Client code may handle presentation and user interaction. Server code must own:
- authorization
- secrets
- privileged provider calls
- final pricing/permission decisions
- sensitive database operations
- webhook verification

Never rely on client state for authorization.

## API design

For each endpoint/action define:
- input schema
- authentication requirement
- authorization rule
- validation
- success response
- known error responses
- idempotency requirement
- rate-limit requirement
- logging/observability behavior

Prefer stable domain-oriented contracts over leaking raw database tables.

## Caching

For every cache, answer:
- what is cached?
- for whom?
- how long?
- what invalidates it?
- is stale data acceptable?

Never cache user-specific or permission-sensitive data in a shared cache without a correct key and isolation strategy.

## Background jobs

Use jobs for email, large exports, media processing, scheduled tasks, expensive AI work, and other work that should not block the request.

Jobs should be:
- idempotent where possible
- retryable
- observable
- bounded by timeouts
- safe against duplicate delivery

## Database transactions

Use a transaction when several writes must preserve one invariant. Do not wrap unrelated expensive network calls inside a database transaction.

## Provider adapters

When using payments, AI, storage, email, search, or analytics, isolate provider-specific code when there is a realistic possibility of changing vendors. Keep the adapter small and expose domain-level operations.

## Anti-patterns

Avoid:
- microservices without operational justification
- duplicated validation with conflicting rules
- database queries directly scattered across UI components
- global mutable state for server data
- hidden network calls inside generic UI primitives
- environment variables read everywhere without validation
- catch-and-ignore error handling
- unbounded queries
- synchronous request chains for long-running work
