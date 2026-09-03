# Stack Selection & Version Intelligence

Use this reference before starting a greenfield project or when the requested stack is ambiguous.

## First rule: inspect before selecting

For an existing repository, do not replace the stack just because another stack is preferred. Read package manifests, lockfiles, config, source conventions, and deployment settings first.

## Greenfield selection matrix

### Next.js + React
Prefer when the product needs a full-stack React application, strong routing/SEO, server rendering, or a single deployable web app.

### React without Next.js
Prefer when the repository is already a client-focused React application or the product does not benefit from a full-stack framework.

### Vue + Nuxt
Prefer when the team/product direction is Vue-oriented and the project benefits from file-based routing, SSR, or full-stack conventions.

### Supabase
Prefer when a managed Postgres + authentication + storage/realtime platform materially reduces product infrastructure. Still design database policies and server boundaries carefully.

### Firebase
Prefer when the product fits Firebase's managed services and document-oriented access patterns, especially when rapid client integration is valuable. Treat security rules as first-class application code.

### FastAPI
Prefer for Python-first APIs, data/ML workloads, or systems where Python ecosystem integration is a primary requirement.

### PostgreSQL
Prefer for relational, transactional, multi-entity systems unless requirements clearly favor another database model.

## Version intelligence

Never hard-code a framework API from memory when the feature is version-sensitive. Inspect the installed version and consult current official documentation when needed.

Do not upgrade major versions as a side effect of an unrelated feature. If an upgrade is necessary, isolate it as a deliberate change and run the full validation suite.

## Dependency policy

Before adding a dependency:
1. check whether the repository already solves the problem
2. prefer platform/framework-native capabilities
3. assess maintenance/security/license/size impact
4. add the smallest package that solves the requirement
5. verify installation and lockfile changes

Avoid dependency duplication such as multiple date libraries, HTTP clients, state managers, or component systems without a concrete reason.
