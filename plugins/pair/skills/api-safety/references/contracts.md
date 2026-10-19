# Pair 4 API contracts

Use the installed `src/Api` and its tests as the method authority; older Pair versions and legacy helpers differ.

## Explicit validation and response flow

`Request::validateOrResponse()` returns validated data or `ApiErrorResponse`; `validateObjectOrResponse()` returns `RequestData` or `ApiErrorResponse`. Return an error response before using the result as domain input. `RequestData::fromArray()` maps already validated values; implementing it does not install validation rules.

`ApiResponse::jsonResponse()` and `errorResponse()` produce response objects. Legacy methods such as `respond()` may emit directly. Preserve the endpoint's dispatch model and public envelope. `ApiController` performs API setup in `boot()` and retains an `_init()` compatibility hook in current Pair 4: inspect the base and preserve required parent initialization before changing either hook.

## Read models and CRUD

`ReadModel` includes `JsonSerializable` plus `toArray()`; satisfy both, using `ArraySerializableData` where the existing pattern does. `MapsFromRecord` supplies explicit record mapping. Inspect the installed generator for a complete example.

`CrudResourceConfig` accepts an explicit `readModel` or a legacy `resource`; current `CrudController` throws when neither exists. Prefer typed read models for new v4 code. Review each public field and related-record mapping; do not restore a raw record serialization fallback.

Review `searchable`, `sortable`, `filterable`, `includes`, `includeReadModels` / `includeResources`, page limits, and validation rules where used. Use an available `includePreloader` for bulk relation loading when needed, and verify query counts rather than assuming N+1 is solved. Configuration is not proof of tenant isolation or operation authorization: inspect the actual query and mutation path.

The current generic CRUD write path maps incoming bound properties; output read models and `filterable` do not constitute a write allowlist. Non-empty `rules.create` / `rules.update` maps invoke validation that returns only rule-named fields; empty maps skip that step and leave bound input fields eligible. Review both operations and keep server-owned fields out of caller input. Check the installed validator's supported rules and enforce domain enums explicitly rather than assuming an unrecognized rule validates them. Do not invent a configuration key to enforce write restrictions.

`OpenApi\SpecGenerator` can derive response schemas from configured read models. Verify generated schemas against actual responses and the contract consumed by clients.
