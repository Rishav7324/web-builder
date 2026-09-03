# Section Content Specifications — V4 (Preserved Reference)

This reference is retained from the original Web Blueprint Engine package. Its former AI-coding-prompt and wireframe sections are converted in V6 into direct implementation requirements.

## Design and UX implementation

Translate design requirements into actual:
- responsive layouts
- reusable UI primitives
- page/route composition
- typography hierarchy
- spacing system
- color/theme tokens
- interaction states
- loading/empty/error states
- keyboard/focus behavior
- mobile navigation

Do not output a coding prompt instead of implementing the interface.

## Architecture implementation

Turn the former architecture-prompt concepts into actual repository structure appropriate to the chosen stack. Avoid copying a generic tree when the project does not need it.

Typical layers may include:
- routes/pages
- UI components
- domain/feature modules
- server/API layer
- database/repositories
- authentication/authorization
- integrations
- validation/types
- tests
- deployment configuration

## Wireframe-to-code rule

If the user supplies a reference image, mockup, Figma design, or wireframe:
1. inspect the reference
2. identify layout hierarchy and interactions
3. implement the actual UI
4. preserve accessibility and responsive behavior
5. verify the rendered result

Do not stop at a wireframe description.

## Prompt package conversion

The original package generated AI coding prompts. V6 treats those prompts as internal acceptance criteria instead. The agent must execute the work directly.

For each major feature, internally determine:
- objective
- user roles
- entry points
- data dependencies
- UI states
- validation
- permissions
- failure recovery
- tests
- observability

Then implement it.

## Quality gate

Before declaring a feature complete:
- the UI is wired to real behavior
- important actions have working handlers
- server-side validation exists where needed
- authorization is enforced outside the UI
- persistent data survives refresh when persistence is expected
- tests cover important business logic
- lint/typecheck/build are clean
- browser verification passes when available

## Reference preservation

This file is intentionally retained so the original Web Blueprint Engine package's detailed section concepts remain available during migration. The canonical `skill/SKILL.md` takes precedence whenever the old document-generation workflow conflicts with the new direct-build workflow.
