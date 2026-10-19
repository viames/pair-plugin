---
name: api-safety
description: Change or review a Pair PHP endpoint, request validation, authorization, serialization, or API contract. Use when endpoint behavior or its consumers are affected.
---

# Pair API changes

Read repository instructions, the installed Pair API classes, the owning endpoint, and its nearest consumer or contract. Distinguish `Pair\Api\ApiController` / `CrudController` from web-controller AJAX actions and legacy API flows; do not assume identical helpers, hooks, or envelopes.

## Request and access boundary

- Validate method, content type, payload shape, and domain values using the installed request APIs. `RequestData` is a mapping contract, not automatic validation; handle explicit validation-error responses before mutation.
- Resolve every requested entity within its tenant/company/user scope. Check operation permissions and ownership before reading or mutating it, including list filters, exports, and related-record includes.
- Review writable fields separately from output fields. Prevent caller-controlled ownership, role, or system fields from entering a write merely because the ORM binds them.
- Keep business rules in the owning model/service layer. Preserve transaction boundaries and use the existing idempotency mechanism where clients can retry mutations.
- Retain the endpoint's authentication model: cookie/session writes need the applicable CSRF protection; bearer/mobile endpoints must preserve their token and refresh semantics. Do not log credentials or sensitive payloads.

## Response and contract

For Pair 4, prefer explicit response objects and intentional read models. Inspect [Pair 4 API contracts](references/contracts.md) when changing serialization, validation helpers, or auto-CRUD. Preserve older contracts for a focused legacy fix rather than silently migrating clients.

Update the actual contract owner: a checked-in OpenAPI file, generator configuration, or another repository-defined source. If generated, update its source and regenerate through the project's workflow. Verify that status codes, error bodies, nullability, and exposed fields match runtime behavior.

Check success, malformed input, forbidden ownership, and missing resources for the changed flow. Include retry or partial-failure checks when mutation behavior requires them. For auth changes involving native clients, use the [authentication and mobile reference](../pair/references/auth-mobile.md) to locate the affected platform's contracts, including repository-only files absent from Composer dist.
