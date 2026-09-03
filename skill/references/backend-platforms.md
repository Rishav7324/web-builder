# Backend Platform Playbook

Use this reference when the stack includes Supabase, Firebase, FastAPI, or a managed backend platform.

## Supabase

Treat Postgres as the source of truth when using Supabase. Use Row Level Security for tenant/user data where appropriate. Keep service-role credentials server-side. Separate public client configuration from privileged server configuration.

For storage, enforce object ownership/access policies rather than relying only on hidden UI. For Realtime, subscribe only to data the current user is authorized to receive.

For auth, preserve the provider's session model and enforce authorization in database policies and/or server boundaries as appropriate.

## Firebase

Choose the Firebase services actually required. Keep Admin SDK credentials server-side. Define Firestore/Storage security rules as part of the feature, not as an afterthought.

When using Firestore, design queries around known access patterns because query shape and indexes influence the data model. Avoid fetching entire collections for UI filtering.

For Cloud Functions/server code, keep privileged operations isolated and observable.

## FastAPI

Structure non-trivial APIs around routers, schemas, dependencies, services/domain logic, and persistence rather than placing all logic in route handlers.

- validate request bodies and parameters with typed schemas
- define explicit response models
- enforce authentication/authorization through dependencies or service boundaries
- use async I/O where it provides real benefit
- keep blocking operations out of async request paths
- centralize exception handling and safe error responses
- generate/verify OpenAPI behavior through actual tests

## PostgreSQL

Prefer relational modeling for transactional products. Use foreign keys, unique constraints, check constraints, indexes, transactions, and appropriate isolation/concurrency controls. Inspect real query patterns before adding indexes. Do not use application code as the only enforcement layer for invariants that the database can guarantee.

## Platform selection

Do not select a backend service simply because it is popular. Compare:
- existing repository constraints
- auth needs
- database model
- storage
- realtime requirements
- server-side logic
- deployment target
- cost/scale
- vendor lock-in
- migration path

## Official documentation

Supabase: https://supabase.com/docs
Firebase: https://firebase.google.com/docs
FastAPI: https://fastapi.tiangolo.com/
PostgreSQL: https://www.postgresql.org/docs/
