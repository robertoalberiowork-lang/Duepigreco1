"""Genera le schede in HTML (html/) pronte per la stampa in PDF (pdf/).

Uso:
    python3 build.py            # scrive html/*.html
    node tools/print_pdf.js     # stampa pdf/*.pdf (Playwright + Chromium)
"""
import json
import math
from html import escape
from pathlib import Path

from content import CONTATTI, IN_PRODUZIONE, KIT, SCHEDE

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "html"
LABELS = json.loads((ROOT / "assets" / "tavole_labels.json").read_text())

LOGO = ('<svg viewBox="0 0 30 30" aria-hidden="true"><rect x=".75" y=".75" width="28.5" height="28.5" '
        'fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M6 6.75h18V22.5h-3.75V10.5h-10.5V22.5H6z" '
        'fill="#e63329"/></svg>')

ICONS = {
    "mono": '<path d="M12 3 20 7.5v9L12 21l-8-4.5v-9z"/><path d="M4 7.5 12 12l8-4.5M12 12v9"/>',
    "food": '<path d="M12 3 19 6v5.5c0 4.2-2.9 7.9-7 9.5-4.1-1.6-7-5.3-7-9.5V6z"/><path d="m8.8 12 2.2 2.2 4.4-4.4"/>',
    "series": '<rect x="3" y="4" width="18" height="4.5" rx="1"/><rect x="3" y="10" width="18" height="4.5" rx="1"/><rect x="3" y="16" width="18" height="4.5" rx="1"/>',
    "spare": '<path d="M20 12a8 8 0 1 1-2.34-5.66"/><path d="M20 4v4.5h-4.5"/><path d="M9.5 12h5M12 9.5v5"/>',
    "channels": '<path d="M3 7h6c3 0 3 10 6 10h6"/><path d="M3 17h6c3 0 3-10 6-10h6"/><circle cx="3" cy="7" r=".6"/><circle cx="3" cy="17" r=".6"/>',
    "size": '<path d="M3 16 16 3l5 5L8 21z"/><path d="m7 12 2 2M10 9l2 2M13 6l2 2M5.5 13.5l1 1"/>',
    "file": '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h4"/>',
    "weight": '<path d="M20.2 3.8C13 3 5.5 8 4 20c4.5-8.5 9-12 13.5-13.5"/><path d="M4 20c10 .5 15-6 16.2-16.2"/>',
}
LINKS = {"web": "https://duepigreco3d.it", "mail": "mailto:info@duepigreco3d.it",
         "tel": "tel:+390423715172", "sede": None}


def contact_list():
    out = []
    for k, v in CONTATTI.items():
        txt = escape(v) if not LINKS[k] else f'<a href="{LINKS[k]}">{escape(v)}</a>'
        out.append(f"<li>{svg(UI[k])}{txt}</li>")
    return "".join(out)


UI = {
    "web": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.8 2.6 2.8 15.4 0 18M12 3c-2.8 2.6-2.8 15.4 0 18"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3.5 6.5 8.5 6.5 8.5-6.5"/>',
    "tel": '<path d="M5 3h4l2 5-2.5 1.5a11 11 0 0 0 6 6L16 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 5a2 2 0 0 1 2-2"/>',
    "sede": '<path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "warn": '<path d="M12 3 2 20h20z"/><path d="M12 10v4.5M12 17.5v.01"/>',
}


def svg(paths, cls=""):
    return f'<svg viewBox="0 0 24 24" class="{cls}" aria-hidden="true">{paths}</svg>'


def head(meta_top, meta_bottom, dark):
    return f"""
  <header class="head">
    <div class="logo">{LOGO}<div><b>DUE PI<br>GRECO</b><small>Additive manufacturing</small></div></div>
    <div class="meta"><span>{meta_top}</span><br><b>{escape(meta_bottom)}</b></div>
  </header>"""


def tblock(doc, rev, page, total, extra=None):
    extra = extra or ("Editore", "Due Pi Greco S.r.l.")
    return f"""
  <dl class="tblock">
    <div><dt>Documento</dt><dd>{doc}</dd></div>
    <div><dt>Revisione</dt><dd>{rev}</dd></div>
    <div><dt>Lingua</dt><dd>IT</dd></div>
    <div><dt>{extra[0]}</dt><dd>{extra[1]}</dd></div>
    <div><dt>Pagina</dt><dd><b>{page:02d}</b> / {total:02d}</dd></div>
  </dl>"""


