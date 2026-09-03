# Product-Type Implementation Patterns

Use only the sections relevant to the requested product. These are minimum patterns, not mandatory feature dumps.

## SaaS

Think in tenant/workspace boundaries. Typical concerns: onboarding, membership/invitations, roles, usage limits, billing state, settings, auditability, and account recovery.

## E-commerce

Model product, variant, inventory, cart, order, payment, fulfillment, and customer state separately where required. Never trust browser totals. Preserve an auditable order snapshot.

## Marketplace

Separate buyer/seller permissions. Listings need ownership/moderation rules. Transactions should be independent of listing display state. Reviews should be tied to eligible transactions where the business rule requires it.

## Blog/CMS

Separate draft and published states. Public pages should be stable and indexable; editor/admin surfaces must be protected. Publishing should invalidate/update relevant caches and metadata.

## Booking

Treat availability as concurrency-sensitive. Store timezone-aware times. Prevent double booking using a transaction/constraint/locking strategy appropriate to the database.

## Education

Separate course structure from learner progress. Progress should be resilient to repeated submissions. Instructor/admin permissions must be server-enforced.

## Portfolio/content site

Prioritize content hierarchy, responsive media, SEO, accessibility, contact conversion, and fast initial rendering. Avoid unnecessary backend infrastructure.

## Admin dashboard

Treat it as an operational tool: filters, bulk actions, safe destructive confirmations, auditability, clear status indicators, pagination, and role boundaries matter more than decorative charts.

## AI application

Separate provider/model selection from product logic. Define input limits, timeout/retry behavior, streaming behavior, usage accounting, history/privacy policy, and abuse controls. Never expose provider secrets to the browser.

## Membership/community

Model membership status independently from authentication. Gate server-side. Handle subscription changes, expiration, cancellation, and restoration explicitly.

## General rule

Do not implement every item listed here automatically. Select the smallest set that satisfies the user's actual product requirements.
