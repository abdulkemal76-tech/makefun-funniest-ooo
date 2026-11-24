#!/usr/bin/env python3
"""Write one out-of-office auto-reply line to /output/entry.txt.

The line: a real one-line out-of-office reply, funny because the inbox
is left in the care of a named ficus who judges instead of answering.
"""

import os

LINE = (
    "Out of office until Monday. "
    "My inbox is guarded by Kevin, a ficus. "
    "He does not read email. He judges it."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
