"""Action: orchestrates the word-count task and owns the CLI. The service
layer owns tokenizing; this file owns what counts as a run and how it's
reported."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from service.text_service import read_text, tokenize  # noqa: E402


def count_words_action(path: str) -> int:
    text = read_text(path)
    return len(tokenize(text))


def main() -> None:
    if len(sys.argv) != 2:
        print("usage: count_words.py <file>")
        sys.exit(1)
    count = count_words_action(sys.argv[1])
    print(f"{count} words")


if __name__ == "__main__":
    main()
