---
name: evidence-driven-testing
description: Use whenever a change needs verifiable proof that it works instead of a prose claim — captured command output, screenshots, or (when a GUI and computer-use tooling are available) a live screen recording.
---

# Evidence-driven testing

Follow `knowledge/03-evidence-driven-testing.md` at the root of this
factory. It's tiered by what the environment supports:

1. Command-output before/after pairs (default — shell only, no GUI needed).
2. Scripted screenshots / headless browser (web UI, no display).
3. Live screen recording, annotated as you go — only with a real GUI and a
   computer-use or actuator tool Claude Code can drive.

Always reproduce the failing case *before* fixing it and save that capture —
it's the "before" half of the pair the ship beat needs.
