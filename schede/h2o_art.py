"""Disegni vettoriali della scheda DPG-SET-H2O: pannello filtrante, mappa dell'impianto,
sezione del foro, superficie aperta, flusso del ricambio."""
import math

R, W, G, INK = "#e63329", "#faf9f7", "#1c1c1f", "#0b0b0c"
H2O = "#5fb4d9"          # solo per l'acqua

# etichette dei disegni: h2o.py le sostituisce per ogni lingua
LBL = {
    "c_hole": "Foro da 2 mm a quinconce, anche conico", "c_module": "Modulo sostituibile da solo",
    "c_clip": "Clip di aggancio stampate nel pezzo", "c_frame": "Telaio e nervatura in un pezzo",
    "lift": "Sollevamento", "screen": "Grigliatura", "grit": "Dissabbiatura", "prim": "Sedimentazione I",
    "dose": "Dosaggio", "bio": "Biologico · MBBR", "sec": "Sedimentazione II", "filt": "Filtrazione",
    "dis": "Disinfezione", "dis_off": "UV / ozono: fuori campo", "odour": "Deodorizzazione",
    "thick": "Ispessimento", "dewat": "Disidratazione", "dig": "Digestione", "dig_off": "Atex: fuori campo",
    "sludge": "Linea fanghi",
    "h_straight": "FORO DRITTO, PUNZONATO", "h_conical": "FORO CONICO, STAMPATO",
    "h_stuck": "si incastra a metà spessore", "h_pass": "passa, o resta sopra e il lavaggio la stacca",
    "flow": "FLUSSO", "pitch": "passo", "web": "setto", "plate": "LAMIERA FORATA TIPICA 30–45%", "dec": ",",
}
GREY = "#8c8c90"
C30, S30 = math.cos(math.radians(30)), 0.5

GLOW = ('<filter id="{id}" x="-20%" y="-20%" width="140%" height="140%">'
        '<feGaussianBlur in="SourceGraphic" stdDeviation="{s}" result="b"/>'
        '<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')


def iso(x, y, z=0.0):
    return ((x - y) * C30, (x + y) * S30 - z)


def pts(seq):
    return " ".join(f"{a:.2f},{b:.2f}" for a, b in (iso(*p) for p in seq))


# ------------------------------------------------------------------ copertina: pannelli
def panel(ox, oy, w=96, d=64, t=5, pitch=6.2, r=1.9):
    """Pannello forato con telaio, in pianta isometrica. Restituisce (svg, punti utili)."""
    out = []
    x0, y0, x1, y1 = ox, oy, ox + w, oy + d
    side = lambda a: f'<polygon points="{pts(a)}" fill="#120b0b" stroke="{R}" stroke-width=".7" stroke-linejoin="round"/>'
    out.append(side([(x1, y0, 0), (x1, y1, 0), (x1, y1, t), (x1, y0, t)]))
    out.append(side([(x0, y1, 0), (x1, y1, 0), (x1, y1, t), (x0, y1, t)]))
    out.append(f'<polygon points="{pts([(x0, y0, t), (x1, y0, t), (x1, y1, t), (x0, y1, t)])}" fill="#170c0c" stroke="{R}" stroke-width=".8" stroke-linejoin="round"/>')
    # cornice interna del telaio
    m = 5
    out.append(f'<polygon points="{pts([(x0+m, y0+m, t), (x1-m, y0+m, t), (x1-m, y1-m, t), (x0+m, y1-m, t)])}" fill="none" stroke="{R}" stroke-width=".45" opacity=".8"/>')
    # nervatura centrale
    out.append(f'<polyline points="{pts([(x0+w/2, y0+m, t), (x0+w/2, y1-m, t)])}" fill="none" stroke="{R}" stroke-width=".45" opacity=".8"/>')
    # fori a quinconce
    rx, ry = r * math.sqrt(2) * C30, r * math.sqrt(2) * S30
    row = 0
    yy = y0 + m + pitch * .7
    while yy < y1 - m - 1.5:
        xx = x0 + m + pitch * (.6 if row % 2 == 0 else 1.1)
        while xx < x1 - m - 1.5:
            if abs(xx - (x0 + w / 2)) > 2.6:
                cx, cy = iso(xx, yy, t)
                out.append(f'<ellipse cx="{cx:.2f}" cy="{cy:.2f}" rx="{rx:.2f}" ry="{ry:.2f}" fill="#050506" stroke="{R}" stroke-width=".38"/>')
            xx += pitch
        yy += pitch * .866
        row += 1
    # clip di aggancio sul lato corto
    for cy_ in (y0 + d * .28, y0 + d * .72):
        a, b = cy_ - 4, cy_ + 4
        out.append(f'<polygon points="{pts([(x1, a, t), (x1+5, a, t), (x1+5, b, t), (x1, b, t)])}" fill="#170c0c" stroke="{R}" stroke-width=".6"/>')
        out.append(f'<polygon points="{pts([(x1+5, a, 0), (x1+5, b, 0), (x1+5, b, t), (x1+5, a, t)])}" fill="#120b0b" stroke="{R}" stroke-width=".6"/>')
    # codice inciso sul telaio
    tx, ty = iso(x0 + 7, y1 - 1.6, t)
    out.append(f'<text transform="translate({tx:.2f},{ty:.2f}) matrix({C30:.4f},{S30:.4f},{-C30:.4f},{S30:.4f},0,0)" '
               f'font-family="IBM Plex Mono" font-size="3" letter-spacing=".5" fill="#6a2a26">DPG · PP · R02</text>')
    return "".join(out)


