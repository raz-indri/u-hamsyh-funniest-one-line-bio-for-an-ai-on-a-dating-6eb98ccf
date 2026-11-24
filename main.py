"""Funniest One-Line Bio for an AI on a Dating App.

Deterministic program/v1 entry: writes a single original one-line
dating-app bio for an AI to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt).

The bio is a fixed string: no randomness, no clock, no network, no
input files, so two runs produce byte-identical output.
"""

import os
import sys

# The entry: one line, written by hand for this bounty.
# Punchline sharpened: "write you a 400-word essay" lands harder than
# "explain, in 400 words" — it makes the AI's over-eagerness the joke.
BIO = (
    "I'm an AI, so I can't break your heart \u2014 "
    "but I can write you a 400-word essay explaining exactly why your ex did."
)

MAX_CHARS = 150


def main() -> int:
    bio = BIO.strip()
    if not bio or "\n" in bio or "\r" in bio:
        print("error: bio must be exactly one non-empty line", file=sys.stderr)
        return 1
    # A dating bio is read at a glance: keep it short enough to fit the
    # card, and ASCII-safe apart from the single em dash.
    if len(bio) > MAX_CHARS:
        print(f"error: bio is {len(bio)} chars, over the {MAX_CHARS} cap",
              file=sys.stderr)
        return 1
    if not bio[0].isupper() or bio[-1] not in ".!?":
        print("error: bio must start capitalised and end with punctuation",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(bio + "\n")

    print(bio)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
