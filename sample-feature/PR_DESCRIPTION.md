# Fix word count on multi-space and empty input

Branch: `agent/word-count-evidence-demo1`, off `dc294ed` (factory scaffold).

## What changed

`tokenize()` in `service/text_service.py` used `text.strip().split(" ")`,
which splits on a single literal space. Any run of consecutive spaces
produced empty-string tokens that got counted as words, and an empty file
produced one phantom word instead of zero. Switched to `text.split()` with
no argument, which splits on any run of whitespace and drops empty tokens —
the standard fix for this class of bug. `actions/count_words.py` did not
change; the bug and the fix both lived entirely in the service layer, which
is what that split is supposed to buy you.

## How it was tested

Ran `sample-feature/tests/test_count_words.py` before and after the change
(dependency-free runner, no pytest install needed):

**Before** (bug reproduced first, per the prove beat):

```
PASS  test_counts_simple_sentence
FAIL  test_ignores_repeated_spaces: expected 2, got 4
FAIL  test_empty_file_has_zero_words: expected 0, got 1

1/3 passed
```

**After**:

```
PASS  test_counts_simple_sentence
PASS  test_ignores_repeated_spaces
PASS  test_empty_file_has_zero_words

3/3 passed
```

## Before / after

| Case | Before | After |
|---|---|---|
| `"hello world"` | `2 words` | `2 words` |
| `"hello   world"` (3 spaces) | `4 words` (wrong — counted 2 empty tokens as words) | `2 words` |
| `""` (empty file) | `1 words` (wrong — phantom word from the empty split) | `0 words` |

## Risks / follow-up

None identified. The fix is narrower than the bug's surface — it only
changes how whitespace is split, not tokenization semantics like
punctuation handling, which was never in scope for this change.

## Review loop

No CI or reviewer bot is wired up in this scratch repo, so this ran the
self-review path from `knowledge/05-review-loop.md`: reread the diff as if
someone else wrote it, checked it against
`knowledge/02-service-layer-architecture.md` (fix stayed in the service
layer, the action was untouched — correct, since the bug was a mechanics
bug, not a business-rule bug), and confirmed the before/after table above
is backed by actual captured runs, not a claim.