def cover_art():
    parts = []
    # griglia a pavimento
    for i in range(-40, 361, 16):
        a, b = iso(i, -40, -30), iso(i, 150, -30)
        parts.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{G}" stroke-width=".5"/>')
    for j in range(-40, 151, 16):
        a, b = iso(-40, j, -30), iso(360, j, -30)
        parts.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{G}" stroke-width=".5"/>')
    # acqua che attraversa i pannelli: filetti sotto
    for k in range(9):
        x = 10 + k * 34
        for y in (14, 38):
            a, b = iso(x, y, -2), iso(x, y, -26)
            parts.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{H2O}" stroke-width=".6" stroke-dasharray="1.6 2.2" opacity=".75"/>')
    # telaio inox del nastro (contesto, in bianco)
    for y in (-6, 70):
        a, b = iso(-14, y, 2.5), iso(328, y, 2.5)
        parts.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{W}" stroke-width=".7"/>')
    for x in (-14, 328):
        a, b = iso(x, -6, 2.5), iso(x, 70, 2.5)
        parts.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{W}" stroke-width=".7"/>')
    # tre moduli, il terzo sollevato (in sostituzione)
    parts.append(f'<g filter="url(#glowC)">{panel(0, 0)}{panel(106, 0)}</g>')
    parts.append(f'<g transform="translate(0,-26)" filter="url(#glowC)">{panel(212, 0)}</g>')
    # frecce di sostituzione
    a, b = iso(260, 32, 6), iso(260, 32, 26)
    parts.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]+4:.1f}" stroke="{W}" stroke-width=".5" stroke-dasharray="2 2"/>')
    # acqua in arrivo sopra
    for k in range(5):
        x = 30 + k * 60
        a = iso(x, 32, 44)
        parts.append(f'<path d="M{a[0]:.1f},{a[1]:.1f} q3,6 0,12 q-3,6 0,12" fill="none" stroke="{H2O}" stroke-width=".7" opacity=".7"/>'
                     f'<path d="M{a[0]-2:.1f},{a[1]+21:.1f} l2,4 l2,-4" fill="none" stroke="{H2O}" stroke-width=".7" opacity=".7"/>')
    anchors = {
        "foro": iso(40, 30, 5), "telaio": iso(106 + 96, 20, 5),
        "clip": iso(96 + 3, 18, 5), "modulo": (iso(260, 20, 5)[0], iso(260, 20, 5)[1] - 26),
    }
    return parts, anchors


def cover_svg():
    parts, anc = cover_art()
    x0, x1, y0, y1 = -96.0, 318.0, -56.0, 200.0
    vw, vh = x1 - x0, y1 - y0
    spec = [(LBL["c_hole"], anc["foro"], (4, 7)),
            (LBL["c_module"], anc["modulo"], (60, 7)),
            (LBL["c_clip"], anc["clip"], (4, 94)),
            (LBL["c_frame"], anc["telaio"], (60, 94))]
    leaders, labels = [], []
    for txt, (ax, ay), (px, py) in spec:
        lx, ly = x0 + vw * px / 100, y0 + vh * py / 100
        ex, ey = lx + 30, ly + (4 if py < 50 else -4)
        leaders.append(f'<polyline points="{ex:.1f},{ey:.1f} {ax:.1f},{ay:.1f}" fill="none" stroke="{GREY}" stroke-width=".4"/>'
                       f'<circle cx="{ax:.1f}" cy="{ay:.1f}" r="1.2" fill="{R}"/>')
        labels.append({"text": txt, "x": px, "y": py})
    s = (f'<svg viewBox="{x0} {y0} {vw} {vh}" style="position:absolute;inset:0;width:100%;height:100%">'
         f'<defs>{GLOW.format(id="glowC", s=1.0)}</defs>{"".join(parts)}{"".join(leaders)}</svg>')
    return s, labels, vw / vh


