# Agent workflow

Every task moves through the same four beats. Each beat is backed by a
knowledge file in `knowledge/` — plain instructions, no harness-specific
syntax, readable by any agent that can read a file or be given text as
context.

This file itself follows the `AGENTS.md` convention that a growing set of
coding agents (Codex CLI, Cursor, Aider-family tools, Claude Code, and
others) read automatically when it sits at a repo's root. Drop it into any
project and fill in the repo-specific section at the bottom.

## Workflow

1. **Isolate — `knowledge/01-isolate.md`.** Every new feature starts on its
   own branch (and worktree, if the repo warrants one) cut from the latest
   trunk. Never build on `main`.
2. **Build — `knowledge/02-service-layer-architecture.md`.** Actions
   orchestrate the "why/when"; a service layer owns the reusable "how,"
   with explicit inputs and structured returns.
3. **Prove — `knowledge/03-evidence-driven-testing.md`.** Verify with the
   repo's own checks plus captured evidence — command-output pairs by
   default, screenshots or a live recording only when the harness and
   environment actually support them. Capture the *before* state while
   reproducing the issue, before fixing it, when it's cheapest.
4. **Ship — `knowledge/04-before-after-proof.md`, then
   `knowledge/05-review-loop.md`.** Open the PR/MR with before/after proof
   embedded in the description. Then loop against whatever review signal
   the repo has (an AI reviewer bot, required checks, or a human's comments)
   until it's clean or the iteration cap is hit. Finish by presenting the
   PR/MR URL.

Apply `knowledge/06-writing-for-humans.md` to anything written for a person
along the way: commit messages, the PR title and body, docs, replies.

## Which beats an agent can actually run

Not every agent has the same capabilities. Before starting, check which of
these you have, and use the matching path in the relevant knowledge file:

| Capability | Unlocks |
|---|---|
| Shell + git access | Isolate (branch/worktree), build, tier-1 evidence (command output), ship (push, open PR via CLI) |
| Shell but no git/PR access | Build and tier-1 evidence only — hand the diff and evidence to whoever has repo access for isolate/ship |
| Browser or headless-browser tool, no GUI | Tier-2 evidence (scripted screenshots) in addition to the above |
| Live GUI + computer-use/actuator tool | Tier-3 evidence (live recording) in addition to all of the above |
| Chat-only, no file or shell access | None of the four beats directly — the operator runs them and brings you the diff/evidence to review or discuss. See `adapters/chat-agents/SYSTEM_PROMPT.md`. |

## Multi-agent rules

- Never commit directly to the trunk branch.
- One branch/worktree per task per agent — never reuse or modify another
  agent's in-progress work.
- Scope check before starting: skim open PRs'/MRs' changed files and look
  for uncommitted work in shared checkouts. On overlap, stop and ask for
  direction.
- Never force-push to trunk, and never a plain `--force` anywhere — only
  `--force-with-lease`, only on your own branch.
- Resolve lockfile conflicts by regenerating, never by hand-merging.
- Confirm a dev-server port answers *your* process before trusting it;
  don't run schema experiments against a shared database.
- If a conflict can't be resolved confidently, stop and report instead of
  guessing.

## Completing a task

1. Keep changes limited to the assigned task.
2. Run the repo's checks *(repo-specific — list the exact commands in the
   section below)*.
3. Assemble the evidence captured along the way into a before/after pair.
4. Commit with a clear message, rebase onto the latest trunk, rerun checks.
5. Push; after rebasing an already-pushed branch, force with lease.
6. Open the PR/MR. The body must explain what changed, how it was tested
   (every claim backed by evidence), before/after proof, and any risks or
   follow-up work. Run the title and body through
   `knowledge/06-writing-for-humans.md` before posting.
7. Loop per `knowledge/05-review-loop.md` until clean.
8. End by presenting the PR/MR URL.

Do not merge unless explicitly instructed. Keep the branch/worktree until
the change is merged or closed.

## Harness adapters

- `adapters/claude-code/skills/` — real Claude Code skills (SKILL.md +
  frontmatter) that each forward to the matching `knowledge/*.md` file, so
  Claude Code auto-invokes them and they stay in sync with one source of
  truth.
- `adapters/file-convention-agents/NOTES.md` — for anything that already
  reads `AGENTS.md` natively (Codex CLI, Cursor, Aider-family tools): no
  extra setup, this file and `knowledge/` are already enough.
- `adapters/chat-agents/SYSTEM_PROMPT.md` — a condensed, paste-as-system-
  prompt version of the whole knowledge base, for chat-only agents with no
  filesystem access (a Grok-style bot, Hermes Agent, or any model you're
  driving through a plain chat interface).

## Repo-specific section (fill this in per project)

*(Append here when dropping this file into an actual project: the exact
check/test/build commands, hard invariants — security and architecture
rules specific to that codebase — an environment quick reference, local
test infrastructure, and anything that can't be verified locally.)*
