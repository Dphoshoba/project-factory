---
name: before-after-proof
description: Use when a PR/MR needs before/after proof embedded in its description — a screenshot comparison table for UI changes, or a before/after output table for CLIs, APIs, and other non-visual changes.
---

# Before/after proof

Follow `knowledge/04-before-after-proof.md` at the root of this factory.
UI changes get a `| Before | After |` screenshot table (the
`@vercel/before-and-after` CLI with `--markdown` generates it directly).
Non-visual changes get a `| Case | Before | After |` table built from the
command-output pairs captured during the prove beat. Current state is
always "after"; ask rather than guess what "before" means if it's unclear.
