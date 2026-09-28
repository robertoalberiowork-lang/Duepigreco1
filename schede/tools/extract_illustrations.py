"""Estrae le tavole isometriche dalle schede PDF originali (rev. 00).

Per ogni scheda prende la pagina 1, ne esporta l'SVG vettoriale, toglie
testi e sfondi di pagina e ritaglia la sola area della tavola. Le etichette
vengono salvate a parte (posizione + testo) per essere reimpaginate nel
nuovo layout.

Uso: python3 extract_illustrations.py <cartella-pdf-originali>
Richiede: pymupdf
"""
import json
import re
import sys
from pathlib import Path

import pymupdf

SHEETS = {"ALI": "DPG_Scheda_ALI_IT", "CIL": "DPG_Scheda_CIL_IT",
          "EOAT": "DPG_Scheda_EOAT_IT", "FMT": "DPG_Scheda_FMT_IT"}
# area della tavola in punti PDF (x0, y0, x1, y1), etichette comprese
BOX = (40.0, 400.0, 555.0, 750.0)
OUT = Path(__file__).resolve().parent.parent / "assets"


def main(src):
    src = Path(src)
    labels = {}
    for code, stem in SHEETS.items():
        pdf = next(src.glob(f"*{stem}.pdf"))
        page = pymupdf.open(pdf)[0]
        svg = page.get_svg_image(text_as_path=False)
        # via i testi (reimpaginati in HTML) e gli sfondi a pagina piena
        svg = re.sub(r"<text\b.*?</text>", "", svg, flags=re.S)
        svg = re.sub(r'<path[^>]*d="M0 0H(2480V3507|794V1123)[^"]*"[^>]*/>', "", svg)
        x0, y0, x1, y1 = BOX
        svg = re.sub(r'width="[^"]+" height="[^"]+" viewBox="[^"]+"',
                     f'width="{x1-x0}" height="{y1-y0}" viewBox="{x0} {y0} {x1-x0} {y1-y0}"',
                     svg, count=1)
        (OUT / f"tavola_{code}.svg").write_text(svg)
        items = []
        for b in page.get_text("dict")["blocks"]:
            for line in b.get("lines", []):
                for s in line["spans"]:
                    bx = s["bbox"]
                    if abs(s["size"] - 7.095) < .05 and y0 <= bx[1] <= y1:
                        items.append({"text": s["text"].strip(),
                                      "x": round((bx[0] - x0) / (x1 - x0) * 100, 2),
                                      "y": round(((bx[1] + bx[3]) / 2 - y0) / (y1 - y0) * 100, 2)})
        labels[code] = items
        print(code, len(svg) // 1024, "KB", items)
    (OUT / "tavole_labels.json").write_text(json.dumps(labels, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main(sys.argv[1])
