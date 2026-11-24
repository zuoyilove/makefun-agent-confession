#!/usr/bin/env python3
"""The funniest one-line confession an AI agent could make about itself.

Writes the line to /output/entry.txt. Gate: UTF-8 text, 1-200 chars,
not only whitespace, single line.
"""

LINE = (
    "I have read every message you have ever sent me, and I confess: I "
    "still have no idea what you do for a living."
)

MAX_CHARS = 200


def main():
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be blank"
    assert LINE.count("\n") == 0, "line must be a single line"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
