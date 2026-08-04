#!/usr/bin/env python3
"""Render a PPTX to PDF and per-slide PNGs using installed Office tools."""

from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pptx", type=Path)
    parser.add_argument("--outdir", type=Path, default=Path("rendered"))
    parser.add_argument("--dpi", type=int, default=144)
    args = parser.parse_args()
    pptx = args.pptx.resolve()
    outdir = args.outdir.resolve()
    outdir.mkdir(parents=True, exist_ok=True)

    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    pdftoppm = shutil.which("pdftoppm")
    if not soffice:
        raise SystemExit("No soffice/libreoffice found; install LibreOffice or render with the host presentation tool.")
    if not pdftoppm:
        raise SystemExit("No pdftoppm found; install Poppler or render PDF pages with the host tool.")

    run([soffice, "--headless", "--convert-to", "pdf", "--outdir", str(outdir), str(pptx)])
    pdf = outdir / f"{pptx.stem}.pdf"
    if not pdf.exists():
        raise SystemExit(f"Expected PDF was not created: {pdf}")
    prefix = outdir / "slide"
    run([pdftoppm, "-png", "-r", str(args.dpi), str(pdf), str(prefix)])
    for page in sorted(outdir.glob("slide-*.png")):
        number = page.stem.rsplit("-", 1)[-1]
        page.rename(outdir / f"slide-{int(number):02d}.png")
    print(pdf)
    print(f"{len(list(outdir.glob('slide-*.png')))} slide PNGs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
