#!/usr/bin/env python3
"""One Line, One Laugh — writes a single funny line to /output/entry.txt."""

import os

LINE = "My fridge now locks itself at midnight and leaves a note saying, 'We both know you're not hungry, you're bored.'"


def main():
    if not LINE or not LINE.strip():
        raise ValueError("joke line must not be empty or only whitespace")
    if len(LINE) > 140:
        raise ValueError("joke line must be at most 140 characters")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("joke line must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Write-back verification: read the file back and compare byte-for-byte.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    if written != LINE.encode("utf-8"):
        raise ValueError("write-back verification failed: file differs from line")


if __name__ == "__main__":
    main()
