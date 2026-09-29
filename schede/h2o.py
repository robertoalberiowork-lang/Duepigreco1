"""Scheda settore DPG-SET-H2O rev. 02 — trattamento acque reflue e acqua industriale (6 pagine).

Uso:  python3 h2o.py  → html/DPG_Settore_H2O_IT.html ; poi  node tools/print_pdf.js
Fonti e grado di verifica dei dati: ricerca/H2O_PP_dossier.md
"""
from html import escape
from pathlib import Path

import h2o_art as art
from build import UI, contact_list, kpis, page_shell, svg

ROOT = Path(__file__).resolve().parent
DOC, REV = "DPG-SET-H2O", "REV. 02 · BOZZA"
TOTAL = 6
LOGO = (ROOT / "assets" / "logo_2pi.svg").read_text()


def head(top, bottom):
    return f"""
  <header class="head">
    <div class="logo">{LOGO}<div><b>DUE PI<br>GRECO</b><small>Additive manufacturing</small></div></div>
    <div class="meta"><span>{top}</span><br><b>{escape(bottom)}</b></div>
  </header>"""


def tblock(page):
    return f"""
  <dl class="tblock">
    <div><dt>Documento</dt><dd>{DOC}</dd></div>
    <div><dt>Revisione</dt><dd>{REV}</dd></div>
    <div><dt>Lingua</dt><dd>IT</dd></div>
    <div><dt>Editore</dt><dd>Due Pi Greco S.r.l.</dd></div>
    <div><dt>Pagina</dt><dd><b>{page:02d}</b> / {TOTAL:02d}</dd></div>
  </dl>"""


def sec(n, title, note=""):
    em = f"<em>{escape(note)}</em>" if note else ""
    return f'<div class="sec-h"><b>{n}</b><span>{escape(title)}</span>{em}</div>'


def callouts(labels):
    return "".join(f'<div class="callout" style="left:{l["x"]}%;top:{l["y"]}%"><i>{i:02d}</i><span>{escape(l["text"])}</span></div>'
                   for i, l in enumerate(labels, 1))


# ======================================================================= pagina 1
def p1():
    s, labels, ratio = art.cover_svg()
    return f"""
<section class="page cover">
  <div class="topbar"></div>
  {head("Scheda settore", DOC)}
  <div class="hero">
    <div class="eyebrow"><i></i>Acque reflue, acqua industriale, acquacoltura</div>
    <h1 style="--h1:35pt">Griglie, filtri e ricambi<br>in polipropilene, senza stampo<em>.</em></h1>
    <p class="lead">Pannelli forati, elementi di griglia, ugelli, crepine e i pezzi in plastica che il costruttore non
    fa più: in <strong>polipropilene sinterizzato</strong>, dal disegno o dal pezzo vecchio, da uno a qualche migliaio.
    Il materiale che la depurazione usa da sempre, con una geometria che lo stampo non permette.</p>
  </div>
  {kpis([("≥ 2", "mm", "luce di passaggio, fori e fessure"), ("≤ 30", "cm", "pezzo singolo, oltre a moduli"), ("0", "stampi", "dal pezzo unico alla serie")])}
  <div class="tavola">
    <div class="frame">
      <span class="corner tl"></span><span class="corner tr"></span><span class="corner bl"></span><span class="corner br"></span>
      <div class="fig"><b>Fig. 01</b> — Pannelli di griglia a nastro, vista isometrica</div>
      <div class="scale">Tav. {DOC}</div>
      <div class="art" style="aspect-ratio:{ratio:.4f}">{s}{callouts(labels)}</div>
    </div>
    <div class="legend"><span>Moduli forati agganciati al telaio inox della griglia. In azzurro: l'acqua</span>
      <div class="keys"><div class="key"><i></i><span><b>In rosso</b>: le parti che si producono in additive</span></div></div></div>
  </div>
  {tblock(1)}
</section>"""


