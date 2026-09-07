---
name: new-feature
description: Start a new task in an isolated Git branch/worktree from the latest trunk so multiple agents can work on the same repo in parallel without conflicts. Use at the beginning of every new feature, fix, or task, before writing any code.
---

# New feature

Follow `knowledge/01-isolate.md` at the root of this factory (resolve the
path relative to wherever this skill was installed from — typically the
repo this skill folder was copied into, two levels up from this file if
installed as `.claude/skills/new-feature/`, or check the factory's own
`AGENTS.md` for the canonical copy).

Claude Code manages its own worktrees under `.claude/worktrees/<name>` — when
running inside Claude Code, skip the manual `git worktree add`/`remove`
steps in that file and keep the harness-assigned branch name. The scope
check, naming, and cleanup-after-merge steps still apply.
