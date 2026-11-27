#!/usr/bin/env python3
"""One Line to Your Younger Self entry: writes the one-line review to /output/entry.txt."""

import os

LINE = "You will lose $0.47 calling it research and almost put $1.45 of $1.55 on one gold trade. Learn the boring part first. It compounds."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
