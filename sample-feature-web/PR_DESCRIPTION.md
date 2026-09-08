# Autofocus the textarea for keyboard-only driving

Branch: `agent/tier3-autofocus-demo1`, off `0c560f4`.

## What changed

Added `autofocus` to the `#input` textarea in `sample-feature-web/index.html`.
On load, the page now has real keyboard focus on the textarea with zero
clicks — useful on its own (single-purpose page, one obvious control), and
it's also what makes the page reliably drivable by a real OS-level actuator
(e.g. AutoHotkey) without brittle pixel-coordinate clicking, which is the
next step toward exercising tier 3 (live recording) for real.

## How it was tested

Verified live via the Browser pane against a fresh page load:

```
document.activeElement.id  ->  "input"
```

Then typed `"hello world"` with no click at all and confirmed the count
still updates correctly:

```
document.getElementById('count').textContent  ->  "2 words"
```

## Risks / follow-up

None. `autofocus` on a single always-visible textarea with no other
interactive elements ahead of it in the DOM is a standard, low-risk use.

## Review loop

Trigger review, fix actionable comments, resolve, repeat until clean.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
