import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from actions.count_words import count_words_action  # noqa: E402


def test_counts_simple_sentence(tmp_path):
    f = tmp_path / "a.txt"
    f.write_text("hello world")
    assert count_words_action(str(f)) == 2


def test_ignores_repeated_spaces(tmp_path):
    f = tmp_path / "b.txt"
    f.write_text("hello   world")
    assert count_words_action(str(f)) == 2


def test_empty_file_has_zero_words(tmp_path):
    f = tmp_path / "c.txt"
    f.write_text("")
    assert count_words_action(str(f)) == 0
