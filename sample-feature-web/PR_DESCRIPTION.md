# Add a web-UI sample feature and prove tier-2 evidence for real

Branch: `agent/web-ui-evidence-demo1`, off `54d0d03`. Evidence below was
captured against `80382f47b894194834702f6b9d8dc46e41244b09` (the commit that
introduced the feature, before the review-loop fixes in this PR).

## What changed

`sample-feature/` (the CLI word counter) only ever exercised tier-1 evidence
(command-output pairs) — tier 2 (scripted screenshots) and tier 3 (live
recording) in `knowledge/03-evidence-driven-testing.md` were written up but
never actually run. This adds `sample-feature-web/`, a tiny live word-count
UI with the same bug class ported to JavaScript, and runs it through the
factory's four beats to actually exercise tier 2.

- `service/word_count.js` — same service-layer split as the CLI version.
  Started with the same bug (`text.split(" ")`, so repeated spaces and an
  empty input both miscount), fixed to `text.trim().split(/\s+/).filter(Boolean)`.
- `actions/app.js` — orchestrates the DOM: wires the textarea's `input`
  event to the service and updates the `#count` display. Untouched by the
  fix, same as the CLI demo's action file.
- `_devserver.py` — dev-only static server with a `/save/<name>` endpoint so
  a live screenshot can be persisted straight to disk from the browser,
  without copying image bytes through a conversation by hand.
- `evidence/before.png` and `evidence/after.png` — the actual captured
  screenshots (not staged, not mocked) proving the bug and the fix.
- `knowledge/03-evidence-driven-testing.md` — added the in-page
  `html2canvas` capture pattern as a tier-2 option for harnesses with only a
  scriptable browser and no dedicated screenshot CLI, plus a caching pitfall
  hit while doing this run (see below).

## How it was tested

Drove the live page via the Claude Code Browser pane: typed `"hello   world"`
(3 spaces) into the textarea, rendered the DOM with `html2canvas`, and POSTed
the resulting PNG to the dev server to persist it — twice, once before the
fix and once after.

| Case | Before | After |
|---|---|---|
| `"hello   world"` (3 spaces) | ![before](https://raw.githubusercontent.com/Dphoshoba/project-factory/80382f47b894194834702f6b9d8dc46e41244b09/sample-feature-web/evidence/before.png) <br> **4 words** (wrong) | ![after](https://raw.githubusercontent.com/Dphoshoba/project-factory/80382f47b894194834702f6b9d8dc46e41244b09/sample-feature-web/evidence/after.png) <br> **2 words** |

Image links are pinned to that commit SHA rather than the branch name, so
they keep resolving after the branch is deleted post-merge.

Full write-up: `.artifacts/web-ui-evidence-demo1/report.md` (gitignored, not
part of this PR — evidence gets attached, not committed, per the prove
beat's own rule; the two PNGs above are the exception, committed
deliberately so they render inline here).

## A real snag, and why it's now in the knowledge file

The first "after" capture attempt still showed **4 words** even with the fix
applied and the page reloaded — the dev server sent no cache-control
headers, so the browser served a cached copy of the old `word_count.js`.
Caught it by screenshotting before trusting the capture, fixed the server to
send `Cache-Control: no-store`, and re-verified. Added this as an explicit
pitfall in `knowledge/03-evidence-driven-testing.md` so the next agent
running this pattern doesn't lose time to it.

## Risks / follow-up

Tier 3 (live annotated screen recording) is still not exercised — this
sandbox has no screen-recorder tool and no OS-level actuator on the Browser
pane, and the knowledge file explicitly forbids faking a recording from
stitched screenshots. Left open in the manual's roadmap.

## Review loop

Same as PR #1: trigger review, fix actionable comments, resolve, repeat
until clean.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