# ------------------------------------------------------------------ mappa dell'impianto
def marker(n, x, y):
    return (f'<g><circle cx="{x}" cy="{y}" r="9" fill="{R}" filter="url(#glowM)"/>'
            f'<text x="{x}" y="{y+3.2}" text-anchor="middle" font-family="IBM Plex Mono" font-weight="600" font-size="9" fill="#fff">{n:02d}</text></g>')


def lbl(x, y, t, anchor="middle", col=GREY, size=7.2):
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="IBM Plex Mono" font-size="{size}" '
            f'letter-spacing=".9" fill="{col}" stroke="{INK}" stroke-width="4" paint-order="stroke">{t.upper()}</text>')


def plant_svg():
    s = []
    L = f'stroke="{W}" stroke-width="1.1" fill="none" stroke-linejoin="round"'
    Lf = f'stroke="{W}" stroke-width="1.1" fill="{INK}" stroke-linejoin="round"'
    wl = 196  # quota del pelo libero
    # linea acqua
    s.append(f'<path d="M8 {wl+34} H990" stroke="{H2O}" stroke-width="2.2" opacity=".55"/>')
    for x in (100, 212, 318, 452, 628, 744, 858, 968):
        s.append(f'<path d="M{x-5} {wl+30} l6 4 l-6 4" stroke="{H2O}" stroke-width="1.4" fill="none"/>')
    # 1 sollevamento
    s.append(f'<path d="M20 {wl-10} V{wl+60} H86 V{wl-10}" {L}/>')
    s.append(f'<rect x="40" y="{wl+30}" width="20" height="22" {Lf}/><path d="M50 {wl+30} V{wl-30} H96" {L}/>')
    s.append(lbl(53, wl+86, LBL["lift"]))
    # 2 grigliatura
    s.append(f'<path d="M110 {wl+10} V{wl+54} H200 V{wl+10}" {L}/>')
    s.append(f'<path d="M126 {wl+54} L176 {wl-40}" stroke="{R}" stroke-width="2.4" filter="url(#glowM)"/>')
    s.append(f'<path d="M134 {wl+54} L184 {wl-40}" stroke="{R}" stroke-width="1" opacity=".7"/>')
    for i in range(6):
        y = wl + 44 - i * 15
        x = 131 + i * 8
        s.append(f'<path d="M{x-3} {y} h9" stroke="{R}" stroke-width="1"/>')
    s.append(f'<rect x="170" y="{wl-62}" width="36" height="22" {Lf}/>')
    s.append(lbl(155, wl+86, LBL["screen"]))
    s.append(marker(1, 196, wl-4))
    # 3 dissabbiatura
    s.append(f'<path d="M222 {wl+10} V{wl+48} L240 {wl+66} H282 L300 {wl+48} V{wl+10}" {L}/>')
    s.append(f'<path d="M232 {wl+22} H290" stroke="{W}" stroke-width=".6" stroke-dasharray="3 3"/>')
    s.append(lbl(261, wl+86, LBL["grit"]))
    # 4 primaria
    s.append(f'<path d="M324 {wl+10} V{wl+40} L372 {wl+70} L420 {wl+40} V{wl+10}" {L}/>')
    s.append(f'<path d="M318 {wl+4} H426" stroke="{W}" stroke-width="1.6"/>')
    s.append(f'<path d="M372 {wl+4} V{wl+40} M346 {wl+30} H398" stroke="{W}" stroke-width=".9"/>')
    s.append(f'<rect x="342" y="{wl+26}" width="8" height="6" fill="{R}" filter="url(#glowM)"/><rect x="394" y="{wl+26}" width="8" height="6" fill="{R}" filter="url(#glowM)"/>')
    s.append(lbl(372, wl+86, LBL["prim"]))
    s.append(marker(2, 420, wl-14))
    # dosaggio
    s.append(f'<rect x="424" y="{wl-86}" width="26" height="34" {Lf}/><path d="M437 {wl-52} V{wl+22}" stroke="{W}" stroke-width=".9" stroke-dasharray="2 2"/>')
    s.append(f'<rect x="431" y="{wl+16}" width="12" height="18" fill="{INK}" stroke="{R}" stroke-width="1.4" filter="url(#glowM)"/>')
    s.append(lbl(437, wl-94, LBL["dose"]))
    s.append(marker(3, 458, wl-60))
    # 5 biologico
    s.append(f'<path d="M466 {wl+2} V{wl+66} H612 V{wl+2}" {L}/>')
    for i in range(7):
        x = 480 + i * 19
        s.append(f'<rect x="{x}" y="{wl+60}" width="11" height="3" fill="{R}" filter="url(#glowM)"/>')
        for j in range(3):
            s.append(f'<circle cx="{x+5+(j%2)*3}" cy="{wl+50-j*12}" r="{1.4+j*.4}" fill="none" stroke="{H2O}" stroke-width=".7"/>')
    s.append(f'<rect x="600" y="{wl+14}" width="8" height="40" fill="none" stroke="{R}" stroke-width="1.6" filter="url(#glowM)"/>')
    s.append(f'<path d="M540 {wl-26} V{wl+24}" stroke="{W}" stroke-width=".8"/><rect x="535" y="{wl+24}" width="10" height="14" fill="{INK}" stroke="{R}" stroke-width="1.4" filter="url(#glowM)"/>')
    s.append(lbl(539, wl+86, LBL["bio"]))
    s.append(marker(4, 458, wl+62))
    s.append(marker(5, 622, wl+8))
    s.append(marker(6, 540, wl-40))
    # 6 secondaria
    s.append(f'<path d="M632 {wl+10} V{wl+40} L680 {wl+70} L728 {wl+40} V{wl+10}" {L}/>')
    s.append(f'<path d="M626 {wl+4} H734" stroke="{W}" stroke-width="1.6"/><path d="M680 {wl+4} V{wl+46}" stroke="{W}" stroke-width=".9"/>')
    s.append(lbl(680, wl+86, LBL["sec"]))
    # 7 terziario
    s.append(f'<path d="M750 {wl-2} V{wl+66} H838 V{wl-2}" {L}/>')
    s.append(f'<path d="M750 {wl+46} H838" stroke="{W}" stroke-width=".9"/>')
    s.append(f'<path d="M756 {wl+8} H832 V{wl+44} H756 Z" fill="{W}" opacity=".06"/>')
    for i in range(7):
        x = 760 + i * 11
        s.append(f'<path d="M{x} {wl+46} v-6 h5 v6" fill="{INK}" stroke="{R}" stroke-width="1.2" filter="url(#glowM)"/>')
    s.append(lbl(794, wl+86, LBL["filt"]))
    s.append(marker(7, 840, wl-16))
    # 8 disinfezione
    s.append(f'<path d="M858 {wl+10} V{wl+54} H940 V{wl+10}" {L}/>')
    for i in range(4):
        s.append(f'<rect x="{868+i*18}" y="{wl+18}" width="6" height="30" rx="3" fill="none" stroke="{GREY}" stroke-width=".9"/>')
    s.append(lbl(899, wl+86, LBL["dis"]))
    s.append(lbl(899, wl+100, LBL["dis_off"], col="#5c5c61", size=6.2))
    # uscita
    s.append(f'<path d="M950 {wl+44} q14 -8 28 0 q14 8 28 0" stroke="{H2O}" stroke-width="1.4" fill="none"/>')
    # deodorizzazione (aria dalla grigliatura)
    s.append(f'<path d="M206 {wl-52} H300 V{wl-150} H330" stroke="{GREY}" stroke-width=".9" stroke-dasharray="1 3" fill="none"/>')
    s.append(f'<path d="M330 {wl-176} V{wl-100} H370 V{wl-176} Z" {Lf}/>')
    s.append(f'<path d="M336 {wl-160} H364" stroke="{R}" stroke-width="2" filter="url(#glowM)"/>')
    for i in range(5):
        s.append(f'<path d="M{338+i*6} {wl-156} v4" stroke="{H2O}" stroke-width=".8"/>')
    s.append(f'<path d="M336 {wl-136} H364 M336 {wl-128} H364 M336 {wl-120} H364" stroke="{W}" stroke-width=".5"/>')
    s.append(f'<path d="M350 {wl-176} V{wl-192}" {L}/>')
    s.append(lbl(350, wl-200, LBL["odour"]))
    s.append(marker(8, 384, wl-164))
    # linea fanghi
    fy = wl + 150
    s.append(f'<path d="M372 {wl+70} V{fy} H890" stroke="#b08a5a" stroke-width="1.6" stroke-dasharray="5 3" fill="none" opacity=".8"/>')
    s.append(f'<path d="M680 {wl+70} V{fy}" stroke="#b08a5a" stroke-width="1.6" stroke-dasharray="5 3" fill="none" opacity=".8"/>')
    s.append(f'<path d="M470 {fy-34} V{fy+26} L500 {fy+44} L530 {fy+26} V{fy-34}" {Lf}/>')
    s.append(lbl(500, fy+64, LBL["thick"]))
    s.append(f'<rect x="596" y="{fy-22}" width="96" height="36" rx="18" {Lf}/>')
    for i in range(4):
        s.append(f'<circle cx="{614+i*20}" cy="{fy-4}" r="7" fill="none" stroke="{W}" stroke-width=".8"/>')
    s.append(f'<path d="M604 {fy-30} H684" stroke="{R}" stroke-width="2" filter="url(#glowM)"/>')
    s.append(lbl(644, fy+36, LBL["dewat"]))
    s.append(marker(9, 706, fy-34))
    s.append(f'<path d="M790 {fy+30} V{fy-20} Q820 {fy-44} 850 {fy-20} V{fy+30} Z" {Lf}/>')
    s.append(lbl(820, fy+48, LBL["dig"]))
    s.append(lbl(820, fy+62, LBL["dig_off"], col="#5c5c61", size=6.2))
    s.append(lbl(440, fy-8, LBL["sludge"], col="#b08a5a", size=6.4, anchor="end"))
    # strumentazione ovunque: marker 10 nel canale di grigliatura
    s.append(f'<path d="M262 {wl-40} V{wl+26}" stroke="{W}" stroke-width=".8"/><rect x="257" y="{wl+26}" width="10" height="12" fill="{INK}" stroke="{R}" stroke-width="1.4" filter="url(#glowM)"/>')
    s.append(marker(10, 262, wl-52))
    defs = f'<defs>{GLOW.format(id="glowM", s=1.4)}</defs>'
    return f'<svg viewBox="0 0 1000 440" style="width:100%;height:auto;display:block">{defs}{"".join(s)}</svg>'


