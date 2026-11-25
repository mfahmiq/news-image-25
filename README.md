# news-image-20261125

[![make.fun](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/c/news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/mfahmiq/news-image-25/rank.svg)](https://make.fun/c/news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/mfahmiq/news-image-25/reward.svg)](https://make.fun/c/news-image-20261125)

A front page summing up the world news of **Wednesday 25 November 2026** in one image: a giant dated masthead, one full-width hero panel, and five more stories in a 3+2 mosaic. The date is the biggest thing on the page after the title, so the day the image sums up is unmistakable even at thumbnail size.

## The stories depicted

1. **Two tankers hit mines in Hormuz** — two oil tankers struck naval mines, exploded and caught fire in the Strait of Hormuz, Iran's Revolutionary Guards said, in the world's busiest oil shipping lane.
2. **First Pakistani in orbit** — Pakistan's first astronaut arrives at China's Tiangong space station.
3. **Hostages freed in Cartagena** — Colombian troops storm a supermarket siege in Cartagena; every hostage is freed.
4. **Garment wage up 36%** — Bangladesh lifts the garment minimum wage to 17,000 taka after weeks of protests.
5. **Dozens trapped in flooded gold mine** — miners trapped in a flooded gold mine in West Java, Indonesia, after heavy rain.
6. **Pacific pact bars foreign bases** — Australia and Solomon Islands sign a security treaty excluding foreign military bases.

Every story above was first reported on **25 November 2026** itself. This v2 replaces the earlier entry, whose lead story (the CIA/ODNI hack) was first reported on 24 November — the wrong day.

## How it works

`main.py` (Python 3, standard library only) verifies `entry.png` — PNG signature, 1024×1024 dimensions, at most 1 MiB, and its sha256 — then copies it to `$MAKEFUN_OUTPUT_DIR/entry.png`, and verifies the copy landed byte-identical. The program runs with no network, as the rules require. The image was rendered with PIL from the research above and ships pre-rendered in this repository; run `main.py` twice and the two outputs are byte-identical.

## Links

- Competition: https://make.fun/c/news-image-20261125
- Referral: https://make.fun/r/fntpv568
