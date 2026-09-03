# Next.js + React Playbook

Use when the repository uses Next.js or React. Verify the project's installed versions and current official documentation before relying on version-sensitive APIs. Next.js currently documents both App Router and Pages Router; prefer the router already used by the repository and do not migrate a working app merely for style. citeturn0search4turn0search7

## Next.js

- Inspect whether the project uses App Router or Pages Router before editing routes.
- Preserve existing routing conventions during incremental work.
- Keep server-only operations server-side.
- Use Server Components/server rendering where it naturally reduces client JavaScript; use client components only when browser interactivity/state is needed.
- Define route-level loading and error behavior where supported by the router.
- Keep secrets out of client bundles.
- Use framework-native metadata, image, font, caching, and route primitives when they fit the project.
- Verify dynamic/static rendering assumptions rather than guessing.
- Avoid unnecessary client-side data fetching when server data access is appropriate.

## React

- Build compositionally: small feature components with clear responsibilities.
- Keep state as local as possible; lift only when multiple consumers need it.
- Avoid effects for values that can be derived during render.
- Treat effects as synchronization with external systems, not as a general workflow mechanism.
- Use stable keys for lists; never use array indexes when item identity can change.
- Keep expensive calculations out of render when measurement shows they matter.
- Preserve existing state-management conventions before introducing another library.

## Forms/data

Choose server actions, route handlers, API endpoints, or client data libraries based on the existing architecture. Validate on the server regardless of client validation.

## UI stack

If the project already uses a component system, extend it. If introducing shadcn/ui, add only required components and customize the source in the repository rather than creating a second component abstraction. shadcn/ui is intentionally open-code and composable. citeturn0search6turn0search17

## Verification

Run the repository's native lint/typecheck/test/build commands. For route changes, verify direct navigation, refresh, browser back/forward, loading/error states, and mobile behavior.

## Official references

- Next.js docs: urlNext.js Documentationhttps://nextjs.org/docs
- React docs: urlReact Documentationhttps://react.dev/
- shadcn/ui docs: urlshadcn/ui Documentationhttps://ui.shadcn.com/docs
