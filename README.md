# Project factory

Harness-agnostic, model-agnostic domain knowledge for building software
through a four-beat loop: isolate, build, prove, ship. Adapted from
[michaelshimeles/skills](https://github.com/michaelshimeles/skills), which
packages the same ideas as Claude Code-specific skills. This factory pulls
the actual playbooks out into plain markdown so they work with any coding
agent, not just one harness.

## Layout

- **`knowledge/`** — the real content. Six playbooks, no harness-specific
  syntax: isolate, service-layer architecture, evidence-driven testing,
  before/after proof, the review loop, writing for humans. This is the
  single source of truth; everything else just points back at it.
- **`AGENTS.md`** — the universal entry point. Many coding-agent CLIs
  (Codex CLI, Cursor, Aider-family tools, Claude Code) already read this
  file automatically from a repo root.
- **`adapters/`** — harness-specific shims, kept thin on purpose:
  - `claude-code/skills/` — real `SKILL.md` files so Claude Code
    auto-invokes the right playbook by description match.
  - `file-convention-agents/NOTES.md` — for tools that already read
    `AGENTS.md` natively; there's nothing to adapt, just copy the files.
  - `chat-agents/SYSTEM_PROMPT.md` — a condensed version to paste into a
    chat-only agent (Grok bot, Hermes Agent, or similar) that has no
    filesystem access of its own.
- **`sample-feature/`** — a tiny CLI run through all four beats, as proof
  the factory actually works end to end.

## Using it

**With Claude Code:**

```bash
cp -r adapters/claude-code/skills/* ~/.claude/skills/    # all projects
# or: cp -r adapters/claude-code/skills/* /path/to/project/.claude/skills/
cp AGENTS.md /path/to/project/AGENTS.md
cp -r knowledge /path/to/project/knowledge
```

**With Codex CLI, Cursor, Aider, or anything else that reads `AGENTS.md`:**

```bash
cp AGENTS.md /path/to/project/AGENTS.md
cp -r knowledge /path/to/project/knowledge
```

No skills folder needed — see `adapters/file-convention-agents/NOTES.md`.

**With a chat-only agent (Grok bot, Hermes Agent, a raw model in a chat
UI):** paste `adapters/chat-agents/SYSTEM_PROMPT.md` as its system prompt.
You run the shell/git/browser steps yourself and bring it the output.

In every case, append the repo-specific section at the bottom of `AGENTS.md`
once it's in a real project: the exact check/test/build commands, hard
invariants, environment notes.

## Why knowledge and adapters are separate

A SKILL.md with Claude-specific frontmatter, or a slash-command convention
tied to one CLI, is plumbing — it tells one particular tool when to pull the
knowledge in. The knowledge itself (what a service layer is, what counts as
evidence, how to structure a before/after table) doesn't change across
tools. Keeping them apart means updating a playbook once, in one file,
instead of re-editing it inside every harness's own format.

## Adding a new playbook

1. Write it as `knowledge/NN-name.md` — imperative instructions, no
   assumptions about which tool is reading it.
2. Add it to the workflow in `AGENTS.md` if it's part of the four-beat loop,
   or note it as a standalone playbook otherwise.
3. Add a thin `adapters/claude-code/skills/<name>/SKILL.md` if you want
   Claude Code to auto-invoke it; update `adapters/chat-agents/
   SYSTEM_PROMPT.md` if chat-only agents need it condensed into their
   system prompt too.
