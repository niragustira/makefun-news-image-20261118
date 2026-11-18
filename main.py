"""Wednesday 18 November 2026, summed up in a single picture.

Running this file places a copy of the front-page collage kept next to
it at the location the competition reads, /output/entry.png, or in the
directory named by MAKEFUN_OUTPUT when that variable is set.

The collage is a newspaper front page for WEDNESDAY 18 NOVEMBER 2026.
Four stories share the page: the Kerch Bridge to Crimea is hit again
while bridges in Kyiv come under fire; drones aimed at a US radar site
at Isa Air Base in Bahrain are all intercepted; Trump lands in Manila
for the Quad talks and the ASEAN and East Asia summits; and Cyclone
Akvan builds into a severe cyclonic storm in the Bay of Bengal, bound
for the Andhra Pradesh coast.

Nothing here touches the network. The copy is byte for byte the same
every time, so two runs of this program produce identical files.
"""

import os
import shutil
import sys
from pathlib import Path

IMAGE_FILE = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"


def locate_image() -> Path:
    here = Path(__file__).resolve().parent
    image = here / IMAGE_FILE
    if not image.is_file():
        raise FileNotFoundError(f"no {IMAGE_FILE} beside {__file__}")
    with image.open("rb") as handle:
        if handle.read(8) != b"\x89PNG\r\n\x1a\n":
            raise ValueError(f"{IMAGE_FILE} is not a PNG file")
    return image


def choose_destination() -> Path:
    wanted = os.environ.get("MAKEFUN_OUTPUT") or DEFAULT_OUTPUT_DIR
    return Path(wanted) / IMAGE_FILE


def place_copy(image: Path, destination: Path) -> int:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(image, destination)
    if destination.stat().st_size != image.stat().st_size:
        raise IOError(f"copy incomplete: {destination}")
    return 0


def main() -> int:
    image = locate_image()
    return place_copy(image, choose_destination())


if __name__ == "__main__":
    sys.exit(main())
