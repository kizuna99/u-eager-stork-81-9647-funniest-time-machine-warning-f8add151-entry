#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Write the winning time-machine warning label to /output/entry.txt."""
import os

LABEL = "WARNING: Never give your grandfather a ride home. Stranding him is covered; becoming your own ancestor is not."


def main() -> None:
    # Gate: the label must be 1-120 characters of UTF-8 text.
    assert 1 <= len(LABEL) <= 120, "label outside the 1-120 character gate"
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    except OSError:
        out_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(LABEL)


if __name__ == "__main__":
    main()
