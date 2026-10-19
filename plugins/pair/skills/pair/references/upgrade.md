# Upgrading a Pair application

Read this only for a requested Pair major-version upgrade. Database migrations alone belong to `pair:migration-review`.

Determine the installed starting version and review the target checkout's `UPGRADE_V4.md`, scripts, and application instructions. The current tool sequence is v1 -> v2 -> v3 -> v4; start at the application's actual major. Preserve local changes and use a clean working tree or verified backup for automated rewrites.

From the application root, use an available reviewed script and an explicit preview flag, for example:

```sh
php vendor/viames/pair/scripts/upgrade-to-v4.php --dry-run
```

If the old installed package does not contain the required upgrader, use the target framework checkout's script with its supported `--path=/absolute/app/path` option. Verify that option in the actual script and point it at the protected application workspace, not at the framework checkout.

Review the proposed changes and manual-work report before the authorized write phase. Use explicit `--dry-run` and `--write` flags for the v2 and v3 scripts too: their legacy default can write. Do not invoke an upgrader for an ordinary feature or patch.

The v4 tool only switches controller bases when it can establish an explicit response flow. Controllers relying on implicit models, views, `setView()`, `assign()`, `assignState()`, or view-owned page metadata require application-specific migration. A `Payload` adapter or generated page-state skeleton is a bridge, not proof that explicit application contracts are complete. Inspect exit status and partial write failures.

Check affected login/session behavior, API payloads, layouts, asset copies, and schema prerequisites described in the installed upgrade guide. Validate application behavior and remaining legacy paths after each applicable stage. Report automated changes, manual work still required, and runtime evidence separately. An updater's success message is not a completed application migration.
