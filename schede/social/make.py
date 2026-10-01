"""Immagini per LinkedIn (1080 × 1350) dai ritagli delle schede in social/src/.
Uso: python3 social/make.py && NODE_PATH=$(npm root -g) node social/shot.js"""
from pathlib import Path
ROOT = Path(__file__).resolve().parent
LOGO = (ROOT.parent / "assets" / "logo_2pi.svg").read_text()
CARDS = [
    ("01_h2o_copertina", "h2o_cover", "Trattamento acque", "Griglie, filtri e ricambi in polipropilene.", "Senza stampo, da un pezzo a qualche migliaio.", True),
    ("02_h2o_mappa", "h2o_mappa", "Trattamento acque", "Dieci punti dell'impianto dove il PP stampato ha senso.", "E quelli dove non ce l'ha, scritti in chiaro.", True),
    ("03_h2o_pannello", "h2o_pannello", "Trattamento acque", "Il pannello forato in plastica, al posto della lamiera.", "Foro conico che non si incastra, clip nel pezzo.", False),
    ("04_kit_campioni", "kit_cover", "Kit campioni", "Undici materiali da toccare con mano.", "Il nome è inciso nel pezzo, non su un'etichetta.", True),
    ("05_cil_copertina", "cil_cover", "Schede applicazione", "Tamburi, rulli e rotori con i canali già dentro.", "Fino a 700 mm in un pezzo, da 1 a 50 pezzi.", True),
]
CSS = (ROOT.parent / "assets" / "fonts.css").read_text().replace("url(fonts/", "url(../assets/fonts/")
for name, img, tag, h, sub, dark in CARDS:
    html = f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;background:#0b0b0c;color:#faf9f7;font-family:'Archivo',sans-serif;position:relative;overflow:hidden}}
body::before{{content:"";position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.03) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.03) 1px,transparent 1px);background-size:24px 24px;-webkit-mask-image:radial-gradient(120% 80% at 80% 10%,#000 20%,transparent 70%)}}
body::after{{content:"";position:absolute;inset:0;background:radial-gradient(500px 500px at 960px 60px,rgba(230,51,41,.18),transparent)}}
.bar{{position:absolute;top:0;left:0;right:0;height:10px;background:#e63329;z-index:2}}
header{{position:absolute;top:52px;left:64px;right:64px;display:flex;justify-content:space-between;align-items:center;z-index:2}}
.logo{{display:flex;align-items:center;gap:16px;color:#faf9f7}}.logo svg{{width:52px;height:56px}}
.logo b{{font-weight:800;font-size:22px;line-height:1}}
.tag{{font-family:'IBM Plex Mono',monospace;font-size:17px;letter-spacing:.2em;text-transform:uppercase;color:#e63329}}
.shot{{position:absolute;left:64px;right:64px;top:150px;height:820px;border-radius:14px;overflow:hidden;z-index:2;display:flex;align-items:center;justify-content:center;
  background:{"#0b0b0c" if dark else "#f8f7f3"};box-shadow:0 0 0 1px #2b2b2f,0 30px 80px -30px rgba(0,0,0,.8)}}
.shot img{{width:100%;height:100%;object-fit:contain}}
.txt{{position:absolute;left:64px;right:64px;bottom:70px;z-index:2}}
.txt h1{{font-weight:800;font-size:56px;line-height:1.02;letter-spacing:-.03em}}
.txt h1 em{{font-style:normal;color:#e63329}}
.txt p{{font-family:'IBM Plex Serif',serif;font-size:26px;color:#c9c7c3;margin-top:18px}}
.foot{{position:absolute;left:64px;right:64px;bottom:30px;display:flex;justify-content:space-between;font-family:'IBM Plex Mono',monospace;font-size:15px;color:#8c8c90;letter-spacing:.12em;z-index:2}}
</style></head><body><div class="bar"></div>
<header><div class="logo">{LOGO}<b>DUE PI<br>GRECO</b></div><div class="tag">{tag}</div></header>
<div class="shot"><img src="src/{img}.png"></div>
<div class="txt"><h1>{h[:-1]}<em>{h[-1]}</em></h1><p>{sub}</p></div>
<div class="foot"><span>DUEPIGRECO3D.IT</span><span>ADDITIVE MANUFACTURING · RESANA (TV)</span></div>
</body></html>"""
    (ROOT / f"{name}.html").write_text(html)
print("ok")