# ------------------------------------------------------------------ sezione del foro
def hole_section_svg():
    s = []
    def plate(x0, conical):
        out = [f'<text x="{x0+70}" y="14" text-anchor="middle" font-family="IBM Plex Mono" font-size="6.2" letter-spacing="1" fill="{GREY}">'
               f'{LBL["h_conical"] if conical else LBL["h_straight"]}</text>']
        top, bot = 58, 82
        holes = [(x0 + 30 + i * 40) for i in range(3)]
        prev = x0
        for hx in holes:
            a_top, a_bot = 6, (10 if conical else 6)
            out.append(f'<polygon points="{prev},{top} {hx-a_top},{top} {hx-a_bot},{bot} {prev},{bot}" fill="{"#2a1614" if conical else "#26262a"}" stroke="{R if conical else W}" stroke-width="1"/>')
            prev = hx + a_top
            nxt = hx + a_top
            out.append(f'<line x1="{hx+a_top}" y1="{top}" x2="{hx+a_bot}" y2="{bot}" stroke="{R if conical else W}" stroke-width="1"/>')
        out.append(f'<polygon points="{prev},{top} {x0+140},{top} {x0+140},{bot} {prev + (4 if conical else 0)},{bot}" fill="{"#2a1614" if conical else "#26262a"}" stroke="{R if conical else W}" stroke-width="1"/>')
        # particelle
        hx = holes[1]
        if conical:
            out.append(f'<circle cx="{hx}" cy="{bot+18}" r="5.4" fill="none" stroke="{H2O}" stroke-width="1.2"/>')
            out.append(f'<path d="M{hx} {top-30} V{bot+8}" stroke="{H2O}" stroke-width=".8" stroke-dasharray="2 2"/>')
            out.append(f'<text x="{x0+70}" y="{bot+42}" text-anchor="middle" font-family="IBM Plex Mono" font-size="5.6" fill="{W}">{LBL["h_pass"]}</text>')
        else:
            out.append(f'<circle cx="{hx}" cy="{top+8}" r="5.4" fill="none" stroke="{R}" stroke-width="1.2"/>')
            out.append(f'<text x="{x0+70}" y="{bot+42}" text-anchor="middle" font-family="IBM Plex Mono" font-size="5.6" fill="{W}">{LBL["h_stuck"]}</text>')
        out.append(f'<path d="M{x0+4} {top-22} V{top-6}" stroke="{H2O}" stroke-width="1"/><path d="M{x0+1} {top-10} l3 4 l3 -4" stroke="{H2O}" fill="none"/>')
        out.append(f'<text x="{x0+10}" y="{top-14}" font-family="IBM Plex Mono" font-size="5.8" fill="{GREY}">{LBL["flow"]}</text>')
        return "".join(out)
    s.append(plate(4, False))
    s.append(plate(172, True))
    s.append(f'<line x1="160" y1="24" x2="160" y2="130" stroke="#2b2b2f" stroke-width="1"/>')
    return f'<svg viewBox="0 0 320 136" style="width:100%;height:auto;display:block">{"".join(s)}</svg>'


