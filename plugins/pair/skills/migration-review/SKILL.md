---
name: migration-review
description: Create or review Pair application database schema changes and data migrations. Use for tables, columns, indexes, constraints, or backfills; major framework upgrades use the Pair entry skill.
---

# Pair database migrations

Read the application's migration conventions, runner, database version, and the entity's actual readers and writers. Use the existing naming and SQL style; do not assume every Pair application uses the same runner or that its deploy script applies migrations.

## Design and compatibility

- Confirm that an existing field or relation cannot satisfy the request. Add a new migration rather than rewriting an applied one.
- Review historical rows, defaults, nullability, uniqueness, foreign keys, and indexes against real filters and joins. Check duplicates and invalid legacy values before introducing constraints.
- Preserve compatibility between old and new application instances when deployment overlaps. Separate schema expansion, data backfill, consumer changes, and destructive cleanup when sequencing matters.
- For significant backfills, define bounded batches, restart behavior, expected counts, and a preview query. Do not rewrite historical accounting or audit records from current catalog values.
- MySQL DDL may commit implicitly; wrapping it in a transaction is not a reliable rollback plan. Specify whether recovery is reversible SQL, a compensating migration, or restoration from a verified backup.

## Affected contracts and delivery

Review ORM bindings/casts and initialization, typed page/read models, validation, forms, lists, API schemas, exports, and scheduled jobs that use the changed data. Load only the relevant companion skill when implementation crosses one of those boundaries.

Validate syntax and the meaningful before/after data invariants using the project's disposable test database or other authorized environment. Writing a migration does not by itself authorize applying it to production. When application or deployment is already requested, carry out the authorized sequence without asking again merely because a migration is involved; unresolved destructive scope still requires clarification.

Report the migration path, whether it was actually applied and where, deployment order, backfill status, and realistic recovery limits. Keep file creation, successful execution, and verified production postconditions distinct.