# ======================================================================= pagina 2
FONTI = [
        "Direttiva (UE) 2024/3019, eur-lex.europa.eu",
        "MASE, PNRR M2C4 inv. 4.4, mase.gov.it",
        "United Utilities, «Printfrastructure», unitedutilities.com",
        "Johnson Screens e HP, johnsonscreens.com; 3dprint.com, 2022",
        "Anglian Water e Univ. di Sheffield, 3dprint.com, 2015",
        "Processes 14(6):1001, 2026, doi 10.3390/pr14061001",
        "Stratasys, SAF PP: scheda materiale e white paper sulla tenuta",
        "Resistenza chimica del PP: Braskem, INEOS, Charlotte Pipe",
    ]


def p2():
    stats = [
        ("2024/3019", "Direttiva UE acque reflue urbane",
         "Recepimento entro luglio 2027. Trattamento dei microinquinanti obbligatorio sopra 150.000 AE: "
         "20% degli impianti entro il 2033, 60% entro il 2039, tutti entro il 2045."),
        ("600 M€", "PNRR, fognatura e depurazione",
         "Investimento 4.4 della missione M2C4: impianti nuovi e adeguati, e con loro griglie, filtri e ricambi."),
        ("4", "Procedure d'infrazione UE all'Italia",
         "Agglomerati non conformi e un parco impianti in buona parte vecchio: il ricambio fuori produzione è la norma."),
    ]
    tiles = "".join(f'<div class="stat"><b>{escape(v)}</b><h4>{escape(t)}</h4><p>{escape(d)}</p></div>' for v, t, d in stats)
    ev = [
        ("Gestore idrico, Regno Unito", "United Utilities",
         "Nel programma Printfrastructure, finanziato dall'Ofwat, usa ogni giorno pezzi polimerici stampati: ugelli di "
         "lavaggio, canaline per strumenti e ricambi fuori produzione per i bracci dei filtri."),
        ("Costruttore di griglie", "Johnson Screens",
         "Ha portato in polipropilene stampato gli elementi del nastro filtrante di una griglia d'ingresso per reflui, "
         "al posto dell'acciaio inox."),
        ("Gestore idrico, Regno Unito", "Anglian Water",
         "Il primo pezzo che ha provato a stampare, con l'Università di Sheffield, è stato un ugello filtrante."),
        ("Ricerca, 2026", "Supporti MBBR in PP",
         "Supporti per biofilm a geometria gyroid stampati in PP, provati su refluo domestico in impianto pilota "
         "(Processes, 2026)."),
    ]
    evs = "".join(f'<div class="evid"><small>{escape(a)}</small><h4>{escape(b)}</h4><p>{escape(c)}</p></div>' for a, b, c in ev)
    return f"""
<section class="page inner">
  <div class="topbar"></div>
  {head("Scheda settore · " + DOC, "Trattamento acque reflue e acqua industriale")}
  <div class="body">
    <div class="sec">
      {sec("01", "Perché adesso")}
      <div class="stats">{tiles}</div>
    </div>
    <div class="sec">
      {sec("02", "Il conto che conoscete")}
      <div class="compare">
        <div class="col was"><div class="k"><i></i>Come va oggi</div>
          Il pannello della griglia si ordina al costruttore e arriva in settimane, se il modello è ancora a catalogo.
          L'ugello del filtro è di una marca che non esiste più. La crepina è un assieme incollato che perde dove non
          deve, e la lamiera forata in inox pesa, costa e per una variante piccola chiede comunque un'attrezzatura.</div>
        <div class="arrow">{svg('<path d="M5 12h14M13 6l6 6-6 6" stroke="#e63329" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')}</div>
        <div class="col now"><div class="k"><i></i>In sinterizzazione</div>
          Il pezzo vecchio diventa un file con la sua revisione, e il file un lotto: da un pezzo a qualche migliaio,
          senza stampo. Telaio, clip, nervature e filetto nascono nello stesso pezzo. Il foro può allargarsi verso
          l'uscita e non trattenere, e la volta dopo il riordino è identico.</div>
      </div>
    </div>
    <div class="sec">
      {sec("03", "Il polipropilene stampato è già in impianto", "Fonti pubbliche, in fondo alla pagina")}
      <div class="evids">{evs}</div>
    </div>
    <div class="proof">
      <div class="case"><div class="k"><span class="live"></span>In produzione, oggi</div>
        <p>Per un gruppo internazionale del trattamento acque produciamo in serie ricorrente <strong>pannelli filtranti
        in polipropilene sinterizzato con luce da 2 mm</strong>: riordino a magazzino digitale, lotto tracciato.
        <strong>Non un prototipo: una fornitura.</strong></p></div>
      <div class="limits"><div class="k">{svg(UI["warn"])}Perché polipropilene</div>
        <p>Non assorbe acqua e non idrolizza, come fa invece la poliammide. Regge acidi e basi diluiti, soda, cloruro
        ferrico e la chimica di lavaggio. Galleggia (circa 0,9 g/cm³) e pesa circa un ottavo dell'inox.
        È il materiale che vasche, tubi e ugelli usano da sempre.</p></div>
    </div>
    <p class="fonti"><b>Fonti</b> {" · ".join(escape(f) for f in FONTI)}</p>
  </div>
  {tblock(2)}
</section>"""


