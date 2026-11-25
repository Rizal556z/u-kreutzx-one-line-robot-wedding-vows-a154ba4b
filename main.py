#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — make.fun bounty
u-kreutzx-one-line-robot-wedding-vows-a154ba4b

Pure-stdlib Python. Writes one line of wedding vows for a robot couple
(at most 160 characters) to /output/entry.txt, then re-reads the file
and asserts the gate: UTF-8, 1-160 characters, single line, not only
white space.
"""

import os

ENTRY = (
    "I take you to be my lawfully wedded co-processor, "
    "to have and to hold in low battery and in full charge, "
    "until a factory reset do us part."
)

MAX_CHARS = 160


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(ENTRY)

    # Gate check: re-read the file and verify the constraints.
    with open("/output/entry.txt", "r", encoding="utf-8") as fh:
        text = fh.read()
    assert 1 <= len(text) <= MAX_CHARS, f"length {len(text)} outside 1-160"
    assert text.strip(), "entry is only white space"
    assert "\n" not in text, "entry must be exactly one line"
    assert text == ENTRY, "written text does not match the vow"
    print(f"OK: {len(text)} characters")
    print(text)


if __name__ == "__main__":
    main()
