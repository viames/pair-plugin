# Pair capability map

Use this map only when locating an unfamiliar capability. These are source locations in Pair 4, not a promise that an older installed release contains every symbol. The installed code owns method signatures and behavior.

## Locate the authority

For an application, resolve the actual Composer package path; `vendor/viames/pair` is the usual location. Check its source and the application's use of it first. Framework checkout instructions and tests apply when working on that checkout.

Composer dist intentionally excludes framework `AGENTS.md`, `SKILL.md`, `tests/`, `docs/`, and `mobile/`. Missing repository-only files in vendor are expected. Use an available matching framework checkout or the [official wiki](https://github.com/viames/pair/wiki) and [framework repository](https://github.com/viames/pair) for task-specific references. Check documentation against the installed version; current wiki examples may target a newer release. Do not download an entire manual or install dependencies merely to inspect an API.

## Source and workflow map

Paths below are relative to the resolved Pair package or framework root. Wiki names are search terms, not invented local filenames.

| Capability | Source | Owning workflow / wiki search |
| --- | --- | --- |
| Request lifecycle, routes, ordering, pagination | `src/Core/Application.php`, `src/Core/Router.php` | `pair:module-workflow`; Application, Router |
| Explicit pages, fragments, state and read mapping | `src/Web/`, `src/Data/` | `pair:module-workflow`; PageResponse, ReadModel, MapsFromRecord |
| Input, uploads, JSON/text/empty responses, HTTP cache | `src/Http/`, `src/Core/Controller.php` | Module/API workflow; Input, UploadedFile, HttpCache; inspect legacy file/stream helpers before assuming a response class exists |
| Validation, middleware, auth, CORS, throttling, idempotency, CRUD, OpenAPI | `src/Api/`, `src/Api/OpenApi/` | `pair:api-safety`, `pair:crud-review`; API, CrudController, SpecGenerator |
| Records, queries, relations, collections, transactions | `src/Orm/`, `src/Models/`, `src/Traits/` | [Data and runtime](runtime.md); ActiveRecord, Query, Collection |
| Schema and data upgrades | `migrations/`, application migration runner | `pair:migration-review`; Migration |
| Forms, controls, widgets, menus, templates, themes | `src/Html/`, `src/Html/UiTheme.php`, `assets/pair.css` | `pair:frontend-forms`; Form, TemplateRenderer, UiTheme |
| PairUI, validation, maps, device, router and skeleton helpers | `assets/`, related `src/Helpers/` and `src/Html/` classes | `pair:frontend-forms`; PairUI.js, PairValidation.js; preserve the application's navigation owner |
| Sessions, users, ACL, OAuth, passkeys, mobile auth | `src/Models/`, `src/Services/`, `src/Api/ApiController.php`, `src/Api/PasskeyController.php` | [Authentication and mobile](auth-mobile.md); User, Acl, ApiToken, SocialAuth, PasskeyAuth |
| iOS and Android companion libraries | Repository-only `mobile/`, `docs/` | [Authentication and mobile](auth-mobile.md); Mobile-auth-app-setup, Mobile-iOS-stack, Mobile-Android-stack |
| PWA, service workers, subscriptions, Web Push | `src/Push/`, `src/Helpers/Pwa*.php`, `assets/PairPWA.js`, `assets/PairSW.js`, `assets/PairPush.js` | [PWA and push](pwa-push.md); PWA, PushDispatcher, VapidConfig |
| File and Redis caches | `src/Cache/` | [Data and runtime](runtime.md); Cache, HttpCache |
| Environment, logging, observability, scheduling | `src/Core/`, `src/Helpers/Schedule.php`, `src/Helpers/Log*.php`, `src/Exceptions/` | [Data and runtime](runtime.md); Env, Logger, Observability, Schedule |
| Runtime extensions, adapters, ZIP packages | `src/Core/RuntimeExtensionInterface.php`, `src/Core/AdapterRegistry.php`, `src/Packages/` | [Data and runtime](runtime.md); RuntimeExtensionInterface, InstallablePackage |
| Localization, dates, charts, reports and shared helpers | `translations/`, `src/Helpers/`, `src/Html/`, `src/Models/Locale.php` | [Data and runtime](runtime.md); Translator, Locale, DateRange, ChartJs, Report |
| Provider clients and search read models | `src/Services/`, `src/Search/`, `src/Helpers/Mailer.php` | [Service integrations](integrations.md); Integrations and the selected provider class |
| Module/API/CRUD generation | `src/Console/MakeCommand.php`, `bin/pair` | `pair:crud-review`; Generator |
| Pair major upgrades | `scripts/upgrade-to-v*.php`, `UPGRADE_V4.md` | [Upgrade guide](upgrade.md) |

For verification, locate the affected application's tests or the framework's nearby `tests/Unit/<component>` tests. Test infrastructure, installed code, copied assets, deployed PHP, and native client releases are separate evidence sources.