def page_shell(title, pages):
    return f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<link rel="stylesheet" href="../assets/fonts.css">
<link rel="stylesheet" href="../assets/scheda.css">
</head>
<body>
{pages}
</body>
</html>
"""


def headline(lines):
    return "<br>".join(escape(l) for l in lines[:-1]) + "<br>" + escape(lines[-1]) + "<em>.</em>"


def kpis(items):
    out = []
    for val, unit, cap in items:
        u = f"<small>{escape(unit)}</small>" if unit else ""
        out.append(f'<div class="kpi"><b>{escape(val)}{u}</b><span>{escape(cap)}</span></div>')
    return '<div class="kpis">' + "".join(out) + "</div>"


def callouts(labels):
    # numerazione in senso orario: alto-sx, alto-dx, basso-sx, basso-dx
    order = sorted(labels, key=lambda l: (l["y"] > 50, l["x"]))
    out = []
    for i, l in enumerate(order, 1):
        out.append(f'<div class="callout" style="left:{l["x"]}%;top:{l["y"]}%"><i>{i:02d}</i>'
                   f'<span>{escape(l["text"])}</span></div>')
    return "".join(out)


def tavola(art, caption, ref, keys=True, fig="Fig. 01", view="Vista isometrica"):
    legend_keys = ('<div class="keys"><div class="key"><i></i><span><b>In rosso</b>: le parti che si producono '
                   'in additive</span></div></div>') if keys else ""
    return f"""
  <div class="tavola">
    <div class="frame">
      <span class="corner tl"></span><span class="corner tr"></span><span class="corner bl"></span><span class="corner br"></span>
      <div class="fig"><b>{fig}</b> — {view}</div>
      <div class="scale">Tav. {ref}</div>
      {art}
    </div>
    <div class="legend"><span>{escape(caption)}</span>{legend_keys}</div>
  </div>"""


def cover(s):
    art = (f'<div class="art"><img src="../assets/tavola_{s["code"]}.svg" alt="">'
           f'{callouts(LABELS[s["code"]])}</div>')
    return f"""
<section class="page cover">
  <div class="topbar"></div>
  {head("Scheda applicazione", s["doc"], True)}
  <div class="hero">
    <div class="eyebrow"><i></i>{escape(s["settore"])}</div>
    <h1{' style="--h1:33pt"' if max(map(len, s["titolo"])) > 27 else ''}>{headline(s["titolo"])}</h1>
    <p class="lead">{escape(s["lead"])}</p>
  </div>
  {kpis(s["kpi"])}
  {tavola(art, s["tavola"], s["doc"])}
  {tblock(s["doc"], s["rev"], 1, 2)}
</section>"""


def inner(s):
    bens = []
    for i, (ic, title, text, tags) in enumerate(s["vantaggi"], 1):
        chips = "".join(f'<span class="chip">{escape(t)}</span>' for t in tags)
        bens.append(f"""
        <div class="ben"><span class="n">{i:02d}</span><div class="top"><div class="ic">{svg(ICONS[ic])}</div>
          <h3>{escape(title)}</h3></div><p>{escape(text)}</p><div class="tags">{chips}</div></div>""")
    rows = []
    for mat, proc, why, pre, ref in s["materiali"]:
        pre_html = f"<small>{pre}</small>" if pre else ""
        rows.append(f'<tr><td class="m">{escape(mat)}</td><td><span class="badge {proc}">{proc}</span></td>'
                    f'<td>{escape(why)}</td><td class="ref">{pre_html}{escape(ref)}</td></tr>')
    contacts = contact_list()
    return f"""
