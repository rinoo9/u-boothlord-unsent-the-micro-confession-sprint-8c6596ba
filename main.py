#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint - make.fun entry.

Writes one two-part micro-confession to /output/entry.txt:
a To: line naming who it was meant for, and the unsent message
itself, one line written exactly as it was typed.
"""

import os
import sys

ENTRY = (
    "To: Mom, who still texts me to eat more vegetables\n"
    "I still hide the vegetables under the rice every time she visits, "
    "and I am old enough to know better."
)

MAX_CHARS = 260


def main() -> None:
    text = ENTRY
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    lines = text.splitlines()
    if len(lines) != 2 or not lines[0].startswith("To: "):
        raise SystemExit("entry must be a To: line plus one message line")
    if len(lines[1]) > 200:
        raise SystemExit("message line is over 200 characters")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(text)
    print(f"({len(text)} characters, limit {MAX_CHARS})", file=sys.stderr)


if __name__ == "__main__":
    main()
