# Data and runtime

Use the relevant section for Pair persistence, configuration, cache, jobs, diagnostics, localization, or extension work. Locate the existing application owner and installed implementation; do not load every runtime component for a local change.

## ORM, queries, and read contracts

Inspect `Orm/ActiveRecord.php`, `Query.php`, `Collection.php`, `Database.php`, and one real model using the behavior. Preserve binds, nullability, date/time casts, relation loading, tenant scope, and transaction boundaries. Prefer existing relation/collection helpers when they express the query; do not assume another framework's eager-loading API exists. Measure repeated queries on changed list flows. Use `pair:migration-review` for schema/backfills and `pair:api-safety` for public serialization. Schema changes are not a routine requirement for a query fix.

## Configuration and caches

Resolve the actual `Core/Env.php` keys and initialization order. Optional drivers and integrations must remain optional. Never dump `.env` or substitute application credentials for test fixtures.

Inspect `Cache/Cache.php` and the configured file/Redis store. Preserve prefixes, TTL units, invalidation on writes, and user/tenant boundaries in keys. File metadata caches and `Http/HttpCache.php` have different owners and semantics from the data cache. Avoid a global cache clear as a routine test, and do not confuse cached private data with publicly cacheable HTTP output.

## Jobs and diagnostics

`Helpers/Schedule.php` schedules callbacks; inspect the application's real entrypoint, cron registration, timezone, overlap controls, and persistence before treating a callback as a queue worker. Prevent duplicate ownership when old and new applications share a job. Use bounded fixtures for changed job logic; enabling a schedule or invoking it against live data requires the corresponding user scope.

For logging and observability, inspect `Core/Logger.php`, `Observability.php`, `LogEventSanitizer.php`, the selected service adapter, and related `Helpers/Log*` classes/assets. Keep production log visibility and redaction. Debug headers, SQL traces, and browser log bars must not expose credentials, personal data, or internal errors. Distinguish collection/export failure from application failure; do not enable a new exporter just to test formatting.

## Extensions, packages, and helpers

Pair runtime extensions register explicitly through `RuntimeExtensionInterface` and `Application::registerRuntimeExtension()`; adapters use `AdapterRegistry` / `Application::setAdapter()`. This is different from installable ZIP/manifest packages in `src/Packages/`. Preserve each mechanism's initialization, validation, and trust boundary instead of inventing auto-discovery or a new service container.

Reuse `Helpers/Translator.php`, `Models/Locale.php`, `translations/`, and existing date, chart, report, and template helpers. Check the installed date-format convention and timezone; ICU patterns and PHP format strings are not interchangeable. For localization/UI changes, keep translation keys and actual loaded browser strings aligned. Use the closest tests or a focused isolated probe, and report missing runtime proof explicitly.
