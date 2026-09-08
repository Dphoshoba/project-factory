# Test-only autofocus for keyboard-only driving

Branch: `agent/tier3-autofocus-demo1`, off `0c560f4`.

## What changed

`actions/app.js` now focuses the `#input` textarea when the page is loaded
with `?autofocus=1` in the URL — real visitors get standard browser
behavior (no unexpected focus jump), while a test harness can request
reliable keyboard focus with zero clicks by adding that query param. This
is what makes the page drivable by a real OS-level actuator (e.g.
AutoHotkey) without brittle pixel-coordinate clicking, needed for the
tier-3 (live recording) evidence harness.

The first version of this PR used a plain `autofocus` attribute on the
textarea for every visitor; GitHub Copilot's review flagged that as
disruptive for screen-reader users on page load (context jumps into the
field, skipping the heading), which is a real WCAG concern for a page this
sparse but still worth respecting. Making it opt-in via the URL keeps the
default experience unchanged and only changes behavior when the harness
explicitly asks for it.

## How it was tested

Verified live via the Browser pane:

- Fresh load of `index.html` (no query param): `document.activeElement`
  is `<body>`, matching normal, unmodified browser behavior.
- Load of `index.html?autofocus=1`: `document.activeElement.id` is
  `"input"`.
- Typed `"hello world"` on the autofocus load with no click at all;
  `document.getElementById('count').textContent` reads `"2 words"`.

## Risks / follow-up

None identified. The focus call only runs behind an explicit opt-in query
param, so it can't affect a normal page load.

## Review loop

Trigger review, fix actionable comments, resolve, repeat until clean.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