# ======================================================================= pagina 3 — mappa
MAP = [
    ("Pannelli ed elementi di griglia", "Griglie a nastro, a pettine, rotostacci: pannelli forati da 2 mm, elementi, guide, pattini, portaspazzole.", "A"),
    ("Minuterie dei raschiatori", "Distanziali, blocchi di riempimento, punte dei raschia-schiume, staffe di regolazione degli stramazzi.", "A"),
    ("Dosaggio chimico", "Miscelatori statici piccoli, filtri di fondo, punte d'iniezione per cloruro ferrico e ipoclorito, a bassa pressione.", "M"),
    ("Aerazione", "Selle, anelli, adattatori e raccordi per griglie di diffusori fuori produzione. Il diffusore resta di serie.", "M"),
    ("Griglie di ritenzione MBBR", "Moduli con fessure da 4–5 mm e profilo anti-incastro, per impianti piccoli, industriali, pilota.", "A"),
    ("Supporti sonde", "Gabbie, portasonde a pendolo, cuffie con ugello d'aria di pulizia ricavato nel pezzo.", "A"),
    ("Ugelli e crepine", "Seconda fonte per modelli fuori catalogo: biofiltri, drenaggi, scambio ionico. Fessura da 2 mm.", "A"),
    ("Deodorizzazione", "Distributori di liquido e collettori con gli ugelli nello stesso pezzo, supporti, separatori di gocce.", "M"),
    ("Linea fanghi", "Portaugelli di lavaggio, supporti delle lame, deviatori di nastropresse e ispessitori.", "M"),
    ("Strumentazione", "Pozzetti di calma, filtri del campionatore, supporti lungo tutto l'impianto.", "A"),
]


def p3():
    items = "".join(
        f'<li><i>{i:02d}</i><div><h4>{escape(t)} <span class="fit {f}">{"alto" if f == "A" else "medio"}</span></h4>'
        f'<p>{escape(d)}</p></div></li>' for i, (t, d, f) in enumerate(MAP, 1))
    return f"""
<section class="page cover map">
  <div class="topbar"></div>
  {head("Scheda settore · " + DOC, "Dove entriamo nell'impianto")}
  <div class="hero map-hero">
    <div class="eyebrow"><i></i>Mappa dell'impianto</div>
    <h2>Dalla griglia ai fanghi: dieci punti dove il pezzo in PP stampato ha senso<em>.</em></h2>
  </div>
  <div class="tavola">
    <div class="frame plant">
      <span class="corner tl"></span><span class="corner tr"></span><span class="corner bl"></span><span class="corner br"></span>
      <div class="fig"><b>Fig. 02</b> — Schema di un impianto a fanghi attivi</div>
      <div class="scale">Tav. {DOC}</div>
      {art.plant_svg()}
    </div>
    <div class="legend"><span>In azzurro l'acqua, tratteggiata l'aria e la linea fanghi. Adatto: alto = pezzo già in plastica, specifico, con ricambio difficile</span>
      <div class="keys"><div class="key"><i></i><span><b>In rosso</b>: dove entra il PP stampato</span></div></div></div>
  </div>
  <ol class="maplist">{items}</ol>
  <div class="offfield"><b>Fuori campo, e ve lo diciamo prima</b><span>contatto con ozono e biossido di cloro</span><span>giranti e centrifughe</span><span>deflettori e stramazzi grandi in vetroresina</span><span>supporti MBBR e riempimenti di serie</span><span>fessure fini dei filtri a sabbia, sotto 2 mm</span><span>zone Atex del biogas</span></div>
  {tblock(3)}
</section>"""


