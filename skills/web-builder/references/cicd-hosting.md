# CI/CD Pipeline Blueprint + Hosting Plan — Content Specifications (V4)

This file is preserved from the original Web Blueprint Engine package and is now used as an implementation reference. When its original document-generation instructions conflict with the canonical `skill/SKILL.md`, the canonical skill wins: implement the underlying CI/CD and hosting configuration directly in the repository instead of generating a document.

For the complete original specification, see the source package. This reference remains available so agents can reuse its detailed CI/CD, hosting, workflow, secrets, release, rollback, monitoring, and deployment guidance without losing the original package content.

## Compatibility note

The canonical skill has converted the former blueprint/document workflow into a direct-build workflow. Therefore:
- YAML workflows should be created as actual files when required.
- Hosting configuration should be implemented for the selected provider.
- Secrets should be documented by variable name only, never with values.
- Health checks and post-deploy verification should be real.
- Rollback must be safe and provider-appropriate.
