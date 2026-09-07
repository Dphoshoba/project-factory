# Ship, part 2: loop against review until clean

Don't stop at "I opened the PR." Iterate against whatever review signal the
repo has — an AI reviewer bot (Greptile, CodeRabbit, etc.), required CI
checks, or a human reviewer's comments — until it's clean, up to a capped
number of iterations so the loop can't run forever.

This generalizes the `greploop` skill (originally Greptile-specific) to any
reviewer that can (a) be triggered, (b) leave comments or a score somewhere
fetchable, and (c) have those comments marked resolved.

## Inputs

- **PR/MR/CL number** — detect it from the current branch if not given.
- **Max iterations** (default 10) — raise it for large changes that keep
  surfacing new findings, lower it to bound cost.

## Loop

Repeat up to max-iterations times:

1. **Trigger the review.** Push the latest commits (or re-shelve, for
   Perforce-style workflows). If the reviewer needs an explicit trigger
   (e.g. an `@reviewer review` comment) and isn't already running, post it.
   Wait for the check/run to actually start before polling.

2. **Fetch results.** Reviewer output can land in the PR description, a
   general comment (use the most-recently-*updated* one, not the most
   recently created — bots often edit the same comment across cycles), or a
   formal review/check-run API. Pull a confidence score if the reviewer
   gives one, and the list of unresolved inline comments.

3. **Check exit conditions.** Stop when the score is at its maximum AND
   zero comments are unresolved, or when max-iterations is reached.

4. **Fix actionable comments.** For each unresolved comment: read the file
   in context, decide if it's actionable or informational/false-positive.
   Make the fix if actionable; if not, note why and still resolve the
   thread — don't leave noise open.

5. **Resolve threads** you've addressed, via whatever API the platform
   exposes for marking a review comment/discussion resolved.

6. **Commit and push** (or re-shelve), then go back to step 1.

## Report

At the end, state: iterations run, final score, comments resolved, comments
remaining (list them with file:line and the gist of each, if any remain).

## No bot reviewer available

If the repo has no AI review bot, treat a human reviewer's comments the same
way: fetch them, fix what's actionable, reply to the rest, mark addressed
ones resolved, push, and wait for the next round — the loop structure is the
same, only the fetch/trigger/resolve calls change to whatever API the code
host exposes (GitHub, GitLab, Gerrit, etc.). With no reviewer at all, run a
structured self-review pass instead: reread the diff as if someone else
wrote it, check it against the repo's stated conventions and this factory's
own `knowledge/02-service-layer-architecture.md`, and log what you found and
fixed so the PR description's "how it was tested" section has something
concrete to point to.
