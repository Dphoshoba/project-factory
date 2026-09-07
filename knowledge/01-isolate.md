# Isolate: one branch per task

Every task gets its own branch, created from the latest trunk. Never build
directly on `main` (or `master`/`trunk`, whatever the repo calls it).

This file assumes a human or agent with shell access to `git`. An agent that
only has chat access and no repo access cannot perform this beat itself —
tell it to ask its operator to create the branch, or skip straight to the
build beat on a branch the operator already prepared.

## Steps

1. **Sync**: `git fetch origin` (or pull the latest trunk however the repo's
   remote is configured).

2. **Scope check**: list open PRs/MRs and skim their changed files. If your
   task needs files another open PR is already editing, stop and ask for
   direction instead of guessing who wins. Also check for uncommitted work in
   the checkout — someone else may be mid-task.

3. **Name the task**: lowercase-with-hyphens plus a short unique suffix, e.g.
   `word-count-cli-0816a`. If branch/worktree creation fails because the name
   exists, pick a different name — never force or reuse someone else's.

4. **Branch (and worktree, if the repo is large enough to want one)**:

   ```bash
   git worktree add <worktrees-dir>/<task-name> \
     -b <branch-prefix>/<task-name> origin/main
   ```

   Use a gitignored directory for worktrees (e.g. `.worktrees/`) so they can
   never be committed by accident, and a consistent branch prefix (e.g.
   `agent/`). A small repo or a single-agent session can skip the worktree
   and just use a plain branch — the isolation that matters is the branch,
   not the extra checkout.

   Some harnesses manage worktrees themselves (for example, Claude Code
   creates and tracks its own under `.claude/worktrees/<name>`). When the
   harness already gives you an isolated worktree and branch, skip manual
   creation and keep the harness-assigned name — the scope check and cleanup
   steps still apply.

5. **Enter and verify**:

   ```bash
   cd <worktrees-dir>/<task-name>   # if you made a worktree
   git branch --show-current        # must print your new branch, not main
   ```

   Install dependencies fresh inside the worktree — worktrees don't share
   `node_modules`/virtualenvs/etc. Confirm the runtime version the repo
   expects before running anything.

## Remember

- A worktree does **not** isolate shared resources: dev-server ports, shared
  databases, and dependency lockfiles are global to the machine. Confirm a
  port answers *your* process before trusting what it serves, and never run
  schema experiments against a shared database.
- Resolve lockfile conflicts by regenerating, never by hand-merging.
- Never force-push to the trunk branch, and never plain `--force` anywhere —
  only `--force-with-lease`, only on your own task branch.
- If a conflict can't be resolved confidently, stop and report instead of
  guessing.
- Keep the branch/worktree until the change is merged or closed. Clean up
  after merge:

  ```bash
  git worktree remove <worktrees-dir>/<task-name>
  git branch -D <branch-prefix>/<task-name>
  ```

  `-D` (capital) is expected: after a squash- or rebase-merge, lowercase `-d`
  refuses even though the work is merged.