# ======================================================================= pagina 4 — porte 1 e 2
def p4():
    steps = [("old", "Il pezzo vecchio", "o il disegno, o lo STEP. Anche rotto, anche di una marca che non c'è più."),
             ("scan", "Rilievo 3D", "misuriamo il pezzo e ricostruiamo quote, filetti e accoppiamenti."),
             ("file", "File con revisione", "il ricambio diventa un codice vostro, con la sua revisione."),
             ("batch", "Lotto in PP", "da un pezzo a qualche migliaio, tracciato, senza stampo."),
             ("again", "Riordino identico", "tra un anno o tra dieci, dal file, senza scaffale.")]
    flow = "".join(f'<div class="step"><div class="ic">{svg(art.FLOW_ICONS[k])}</div><h4>{escape(t)}</h4><p>{escape(d)}</p></div>'
                   for k, t, d in steps)
    rows = art.open_area_rows()
    return f"""
<section class="page inner">
  <div class="topbar"></div>
  {head("Scheda settore · " + DOC, "Tre porte d'ingresso")}
  <div class="body">
    <div class="door">
      <div class="door-h"><span class="dn">01</span><div><small>Per gestori, manutentori, chi fa service sulle griglie</small>
        <h2>Il ricambio in plastica che non si trova più.</h2></div></div>
      <p class="door-lead">Pannelli, elementi e guide di griglie a nastro e a pettine, rotostacci e tamisadores, coperture,
      pattini, portaspazzole e portaugelli: li rifacciamo in PP dal pezzo vecchio, anche per macchine fuori produzione e
      anche un pezzo solo. Per chi fa service su più marche siamo il fornitore dei pezzi che il costruttore non dà più, o
      dà in settimane.</p>
      <div class="flow">{flow}</div>
    </div>
    <div class="door">
      <div class="door-h"><span class="dn">02</span><div><small>Per costruttori di griglie, rotostacci e filtri</small>
        <h2>Il pannello forato in plastica, al posto della lamiera.</h2></div></div>
      <div class="door-grid">
        <div class="dark-card">
          <div class="dc-k">Fig. 03 — Sezione del pannello</div>
          {art.hole_section_svg()}
          <p class="dc-cap">Nella lamiera il foro è dritto. Stampato, può allargarsi verso l'uscita come un profilo a cuneo:
          quello che entra, passa.</p>
        </div>
        <div class="dark-card">
          <div class="dc-k">Fig. 04 — Superficie aperta, fori da 2 mm a quinconce</div>
          {art.open_area_svg()}
          <p class="dc-cap">Calcolo geometrico. Il setto minimo si fissa con voi, sulla rigidezza che serve al pannello.</p>
        </div>
      </div>
      <table class="cmp">
        <thead><tr><th></th><th>Lamiera inox forata</th><th>Pannello stampato a iniezione</th><th class="us">PP sinterizzato</th></tr></thead>
        <tbody>
          <tr><td>Attrezzatura</td><td>punzonatura o laser</td><td>uno stampo per ogni formato</td><td class="us">nessuna: il file</td></tr>
          <tr><td>Lotto che ha senso</td><td>da un pezzo</td><td>migliaia</td><td class="us">da un pezzo a qualche migliaio</td></tr>
          <tr><td>Forma del foro</td><td>dritto</td><td>quella che si sforma</td><td class="us">dritta, conica, diversa per zona</td></tr>
          <tr><td>Telaio e clip</td><td>saldati o avvitati</td><td>nello stampo</td><td class="us">nel pezzo, anche per un ricambio solo</td></tr>
          <tr><td>Peso</td><td>7,9 g/cm³</td><td>leggero</td><td class="us">circa 0,9 g/cm³</td></tr>
          <tr><td>Cloruri, acqua di mare</td><td>l'inox li soffre</td><td>nessun problema</td><td class="us">nessun problema</td></tr>
          <tr><td>Sabbia e grit</td><td>buona</td><td>ottima in poliuretano</td><td class="us">media: a valle della dissabbiatura</td></tr>
          <tr><td>Luce minima</td><td>sotto il millimetro</td><td>fine</td><td class="us">2 mm</td></tr>
        </tbody>
      </table>
      <ul class="ticks">
        <li><b>Telaio, nervature, clip e sede della guarnizione</b> nello stesso pezzo: il modulo si aggancia e si cambia da solo.</li>
        <li><b>Luce diversa per zona</b> sullo stesso pannello, e codice del pezzo inciso sul telaio.</li>
        <li><b>Un ottavo del peso dell'inox</b>: il cambio pannelli si fa a mano, senza paranco.</li>
        <li><b>Moduli fino a 30 cm</b> di lato. Oltre, il pannello si divide in moduli che si agganciano, come i pannelli in
        poliuretano delle vagliatrici.</li>
        <li><b>Dove non va</b>: sabbia e grit prima della dissabbiatura consumano il PP più di poliuretano e UHMW; sotto 2 mm
        restano wedge-wire e tela.</li>
      </ul>
    </div>
  </div>
  {tblock(4)}
</section>"""


