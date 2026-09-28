"""Anteprime delle copertine (thumbs/*.jpg) e archivio con tutte le schede (pdf/DPG_Schede_IT.zip).

Uso: python3 tools/pack.py   (dopo print_pdf.js; richiede pymupdf)
"""
import zipfile
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
PDF, THUMBS = ROOT / "pdf", ROOT / "thumbs"
ZIP = PDF / "DPG_Schede_IT.zip"


def main():
    THUMBS.mkdir(exist_ok=True)
    pdfs = sorted(PDF.glob("*.pdf"))
    for f in pdfs:
        page = pymupdf.open(f)[0]
        pix = page.get_pixmap(matrix=pymupdf.Matrix(560 / page.rect.width, 560 / page.rect.width))
        pix.save(THUMBS / f"{f.stem}.jpg", jpg_quality=82)
        print(f.name, f.stat().st_size // 1024, "KB")
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
        for f in pdfs:
            z.write(f, f.name)
    print(ZIP.name, ZIP.stat().st_size // 1024, "KB")


if __name__ == "__main__":
    main()
