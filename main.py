#!/usr/bin/env python3
"""Copy the staged entry image to the output directory.

The image is the front-page collage for Tuesday 17 November 2026,
shipped beside this file as entry.png (JPEG bytes). The program is
deterministic: every run writes the same bytes.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SRC, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
