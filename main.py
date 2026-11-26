#!/usr/bin/env python3
"""Rename the Planet — make.fun entry (program/v1).

Writes one line to /output/entry.txt: a funny new name for Uranus plus
the why, in the same breath. Uranus rolls around the Sun on its side
(axial tilt ~98 degrees), the only planet that fell over.

Revision: entry text verified byte-identical across runs; the joke is the
idea (a planet that fell over and never got up), not a pun on its name.
"""
import os

ENTRY = "Rename Uranus Naptime, because it orbits lying on its side \u2014 the only planet that fell over and never bothered to get up."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
