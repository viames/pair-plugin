# Authentication and mobile

Use for Pair login, session, ACL, token, social-auth, passkey, or native-client work. Read the installed implementation and affected application entrypoint. Use `pair:api-safety` when the endpoint contract changes.

## Identify the actual access path

Pair browser sessions, legacy OAuth2 tokens, mobile `ApiToken` flows, and passkeys have different lifecycles. Inspect `Application`, the selected controller base, and the relevant `User`, `Session`, `UserRemember`, `ApiToken`, or `UserPasskey` model. Keep the application's custom user class and permission model. A UI visibility check does not protect an action or direct record lookup.

Preserve tenant scope, account eligibility, cookie/CSRF behavior, token expiry and revocation, and refresh semantics. Verify denied and expired access alongside success; never weaken an access check to make a new client work. Handle untrusted return URLs using the installed redirect rules.

## Native contracts

Current Pair 4 mobile auth lives in `src/Api/ApiController.php`; do not invent a `MobileAuthController` class from a test filename. Inspect `authAction()` and the application's overrides. Login, refresh, current-user, and logout flows differ from application-owned registration. Review actual routes, payloads, token/session identifiers, refresh rotation, logout/revocation, and public-action registration before changing either server or client.

The repository contains `docs/MOBILE_AUTH_APP_SETUP.md`, `docs/MOBILE_IOS_STACK.md`, `docs/MOBILE_ANDROID_STACK.md`, `mobile/ios/PairMobileKit`, and `mobile/android/PairMobileAndroid`. These are excluded from Composer dist; consult a matching framework checkout or the official wiki's Mobile pages when absent in vendor. Client compilation or simulator success does not prove a production endpoint, physical-device association, or store release.

## Passkeys and social login

Inspect `PasskeyController`, `PasskeyAuth`, `PasskeyFlow`, and `SocialAuth` as applicable. Preserve challenge freshness and single use, relying-party ID, trusted origins, owner-scoped credential management, and signature validation. Native passkeys also depend on platform association and signed-app origins; synthetic fixtures cannot establish that deployment layer.

For social redirects, retain state/nonce and provider-specific callback validation. Check current provider documentation only for the affected integration, keeping secrets and real tokens out of logs and fixtures. Prefer local signed fixtures or mocked transport for verification; real account operations remain within the user's requested scope.
