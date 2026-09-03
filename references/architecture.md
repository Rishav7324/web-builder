# Architecture Reference

Choose architecture from actual requirements.

1. Inspect the existing repository before deciding.
2. Prefer the smallest reliable architecture.
3. Prefer one deployable application when service boundaries are not justified.
4. Keep provider-specific integrations behind small adapters when switching providers is plausible.
5. Keep secrets server-side and configuration explicit.
6. Use typed boundaries, validation, indexes, transactions, pagination, and idempotency where appropriate.
7. Generate deployment and CI configuration only for the selected stack.

Typical layers: routes/pages, UI components, feature/domain modules, server/API, repositories/data, auth/RBAC, integrations, validation/types, tests, and deployment configuration.