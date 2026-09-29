# Schede Due Pi Greco

Schede applicazione (ALI, CIL, EOAT, FMT) e kit campioni, A4 fronte/retro.

- `content.py` — i testi (IT). Per correggere una frase si tocca solo questo file.
- `build.py` — impaginazione: genera `html/*.html`.
- `assets/scheda.css` — sistema grafico condiviso (colori, tipografia, componenti).
- `assets/tavola_*.svg` — tavole isometriche vettoriali, estratte dalle schede rev. 00 in `originali/`
  con `tools/extract_illustrations.py` (richiede `pymupdf`).
- `assets/fonts/` — Archivo, IBM Plex Serif, IBM Plex Mono in locale: la stampa non dipende dalla rete.
- `pdf/` — le schede pronte, più `DPG_Schede_IT.zip` con tutte insieme.
- `thumbs/` — anteprime delle copertine usate nella sezione Download del sito (`Index.html#download`).

## Scheda settore trattamento acque (DPG-SET-H2O)

`h2o.py` genera `html/DPG_Settore_H2O_IT.html` (6 pagine); i disegni vettoriali sono in `h2o_art.py`,
gli stili aggiuntivi in `assets/h2o.css`. Fonti e grado di verifica dei dati: `ricerca/H2O_PP_dossier.md`.

## Rigenerare i PDF

```sh
python3 build.py && python3 h2o.py
NODE_PATH=$(npm root -g) node tools/print_pdf.js          # --png per le anteprime in preview/
python3 tools/pack.py                                    # copertine per il sito + ZIP
```

Serve Playwright con Chromium. Gli HTML si possono anche aprire nel browser per un controllo a schermo.