# ------------------------------------------------------------------ superficie aperta
def open_area_rows(d=2.0):
    rows = []
    for p in (2.8, 3.0, 3.5, 4.0):
        oa = 90.69 * (d / p) ** 2
        rows.append((p, round(p - d, 1), oa))
    return rows


def open_area_svg():
    rows = open_area_rows()
    s = []
    x0, w = 104, 200
    # banda della lamiera inox tipica 30–45%
    s.append(f'<rect x="{x0 + w*.30:.1f}" y="4" width="{w*.15:.1f}" height="{len(rows)*22+4}" fill="{W}" opacity=".06"/>')
    s.append(f'<text x="{x0 + w*.375:.1f}" y="{len(rows)*22+18}" text-anchor="middle" font-family="IBM Plex Mono" font-size="6" fill="{GREY}">{LBL["plate"]}</text>')
    for i, (p, lig, oa) in enumerate(rows):
        y = 8 + i * 22
        s.append(f'<text x="0" y="{y+9}" font-family="IBM Plex Mono" font-size="7" fill="{W}">{LBL["pitch"]} {str(p).replace(".", LBL["dec"])} mm</text>')
        s.append(f'<text x="0" y="{y+17}" font-family="IBM Plex Mono" font-size="5.8" fill="{GREY}">{LBL["web"]} {str(lig).replace(".", LBL["dec"])} mm</text>')
        s.append(f'<rect x="{x0}" y="{y+2}" width="{w}" height="12" fill="#1c1c1f"/>')
        s.append(f'<rect x="{x0}" y="{y+2}" width="{w*oa/100:.1f}" height="12" fill="{R}"/>')
        s.append(f'<text x="{x0 + w*oa/100 + 4:.1f}" y="{y+11}" font-family="IBM Plex Mono" font-size="7" font-weight="600" fill="{W}">{oa:.0f}%</text>')
    return f'<svg viewBox="0 0 330 {len(rows)*22+24}" style="width:100%;height:auto;display:block">{"".join(s)}</svg>'


# ------------------------------------------------------------------ icone del flusso ricambio
FLOW_ICONS = {
    "old": '<path d="M5 17 9 6h6l4 11z"/><path d="M8 12h8M10 6l1-3h2l1 3"/><path d="M4 21h16"/>',
    "scan": '<path d="M4 8V5a1 1 0 0 1 1-1h3M16 4h3a1 1 0 0 1 1 1v3M20 16v3a1 1 0 0 1-1 1h-3M8 20H5a1 1 0 0 1-1-1v-3"/><path d="M12 7 17 10v5l-5 3-5-3v-5z"/>',
    "file": '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 14h6M9 17h4M9 11h2"/>',
    "batch": '<rect x="3" y="4" width="18" height="16" rx="1.5"/><path d="M7 9h3v3H7zM14 9h3v3h-3zM7 14h3v3H7zM14 14h3v3h-3z"/>',
    "again": '<path d="M20 12a8 8 0 1 1-2.34-5.66"/><path d="M20 4v4.5h-4.5"/><path d="m9 12 2 2 4-4"/>',
}
