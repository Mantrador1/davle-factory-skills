#!/usr/bin/env python3
"""
DAVLE locked-region compositor.

Black mask pixels preserve SOURCE.
White mask pixels take CANDIDATE.
Gray mask pixels blend the two.

Usage:
  python tools/locked_region_composite.py \
    --source source.png --candidate candidate.png \
    --mask mutable_mask.png --output final.png --feather 1.5

Requires Pillow.
"""
from argparse import ArgumentParser
from pathlib import Path
from PIL import Image, ImageFilter, ImageChops

def main():
    p = ArgumentParser()
    p.add_argument("--source", required=True)
    p.add_argument("--candidate", required=True)
    p.add_argument("--mask", required=True)
    p.add_argument("--output", required=True)
    p.add_argument("--feather", type=float, default=0.0)
    args = p.parse_args()

    src = Image.open(args.source).convert("RGBA")
    cand = Image.open(args.candidate).convert("RGBA")
    mask = Image.open(args.mask).convert("L")

    if cand.size != src.size:
        raise SystemExit(f"candidate size {cand.size} != source size {src.size}")
    if mask.size != src.size:
        raise SystemExit(f"mask size {mask.size} != source size {src.size}")

    if args.feather > 0:
        mask = mask.filter(ImageFilter.GaussianBlur(radius=args.feather))

    out = Image.composite(cand, src, mask)
    out.save(args.output)

    # Deterministic regression check: outside strict mask, output must equal source.
    strict = Image.open(args.mask).convert("L")
    locked = strict.point(lambda v: 255 if v == 0 else 0)
    diff = ImageChops.difference(out, src).convert("RGB")
    diff_locked = Image.composite(diff, Image.new("RGB", src.size, "black"), locked)
    bbox = diff_locked.getbbox()
    print("LOCKED_REGION_DIFF=PASS" if bbox is None else f"LOCKED_REGION_DIFF=FAIL bbox={bbox}")
    print(f"OUTPUT={Path(args.output).resolve()}")

if __name__ == "__main__":
    main()
