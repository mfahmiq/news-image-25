#!/usr/bin/env python3
"""news-image-20261125: one image summing up the world news of
Wednesday 25 November 2026.

Story selection (researched from live news on 25 Nov 2026, ~02:00Z):
  1. CIA & ODNI hit by a cyberattack (CNN, first reported 25 Nov) - the
     day's biggest story; the FBI crime database was hit by a suspected
     breach in the same wave. Lead panel.
  2. WHO evacuates Ebola health workers in DR Congo (25 Nov) - staff fled
     a hospital in Ituri after sheltering 3 days from fighting, mid-outbreak.
  3. NATO to deploy early-warning aircraft to Poland (reported 25 Nov) -
     after missiles landed in Poland during an attack on Ukraine.
  4. Indonesia's Vice-President resigns (reported 25 Nov) - amid political
     strain. Gives the front page an Asian story.
  5. US Army to detonate ~10,000 lb of unstable lead azide in Iowa on
     Wednesday morning, 25 Nov, after days of delays.

Deliberately EXCLUDED (all belong to 24 Nov, not 25 Nov): the Houthi drone
strike on Riyadh's PIF Tower (11 injured, Tue 24 Nov), the Huawei guilty
verdict (24 Nov), Trump awarding Giuliani the Medal of Freedom (24 Nov),
Israel's warning that Iran is building chemical weapons (24 Nov), Sarkozy
ordered to trial (24 Nov), Zelenskyy confirming the sinking of the Russian
corvette Merkury off Libya (23 Nov), Real Madrid 5-1 PSV and England's T20
win over Australia (24 Nov evening). Including them would have made the
image a picture of the wrong day; the five above are the day's own news.

The image was rendered from this research and ships in this repository as
entry.png; this program simply copies it to the grader's output path, as
the rules allow (the program runs with no network).
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    if not os.path.isfile(SRC):
        print("entry.png missing from repository", file=sys.stderr)
        return 1
    shutil.copyfile(SRC, dst)
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
