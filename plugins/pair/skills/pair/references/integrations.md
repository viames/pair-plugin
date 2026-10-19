# Service integrations

Use for Pair service clients and delivery workflows. Locate the installed client and application wrapper before writing a new transport. Consult the official wiki's Integrations page or the provider-class page when behavior is unclear; verify provider API details against current official documentation when the task requires them.

## Select the existing boundary

| Work | Pair source candidates |
| --- | --- |
| Mail | `Helpers/Mailer.php`; `Services/SmtpMailer.php`, `Sendmail.php`, `AmazonSes.php`, `ResendMailer.php` |
| Payments | `Services/StripeGateway.php` |
| AI | `Services/OpenAIClient.php`, `GeminiClient.php`, `ClaudeClient.php` |
| Storage and files | `Services/AmazonS3.php`; `Http/UploadedFile.php` |
| Maps, geocoding, places | `Services/GoogleMapsClient.php`, `GoogleGeocoder.php`, `GooglePlacesService.php`; related helpers and assets |
| Anti-bot | `Services/HumanChallenge.php`, `CloudflareTurnstile.php`, `GoogleRecaptcha.php` |
| Search | `Services/MeilisearchClient.php`, `Search/SearchIndexableReadModel.php` |
| Supabase bridge | `Services/SupabaseClient.php` |
| Messaging | `Services/TelegramBotClient.php`, `WhatsAppCloudClient.php`, `OneSignalNotification.php` |

Paths are relative to `src/`. Check optional SDKs/extensions in the installed source and Composer metadata. A bundled client does not imply installed dependencies, credentials, enabled service, or a configured account. Retain Pair ORM/auth when using a bridge such as Supabase unless a broader migration was requested.

## Preserve delivery semantics

Inspect configuration keys without printing values. Use the application's existing transport injection, client factory, or adapter seam for local fixtures. A development environment may redirect recipients to real administrators; it does not guarantee that no messages leave the process. Honor any no-send/no-network instruction at the transport boundary.

Keep retry rules, idempotency, timeouts, failure mapping, webhook verification, and reconciliation with the owning application service. A valid signature, successful mock, accepted request, provider event, and final business mutation prove different things. For payment or notification bugs, inspect the actual call and consumer before replaying an event or making a live delivery.

For anti-bot work, preserve both browser integration and server verification. For uploads, keep MIME/size checks, storage-path constraints, and access rules. For mail, preserve escaped dynamic content, text/HTML output where supported, attachments, recipients, and the selected transport lifecycle.

## AI clients and model choice

The GPT model running Codex and the model configured in a Pair application's AI client are independent. Updating this plugin does not upgrade `OpenAIClient`, its default model, or the application's environment. Inspect the installed client's methods, accepted options, and tests; do not promise streaming, tools, modalities, or model parameters merely because the provider offers them.

For a requested OpenAI model/API change, use current official OpenAI guidance and the available OpenAI setup workflow when credentials are required. Respect an explicitly selected model. Keep this plugin model-independent and verify the actual configured model and supported request fields; never silently change global Codex or application model settings.
