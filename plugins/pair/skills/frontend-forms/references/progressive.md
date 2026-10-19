# Pair 4 progressive regions

Check these symbols in the installed `src/Web/Controller.php`, `src/Web/FragmentResponse.php`, and deployed `assets/PairUI.js` before adopting them. Pair 4 minor versions and copied application assets may differ.

## Server contract

- `page()` returns the full page with prepared state.
- `fragment()` returns a region's HTML.
- `pageOrFragment(pageLayout, fragmentLayout, state, region, title)` selects the fragment only when the request explicitly asks for that region.
- `pageOrFragments(pageLayout, fragmentLayouts, state, title)` supports a region-to-layout map.
- The request uses `X-Pair-Region`; the DOM target uses `data-pair-region`. A region header changes rendering only: it never substitutes for authorization or scoped data access.

Use the same scoped data preparation and permissions for full-page and fragment requests. Escape output in both layouts. Check the installed fragment renderer and replacement behavior so the expected region root survives an update.

## Client contract

Current PairUI exposes `PairUI.region`, `PairUI.actions`, and `PairUI.filters`. Inspect their installed signatures and existing initialization before adding bindings. Relevant directives include `data-pair-action`, `data-pair-refresh`, and `data-pair-filter`. The helpers add progressive request headers and can interpret refresh metadata from JSON responses.

The current `PairUI.filters` helper stores persistent filter values in cookies; it does not update query parameters or browser history. For a GET/URL-based filter flow, keep the application's URL and history handling and pass the corresponding URL to region refresh rather than assuming `filters.bind()` provides it.

Content replacement emits `pair:region:replaced`. Initialize only newly inserted controls and avoid stacking listeners on persistent ancestors. Preserve any existing application enhancement owner and cleanup conventions.

Keep state in URLs when the current flow supports navigable filters; check reload, back/forward, and full-page requests against the same values. Verify rapid requests cannot let an older result replace the current one, and that denied or failed requests leave usable controls and understandable feedback. Test the actual application's integration rather than assuming the library's presence proves it works.
