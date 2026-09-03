# Frontend, UI & UX Engineering

Use for page structure, component architecture, responsive behavior, forms, interaction states, visual hierarchy, and frontend performance.

## Start from journeys

Design around user goals, not isolated screens. For each primary journey define:
- entry point
- intent
- required data
- primary action
- success state
- validation/error state
- recovery path
- exit/share/bookmark behavior

## Component strategy

Prefer a layered structure:
- page/route composition
- feature components
- reusable UI primitives
- tokens/theme

A component should have one clear responsibility. Do not extract every `<div>` into a component.

## Responsive rules

Design for the smallest realistic viewport first, then enhance for larger screens.

Check:
- navigation collapse
- text wrapping
- tables and overflow
- forms and keyboards
- dialogs/sheets
- touch targets
- image cropping
- sticky elements
- landscape/mobile edge cases

Do not solve mobile overflow by globally hiding content.

## Interaction states

Every interactive control should have, where applicable:
- default
- hover
- focus-visible
- pressed
- disabled
- loading
- success
- error

Every async view should consider:
- loading
- empty
- partial data
- error
- retry

## Forms

- label every field
- use appropriate input types
- validate close to the source and again on the server
- preserve user input after recoverable errors
- show actionable messages
- disable duplicate submission while a request is pending
- expose server errors near the relevant field or form
- never rely on placeholder text as the only label

## Visual hierarchy

A good page should make the next useful action obvious. Establish hierarchy through spacing, type scale, grouping, alignment, contrast, and restrained emphasis rather than excessive decoration.

## Navigation

Keep primary navigation stable and predictable. Preserve browser back/forward semantics. Use URLs for meaningful application state that should be shareable or bookmarkable.

## Tables and dense data

For large datasets:
- provide search/filter/sort where useful
- preserve column meaning on narrow screens
- use pagination or virtualization when needed
- provide empty and no-result states
- keep destructive actions visually distinct

## Motion

Animation should communicate state or hierarchy, not delay the user. Respect reduced-motion preferences. Avoid long page-load animations and motion that blocks interaction.

## Design-system discipline

If the repository already has tokens/components, extend them instead of introducing a second visual language. For greenfield projects, define a small token set for color, spacing, typography, radius, elevation, and motion.

## Avoid generic-AI UI

Do not automatically add:
- random gradients
- glowing borders
- excessive glassmorphism
- oversized headings on every page
- meaningless animated blobs
- decorative cards around every sentence

Visual decisions must support the product's brand and task.