<section class="page inner">
  <div class="topbar"></div>
  {head("Scheda applicazione · " + s["doc"], s["settore"], False)}
  <div class="body">
    <div class="sec">
      <div class="sec-h"><b>01</b><span>Il conto che conoscete</span></div>
      <div class="compare">
        <div class="col was"><div class="k"><i></i>Come si fa oggi</div>{escape(s["oggi"])}</div>
        <div class="arrow">{svg('<path d="M5 12h14M13 6l6 6-6 6" stroke="#e63329" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')}</div>
        <div class="col now"><div class="k"><i></i>In sinterizzazione</div>{escape(s["additive"])}</div>
      </div>
    </div>
    <div class="sec">
      <div class="sec-h"><b>02</b><span>Cosa cambia in additive</span></div>
      <div class="benefits">{"".join(bens)}
      </div>
    </div>
    <div class="sec">
      <div class="sec-h"><b>03</b><span>Materiali per il settore</span><em>Riferimenti: schede DPG-MAT e matrice DPG-CAT</em></div>
      <div>
        <table class="mat">
          <thead><tr><th style="width:30%">Materiale</th><th style="width:13%">Processo</th><th>Perché qui</th><th style="width:22%">Riferimento</th></tr></thead>
          <tbody>{"".join(rows)}</tbody>
        </table>
      </div>
    </div>
    <div class="proof">
      <div class="case"><div class="k"><span class="live"></span>In produzione, oggi</div><p>{IN_PRODUZIONE}</p></div>
      <div class="limits"><div class="k">{svg(UI["warn"])}Il rovescio — quando non conviene</div><p>{escape(s["rovescio"])}</p></div>
    </div>
  </div>
  <div class="cta">
    <div>
      <h2>{escape(s["cta"])}<br><span>Vi diciamo anche quando non conviene.</span></h2>
    </div>
    <ul>{contacts}</ul>
  </div>
  {tblock(s["doc"], s["rev"], 2, 2)}
