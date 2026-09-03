# Vue + Nuxt Playbook

Use when the repository uses Vue or Nuxt. First inspect the installed version and existing routing/state conventions. Do not perform a framework migration unless explicitly required.

## Vue

- Prefer composition around features rather than giant components.
- Keep reactive state close to the feature that owns it.
- Use computed state for derived values instead of duplicated mutable state.
- Use watchers for genuine side effects/synchronization, not routine derivation.
- Keep API/data access separate from presentational components.
- Preserve the project's existing state management approach before introducing a new store library.

## Nuxt

- Inspect the Nuxt major version before using APIs because conventions can differ significantly between major releases.
- Preserve file-based routing and server conventions already used by the project.
- Keep secrets and privileged operations on the server.
- Use SSR/server rendering where it benefits public content, SEO, or initial loading.
- Be explicit about client-only dependencies and browser APIs.
- Use framework-native data fetching/caching patterns when they match the application.
- Verify server/client hydration behavior after changing data-dependent components.

## SEO/content

For public content, verify generated metadata, canonical URLs, sitemap behavior, structured data, and SSR output rather than relying on client-side rendering alone.

## Verification

Run the project's native lint, typecheck, tests, and build. For SSR routes, verify direct refresh and navigation, hydration, error states, and mobile behavior.

## Official documentation

Vue: https://vuejs.org/
Nuxt: https://nuxt.com/docs
