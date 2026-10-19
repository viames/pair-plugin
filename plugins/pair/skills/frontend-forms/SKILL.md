---
name: frontend-forms
description: Edit Pair PHP layouts, forms, module JavaScript, or progressive HTML regions. Use for UI behavior and presentation while preserving server rendering and existing controls.
---

# Pair frontend and forms

Read the affected controller/state or legacy view, layout, module JavaScript, and applicable UI instructions. Verify the actual PHP and browser asset versions; an installed Pair update does not guarantee that an application copied the matching assets.

## Presentation and forms

- Prepare values in typed state or the existing view/model layer. Keep layouts focused on rendering and output escaping; do not add queries, business calculations, or runtime dependencies on comments/docblocks.
- Reuse the application's shared controls, styling, modal helpers, and select conventions. `Toggle`, Select2, NiceSelect2, Tom Select, and SweetAlert2 are choices established by individual applications, not universal Pair requirements.
- Put behavior in the existing module asset and follow its build/copy pipeline. Prefer PairUI or vanilla JavaScript for new behavior; preserve a tightly coupled legacy integration when replacing it would expand the task.
- Keep semantic form actions, field names, server validation, applicable CSRF protection, labels, and keyboard focus. Review user-facing wording in the project's language.

## Progressive behavior

For new Pair 4 partial-page interactions, use existing server-rendered regions where supported; read [progressive regions](references/progressive.md) for the PHP/JavaScript contract. Keep full-page navigation or form behavior available where the flow supports it. Do not introduce a global client router or a new frontend framework for a local change.

Reuse application-specific enhancement layers already owning a screen instead of introducing a second PairUI binding alongside them. Check error and loading states, duplicate submissions, and handler lifecycle after content replacement.

Verify the affected desktop/mobile layout and keyboard interaction when the change warrants it. For asynchronous changes, also check the full-page path, replaced region, URL/history behavior where used, and actual loaded assets. Report browser checks separately from static inspection.