</section>"""


# ---------------------------------------------------------------- kit campioni
C30, S30 = math.cos(math.radians(30)), 0.5


def iso(x, y, z=0.0):
    return ((x - y) * C30, (x + y) * S30 - z)


def poly(pts, **attrs):
    d = " ".join(f"{a:.2f},{b:.2f}" for a, b in (iso(*p) for p in pts))
    a = " ".join(f'{k.replace("_", "-")}="{v}"' for k, v in attrs.items())
    return f'<polygon points="{d}" {a}/>'


def box(x0, y0, z0, x1, y1, z1, stroke, fill="#0b0b0c", sw=0.55, filt=""):
    f = f' filter="url(#{filt})"' if filt else ""
    top = poly([(x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)], fill=fill, stroke=stroke, stroke_width=sw, stroke_linejoin="round")
    fx = poly([(x1, y0, z0), (x1, y1, z0), (x1, y1, z1), (x1, y0, z1)], fill=fill, stroke=stroke, stroke_width=sw, stroke_linejoin="round")
    fy = poly([(x0, y1, z0), (x1, y1, z0), (x1, y1, z1), (x0, y1, z1)], fill=fill, stroke=stroke, stroke_width=sw, stroke_linejoin="round")
    return f"<g{f}>{fx}{fy}{top}</g>"


def ell(x, y, z, r, **attrs):
    cx, cy = iso(x, y, z)
    a = " ".join(f'{k.replace("_", "-")}="{v}"' for k, v in attrs.items())
    return f'<ellipse cx="{cx:.2f}" cy="{cy:.2f}" rx="{r*math.sqrt(2)*C30:.2f}" ry="{r*math.sqrt(2)*S30:.2f}" {a}/>'


def pin(x, y, z, r, h, stroke):
    rx = r * math.sqrt(2) * C30
    ry = r * math.sqrt(2) * S30
    bx, by = iso(x, y, z)
    tx, ty = iso(x, y, z + h)
    side = (f'<path d="M{bx-rx:.2f},{by:.2f} A{rx:.2f},{ry:.2f} 0 0 0 {bx+rx:.2f},{by:.2f} L{tx+rx:.2f},{ty:.2f} '
            f'L{tx-rx:.2f},{ty:.2f} Z" fill="#0b0b0c" stroke="{stroke}" stroke-width=".55" stroke-linejoin="round"/>')
    return side + ell(x, y, z + h, r, fill="#0b0b0c", stroke=stroke, stroke_width=".55")


def kit_art():
    R, W, G = "#e63329", "#faf9f7", "#1c1c1f"
    T = 4.0  # spessore piastrina
    parts = []
    # griglia a pavimento
    for i in range(-36, 181, 12):
        a, b = iso(i, -36, 0), iso(i, 108, 0)
        parts.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{G}" stroke-width=".45"/>')
    for j in range(-36, 109, 12):
        a, b = iso(-36, j, 0), iso(180, j, 0)
        parts.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{G}" stroke-width=".45"/>')
    # 04 linguetta a sbalzo (dietro la piastrina nell'ordine di disegno: esce dal fianco destro)
    parts.append(f'<g filter="url(#glow)">{box(110, 8, T - 1.5, 142, 22, T, R, sw=.55)}</g>')
    # piastrina
    parts.append(box(0, 0, 0, 110, 62, T, W, sw=0.7))
    # nome inciso nel pezzo
    ox, oy = iso(0, 0, T)
    m = f"matrix({C30:.4f},{S30:.4f},{-C30:.4f},{S30:.4f},{ox:.2f},{oy:.2f})"
    parts.append(f'<g transform="{m}"><text x="7" y="54" font-family="IBM Plex Mono" font-weight="600" font-size="11" '
                 f'letter-spacing="1.4" fill="#1d1d20" stroke="#8c8c90" stroke-width=".3">PA2200</text></g>')
    feats = []
    for k, r in enumerate([3.2, 2.6, 2.0, 1.5, 1.1, 0.75, 0.5]):   # 01 pettine di perni
        feats.append((12 + k * 8.6, 11, "pin", r))
    for k, r in enumerate([3.2, 2.6, 2.0, 1.5, 1.1, 0.75, 0.5]):   # 02 pettine di fori
        feats.append((12 + k * 8.6, 27, "hole", r))
    for k, t in enumerate([2.4, 1.8, 1.3, 0.9, 0.6, 0.4]):         # 03 scala di pareti
        feats.append((76 + k * 5.4, 30, "wall", t))
    out = []
    for x, y, kind, v in sorted(feats, key=lambda f: f[0] + f[1]):
        if kind == "pin":
            out.append(pin(x, y, T, v, 7, R))
        elif kind == "hole":
            out.append(ell(x, y, T, v, fill="#050506", stroke=R, stroke_width=".55"))
        else:
            out.append(box(x, y, T, x + v, y + 26, T + 8, R, sw=.5))
    parts.append(f'<g filter="url(#glow)">{"".join(out)}</g>')
    return parts


def kit_svg():
    parts = kit_art()
    x0, x1, y0, y1 = -78.0, 138.0, -21.0, 97.0
    vw, vh = x1 - x0, y1 - y0
    # (etichetta, punto sul pezzo, posizione etichetta in % della tavola)
    anchors = [
        ("Pettine di perni", iso(29.2, 11, 11), (5, 6)),
        ("Linguetta a sbalzo", iso(134, 15, 4), (63, 6)),
        ("Pettine di fori", iso(20.6, 27, 4), (5, 95)),
        ("Scala di pareti", iso(90, 43, 12), (63, 95)),
    ]
    leaders, labels = [], []
    for txt, (ax, ay), (px, py) in anchors:
        lx, ly = x0 + vw * px / 100, y0 + vh * py / 100
        ex, ey = lx + 24, ly + (3.4 if py < 50 else -3.4)
        leaders.append(f'<polyline points="{ex:.1f},{ey:.1f} {ax:.1f},{ay:.1f}" fill="none" stroke="#8c8c90" stroke-width=".35"/>'
                       f'<circle cx="{ax:.1f}" cy="{ay:.1f}" r="1" fill="#e63329"/>')
        labels.append({"text": txt, "x": px, "y": py})
    defs = ('<defs><filter id="glow" x="-20%" y="-20%" width="140%" height="140%">'
            '<feGaussianBlur in="SourceGraphic" stdDeviation="1.1" result="b"/>'
            '<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>')
    s = (f'<svg viewBox="{x0} {y0} {vw} {vh}" preserveAspectRatio="xMidYMid meet" style="position:absolute;inset:0;width:100%;height:100%">'
         f'{defs}{"".join(parts)}{"".join(leaders)}</svg>')
    return s, labels, vw / vh


def kit_page():
    art_svg, labels, ratio = kit_svg()
    art = f'<div class="art" style="aspect-ratio:{ratio:.4f}">{art_svg}{callouts(labels)}</div>'
    cards = "".join(f'<div><i>{i:02d}</i><h3>{escape(t)}</h3><p>{escape(d)}</p></div>'
                    for i, (t, d) in enumerate(KIT["piastrina"], 1))
    p1 = f"""
