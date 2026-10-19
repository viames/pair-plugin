---
name: crud-review
description: Complete or review generated Pair CRUD modules and resources. Use for scaffolding output or a requested CRUD review, rather than every ordinary module edit.
---

# Pair CRUD completion

Identify the installed Pair version, generator, generated files, and nearest mature implementation. Current Pair 4 provides `vendor/bin/pair make:module`, `make:api`, and `make:crud`; legacy applications may use a `crafter` module. Inspect the installed generator's options and output before choosing one, and do not use `--force` to overwrite existing work without a concrete need.

## Review the generated behavior

- Check the actual route, registration, loading, and controller initialization. New Pair 4 web modules use explicit responses and typed page state; legacy modules retain their established lifecycle unless migration is requested.
- Keep persistence objects distinct from page/API read contracts. Generated field types, bindings, read models, and validation rules need domain review; schema scaffolding cannot infer business policy.
- Verify permissions and tenant/company/user scope for each exposed list, detail, create, update, delete, and related-record operation. Scope list queries as well as individual lookups.
- Review accepted write fields and server-owned values independently of response fields. For API CRUD, use `pair:api-safety` and its contract reference to check input validation, explicit serialization, includes, and OpenAPI.
- Review delete constraints, transactional multi-record writes, uniqueness, and retry behavior where relevant. Add schema work through `pair:migration-review` only when required.
- Remove unused fields, placeholders, and generator leftovers. Reuse the application's form controls and asset initialization; use `pair:frontend-forms` for substantive UI changes.

## Verify completion

Exercise only the operations actually exposed, including denied ownership and invalid input. A generated test containing `assertTrue(true)` does not verify the module: replace or omit that placeholder according to the application's test conventions and add meaningful coverage for changed behavior.

Keep the generated structure when it already fits. Report remaining domain decisions explicitly instead of treating successful generation as finished CRUD behavior.
