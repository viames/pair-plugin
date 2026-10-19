---
name: module-workflow
description: Implement or refactor a Pair PHP application module. Use for module features and bugs, preserving the installed Pair version and the module's explicit or legacy controller flow.
---

# Pair module workflow

Read repository instructions and the affected controller, its state/model/service classes, and relevant layouts. Verify the installed Pair version and controller base; use `pair:pair` if context is unclear.

## Pair 4 modules

- New web modules extend `Pair\Web\Controller`; actions return explicit `PageResponse`, `JsonResponse`, or another supported `ResponseInterface`. Use `boot()` for web setup, respecting any specialized base-class initialization.
- Controllers coordinate input, access checks, calls to domain code, and responses. Put business rules and queries in the project's existing model/service layer; the explicit web controller does not implicitly load `model.php` or a view.
- Prepare a typed page-state object before rendering. Keep `ActiveRecord` in the persistence layer; expose selected fields through an explicit read contract when data leaves that layer. Do not turn partially loaded records into a public payload with guessed defaults.
- Layouts render prepared state and escape output. Keep SQL, business calculations, and JavaScript behavior in their owning files. Follow the application's module loading and class placement conventions.

Read [response and state examples](references/responses.md) when adding a controller, page state, or read model. For a new module, inspect the installed `vendor/bin/pair make:module` generator before hand-writing scaffolding; review its output and avoid overwriting existing files.

## Existing and legacy modules

Keep a focused fix compatible with its current `Pair\Core\Controller`, model, and view lifecycle. Do not mechanically replace imports or rename hooks. On an explicitly requested migration, use the [upgrade guide](../pair/references/upgrade.md). Support older Pair projects from their installed code rather than applying v4-only methods.

## Boundaries and verification

Resolve request IDs through the application's tenant/company/user scope before reading or changing records. Preserve access checks and transaction boundaries. Use existing ORM relations and collections where appropriate and check repeated queries on lists.

Load `pair:api-safety` for changed API behavior, `pair:frontend-forms` for substantive UI behavior, or `pair:migration-review` for schema changes. Check the affected response/state contract and failure path; preserve repository language, docblock, and delivery requirements.
