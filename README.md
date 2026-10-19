# Pair plugin for Codex

**Version-aware assistance for Pair PHP applications and framework development.**

By **Viames Marino** · **MIT** · **0.3.0**

[Website](https://viames.github.io/pair-plugin/) · [Italiano](README.it.md) · [Releases](https://github.com/viames/pair-plugin/releases) · [Pair framework](https://github.com/viames/pair)

Six focused skills guide Codex through Pair modules, APIs, forms, migrations and CRUD. On-demand references cover authentication and native mobile contracts, ORM and cache, integrations, PWA and push, runtime extensions, diagnostics and upgrades. The skills inspect the installed Pair version and preserve the application's existing architecture.

## Install

Use a Codex version that supports Git-backed plugin marketplaces:

```sh
codex plugin marketplace add viames/pair-plugin
codex plugin add pair@viames-pair
```

Start a new chat in your Pair project. Invoke `@Pair` or ask for a Pair task. To pin a release, add the marketplace with `--ref v0.3.0`.

Already using `pair@local`? After installing this distribution, disable the old copy in Codex's plugin settings so only one Pair plugin supplies skills. Your project files and framework installation do not need to move.

To refresh a Git-backed marketplace and install its current package:

```sh
codex plugin marketplace upgrade viames-pair
codex plugin add pair@viames-pair
```

The release provides a **marketplace ZIP**, containing this repository's installable catalog, and a **standalone plugin ZIP**, containing only `plugins/pair`. Each release includes SHA-256 checksums. Extract the marketplace ZIP and use its root path with `codex plugin marketplace add /path/to/extracted/marketplace` for local installation.

## Skills

| Skill | Purpose |
| --- | --- |
| `pair:pair` | Establish the actual version and route the task to the relevant capability |
| `pair:module-workflow` | Implement application modules with explicit responses or preserve a legacy flow |
| `pair:api-safety` | Review validation, access, writes, serialization and API contracts |
| `pair:frontend-forms` | Work on forms, shared controls and progressive server-rendered regions |
| `pair:migration-review` | Prepare schema changes and data migrations with realistic rollout boundaries |
| `pair:crud-review` | Complete and verify generated CRUD behavior |

See the [capability map](plugins/pair/skills/pair/references/capabilities.md) and the [plugin instructions](plugins/pair/README.md).

## Requirements and boundaries

The plugin contains Markdown instructions, reference files and visual assets. It has no MCP server, daemon, API keys or runtime dependencies. It uses the code, tools, permissions and model supplied by the host. Pair application development still needs that application's PHP/Composer/runtime environment.

Pair 4 is the primary reference; legacy work is guided by the actually installed source. The plugin does not automatically upgrade Pair or change the model used by Codex or a Pair application's AI client. It is model-independent and has not been behaviorally benchmarked across every GPT model.

This is a public GitHub/Codex marketplace distribution. It is not an OpenAI-directory approval or an MCP Registry listing. No payment or credit card is required to download this project; host/model services retain their own terms.

## Verification and development

```sh
python3 -m venv .venv
# Activate the virtual environment for your shell, then:
python -m pip install -r requirements-dev.txt
python scripts/validate.py
python scripts/package.py
```

Validation checks manifests, skill metadata, internal references, assets and release contents. The packager produces reproducible ZIPs and `SHA256SUMS` in `artifacts/`. CI runs the same checks on Linux, macOS and Windows. The [23 behavioral scenarios](plugins/pair/validation/scenarios.md) remain an explicit manual evaluation plan, separate from structural checks.

See [publishing](PUBLISHING.md), [privacy](plugins/pair/PRIVACY.md) and [license](LICENSE). Report reproducible problems through [GitHub Issues](https://github.com/viames/pair-plugin/issues), without credentials or private application data. This project is independent of OpenAI.
