# Styling, Tailwind & Component-System Playbook

Use when the project uses Tailwind CSS, shadcn/ui, or a similar utility/component approach.

## Existing design system first

Before adding styling:
- inspect existing tokens
- inspect theme variables
- inspect typography
- inspect spacing/radius/elevation conventions
- reuse existing components

Do not create a second design system inside the same app.

## Tailwind-style utility systems

- Keep repeated visual decisions represented by shared tokens/components where useful.
- Avoid huge unreadable class strings when extracting a component improves clarity.
- Prefer semantic component APIs over dozens of ad-hoc boolean styling props.
- Keep responsive variants intentional and test actual breakpoints.
- Do not use arbitrary values everywhere; introduce tokens for repeated values.

## shadcn/ui

When shadcn/ui is already present, treat its component source as application code that can be customized. Add only the components required by the feature. Do not blindly install the entire catalog.

When adding a component, inspect its dependencies and existing styling conventions. Keep accessibility behavior intact when customizing.

## Theme/dark mode

If dark mode exists, test both themes. Avoid hard-coded colors that break theme contrast. If no theme system exists, do not add a full theme engine unless requirements justify it.

## Typography

Use a small type scale with clear hierarchy. Avoid loading multiple font families without a reason. Verify line-height and wrapping on narrow screens.

## Visual QA

After styling significant UI:
- inspect mobile and desktop
- check focus states
- check long text
- check empty/error states
- check dark/light themes if supported
- check overflow and sticky elements
- check reduced motion

## Official documentation

Tailwind CSS: https://tailwindcss.com/docs
shadcn/ui: https://ui.shadcn.com/docs
