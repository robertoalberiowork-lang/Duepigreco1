"""Scheda settore DPG-SET-H2O rev. 02 — trattamento acque reflue e acqua industriale (6 pagine, IT/FR/EN).

Uso:  python3 h2o.py [it fr en]  → html/DPG_Settore_H2O_<LINGUA>.html ; poi  node tools/print_pdf.js
Testi: h2o_text.py. Disegni: h2o_art.py. Fonti e grado di verifica dei dati: ricerca/H2O_PP_dossier.md
"""
import sys
from html import escape
from pathlib import Path

import h2o_art as art
from build import UI, contact_list, kpis, page_shell, svg
from h2o_text import LANGS

ROOT = Path(__file__).resolve().parent
DOC = "DPG-SET-H2O"
TOTAL = 6
LOGO = (ROOT / "assets" / "logo_2pi.svg").read_text()
ART_IT = dict(art.LBL)
ARROW = svg('<path d="M5 12h14M13 6l6 6-6 6" stroke="#e63329" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')


def head(top, bottom):
    return f"""
  <header class="head">
    <div class="logo">{LOGO}<div><b>DUE PI<br>GRECO</b><small>Additive manufacturing</small></div></div>
    <div class="meta"><span>{escape(top)}</span><br><b>{escape(bottom)}</b></div>
  </header>"""


def tblock(t, page):
    a, b, c, d, e = t["tb"]
    return f"""
  <dl class="tblock">
    <div><dt>{a}</dt><dd>{DOC}</dd></div>
    <div><dt>{b}</dt><dd>{t["rev"]}</dd></div>
    <div><dt>{c}</dt><dd>{t["code"]}</dd></div>
    <div><dt>{d}</dt><dd>Due Pi Greco S.r.l.</dd></div>
    <div><dt>{e}</dt><dd><b>{page:02d}</b> / {TOTAL:02d}</dd></div>
  </dl>"""


def sec(n, title, note=""):
    em = f"<em>{escape(note)}</em>" if note else ""
    return f'<div class="sec-h"><b>{n}</b><span>{escape(title)}</span>{em}</div>'


def callouts(labels):
    return "".join(f'<div class="callout" style="left:{l["x"]}%;top:{l["y"]}%"><i>{i:02d}</i><span>{escape(l["text"])}</span></div>'
                   for i, l in enumerate(labels, 1))


def ticks(items):
    return "".join(f"<li><b>{escape(b)}</b>{escape(r)}</li>" for b, r in items)


def frame(fig_n, fig_txt, inner):
    return f"""<span class="corner tl"></span><span class="corner tr"></span><span class="corner bl"></span><span class="corner br"></span>
      <div class="fig"><b>Fig. {fig_n}</b> — {escape(fig_txt)}</div>
      <div class="scale">Tav. {DOC}</div>
      {inner}"""


# ======================================================================= pagina 1
def p1(t):
    s, labels, ratio = art.cover_svg()
    l1, l2 = t["h1"]
    return f"""
<section class="page cover">
  <div class="topbar"></div>
  {head(t["sheet"], DOC)}
  <div class="hero">
    <div class="eyebrow"><i></i>{escape(t["eyebrow1"])}</div>
    <h1 style="--h1:{t["h1_size"]}">{escape(l1)}<br>{escape(l2)}<em>.</em></h1>
    <p class="lead">{t["lead"]}</p>
  </div>
  {kpis(t["kpis"])}
  <div class="tavola">
    <div class="frame">
      {frame("01", t["fig1"], f'<div class="art" style="aspect-ratio:{ratio:.4f}">{s}{callouts(labels)}</div>')}
    </div>
    <div class="legend"><span>{escape(t["legend1"])}</span>
      <div class="keys"><div class="key"><i></i><span>{t["key_red"]}</span></div></div></div>
  </div>
  {tblock(t, 1)}
</section>"""


