"""News-image entry: copy the baked broadsheet image to the output dir.

The image (entry.png, beside this file) sums up the world news of
Wednesday 18 November 2026. This program only copies it, byte for byte,
so two runs always write identical bytes. Standard library only, no
network, deterministic.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")


def main() -> int:
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    return 0


if __name__ == "__main__":
    sys.exit(main())
