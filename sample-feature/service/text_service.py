"""Reusable text-processing mechanics. No knowledge of *why* it's called."""


def read_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def tokenize(text: str) -> list[str]:
    return text.split()