# ======================================================================= pagina 2
def p2(t):
    tiles = "".join(f'<div class="stat"><b>{escape(v)}</b><h4>{escape(h)}</h4><p>{escape(d)}</p></div>' for v, h, d in t["stats"])
    evs = "".join(f'<div class="evid"><small>{escape(a)}</small><h4>{escape(b)}</h4><p>{escape(c)}</p></div>' for a, b, c in t["evidence"])
    return f"""
<section class="page inner">
  <div class="topbar"></div>
  {head(t["sheet"] + " · " + DOC, t["p2_head"])}
  <div class="body">
    <div class="sec">
      {sec("01", t["s01"])}
      <div class="stats">{tiles}</div>
    </div>
    <div class="sec">
      {sec("02", t["s02"])}
      <div class="compare">
        <div class="col was"><div class="k"><i></i>{escape(t["was_k"])}</div>{escape(t["was"])}</div>
        <div class="arrow">{ARROW}</div>
        <div class="col now"><div class="k"><i></i>{escape(t["now_k"])}</div>{escape(t["now"])}</div>
      </div>
    </div>
    <div class="sec">
      {sec("03", t["s03"], t["s03_note"])}
      <div class="evids">{evs}</div>
    </div>
    <div class="proof">
      <div class="case"><div class="k"><span class="live"></span>{escape(t["case_k"])}</div><p>{t["case"]}</p></div>
      <div class="limits"><div class="k">{svg(UI["warn"])}{escape(t["why_k"])}</div><p>{escape(t["why"])}</p></div>
    </div>
    <p class="fonti"><b>{escape(t["fonti_k"])}</b> {" · ".join(escape(f) for f in t["fonti"])}</p>
  </div>
  {tblock(t, 2)}
</section>"""


# ======================================================================= pagina 3 — mappa
def p3(t):
    items = "".join(
        f'<li><i>{i:02d}</i><div><h4>{escape(h)} <span class="fit {f}">{t["fit"][f]}</span></h4>'
        f'<p>{escape(d)}</p></div></li>' for i, (h, d, f) in enumerate(t["map"], 1))
    off = "".join(f"<span>{escape(o)}</span>" for o in t["off"])
    return f"""
<section class="page cover map">
  <div class="topbar"></div>
  {head(t["sheet"] + " · " + DOC, t["p3_head"])}
  <div class="hero map-hero">
    <div class="eyebrow"><i></i>{escape(t["eyebrow3"])}</div>
    <h2>{escape(t["h2_map"])}<em>.</em></h2>
  </div>
  <div class="tavola">
    <div class="frame plant">
      {frame("02", t["fig2"], art.plant_svg())}
    </div>
    <div class="legend"><span>{escape(t["legend3"])}</span>
      <div class="keys"><div class="key"><i></i><span>{t["key3"]}</span></div></div></div>
  </div>
  <ol class="maplist">{items}</ol>
  <div class="offfield"><b>{escape(t["off_k"])}</b>{off}</div>
  {tblock(t, 3)}
</section>"""


# ======================================================================= pagina 4 — porte 1 e 2
def door_head(n, small, title):
    return f'<div class="door-h"><span class="dn">{n}</span><div><small>{escape(small)}</small><h2>{escape(title)}</h2></div></div>'


def p4(t):
    flow = "".join(f'<div class="step"><div class="ic">{svg(art.FLOW_ICONS[k])}</div><h4>{escape(h)}</h4><p>{escape(d)}</p></div>'
                   for k, h, d in t["steps"])
    a, b, c = t["cmp_head"]
    rows = "".join(f'<tr><td>{escape(r[0])}</td><td>{escape(r[1])}</td><td>{escape(r[2])}</td><td class="us">{escape(r[3])}</td></tr>'
                   for r in t["cmp"])
    return f"""
<section class="page inner">
  <div class="topbar"></div>
  {head(t["sheet"] + " · " + DOC, t["p4_head"])}
  <div class="body">
    <div class="door">
      {door_head("01", t["d1_small"], t["d1_h"])}
      <p class="door-lead">{escape(t["d1_lead"])}</p>
      <div class="flow">{flow}</div>
    </div>
    <div class="door">
      {door_head("02", t["d2_small"], t["d2_h"])}
      <div class="door-grid">
        <div class="dark-card">
          <div class="dc-k">Fig. 03 — {escape(t["fig3"])}</div>
          {art.hole_section_svg()}
          <p class="dc-cap">{escape(t["fig3_cap"])}</p>
        </div>
        <div class="dark-card">
          <div class="dc-k">Fig. 04 — {escape(t["fig4"])}</div>
          {art.open_area_svg()}
          <p class="dc-cap">{escape(t["fig4_cap"])}</p>
        </div>
      </div>
      <table class="cmp">
        <thead><tr><th></th><th>{escape(a)}</th><th>{escape(b)}</th><th class="us">{escape(c)}</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
      <ul class="ticks">{ticks(t["ticks4"])}</ul>
    </div>
  </div>
  {tblock(t, 4)}
</section>"""


