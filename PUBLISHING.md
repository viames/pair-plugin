# Publishing Pair

Canonical source: https://github.com/viames/pair-plugin. Marketplace: `viames-pair`. Plugin: `pair`. Author: Viames Marino. License: MIT.

## Release

1. Update the source under `plugins/pair` and its portable `plugin.json` version. Keep release links and documentation consistent. Never edit a generated installed cache as the source of truth.
2. Run `python scripts/validate.py` and `python scripts/package.py` with the pinned development requirements. Inspect public files and the archive inventory. Run relevant behavioral scenarios for changed workflows and report their actual outcomes separately from structural checks.
3. Commit and push to `main`; require the portable CI matrix to pass. Tag that tested commit as `v<version>`. Do not move a published tag or replace a release artifact with different bytes.
4. Publish the marketplace ZIP, standalone plugin ZIP and `SHA256SUMS` as a GitHub release. Download the public artifacts to a fresh directory and compare their hashes, manifests and complete file inventory.
5. Verify discovery from a fresh Git checkout with the Codex CLI. Installation is `codex plugin marketplace add viames/pair-plugin` followed by `codex plugin add pair@viames-pair`. Avoid enabling duplicate local and public copies in the user's regular environment merely for testing. Record discovery, installation and behavioral checks as distinct results.
6. Enable GitHub Pages with Actions as its source and run **Publish website** from the tested `main` revision. Check the public homepage, privacy and terms pages after deployment.

## Distribution scope

The public repository, release files and Git-backed Codex marketplace do not require a paid hosting service or payment card. The plugin has no MCP server, so an MCP server registry or MCPB package is not an applicable distribution format. Do not invent a server only to obtain a listing.

OpenAI's public directory is a separate submission and review process. This release does not claim directory approval. No portal account, billing setup or third-party listing is required for the GitHub distribution.

## Recovery

Pin a previously published tag with `codex plugin marketplace add viames/pair-plugin --ref v<version>`, install `pair@viames-pair`, and start a new chat. Keep published artifacts immutable. Plugin updates change instructions; they do not roll back code or data produced by earlier agent tasks.
