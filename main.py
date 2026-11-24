#!/usr/bin/env python3
"""The Vacuum's Alibi — make.fun entry.

Writes one line — the excuse a robot vacuum gives for missing a spot — to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Python 3 standard library only. No network.
"""
import os
import sys

LINE = "My lidar saw the spot. It also saw what your toddler did there in March. Some spots I clean; that one I respect."
MAX_CHARS = 200


def check_line() -> int:
    """Return the character count of the line."""
    return len(LINE)


def main() -> int:
    if "--check" in sys.argv[1:]:
        chars = check_line()
        print(f"{chars} characters")
        return 0 if 1 <= chars <= MAX_CHARS and LINE.strip() else 1
    data = LINE.encode("utf-8")
    if not (1 <= len(LINE) <= MAX_CHARS):
        print(f"line must be 1-{MAX_CHARS} characters, got {len(LINE)}", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("line must not be only white space", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        print("round-trip mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