# ======================================================================= pagina 5 — porta 3 + idee
def p5(t):
    cards = "".join(f'<div class="idea"><small>{escape(s)}</small><h4>{escape(h)}</h4><p>{escape(d)}</p>'
                    f'<span class="lim">{t["lim"]} · {escape(l)}</span></div>' for h, s, d, l in t["ideas"])
    return f"""
<section class="page inner">
  <div class="topbar"></div>
  {head(t["sheet"] + " · " + DOC, t["p5_head"])}
  <div class="body">
    <div class="door">
      {door_head("03", t["d3_small"], t["d3_h"])}
      <div class="nozzle">
        <div class="nz-img"><img src="../assets/crepina.jpg" alt="">
          <span class="nz-cap">Fig. 05 — {escape(t["fig5"])}</span></div>
        <div class="nz-txt">
          <p>{escape(t["nz_p"])}</p>
          <ul class="ticks">{ticks(t["ticks5"])}</ul>
        </div>
      </div>
    </div>
    <div class="sec">
      {sec("04", t["s04"], t["s04_note"])}
      <div class="ideas">{cards}</div>
    </div>
  </div>
  {tblock(t, 5)}
</section>"""


# ======================================================================= pagina 6 — materiale e limiti
def p6(t):
    chem = "".join(f'<tr><td><span class="dot {c}"></span>{escape(a)}</td><td>{escape(b)}</td></tr>' for a, b, c in t["chem"])
    prow = "".join(f"<tr><td>{escape(a)}</td><td>{escape(b)}</td></tr>" for a, b in t["props"])
    rov = "".join(f"<li><b>{escape(a)}</b>{escape(b)}</li>" for a, b in t["rov"])
    needs = "".join(f"<li>{escape(n)}</li>" for n in t["needs"])
    ok, cond, no, tail = t["chem_key"]
    mh = t["mat_head"]
    mats = "".join(f'<tr><td class="m">{escape(m)}</td><td><span class="badge {p}">{p}</span></td><td>{escape(w)}</td>'
                   f'<td class="ref">{r}</td></tr>' for m, p, w, r in t["mat"])
    c1, c2 = t["cta"]
    return f"""
<section class="page inner">
  <div class="topbar"></div>
  {head(t["sheet"] + " · " + DOC, t["p6_head"])}
  <div class="body">
    <div class="sec">
      {sec("05", t["s05"], t["s05_note"])}
      <div class="mat-grid">
        <div>
          <table class="kv">{prow}</table>
          <p class="note">{escape(t["props_note"])}</p>
        </div>
        <div>
          <table class="chem">{chem}</table>
          <p class="note"><span class="dot ok"></span>{ok} <span class="dot cond"></span>{cond} <span class="dot no"></span>{no} · {escape(tail)}</p>
        </div>
      </div>
    </div>
    <div class="sec">
      {sec("06", t["s06"])}
      <table class="mat">
        <thead><tr><th style="width:24%">{mh[0]}</th><th style="width:12%">{mh[1]}</th><th>{mh[2]}</th><th style="width:20%">{mh[3]}</th></tr></thead>
        <tbody>{mats}</tbody>
      </table>
    </div>
    <div class="sec">
      {sec("07", t["s07"], t["s07_note"])}
      <ul class="rov">{rov}</ul>
    </div>
    <div class="needs-row"><b>{escape(t["needs_k"])}</b><ol>{needs}</ol></div>
  </div>
  <div class="cta">
    <div><h2>{escape(c1)}<br><span>{escape(c2)}</span></h2></div>
    <ul>{contact_list()}</ul>
  </div>
  {tblock(t, 6)}
</section>"""


def build(lang):
    t = LANGS[lang]
    art.LBL.clear()
    art.LBL.update(ART_IT)
    art.LBL.update(t["art"])
    pages = "".join(f(t) for f in (p1, p2, p3, p4, p5, p6))
    html = page_shell(f"Due Pi Greco — {DOC} ({t['code']})", pages)
    html = html.replace('<html lang="it">', f'<html lang="{t["html_lang"]}">')
    html = html.replace('<link rel="stylesheet" href="../assets/scheda.css">',
                        '<link rel="stylesheet" href="../assets/scheda.css">\n<link rel="stylesheet" href="../assets/h2o.css">')
    out = ROOT / "html" / f"{t['file']}.html"
    out.write_text(html)
    print("scritto", out)


if __name__ == "__main__":
    for lang in (sys.argv[1:] or list(LANGS)):
        build(lang)
