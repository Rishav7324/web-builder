# Backend, Database & API Reference

Use for server actions, APIs, schemas, migrations, queries, data integrity, and scaling.

## Data modeling

Model business entities from actual workflows. For each entity define:
- identifier strategy
- required/optional fields
- ownership
- lifecycle/status
- relationships
- uniqueness constraints
- deletion/archive behavior
- timestamps

Prefer database constraints for invariants that must always hold.

## Migrations

- use versioned migrations
- make migrations reproducible
- avoid destructive changes without an explicit migration strategy
- backfill data before removing old fields when necessary
- test migrations against representative data
- keep application and schema compatibility during rolling deployments

## Queries

- select only needed fields
- paginate unbounded collections
- add indexes based on real filters/sorts/joins
- inspect expensive queries
- avoid N+1 access patterns
- use transactions for related writes
- do not put network requests inside database transactions unless unavoidable

## API contract

Every endpoint/action should specify:
- input
- authentication
- authorization
- validation
- success shape
- error semantics
- idempotency
- rate limits

Prefer typed schemas at the boundary. Keep database implementation details out of public API contracts.

## Errors

Distinguish at least:
- invalid input
- unauthenticated
- unauthorized
- not found
- conflict
- rate limited
- dependency failure
- unexpected server failure

Return safe client-facing messages while retaining useful server-side diagnostics.

## Pagination

Use cursor pagination for frequently changing large datasets when appropriate. Offset pagination is acceptable for small/admin datasets where stable ordering is sufficient.

## Idempotency

Use idempotency keys or unique constraints for operations that may be retried, especially payments, webhooks, provisioning, and external side effects.

## Concurrency

Consider race conditions around:
- inventory
- booking slots
- counters/credits
- membership changes
- duplicate submissions
- webhook delivery

Use database constraints, transactions, locks, or compare-and-set semantics as appropriate.

## Files

Store metadata in the database and binary data in object storage when appropriate. Validate file type/size server-side. Generate safe names. Do not trust client-provided MIME types or extensions.

## Seed data

Seed only deterministic development/test data. Never put real credentials or production personal data in seeds.