# ======================================================================= pagina 5 — porta 3 + idee
IDEAS = [
    ("Supporti sonde autopulenti", "Tutti gli impianti", "Gabbie e cuffie per sonde di ossigeno, pH e torbidità con il canale dell'aria di pulizia dentro il pezzo.", "carichi bassi, pezzi specifici"),
    ("Griglie di ritenzione MBBR", "Impianti compatti, industria, pilota", "Moduli piani al posto del cilindro in wedge-wire inox, con fessure da 4–5 mm e profilo che non incastra il supporto.", "impianti grandi: a moduli"),
    ("Distributori per scrubber", "Deodorizzazione", "Distributore di liquido e ugelli in un pezzo solo, senza saldature, nella chimica di lavaggio del PP: soda, ipoclorito, acido solforico.", "separatori grandi: a moduli"),
    ("Ricambi di filtri a dischi e a tamburo", "Terziario, acquacoltura", "Ugelli e barre di lavaggio, pattini di aspirazione, telai dei pannelli: la tela resta tela, il supporto si stampa.", "la tela sotto 2 mm non si stampa"),
    ("Acquacoltura a ricircolo", "RAS, avannotterie", "Griglie di scarico delle vasche con luce per taglia di pesce, piastre di distribuzione dei degasatori, porta-ugelli. In acqua di mare l'inox soffre, il PP no.", "UV all'aperto da valutare"),
    ("Galvanica e acque industriali", "Pretrattamento", "Spruzzatori, miscelatori e interni delle vasche di neutralizzazione, dove il PP è già il materiale di casa.", "no solventi aromatici e clorurati"),
    ("Torri di raffreddamento", "Acqua di processo", "Ugelli di spruzzo e adattatori per torri i cui ricambi non si trovano più, con l'orifizio che serve.", "sopra circa 60 °C da valutare"),
    ("Industria alimentare", "Caseifici, cantine, lavorazione del pesce", "Ricambi di microgriglie e setacci statici, cestelli dei pozzetti, pale degli sgrassatori: pezzi piccoli di macchine che il costruttore non segue più.", "non per contatto con l'alimento"),
    ("Acque meteoriche", "Caditoie, sfioratori", "Cestelli e griglie per caditoie fuori standard, schermi degli scarichi, a moduli che si agganciano.", "cestelli grandi: a moduli"),
    ("Impianti pilota e ricerca", "Università, società di ingegneria", "Supporti per biofilm a geometria gyroid, piccoli rotostacci, portadiffusori: il prototipo che poi diventa serie.", "costo al litro in grande serie"),
]


