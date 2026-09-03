# Accessibility Reference

Target practical accessibility for the whole product, not a last-minute audit.

## Semantic structure

- Use native HTML elements before custom widgets.
- One clear page heading where appropriate.
- Use landmarks (`header`, `nav`, `main`, `footer`) meaningfully.
- Associate labels with form controls.
- Use buttons for actions and links for navigation.
- Do not make clickable `<div>` elements when a button/link is appropriate.

## Keyboard

Core journeys must work without a mouse.

Check:
- logical tab order
- visible focus
- escape behavior for dialogs/menus
- no keyboard traps
- enter/space activation where expected
- focus restoration after overlays close

## Screen readers

Provide accessible names for icon-only controls. Do not use color alone to communicate state. Announce important asynchronous status changes when needed.

## Contrast and states

Check text, controls, borders, focus indicators, disabled states, and error states. Disabled controls should remain understandable; do not make critical information invisible merely because a control is disabled.

## Forms and validation

- label fields
- expose required state
- associate errors with fields
- summarize form-level errors when useful
- do not clear valid user input unnecessarily
- ensure errors are understandable without relying only on color

## Images and media

- meaningful images need useful alt text
- decorative images should not add noise to assistive technology
- provide captions/transcripts where the product requires them
- do not put essential text only inside an image

## Responsive accessibility

Test zoomed layouts, narrow screens, large text, keyboard navigation, and touch interaction. Avoid fixed heights that clip content.

## Reduced motion

Honor `prefers-reduced-motion`. Do not make essential content depend on animation.

## Dialogs, menus and popovers

Manage focus intentionally. Keep escape/close controls available. Ensure content behind an active modal is not accidentally interactive.

## Verification

Use automated checks where available, then manually test the critical journeys. Automated accessibility tooling catches only a subset of real usability problems.
