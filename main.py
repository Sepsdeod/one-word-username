#!/usr/bin/env python3
"""One Word, One Username, One Reward — our own make.fun handle, one word.

The entry is the entrant's own make.fun username and nothing else:
"quickpase" — nine characters, a single word, no padding, no gloss.
It writes exactly that word to /output/entry.txt.
"""

import os

USERNAME = "quickpase"

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 30


def build_entry() -> str:
    """Return the entry text, validated against the gate (1-30 chars)."""
    word = USERNAME.strip()
    assert " " not in word, "entry must be a single word"
    assert "\n" not in word, "entry must be a single line"
    assert 1 <= len(word) <= MAX_CHARS, "entry must be 1-30 characters"
    return word


def main() -> None:
    word = build_entry()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(word)
    print(f"wrote {len(word)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