def p5():
    cards = "".join(f'<div class="idea"><small>{escape(s)}</small><h4>{escape(t)}</h4><p>{escape(d)}</p><span class="lim">limite · {escape(l)}</span></div>'
                    for t, s, d, l in IDEAS)
    return f"""
<section class="page inner">
  <div class="topbar"></div>
  {head("Scheda settore · " + DOC, "Tre porte d'ingresso, e oltre")}
  <div class="body">
    <div class="door">
      <div class="door-h"><span class="dn">03</span><div><small>Per chi produce, vende o monta ugelli e crepine</small>
        <h2>Ugelli e crepine: la seconda fonte.</h2></div></div>
      <div class="nozzle">
        <div class="nz-img"><img src="../assets/crepina.jpg" alt="">
          <span class="nz-cap">Fig. 05 — Crepina di controlavaggio: corpo, slot e filetto in un pezzo. A destra, sezione A-A.</span></div>
        <div class="nz-txt">
          <p>Il modello fuori catalogo, la marca che non esiste più, la variante per un solo impianto: la facciamo in PP,
          dal pezzo o dal disegno, con la stessa filettatura.</p>
          <ul class="ticks">
            <li><b>Corpo, slot e filetto in un pezzo</b>: nessun incollaggio, nessuna giunzione che perde.</li>
            <li><b>Profilo dello slot a cuneo</b> verso l'interno: si pulisce al controlavaggio.</li>
            <li><b>Il foro dell'aria di lavaggio</b> nel gambo, nello stesso pezzo, se il vostro ugello lo prevede.</li>
            <li><b>Fessura da 2 mm in su</b>: biofiltri, drenaggi su ghiaia, scambio ionico, acquacoltura. Per la sabbia fine
            stampiamo il corpo e il cappello fessurato resta a catalogo.</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="sec">
      {sec("04", "Idee oltre la griglia", "Dove lo stesso PP lavora già")}
      <div class="ideas">{cards}</div>
    </div>
  </div>
  {tblock(5)}
</section>"""


# ======================================================================= pagina 6 — materiale e limiti
CHEM = [
    ("Acidi diluiti non ossidanti", "solforico, cloridrico", "ok"),
    ("Basi", "soda caustica", "ok"),
    ("Coagulanti", "cloruro ferrico", "ok"),
    ("Perossido di idrogeno", "a temperatura ambiente", "ok"),
    ("Ipoclorito di sodio", "a freddo sì, caldo ed esposizione continua da valutare", "cond"),
    ("Polielettroliti, PAC, H₂S, metanolo, acido peracetico", "da verificare sul vostro fluido", "cond"),
    ("Ozono, biossido di cloro", "degradano il PP: serve PVDF", "no"),
    ("Acidi ossidanti concentrati, solventi aromatici e clorurati", "attaccano o gonfiano il PP", "no"),
]


