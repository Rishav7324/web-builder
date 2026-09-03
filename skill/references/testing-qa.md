# Testing, QA & Browser Verification

Use this reference after implementation and whenever a feature changes behavior.

## Test pyramid

Choose tests based on risk:
- unit tests for deterministic domain logic
- integration tests for database/service boundaries
- API tests for contracts and authorization
- end-to-end/browser tests for critical journeys

Do not write tests merely to increase coverage numbers.

## Critical journey

For each product identify the smallest path that proves the product works. Examples:
- visitor → signup → onboarding → first value
- product → cart → checkout → order
- provider → availability → booking → confirmation
- author → draft → publish → public post
- AI input → generation → history/retry

That journey gets the strongest verification.

## Edge cases

Check:
- empty data
- no search results
- invalid input
- duplicate submission
- unauthorized access
- expired session
- missing resource
- provider timeout
- rate limiting
- concurrent mutation
- slow network
- mobile viewport

## Browser verification

When browser tooling is available:
1. start the app
2. open the real route
3. inspect console errors
4. exercise the primary CTA
5. test navigation/back behavior
6. verify forms and validation
7. verify authenticated boundaries
8. inspect important network failures
9. check narrow/mobile layout
10. repeat after fixes

Do not rely on screenshots alone; functional state matters.

## Build verification

Run the project's native commands discovered from package metadata/docs. Typical checks include lint, typecheck, tests, and production build.

Do not silence a failing check without understanding why it failed.

## Regression discipline

After changing shared components, auth, schema, routing, or configuration, rerun adjacent checks because the blast radius is larger.

## Test data

Use deterministic fixtures/factories. Avoid tests depending on production data or real third-party accounts unless the test is explicitly an integration environment.

## Completion report

Report what was actually verified. Distinguish:
- passed
- skipped because tooling/dependencies were unavailable
- blocked by missing external credentials
- known failing tests unrelated to the change

Never call an unverified flow fully working.