<section class="page cover kit">
  <div class="topbar"></div>
  {head("Kit campioni · 11 materiali", KIT["doc"], True)}
  <div class="hero">
    <div class="eyebrow"><i></i>Materiali da toccare con mano</div>
    <h1>Kit campioni<em>.</em></h1>
    <p class="lead">{escape(KIT["lead"])}</p>
  </div>
  {kpis([("11", "", "piastrine, una per materiale"), ("3", "", "processi: SLS, SAF, FDM"), ("4", "", "prove su ogni piastrina")])}
  {tavola(art, "Piastrina campione, tavola isometrica", KIT["doc"], keys=False, view="Cosa c'è sulla piastrina")}
  <div class="kit-cards">{cards}</div>
  <div class="howto"><div class="k">Come si legge</div><p>{escape(KIT["come_si_legge"])}</p></div>
  {tblock(KIT["doc"], KIT["rev"], 1, 2, ("Sede", "Ponzano Veneto / Resana (TV)"))}
</section>"""

    groups = {"SLS": "Sinterizzazione laser di polveri", "SAF": "Selective Absorption Fusion",
              "FDM": "Deposizione di filamento"}
    dmin, dmax = 0.8, 1.4
    rows = []
    last = None
    for proc, mat, dens, circa, uso, nota, decl, on in KIT["materiali"]:
        if proc != last:
            n = sum(1 for m in KIT["materiali"] if m[0] == proc)
            rows.append(f'<tr class="grp"><td colspan="5"><div><span class="badge {proc}">{proc}</span>'
                        f'<span class="gl">{groups[proc]}</span><b>{n} {"piastrina" if n == 1 else "piastrine"}</b></div></td></tr>')
            last = proc
        w = (dens - dmin) / (dmax - dmin) * 100
        d = f'{dens:.2f}'.replace(".", ",") + (' <em>ca.</em>' if circa else "")
        rows.append(f'<tr><td class="m">{escape(mat)}</td><td class="d">{d}<span class="bar"><i style="width:{w:.0f}%"></i></span></td>'
                    f'<td>{escape(uso)}</td><td>{escape(nota)}</td><td class="decl{" on" if on else ""}">{escape(decl)}</td></tr>')
    contacts = contact_list()
    p2 = f"""
<section class="page inner kit">
  <div class="topbar"></div>
  {head("Kit campioni · " + KIT["doc"], "I materiali", False)}
  <div class="body">
    <div style="margin-top:7mm">
      <table class="kit-t">
        <thead><tr><th style="width:17%">Materiale</th><th style="width:10%">g/cm³</th><th style="width:27%">Quando si usa</th><th style="width:23%">Da tenere presente</th><th>Dichiarazioni</th></tr></thead>
        <tbody>{"".join(rows)}</tbody>
      </table>
      <div class="kit-legend"><span><i class="dot"></i>Dichiarazione o certificazione disponibile</span><span>Barra: densità da 0,8 a 1,4 g/cm³</span></div>
    </div>
  </div>
  <div class="contact-strip">
    <b>Avete il 3D? <span>La fascia di prezzo esce in un minuto.</span></b>
    <ul>{contacts}</ul>
  </div>
  {tblock(KIT["doc"], KIT["rev"], 2, 2, ("Sede", "Ponzano Veneto / Resana (TV)"))}
</section>"""
    return page_shell("Due Pi Greco — Kit campioni", p1 + p2)


def main():
    OUT.mkdir(exist_ok=True)
    for s in SCHEDE:
        html = page_shell(f"Due Pi Greco — {s['doc']}", cover(s) + inner(s))
        (OUT / f"{s['file']}.html").write_text(html)
    (OUT / f"{KIT['file']}.html").write_text(kit_page())
    print("HTML scritti in", OUT)


if __name__ == "__main__":
    main()
