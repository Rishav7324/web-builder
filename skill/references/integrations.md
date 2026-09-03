# Third-Party Integrations Reference

Use this reference for payments, email, storage, search, analytics, AI, maps, OAuth, and external APIs.

## Integration boundary

For each provider define:
- server/client location
- credentials and environment variables
- timeout
- retry policy
- error mapping
- rate limits
- idempotency behavior
- webhook/event handling
- local development strategy
- observability

Keep provider SDK calls out of reusable UI components.

## Environment configuration

Validate required environment variables at startup or at the integration boundary. Keep public and secret configuration clearly separated. Never commit credentials.

## Payments

Use provider-hosted/tokenized payment flows when appropriate. Recalculate authoritative totals server-side. Verify webhooks. Make payment events idempotent. Never mark an order paid solely because the browser returned to a success page.

## Email

Use a transactional email provider for production mail. Keep templates versioned. Make sending failures observable. Do not send email synchronously inside a request when latency/retry behavior would be problematic.

## Object storage

Use signed URLs or controlled server endpoints for private files. Validate uploads. Store metadata and ownership in the application database.

## Search

Start with database search when requirements are small. Introduce a search service only when relevance, scale, typo tolerance, or indexing requirements justify it. Keep indexing asynchronous when appropriate.

## Analytics

Track meaningful product events rather than every click. Avoid sensitive/personal data unless explicitly required and legally appropriate. Keep analytics optional when it should not block core functionality.

## AI providers

Use a provider/model adapter. Define:
- model capability assumptions
- token/input limits
- timeout
- retry policy
- streaming behavior
- cost/usage accounting
- safety/abuse controls
- data retention expectations

Never send secrets or unnecessary private data to a model provider.

## OAuth/social login

Validate redirect URIs, state/nonce where applicable, and provider identity claims. Do not treat an email address alone as proof of authorization to an existing privileged account.

## External APIs

Treat external responses as untrusted. Validate response shape. Add timeouts. Map provider errors to safe domain errors. Avoid cascading failures by making optional integrations fail gracefully.

## Webhooks

Verify authenticity, deduplicate events, persist event IDs when useful, and return quickly after safe acceptance. Move expensive processing to jobs.
