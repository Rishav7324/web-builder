# CI/CD Pipeline Blueprint + Hosting Plan — Content Specifications

This reference preserves the deployment, CI/CD, hosting, workflow, secrets, release, rollback, monitoring, and verification guidance from the original Web Blueprint Engine package.

The canonical `skill/SKILL.md` is authoritative: implement these requirements directly in the repository instead of generating a blueprint document.

## Implementation rules

- Create actual YAML workflows when the project needs CI/CD.
- Configure the selected hosting provider directly when configuration belongs in the repository.
- Document secret names only; never commit secret values.
- Add health checks and post-deploy verification when appropriate.
- Use safe, provider-appropriate rollback procedures.
- Keep staging and production behavior explicit when multiple environments are required.
- Include lint, typecheck, tests, and build in the quality gate when supported by the stack.
- Add package/mobile release automation only when the project scope requires it.
