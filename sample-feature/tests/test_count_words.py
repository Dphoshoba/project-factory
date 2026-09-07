"""No pytest dependency on purpose — run with `python3 tests/test_count_words.py`
so this factory demo has zero install step."""

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from actions.count_words import count_words_action  # noqa: E402


def with_tmp_file(name: str, content: str):
    tmp_dir = tempfile.mkdtemp()
    path = Path(tmp_dir) / name
    path.write_text(content, encoding="utf-8")
    return str(path)


def test_counts_simple_sentence():
    f = with_tmp_file("a.txt", "hello world")
    assert count_words_action(f) == 2, f"expected 2, got {count_words_action(f)}"


def test_ignores_repeated_spaces():
    f = with_tmp_file("b.txt", "hello   world")
    assert count_words_action(f) == 2, f"expected 2, got {count_words_action(f)}"


def test_empty_file_has_zero_words():
    f = with_tmp_file("c.txt", "")
    assert count_words_action(f) == 0, f"expected 0, got {count_words_action(f)}"


if __name__ == "__main__":
    tests = [
        test_counts_simple_sentence,
        test_ignores_repeated_spaces,
        test_empty_file_has_zero_words,
    ]
    failures = 0
    for t in tests:
        try:
            t()
            print(f"PASS  {t.__name__}")
        except AssertionError as e:
            failures += 1
            print(f"FAIL  {t.__name__}: {e}")
    print(f"\n{len(tests) - failures}/{len(tests)} passed")
    sys.exit(1 if failures else 0)
