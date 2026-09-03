# Authentication, Authorization, Security & Privacy

Use this reference whenever accounts, roles, uploads, payments, webhooks, private data, or privileged operations exist.

## Threat model first

Identify:
- anonymous users
- authenticated users
- privileged/admin users
- external providers/webhooks
- untrusted browser input
- sensitive data
- high-impact actions

Then define who can perform each mutation.

## Authentication

Use the chosen provider/framework correctly. Prefer secure, established session mechanisms over inventing cryptography.

Protect:
- session cookies
- refresh tokens
- password reset tokens
- email verification tokens
- API keys

Never log credentials or tokens.

## Authorization

Authorization must be enforced server-side. Check ownership/role/permission at the data or service boundary, not only at route rendering.

For multi-tenant systems, every query involving tenant data must have an explicit tenant boundary.

## RBAC/permissions

Keep permission names stable and centralized. Avoid scattering role strings across the application. Privileged actions should generate useful audit records when appropriate.

## Input safety

Treat all browser input, query parameters, headers, uploaded files, webhook bodies, and external API responses as untrusted.

Validate:
- type
- size
- allowed values
- ownership references
- file type/size
- URL schemes where URLs are accepted

## Web security

Apply the protections appropriate to the stack:
- CSRF/origin validation
- secure cookies
- security headers
- safe redirects
- output encoding
- XSS-safe rendering
- rate limiting
- abuse controls
- dependency updates

Do not disable security middleware just to make a development error disappear.

## Uploads

Use server-side validation, size limits, safe object names, access control, and content-type verification. Do not execute uploaded files. Keep private objects private.

## Webhooks

Verify signatures before processing. Make handlers idempotent. Store provider event IDs when useful to prevent duplicate processing. Return appropriate responses and process expensive work asynchronously when needed.

## Payments

Never trust client-provided prices, plan IDs, payment status, or success redirects. Reconcile important state from the payment provider/webhook. Keep payment provider secrets server-side.

## Privacy

Collect only required data. Avoid logging personal data unnecessarily. Redact secrets and sensitive fields from errors and analytics. Define deletion/retention behavior when the product requires it.

## Security review before completion

Check for:
- exposed secrets
- insecure direct object references
- missing tenant filters
- client-only authorization
- unsafe redirects
- unvalidated uploads
- missing webhook verification
- excessive error disclosure
- debug endpoints
- accidental production credentials
