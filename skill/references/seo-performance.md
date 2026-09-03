# SEO, Performance & Observability Reference

## SEO foundation

For indexable public pages:
- unique title
- useful meta description
- canonical URL
- semantic heading hierarchy
- descriptive link text
- crawlable internal links
- OpenGraph/social metadata
- sitemap
- robots policy
- appropriate structured data

Private, admin, account, draft, and utility routes should not accidentally become indexable.

Do not manufacture structured data that does not match visible page content.

## Content architecture

Use stable, human-readable URLs. Avoid unnecessary query parameters for canonical content. Preserve old URLs with redirects when a redesign changes routes.

## Performance model

Optimize the largest real bottleneck first. Inspect before adding complexity.

Check:
- initial HTML response
- JavaScript shipped to the client
- image dimensions/formats
- font loading
- layout shift
- long tasks
- API latency
- database query time
- cache hit behavior

## Frontend performance

- server-render content when useful
- split code by route/feature
- lazy-load non-critical modules
- size images correctly
- reserve image dimensions
- avoid shipping heavy libraries for trivial tasks
- minimize client state
- debounce high-frequency requests
- virtualize very large lists when appropriate

## Backend performance

- use indexes for common query patterns
- avoid N+1 queries
- paginate large datasets
- cache expensive stable reads where safe
- avoid repeated provider calls
- use background jobs for long work
- set timeouts for external dependencies

## Caching

Document cache ownership, TTL, invalidation, and whether stale data is acceptable. Be especially careful with personalized data.

## Observability

Production apps should have useful signals appropriate to their size:
- structured logs
- request IDs/correlation IDs
- error reporting
- health/readiness checks
- latency/error metrics
- background-job failure visibility

Never log passwords, tokens, API keys, payment credentials, or unnecessary personal data.

## SEO/performance verification

For important pages inspect generated metadata, response behavior, images, links, and runtime errors. Use platform/framework-specific analyzers when available.
