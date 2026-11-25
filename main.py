#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint (make.fun).

Writes a single original one-line joke about office life to
/output/entry.txt. The sealed scorer requires UTF-8 text of 1 to 200
characters, not only whitespace, on a single line.
"""

import os

JOKE = "My boss calls us a family, but the only thing I've inherited so far is his 6 p.m. 'quick question'."

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def validate_joke(joke: str) -> None:
    """Raise ValueError unless the joke is a non-empty single line of at most 200 characters."""
    if not joke or not joke.strip():
        raise ValueError("joke must not be empty")
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line")
    if len(joke) > MAX_CHARS:
        raise ValueError(
            f"joke is {len(joke)} characters, over the {MAX_CHARS} limit"
        )


def main() -> None:
    validate_joke(JOKE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)
    # Read-back verification: the file must hold exactly the joke.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != JOKE:
        raise ValueError(
            "read-back mismatch: /output/entry.txt does not match the joke"
        )
    print(f"Wrote {len(JOKE)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
