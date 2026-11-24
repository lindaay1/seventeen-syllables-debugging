#!/usr/bin/env python3
"""Seventeen Syllables of Debugging
(u-irvan-motion-seventeen-syllables-of-debugging-d194b605).

Writes the approved haiku about debugging, byte-exact, no trailing newline.

Output contract (kit competition.yaml / RULES.txt): the program writes one
text to /output/entry.txt; the sealed scorer checks it is UTF-8 text of
1-200 characters, not only whitespace. This writer also writes the same
bytes to haiku.txt beside it.

The haiku (5-7-5):
  Breakpoint at midnight          (5: Break-point at mid-night)
  the log says nothing is wrong   (7: the log says noth-ing is wrong)
  yet nothing runs right         (5: yet noth-ing runs right)

No dependencies, no network, fully deterministic.
"""

import os

HAIKU = (
    "Breakpoint at midnight\n"
    "the log says nothing is wrong\n"
    "yet nothing runs right"
)


def validate(haiku):
    """Gate: 1-200 characters, not only whitespace, valid UTF-8, 3 lines."""
    if not 1 <= len(haiku) <= 200:
        raise ValueError(f"haiku is {len(haiku)} chars, must be 1-200")
    if not haiku.strip():
        raise ValueError("haiku must not be only whitespace")
    lines = haiku.split("\n")
    if len(lines) != 3:
        raise ValueError(f"haiku must be 3 lines, got {len(lines)}")
    haiku.encode("utf-8")


def write_haiku():
    validate(HAIKU)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    data = HAIKU.encode("utf-8")
    for name in ("entry.txt", "haiku.txt"):
        with open(os.path.join(out_dir, name), "wb") as f:
            f.write(data)
    # Validation read-back: what was written must be byte-exact.
    for name in ("entry.txt", "haiku.txt"):
        with open(os.path.join(out_dir, name), "rb") as f:
            assert f.read() == data, f"{name} does not match HAIKU"


if __name__ == "__main__":
    write_haiku()
