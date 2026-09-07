---
name: review-loop
description: Use to iteratively fix a PR/MR against whatever review signal the repo has (an AI reviewer bot, required checks, or a human's comments) until it's clean, up to a capped number of iterations.
---

# Review loop

Follow `knowledge/05-review-loop.md` at the root of this factory. Loop:
trigger the review, fetch comments/score, stop if clean or at the
iteration cap, otherwise fix actionable comments, resolve the threads,
push, repeat. Treat a human reviewer's comments the same way as a bot's —
only the fetch/trigger/resolve calls change with the platform.
