#!/usr/bin/env python3
"""Museum of the Year 3000 — museum label for an ordinary object from today.

Writes a single original museum label (1-200 characters, UTF-8) to
/output/entry.txt, exactly as the competition gate expects.
"""

import os

# Revised draft (revision pass against the judging criteria): the same
# wet-floor misreading, now with a second true-and-absurd beat — the sign
# stayed up for hours after the floor had dried, so the curator reports
# humans warning each other about a danger that no longer existed. The
# joke stays in the line itself, deadpan, with no explanation around it.
LABEL = (
    "Wet Floor Sign, c. 2024. Placed after mopping, to warn visitors of "
    "the very danger the cleaners had just created \u2014 and left there "
    "for hours after it dried."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = LABEL.strip()
    assert 1 <= len(text) <= 200, f"label must be 1-200 chars, got {len(text)}"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
