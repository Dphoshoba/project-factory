# Ship, part 1: before/after proof in the PR

Open every PR/MR with proof embedded in the description, not linked off to
the side where reviewers won't click. Use whichever form matches what
changed:

- **Visible UI change** → a `| Before | After |` screenshot table.
- **No visible surface** (CLI, API, library, refactor) → a
  `| Case | Before | After |` table of command output or measured numbers,
  pulled straight from the evidence captured in the prove beat
  (`knowledge/03-evidence-driven-testing.md`).

## Screenshot pairs

1. Capture (or reuse) a before image and an after image — two URLs, two
   file paths, or a mix.
2. Generate the comparison table. If using `@vercel/before-and-after`:

   ```bash
   before-and-after <before-url-or-path> <after-url-or-path> --markdown
   ```

   (Use the full package name via `npx @vercel/before-and-after` if it's not
   installed globally — the short name `before-and-after` as an npm package
   does not exist and will resolve to the wrong thing.)
3. The `--markdown` flag uploads both images and prints a ready-to-paste
   `| Before | After |` table. Default upload host is public — fine for
   ordinary UI shots, use a private/authenticated host for anything
   sensitive.
4. Paste the table into the PR description (or append to an existing PR with
   the hosting tool's edit command).

Current state is always "after." If it's ambiguous what "before" should be
(production? a preview deploy? another local port?), ask — don't guess.

## Output-pair proof (no UI)

Pull directly from the prove-beat artifacts:

```markdown
| Case                          | Before                        | After    |
|-------------------------------|--------------------------------|----------|
| `count-words empty.txt`       | `Error: division by zero`     | `0 words`|
| `count-words "a,b c"`         | `2 words` (wrong: should be 3) | `3 words`|
```

Keep it to the cases that actually demonstrate the fix or feature — not
every test in the suite.

## Assembling the PR/MR description

1. What changed, in one or two sentences.
2. How it was tested — every claim backed by the evidence captured in the
   prove beat.
3. The before/after table.
4. Risks, follow-up work, or things intentionally left untested (and why).
5. Run the whole description through `knowledge/06-writing-for-humans.md`
   before posting.
