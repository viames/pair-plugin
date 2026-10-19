# PWA and push

Use for Pair installability, service workers, browser push, or browser-helper lifecycle work. For form/region behavior use `pair:frontend-forms`; do not add a second navigation or enhancement owner.

## PWA and browser assets

Inspect `Helpers/PwaConfig.php`, `PwaManifest.php`, `Core/Application.php`, and the relevant `assets/PairPWA.js`, `PairSW.js`, `PairDevice.js`, `PairRouter.js`, or `PairSkeleton.js`. Follow the application's copy and versioning pipeline; PHP package installation does not establish which browser assets are served. The presence of `PairRouter.js` does not authorize introducing a global client router.

Verify manifest URLs, service-worker URL/scope, cache version/update behavior, offline fallback, and the application's public path. Preserve cache exclusions for authenticated/private data, APIs, and mutations as appropriate to the actual worker strategy. Check installed-worker updates and fresh installations separately when changing lifecycle behavior. A manifest response alone does not prove installability or offline operation.

## Browser push

Inspect `Push/Notification.php`, `SubscriptionRepository.php`, `PushDispatcher.php`, `WebPushSender.php`, `DeliveryResult.php`, `VapidConfig.php`, the subscription model/API, and `assets/PairPush.js` as relevant. Retain permission handling, endpoint validation, subscription ownership, VAPID configuration, payload limits, and revocation on expired subscriptions. Never expose a private VAPID key to browser code or fixtures.

Browser Web Push, a provider such as OneSignal, and native APNs/FCM flows have different transports. Identify the real delivery path before applying Web Push assumptions. Test subscription changes with fixtures or a fake sender, without prompting real users or sending notifications unless requested.

For runtime verification, separate subscription persistence, provider acceptance, browser receipt, service-worker display, and notification-click behavior. Report the actual browser/device tested; desktop success does not prove mobile support or a native app release.
