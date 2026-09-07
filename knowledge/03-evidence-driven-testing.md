# Prove: evidence over prose claims

Never close out a change with a prose claim ("this works now"). Attach
evidence: a captured before/after pair, a test run, measured numbers, or a
recording — whichever fits what changed and what tools the current harness
and environment actually have.

This file is ordered from least to most infrastructure required. Use the
first tier your environment supports; don't reach for screen recording just
because the original skill this is adapted from defaults to it — most coding
agents (Codex-, Claude Code-, Cursor-, Aider-style CLIs) have shell access
but no GUI, so the command-output tier below is the common case.

## Always do this regardless of tier

- Reproduce the bug or missing behavior **before** writing the fix, while
  it's cheapest to capture, and save that capture. That's the "before" half
  of the pair.
- State the exact commit/branch tested against (`git rev-parse HEAD`,
  `git branch --show-current`).
- One assertion per meaningful state change; mark anything you couldn't test
  `untested` with the reason — never skip silently.
- Evidence complements the repo's own checks (typecheck/build/tests); it
  never replaces them.
- Save captures under a gitignored artifacts directory (e.g. `.artifacts/
  <task-name>/`) — evidence gets attached to the PR/report, not committed to
  the tree.

## Tier 1 — command-output pairs (default; no GUI or browser needed)

For CLIs, APIs, libraries, scripts, build tooling — anything you can run and
read the output of.

1. Run the failing case, capture stdout/stderr/exit code to
   `.artifacts/<task-name>/before.txt`.
2. Make the fix.
3. Run the same case again, capture to `.artifacts/<task-name>/after.txt`.
4. Run the full test suite (or the smallest command that exercises the
   change) and capture that too.
5. Write `.artifacts/<task-name>/report.md`: what was tested, the exact
   commit, a table of test name → before result → after result, and any
   caveats. Don't leave a caveats placeholder unfilled — say "none" if there
   are none.

## Tier 2 — scripted screenshots / headless browser (web UI, no display)

- Use a screenshot CLI (for example `@vercel/before-and-after`, or a one-off
  Playwright script run via `npx --yes --package=playwright node
  record.mjs`) against a running local server.
- Number captures in test order with the assertion in the filename:
  `01-precondition-signed-in.png`, `02-it-saves-on-blur-passed.png`.
- Keep an `assertions.md` alongside the images listing each `test_start` /
  `assertion` with its result (`passed` / `failed` / `untested` + reason) —
  this is the same discipline as tier 3's annotations, just as files instead
  of a burned-in overlay.
- In containers/VMs where headless Chrome fails with "No usable sandbox",
  pass the no-sandbox flag the tool exposes for that.

## Tier 3 — live screen recording (GUI environment + computer-use actuator)

Only when the harness can actually drive a GUI live (built-in computer use,
or an actuator like a driver CLI) and the change has a visible surface worth
watching in motion.

- Start a recorder before the first action; perform every interaction
  through the actuator on the live app, so the recording and the test are
  the same act. Never present scripted playback or synthetic footage as a
  recording.
- Annotate as you go: a `setup` note for starting context, a `test_start`
  note per named behavior, an `assertion` note (`passed`/`failed`/
  `untested`) after each check. Keep messages short and high-signal.
- Stop after the final assertion, confirm the render, then extract a frame
  at each assertion timestamp and check the state is actually visible before
  calling it evidence.
- Never record a screen showing secrets, tokens, or real customer/payment
  data — mark that flow `untested` instead.

## Non-UI changes still need evidence

- API/performance: a scripted probe with measured numbers (request counts,
  latency before/after).
- Agent/LLM behavior: the relevant transcript excerpt showing the call and
  response.
- Rendering/shader/canvas: rendered frames plus a pixel diff, reviewed by
  eye.

## Posting the evidence

Attach the report (and recording/screenshots, if any) to the PR/MR
description and any tracker issue. If the posting tool can't attach a local
file directly, upload it and link it, then confirm the link actually opens
before claiming it's posted.
