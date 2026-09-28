# Schede Due Pi Greco

Schede applicazione (ALI, CIL, EOAT, FMT) e kit campioni, A4 fronte/retro.

- `content.py` — i testi (IT). Per correggere una frase si tocca solo questo file.
- `build.py` — impaginazione: genera `html/*.html`.
- `assets/scheda.css` — sistema grafico condiviso (colori, tipografia, componenti).
- `assets/tavola_*.svg` — tavole isometriche vettoriali, estratte dalle schede rev. 00 in `originali/`
  con `tools/extract_illustrations.py` (richiede `pymupdf`).
- `assets/fonts/` — Archivo, IBM Plex Serif, IBM Plex Mono in locale: la stampa non dipende dalla rete.
- `pdf/` — le schede pronte.

## Rigenerare i PDF

```sh
python3 build.py
NODE_PATH=$(npm root -g) node tools/print_pdf.js          # --png per le anteprime in preview/
```

Serve Playwright con Chromium. Gli HTML si possono anche aprire nel browser per un controllo a schermo.
