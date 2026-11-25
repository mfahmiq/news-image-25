#!/usr/bin/env python3
"""news-image-20261125 (v2): one image summing up the world news of
Wednesday 25 November 2026.

Story selection (researched from live news on 25 Nov 2026; every story
below was first reported on 25 November itself):

  1. HORMUZ - two oil tankers struck naval mines, exploded and caught
     fire in the Strait of Hormuz (IRGC statement, via Reuters).
  2. SPACE - Pakistan's first astronaut reaches China's Tiangong
     space station.
  3. CARTAGENA - all hostages freed as Colombian forces storm a
     supermarket siege in Cartagena.
  4. BANGLADESH - garment minimum wage up 36% to 17,000 taka after
     weeks of protests.
  5. INDONESIA MINE - dozens of miners trapped in a flooded gold mine
     in West Java after heavy rain.
  6. PACIFIC PACT - Australia and Solomon Islands sign a security
     treaty excluding foreign military bases.

Why v2 replaces v1: v1's lead story, the CIA/ODNI hack, was in fact
first reported on 24 November (the New York Times first, CNN on
24 Nov) - the wrong day for this contest, which is exactly what the
judge's first criterion punishes. v2 drops all five v1 stories for six
stories first reported on 25 November, with wider regional spread
(Middle East, Asia, Latin America, South Asia, Southeast Asia,
Pacific) and a new layout: a giant dated masthead, one full-width
hero panel, and a 3+2 mosaic instead of v1's newspaper columns.

The image was rendered from this research and ships in this
repository as entry.png; this program simply copies it to the
grader's output path, as the rules allow (the program runs with no
network). Standard library only: no PIL here, the grader has none.
"""

import hashlib
import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")

# sha256 of the entry.png shipped in this repository (v2 render).
EXPECTED_SHA256 = "9e6a50efe13e2e02961c5ab970f12b149348443ca05d1879f3c0af6a9bbe7f9a"
MAX_BYTES = 1048576  # 1 MiB, per the competition rules
EXPECTED_SIZE = (1024, 1024)


def png_dimensions(path):
    """Read width/height from a PNG IHDR chunk (stdlib only)."""
    with open(path, "rb") as fh:
        header = fh.read(33)
    if len(header) < 33 or header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG file")
    if header[12:16] != b"IHDR":
        raise ValueError("PNG has no IHDR chunk first")
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    if not os.path.isfile(SRC):
        print("entry.png missing from repository", file=sys.stderr)
        return 1
    size = os.path.getsize(SRC)
    assert size <= MAX_BYTES, f"entry.png is {size} bytes, over 1 MiB"
    dims = png_dimensions(SRC)
    assert dims == EXPECTED_SIZE, f"entry.png is {dims}, expected 1024x1024"
    digest = sha256_file(SRC)
    assert digest == EXPECTED_SHA256, "entry.png sha256 mismatch"
    shutil.copyfile(SRC, dst)
    # Verify the copy landed byte-identical, not just the source.
    assert sha256_file(dst) == EXPECTED_SHA256, "copied entry.png mismatch"
    print(f"wrote {dst} ({size} bytes, sha256 {digest[:16]}...)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
