# Security Reference

Apply security at trust boundaries, not only in the UI.

- Validate and sanitize untrusted input server-side.
- Enforce authorization/RBAC at the data/API boundary.
- Keep secrets out of source control and client bundles.
- Use secure cookies/tokens and appropriate CSRF/origin protection.
- Add rate limits to abuse-prone endpoints.
- Secure file uploads and external callbacks/webhooks.
- Add security headers where supported.
- Log privileged/auditable actions without logging secrets.
- Use least privilege and fail closed.
- Never claim an integration works when credentials or external configuration are missing.
