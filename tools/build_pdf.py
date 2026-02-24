#!/usr/bin/env python3
"""
SCU PDF Builder — Assembles episode slide images into a single PDF.

Usage:
    py tools/build_pdf.py --episode EP1
    py tools/build_pdf.py --episode EP1 --series decisive-intelligence
    py tools/build_pdf.py --episode EP1 --output custom_name.pdf

Images are embedded lossless (no re-encoding). Output PDF preserves
full PNG quality at original resolution (2752x1536, 16:9).
"""

import argparse
import re
import sys
from pathlib import Path

try:
    import img2pdf
except ImportError:
    print("Error: img2pdf not installed. Run: pip install img2pdf")
    sys.exit(1)


def natural_sort_key(filename: str):
    """Sort files naturally: 0, 1, 2, ... 9, 10, ... 36, 36B, 36C, 37 ..."""
    stem = Path(filename).stem
    # Split into numeric prefix and optional letter suffix
    match = re.match(r'^(\d+)([A-Z]?)$', stem)
    if match:
        num = int(match.group(1))
        suffix = match.group(2) or ''  # empty string sorts before any letter
        return (num, suffix)
    # Fallback for unexpected names
    return (999999, stem)


def find_images(images_dir: Path) -> list[Path]:
    """Find and sort all PNG images in the episode directory."""
    pngs = sorted(images_dir.glob("*.png"), key=lambda p: natural_sort_key(p.name))
    return pngs


def build_pdf(images: list[Path], output_path: Path):
    """Build PDF from images using img2pdf (lossless, no re-encoding)."""
    # img2pdf doesn't support RGBA PNGs directly (PDF doesn't support alpha).
    # We need to strip the alpha channel first.
    from PIL import Image
    import io
    import tempfile

    print(f"Processing {len(images)} images...")

    converted_paths = []
    tmpdir = Path(tempfile.mkdtemp(prefix="scu_pdf_"))

    for i, img_path in enumerate(images):
        img = Image.open(img_path)
        if img.mode == 'RGBA':
            # Composite onto white background to remove alpha
            bg = Image.new('RGB', img.size, (0, 0, 0))  # black background
            bg.paste(img, mask=img.split()[3])  # paste using alpha as mask
            out_path = tmpdir / f"{i:04d}.png"
            bg.save(out_path, 'PNG', optimize=False)
            converted_paths.append(out_path)
        else:
            converted_paths.append(img_path)

        # Progress indicator
        pct = (i + 1) / len(images) * 100
        print(f"  [{i+1}/{len(images)}] {img_path.name} ({pct:.0f}%)", end='\r')

    print()  # newline after progress

    # Build PDF
    print(f"Assembling PDF...")
    pdf_bytes = img2pdf.convert([str(p) for p in converted_paths])

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'wb') as f:
        f.write(pdf_bytes)

    # Cleanup temp files
    for p in tmpdir.glob("*"):
        p.unlink()
    tmpdir.rmdir()

    size_mb = output_path.stat().st_size / (1024 * 1024)
    print(f"PDF created: {output_path} ({size_mb:.1f} MB, {len(images)} pages)")


def main():
    parser = argparse.ArgumentParser(
        description="SCU PDF Builder — Assemble episode slides into PDF"
    )
    parser.add_argument(
        "--episode", required=True,
        help="Episode directory name (e.g., EP1, EP2, EP3)"
    )
    parser.add_argument(
        "--series", default="decisive-intelligence",
        help="Series directory name (default: decisive-intelligence)"
    )
    parser.add_argument(
        "--output", default=None,
        help="Output PDF filename (default: auto-generated from episode name)"
    )

    args = parser.parse_args()

    # Resolve paths relative to repo root
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent

    images_dir = repo_root / args.series / "extended-cut" / "images" / args.episode

    if not images_dir.exists():
        print(f"Error: Images directory not found: {images_dir}")
        sys.exit(1)

    images = find_images(images_dir)
    if not images:
        print(f"Error: No PNG images found in {images_dir}")
        sys.exit(1)

    # Output path
    if args.output:
        output_path = Path(args.output)
        if not output_path.is_absolute():
            output_path = repo_root / args.series / "extended-cut" / args.output
    else:
        output_path = repo_root / args.series / "extended-cut" / f"{args.episode}_Extended_Cut.pdf"

    print(f"SCU PDF Builder")
    print(f"  Series:  {args.series}")
    print(f"  Episode: {args.episode}")
    print(f"  Images:  {len(images)} slides")
    print(f"  Source:  {images_dir}")
    print(f"  Output:  {output_path}")
    print()

    # Show slide order
    print("Slide order:")
    for img in images:
        print(f"  {img.name}")
    print()

    build_pdf(images, output_path)


if __name__ == "__main__":
    main()