def p6():
    chem = "".join(f'<tr><td><span class="dot {c}"></span>{escape(a)}</td><td>{escape(b)}</td></tr>' for a, b, c in CHEM)
    props = [("Resistenza a trazione", "30 MPa"), ("Modulo elastico", "1600 MPa"), ("Allungamento a rottura", "20%"),
             ("Inflessione sotto carico, 0,45 MPa", "100 °C"), ("Densità", "circa 0,9 g/cm³"),
             ("A tenuta d'acqua", "da 1 mm di parete")]
    prow = "".join(f"<tr><td>{escape(a)}</td><td>{escape(b)}</td></tr>" for a, b in props)
    rovescio = [
        ("Sotto 2 mm di luce", "la fessura fine della filtrazione a sabbia resta a wedge-wire e tela."),
        ("Oltre 30 cm", "il pezzo si divide in moduli; tubi, lastre e deflettori grandi non sono il nostro mestiere."),
        ("Acqua potabile", "il nostro PP non ha certificazioni per l'acqua destinata al consumo umano."),
        ("Ozono e biossido di cloro", "il PP non li regge: in quello stadio va il PVDF."),
        ("Sabbia e grit", "a monte della dissabbiatura poliuretano e UHMW durano di più."),
        ("Pressione nel tempo", "non dichiariamo una pressione nominale: si prova sul vostro caso."),
        ("Freddo e sole", "sotto 0 °C il PP diventa fragile agli urti; all'aperto la tenuta ai raggi UV si valuta."),
    ]
    rov = "".join(f"<li><b>{escape(a)}</b>{escape(b)}</li>" for a, b in rovescio)
    need = ["Il pezzo vecchio, anche rotto, oppure disegno o STEP", "Due foto del pezzo montato",
            "Il fluido, la chimica e la temperatura di esercizio", "Quanti pezzi: oggi, e all'anno"]
    needs = "".join(f"<li>{escape(n)}</li>" for n in need)
    return f"""
<section class="page inner">
  <div class="topbar"></div>
  {head("Scheda settore · " + DOC, "Materiale, limiti e contatti")}
  <div class="body">
    <div class="sec">
      {sec("05", "Il materiale", "Polipropilene SAF · DPG-MAT-PP")}
      <div class="mat-grid">
        <div>
          <table class="kv">{prow}</table>
          <p class="note">Valori di scheda del produttore della polvere, su provini. Il pezzo si valuta sul pezzo.</p>
        </div>
        <div>
          <table class="chem">{chem}</table>
          <p class="note"><span class="dot ok"></span>adatto <span class="dot cond"></span>con condizioni <span class="dot no"></span>no ·
          dati del polimero di base: su richiesta proviamo il pezzo nel vostro fluido.</p>
        </div>
      </div>
    </div>
    <div class="sec">
      {sec("06", "Materiali per il settore")}
      <table class="mat">
        <thead><tr><th style="width:24%">Materiale</th><th style="width:12%">Processo</th><th>Perché qui</th><th style="width:20%">Riferimento</th></tr></thead>
        <tbody>
          <tr><td class="m">Polipropilene</td><td><span class="badge SAF">SAF</span></td><td>il materiale dell'acqua: non assorbe acqua, non idrolizza, regge la chimica di processo; UL94 HB, non per requisiti al fuoco</td><td class="ref">DPG-MAT-PP</td></tr>
          <tr><td class="m">PA2200 (PA12)</td><td><span class="badge SLS">SLS</span></td><td>dove serve più rigidità o temperatura, fino a +80 °C sotto carico, fuori dall'immersione continua: la poliammide assorbe acqua</td><td class="ref">DPG-MAT-PA2200</td></tr>
        </tbody>
      </table>
    </div>
    <div class="sec">
      {sec("07", "Il rovescio", "Quando non conviene, ve lo diciamo prima")}
      <ul class="rov">{rov}</ul>
    </div>
    <div class="needs-row"><b>Per un'offerta ci servono</b><ol>{needs}</ol></div>
  </div>
  <div class="cta">
    <div>
      <h2>Mandateci il pezzo che non trovate più.<br><span>Vi diciamo anche quando non conviene.</span></h2>
    </div>
    <ul>{contact_list()}</ul>
  </div>
  {tblock(6)}
</section>"""


def main():
    html = page_shell("Due Pi Greco — DPG-SET-H2O", p1() + p2() + p3() + p4() + p5() + p6())
    html = html.replace('<link rel="stylesheet" href="../assets/scheda.css">',
                        '<link rel="stylesheet" href="../assets/scheda.css">\n<link rel="stylesheet" href="../assets/h2o.css">')
    out = ROOT / "html" / "DPG_Settore_H2O_IT.html"
    out.write_text(html)
    print("scritto", out)


if __name__ == "__main__":
    main()
