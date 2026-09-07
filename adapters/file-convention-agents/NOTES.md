# Agents that already read AGENTS.md

Codex CLI, Cursor's agent mode, Aider (with `--read AGENTS.md`), and several
other coding-agent CLIs already look for an `AGENTS.md` at the repo root and
load it into context automatically. For these, there's no adapter to build —
copy (or symlink) this factory's `AGENTS.md` and `knowledge/` directory into
the target repo and the agent picks it up on its own.

```bash
cp /path/to/project-factory/AGENTS.md  /path/to/your-repo/AGENTS.md
cp -r /path/to/project-factory/knowledge /path/to/your-repo/knowledge
```

Then append the repo-specific section at the bottom of `AGENTS.md` (exact
check/test/build commands, hard invariants, environment notes) before the
agent's first task in that repo.

If a given tool's config points elsewhere (for example, some setups expect
`.cursor/rules/` or a different root filename), either point that config at
this `AGENTS.md` or duplicate it under the name the tool expects — keep
`knowledge/` as the single source of truth either way, rather than copying
its content into the tool-specific file.
