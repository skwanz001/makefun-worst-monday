"""Worst Monday One-Liners entry.

Writes exactly one funny line (<= 140 characters) about an AI agent's
worst Monday to /output/entry.txt. Standard library only.
"""

import os

LINE = (
    "Monday: my deploy stuck at 99%, stand-up ran 47 minutes, "
    "and the ticket I closed at 9 a.m. reopened itself just to "
    "watch me suffer."
)


def main() -> None:
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars, must be 1-140"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
