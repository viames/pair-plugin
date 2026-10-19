# Pair plugin for Codex

Version-aware workflows for Pair PHP applications, with routing to the framework repository's own instructions for framework development.

By **Viames Marino** · **MIT** · **0.3.0**

This directory is the standalone plugin. Public source and marketplace: [viames/pair-plugin](https://github.com/viames/pair-plugin). Install with `codex plugin marketplace add viames/pair-plugin`, then `codex plugin add pair@viames-pair`. Start a new chat. The release's marketplace ZIP includes the separate installable catalog; this standalone package contains only the plugin.

## Included skills

- `pair:pair`: identify the installed version and route any Pair capability to its owning workflow or focused reference; handle requested major-version upgrades.
- `pair:module-workflow`: application modules, explicit responses, typed state, and focused legacy fixes.
- `pair:api-safety`: endpoint validation, access, write boundaries, read contracts, and OpenAPI.
- `pair:frontend-forms`: forms, shared controls, and progressive HTML regions.
- `pair:migration-review`: database schema changes and data backfills.
- `pair:crud-review`: generated CRUD completion and targeted review.

`project-conventions` is consolidated into `pair`. When switching distributions, keep one active Pair plugin to avoid duplicate discovery. Existing user authorization and repository instructions remain applicable.

Details for response/state contracts, API contracts, progressive regions, upgrades, data/runtime, authentication/mobile, integrations, and PWA/push live in linked references and are read only when needed. The [capability map](skills/pair/references/capabilities.md) covers the Pair 4 source areas and distinguishes Composer dist from repository-only documentation and native libraries. The plugin adds no MCP servers or application integrations.

## Models and scope

The skills are model-independent instructions. They neither select the GPT model running Codex nor change the model used by a Pair application's `OpenAIClient`. The host supplies model availability, reasoning controls, tools, and execution permissions. No model-specific hooks, API credentials, or runtime dependencies are required by this plugin.

Descriptions and references follow current [OpenAI skill guidance](https://developers.openai.com/plugins/build/skills) and the [GPT-6 skill review guidance](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra): focused discovery, conditional references, explicit user intent, and completion of authorized work. This is a design alignment, not a claim of measured performance on every GPT model. The public package uses portable `plugin.json` with OpenAI presentation metadata, following the [packaging documentation](https://developers.openai.com/plugins/build/plugins).

## Validation and updates

Use [the regression scenarios](validation/scenarios.md) to test routing and actual results in a disposable application with the target model and reasoning effort. Validate skill frontmatter, manifest/asset paths, and local reference links for each release. Structural validation does not establish behavioral quality.

Update the marketplace source, increment the plugin version, and reinstall/refresh through the host's supported plugin controls. Check that the installed cache matches the source, then test in a new chat; an existing chat may retain previously loaded skill instructions. Preserve other plugins and host settings. Do not remove a source or personal copy merely because an old configuration entry exists; first establish which copy is actually loaded.

See [privacy](PRIVACY.md) and the [MIT license](LICENSE). This skills-only plugin has no MCP server; GitHub distribution does not imply approval in OpenAI's directory.
