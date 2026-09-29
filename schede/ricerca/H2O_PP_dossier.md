# Polipropilene SAF nel trattamento acque reflue — dossier di ricerca

Base per la nuova versione della scheda **DPG-SET-H2O** e per l'allegato ai contatti del Lotto 16.
Data: 29/09/2026. Ricerca da fonti pubbliche, in quattro filoni: materiali, letteratura e casi, mappa
dell'impianto, pannelli filtranti e settori vicini.

**Come leggere le fonti.** Da questo ambiente le pagine originali non si potevano aprire: i dati vengono
dagli estratti dei motori di ricerca. Ogni numero ha la sua fonte, ma **prima di stamparlo va riletto sul
documento originale**. Etichette: **[P]** dichiarazione del produttore, **[I]** fonte indipendente,
**[D]** deduzione nostra, **[DA VERIFICARE]** dato incerto o incoerente.

---

## 0. I paletti di partenza (da Due Pi Greco)

- Processo: **SAF, Stratasys H350**, PP (polvere BASF / Forward AM). Volume di stampa circa
  315 × 208 × 293 mm: **pezzo singolo fino a circa 30 cm**.
- **Luce da 2 mm in su.** Sotto, wedge-wire e rete restano la risposta giusta.
- **PP non certificato per acqua potabile**: il campo è reflui, acqua industriale, acquacoltura.
- Caso in produzione: pezzi filtranti in PP in serie per un gruppo internazionale del trattamento acque
  (non citabile per nome). Pannelli con luce da 2 mm, circa il 30% di una macchina.

---

## 1. Il materiale

### 1.1 Gradi PP a letto di polvere a confronto

| Grado | Processo | Resistenza a trazione | Modulo | Allungamento | HDT | Densità | Note |
|---|---|---|---|---|---|---|---|
| **Stratasys SAF PP** (Forward AM) | SAF, H350 | 30 MPa | 1600 MPa | 20% | 100 °C (0,45 MPa) | n.d. | a tenuta d'acqua e d'aria; in commercio da fine 2024 [P] |
| HP 3D HR PP (BASF) | MJF | 30 MPa | 1600 MPa | 20% XY / 18% Z | 100 °C [DA VERIFICARE carico] | 0,89 g/cm³ | concorrente diretto, stessa base BASF [P] |
| BASF Ultrasint PP nat 01 | SLS | 28 MPa | 1400 MPa | ~30% | n.d. | – | [P] |
| Ricoh PP | SLS | 21,4 MPa | 907 MPa | [DA VERIFICARE] | 71 °C (0,45) / 52 °C (1,8) | 0,84 g/cm³ | **approvazione WRAS 1805518** [P, DA VERIFICARE] |
| Sinterit PP | SLS | 19,3 MPa | 820 MPa | 44% | 85 °C / 50 °C | – | "saldabile" [P] |
| Formlabs PP | SLS | 29 MPa | 1640 MPa | 34% XY / 16% Z | 58 °C (1,8) | – | **fuori produzione** [P] |
| ALM PP 400 (gruppo EOS), EOS PP 1101, Prodways PP 1200 | SLS | n.d. | n.d. | – | – | – | per fluidi e serbatoi, senza numeri pubblici [P] |

Fonti: [Stratasys SAF PP](https://www.stratasys.com/en/materials/materials-catalog/saf-materials/saf-pp-polypropylene/),
[Forward AM](https://forward-am.com/material-portfolio/ultrasint-powders-for-powder-bed-fusion-pbf/pp-line/stratasys-saf-pp-enabled-by-forward-am/),
[HP PP](https://h20195.www2.hp.com/v2/GetDocument.aspx?docname=4AA7-7426ENW),
[Ultrasint PP TDS](https://forward-am.com/wp-content/uploads/2021/04/BASF_3DPS_TDS_Ultrasint_PP-Nat-01.pdf),
[Ricoh TDS](https://3d.ricoh.com/wp-content/uploads/2019/10/Ricoh-TDS-SLS-PP-Web-Final.pdf),
[Sinterit](https://sinterit.com/materials/polypropylene-pp/),
[Formlabs TDS](https://formlabs-media.formlabs.com/datasheets/2301856-TDS-ENUS-0.pdf).

**Cosa ne ricaviamo**
- SAF PP e HP PP hanno numeri quasi uguali (stessa base BASF). Sulla carta il materiale non vi distingue
  da chi stampa in MJF: vi distinguono il servizio, il ricambio dal pezzo vecchio e la produzione in serie
  già in corso. [D]
- I gradi stampati fondono a **125–138 °C**, contro i circa 160–165 °C del PP-H in lastra e tubo. Sono
  probabilmente copolimeri. Conta per la saldatura (§1.4). [D]

### 1.2 Tenuta, pressione, invecchiamento

- **Tenuta (white paper Stratasys) [P].** Pareti da 1 mm a tenuta fino alla rottura, in qualsiasi
  orientamento di stampa. Rottura media a **14,1 bar** (min 10, max 15). La frattura non segue i layer. Il
  valore dipende dalla velocità di salita della pressione: è **scoppio a breve termine, non pressione di
  esercizio**. Caso di prova: corpo filtro per pompa con filetto da ½", 25 pezzi in circa 35 h (11 di
  stampa e 24 di raffreddamento).
  [PDF](https://www.stratasys.com/siteassets/resources/white-papers/achieve-watertight-excellence-with-saf-polypropylene/wp_saf_pp-for-watertight-applic_0125a.pdf)
- **UV [P].** SAF PP dopo 1500 h (ISO 4892-3): resistenza a trazione invariata, allungamento da 9,8% a
  8,3%. Stratasys lo equipara a 1,5–3 anni all'aperto.
  [PDF](https://www.stratasys.com/contentassets/155355c980974a9a9aa809b498f13001/wp_saf_pa12--pp-uv--weathering-exposure_0425a.pdf)
- **Idrolisi [I].** Il PP non idrolizza, la poliammide sì, e l'acqua calda ossigenata la accelera. Il PA6
  assorbe 6–8 volte più acqua del PP. È l'argomento chiave "PP e non PA12" per l'acqua.
  [fonte](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8537549/)
- **Freddo [I].** La Tg del PP è intorno a 0 °C: tra −5 e +5 °C diventa fragile. Conta per vasche
  all'aperto d'inverno e per i pezzi soggetti a urto.
- **Creep [DA VERIFICARE].** Nessun dato di creep o di resistenza idrostatica a lungo termine per PP
  stampato. **Non promettere una pressione nominale nel tempo.**
- **Finitura [P].** Con la levigatura a vapore AMT PostPro la rugosità del PP stampato scende da Ra 11 µm a
  1,45 µm e la superficie si sigilla.
  [fonte](https://amtechnologies.com/resources/whitepapers/postpro-vapor-smoothing-ultrasint-pp-parts-to-unlock-new-potentials/)
- **Tolleranze e deformazione [P, guide MJF].** Circa ±1,75% (min ±0,7 mm). Pannelli piatti fino a
  0,3–1,0 mm di svergolamento su 200 mm. Il SAF avrà valori suoi: vanno misurati sui vostri pannelli. [D]

### 1.3 Resistenza chimica (dati del PP di base, non del PP stampato)

Nessun produttore pubblica tabelle di immersione del PP stampato con i reagenti della depurazione.
Stratasys ha provato i materiali SAF solo con fluidi auto. Nel documento la formula corretta è
**"in base al polimero di base; su richiesta prove sul vostro fluido"**.

| Mezzo | PP | Nota |
|---|---|---|
| Acidi non ossidanti diluiti (solforico, cloridrico) | buona | [Braskem](https://www.braskem.com.br/Portal/Principal/Arquivos/html/boletm_tecnico/PP%20Chemical%20Resistance.pdf) |
| Soda caustica e alcali | buona | Braskem |
| Cloruro ferrico | buona | [Engineering Toolbox](https://www.engineeringtoolbox.com/polypropylene-pp-chemical-resistance-d_435.html) |
| Perossido di idrogeno 30% | buona a temperatura ambiente | [INEOS](https://www.ineos.com/globalassets/ineos-group/businesses/ineos-olefins-and-polymers-usa/products/technical-information--patents/ineos-pp-chemical-resistance-guide.pdf); degrada con esposizione lunga |
| **Ipoclorito di sodio 20%** | A a 20 °C, B a 60 °C | **condizionale**: degrada con esposizione lunga, per servizio continuo CPVC/PVDF ([Charlotte Pipe](https://www.charlottepipe.com/articles/evaluating-the-chemical-resistance-of-piping-materials)) |
| **Ozono** | scarsa | **escluso**, serve PVDF ([Delozone](https://delozone.com/ozone-material-compatibility-chart/)) |
| **Biossido di cloro** | scarsa | invecchia più in fretta che con il cloro |
| Acidi ossidanti concentrati (nitrico) | scarsa | escluso |
| Solventi aromatici e clorurati | scarsa | rigonfiamento |
| H₂S, PAC/solfato di alluminio, polielettroliti, metanolo, acido peracetico, detergenti | [DA VERIFICARE] | leggere la guida completa [IPEX PP](https://ipexna.com/wp-content/uploads/2022/08/chemical-guide-caen-ipex-pp.pdf) o [PPI TR-19](https://conduitcalc.plasticpipe.org/pdf/tr-19-2020.pdf) |

**Correzione alla scheda attuale.** La rev. 01 dice "Cloro, ipoclorito, flocculanti, acidi e detergenti:
il PP è il materiale che il trattamento acque usa da sempre". Va sfumata: **ipoclorito sì ma con limiti di
temperatura e tempo, ozono e biossido di cloro no.** L'impianto per microinquinanti con ozono (vedi §3.1) è
fuori dal perimetro del PP.

### 1.4 Saldatura al PP esistente

- HP dice di aver saldato con successo il suo PP a PP stampato a iniezione. Sinterit dichiara il suo PP
  "facilmente saldabile" [P].
- **Nessuna fonte dà la resistenza del giunto, né prove di saldatura a gas caldo o per estrusione su lastra
  o tubo PP-H** [DA VERIFICARE].
- La differenza di temperatura di fusione (125–138 °C contro 160–165 °C) può indebolire il giunto [D].
- **Da fare in casa, prima di prometterlo:** saldare provini SAF PP su lastra PP-H e trazione sul giunto.
  Se funziona è un argomento forte ("il pezzo stampato si salda alla vostra vasca"), che la PA12 non ha.

### 1.5 Certificazioni

- **Acqua potabile.** L'unico PP stampato con approvazione trovata è **Ricoh SLS PP, WRAS 1805518** [P,
  da controllare nel [registro WRAS](https://www.wrasapprovals.co.uk/approvals-directory/)]. Nessun PP a
  letto di polvere con NSF/ANSI 61, KTW/UBA, ACS o DM 174/2004. Il perimetro "reflui e industria" è
  corretto.
- **SAF PP:** nessuna dichiarazione per contatto alimentare o biocompatibilità trovata.

---

## 2. Cosa dice la letteratura e chi l'ha già fatto

### 2.1 Casi industriali (i più utili per vendere)

1. **Johnson Screens (gruppo Aqseptence) + EVOK3D, Australia.** Elementi del nastro filtrante di una
   griglia d'ingresso per reflui, riprogettati per la stampa e prodotti **in PP con HP MJF**. Dichiarati:
   fino a **10 settimane** in meno di tempi di consegna, **40%** in meno di tempo di montaggio. Secondo un
   estratto, i pezzi stampati hanno fatto meglio degli originali in acciaio inox dopo 9 mesi [DA VERIFICARE].
   [3DPrint.com](https://3dprint.com/297882/filtration-leader-3d-prints-critical-wastewater-screens-with-hps-mjf/),
   [Johnson Screens](https://johnsonscreens.com/johnson-screens-and-hp-partnership-revolutionizes-screens-manufacturing/).
   **È l'unico caso confermato di pannelli filtranti stampati in PP. Prova che il mercato esiste, e che
   un grande costruttore è già entrato con la tecnologia HP.** [D]
2. **United Utilities (UK), "Water Industry Printfrastructure".** Programma finanziato dall'Ofwat, con
   Scottish Water, Manchester Metropolitan University e ChangeMaker3D. Pezzi polimerici stampati in uso
   quotidiano: ugelli di lavaggio, piastra per skid CCTV, canaline per strumenti, **ricambi fuori
   produzione per bracci filtranti**. Scala sul piano di investimenti AMP8 2025–2030.
   [UU](https://corporate.unitedutilities.com/corporate/about-us/innovation/case-studies/printfrastructure/).
   Collegamento con il Lotto 16: la consultazione "3D Printing Services" (PF03).
3. **Anglian Water + Università di Sheffield, circa 2015.** Primo gestore UK a provare la stampa: il primo
   pezzo è stato un **ugello filtrante**. [3DPrint.com](https://3dprint.com/102405/uk-3dp-water-technology/)
4. **Hydro International per Thames Water.** Contratto quadro per i servizi sulle griglie: ricambi "OEM e
   pattern parts" di tutte le marche. Il ricambio originale arriva in 6–8 settimane.
   [Hydro Intl](https://hydro-int.com/en/services/parts-spares)
5. **Costruttori di pompe (metallo, non PP):** Sulzer (giranti e ricambi di pompe vecchie), Xylem (anime in
   sabbia stampate, 4 pezzi in 1), Grundfos (reparto AM interno). Dimostrano che il settore accetta il
   ricambio stampato.
6. **Riferimento fuori settore: Deutsche Bahn.** Oltre 200.000 pezzi stampati e più di 1.000 applicazioni,
   con magazzino digitale per i ricambi fuori produzione. Obiettivo 10.000 modelli entro il 2030.
   [DB](https://www.deutschebahn.com/en/3d_printing-6935100)

**Nessun caso pubblico trovato** per Veolia, Suez, Acea, Hera, A2A, Huber, Andritz, Evoqua. Non vuol dire
che non esistano.

### 2.2 Ricerca (laboratorio e pilota)

| Tema | Studio | Risultato |
|---|---|---|
| Supporti per biofilm MBBR | *Processes* 14(6):1001, 2026 — [doi](https://doi.org/10.3390/pr14061001) | gyroid in **PP**, pilota su refluo domestico: fino a 87% BOD, 87% ammoniaca, 97% nitrati rimossi (processo di stampa non chiaro, probabilmente FDM) |
| Supporti MBBR | *PLOS ONE* 2020 — [link](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0238386) | gyroid con superficie oltre 1980 m²/m³: 99,3% di conversione dell'ammoniaca, meglio del K1 |
| Supporti MBBR | *Scientific Reports* 2015 — [link](https://www.nature.com/articles/srep12400) | primo studio: biofilm più attivo del K3 commerciale |
| Spaziatori per membrane | *Water Research* 2016; *Desalination* 2018 | meno perdita di carico, meno biofouling; prodotto commerciale Aqua Membranes (−60% di perdita di carico dichiarato) |
| Promotori di turbolenza UF | *J. Membrane Sci.* 2018 — [arXiv](https://arxiv.org/abs/1803.08464) | flusso di permeato +130/140% |
| Idrocicloni | *Chem. Eng. J.* 2018 | +10 punti di recupero solidi a pari perdita di carico |
| Riempimenti strutturati TPMS | *Energy Environ. Sci.* 2023 | trasferimento di massa +49–61% rispetto a Mellapak 250Y |
| Filtri anti-intasamento | *Materials* 2022, PA12 SLS a lamelle "manta" | geometrie che resistono all'intasamento |

**Review utili:** Tijing et al., *Applied Materials Today* 2020; Zhang et al., *Chem. Eng. J.* 2024; *ACS
ES&T Water* 2024; *JACS Au* 2023.
**Il punto in comune:** quasi tutto è in laboratorio, con FDM o resina (PLA, ABS). **Il PP industriale a
letto di polvere è quasi assente dagli studi.** Non esistono studi su miscelatori statici stampati per il
dosaggio di coagulanti, su riempimenti per scrubber di deodorizzazione, né su pacchi lamellari in PP
stampato. [I, confermato dalle review]

---

## 3. Il mercato che crea domanda

### 3.1 Europa e Italia

- **Direttiva UE 2024/3019 (rifusione acque reflue urbane).** Recepimento entro il 31/07/2027.
  **Trattamento quaternario** (microinquinanti) obbligatorio sopra 150.000 AE: 20% entro il 2033, 60% entro
  il 2039, tutti entro il 2045. Almeno l'80% del costo è a carico dei produttori (EPR). Neutralità
  energetica entro il 2040. [EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32024L3019)
  Per il PP [D]: nuovi stadi a carbone attivo e filtrazione terziaria (ugelli, crepine, griglie), ma
  **l'ozono è escluso**.
- **PNRR M2C4 inv. 4.4 "Fognatura e depurazione":** 600 M€.
  [MASE](https://www.mase.gov.it/portale/-/-pnrr.-mite-600-milioni-per-migliorare-la-depurazione-e-il-riutilizzo-delle-acque)
- **Italia:** 4 procedure d'infrazione UE, oltre 900 agglomerati non conformi, impianti descritti come
  obsoleti. [Commissario Unico](https://commissariounicodepurazione.it/)
  Parco macchine vecchio vuol dire ricambi fuori produzione. [D]
- **Gare per ricambi:** SIMARSUL (PT) mette a gara i ricambi dei tamisadores Huber, Andritz, M.A.IND e
  Aquagard. Thames Water ha il contratto quadro con Hydro International; Southern Water ha un lotto
  ricambi.

---

## 4. Dove il PP SAF ha senso — mappa dell'impianto

Legenda: **A** alto, **M** medio, **B** basso. ">30" vuol dire che il pezzo va diviso in moduli o saldato;
"<2" vuol dire luce troppo fine.

| Stadio | Componente | Oggi | Adatto | Perché |
|---|---|---|---|---|
| Grigliatura | **Pannelli forati di griglie a nastro** (JWC Finescreen, Headworks Eliminator, Hydro-Dyne, Spirac Bandguard) | pannelli in UHMW o plastica, fori 2/3/6 mm | **A** | già in plastica, usurabili, specifici per modello; moduli entro 30 cm |
| Grigliatura | **Elementi di griglie a pettine** (Parkson Aqua Guard) | elementi stampati su alberi, luce 1–30 mm | **A** | pezzi piccoli e numerosi; ricambio a lotti |
| Grigliatura | Tamburi e coclee (Huber, Lackeby, Klinger) | lamiera inox forata 2–11 mm | B per il cestello, **M** per segmenti | il tamburo è strutturale; sì a segmenti curvi, spazzole, spray, guide |
| Grigliatura | Compattatori, lavaggio grigliato | pattini e liner in UHMW/PA | M | il PP si usura più dell'UHMW: da provare |
| Sedimentazione primaria | **Distanziali e blocchi di riempimento dei raschiatori a catena**, punte dei raschia-schiume | PP, UHMW | **A** | già in PP, piccoli, impianti vecchi |
| Sedimentazione | Stramazzi, deflettori, canali | vetroresina | B (>30) | solo staffe e morsetti di regolazione (M) |
| Biologico | Diffusori | PP/PVC stampati a milioni | B corpo, **M** adattatori | selle, anelli, raccordi per griglie fuori produzione |
| Biologico | **Griglie di ritenzione MBBR** | wedge-wire inox, fessura 4–5 mm | **M–A** | fessure ben sopra i 2 mm; impianti piccoli, industriali e pilota; profilo anti-incastro |
| Biologico | Supporti MBBR | HDPE estruso a pochi centesimi | B in serie, **A per piloti** | geometrie gyroid per ricerca e impianti pilota |
| Terziario | **Ugelli e crepine** di filtri a sabbia e biofiltri | PP/ABS, fessure 0,1–5 mm | **A come seconda fonte** | solo dove la fessura è ≥2 mm (biofiltri, drenaggi grossolani, scambio ionico), oppure si stampa il corpo e il cappello fine si compra |
| Terziario | Filtri a dischi e a tela (Hydrotech, MITA) | telai modulari e tela in poliestere | **A** per spray e pattini, M per telai | la tela resta tela |
| Terziario | Pacchi lamellari | lastra termoformata | B | solo clip e distanziali |
| Disinfezione | UV, ozono | – | **B / escluso** | UV degrada il PP, ozono lo attacca |
| Quaternario | Crepine per carbone attivo | – | M | il carbone è 0,5–2,5 mm: spesso sotto la soglia |
| Fanghi | Nastropresse e ispessitori: portaugelli, supporti lama, deviatori | UHMW/PP | **M–A** | specifici per modello |
| Deodorizzazione | **Distributori di liquido e collettori di ugelli degli scrubber**, supporti, separatori di gocce | PP/PVC saldato | **M–A** | chimica adatta al PP (NaOH, NaOCl, H₂SO₄); distributore e ugelli in un pezzo |
| Dosaggio | Miscelatori statici piccoli (fino a circa DN100), filtri di fondo, punte di iniezione anti-incrostazione | PP/PVC | **M–A** | solo bassa pressione |
| Strumentazione | **Supporti sonde, gabbie a pendolo, cuffie autopulenti con ugelli d'aria**, filtri del campionatore | PVC/PP lavorato, inox | **A** | pochi pezzi, specifici, scarico basso; il canale d'aria nel pezzo è un vero vantaggio della stampa |
| Industria | Galvanica: spruzzatori, miscelatori per neutralizzazione; alimentare/tessile: ricambi di griglie e sgrassatori | PP di serie | **A** | il PP è già il materiale di casa |

**Non proporre:** contatto con ozono; giranti e centrifughe (usura); deflettori e stramazzi grandi in
vetroresina; supporti MBBR e riempimenti di serie; fessure fini dei filtri a sabbia e ugelli DAF (<2).
Fonti: vedi report di mappa (Xylem, Brentwood, Parkson, JWC, Vorex, Orthos, Veolia, Lantec, Inyo…).

---

## 5. Pannelli filtranti: lo spazio del vostro caso

- **I pannelli in plastica sono già accettati.** JWC Finescreen Monster usa un "nastro continuo di
  pannelli forati in UHMW" ([JWC](https://www.jwce.com/products/finescreen-monster/)). Headworks
  Eliminator usa elementi forati "inox o plastica". Hydro-Dyne offre pannelli in UHMWPE.
- **I 2 mm sono la soglia utile.** 2–3 mm di lamiera forata sono "il minimo" per proteggere le membrane
  MBR; Huber raccomanda 2–3 mm per MBR a lastre piane
  ([Water Online](https://www.wateronline.com/doc/the-do-s-and-don-ts-of-mbr-pretreatment-0001)). Il foro
  tondo trattiene fibre e capelli meglio della fessura (Lackeby).
- **Superficie aperta [D].** Con fori da 2 mm a quinconce: circa 40% a passo 3,0 mm e circa 46% a passo
  2,8 mm. La lamiera inox tipica è al 30–45%.
- **Cosa aggiunge la stampa [D]:**
  - foro conico (stretto all'ingresso, largo all'uscita) che non si incastra, come il wedge-wire;
  - telaio, nervature, clip, sede della guarnizione e codice del pezzo in un solo pezzo;
  - luce diversa per zona, sullo stesso pannello;
  - un ottavo del peso dell'inox;
  - nessuno stampo per il ricambio di una griglia vecchia.
- **Limiti:**
  - **abrasione**: poliuretano e UHMW resistono meglio alla sabbia, quindi il pannello in PP va a valle
    della dissabbiatura: grigliatura fine, protezione MBR, acquacoltura;
  - rigidezza e creep sotto battente, che chiedono moduli piccoli e nervati;
  - spazzole d'acciaio da evitare;
  - UV da verificare.
- **Nessun fornitore commerciale di pannelli filtranti stampati in PP trovato**, a parte il caso Johnson
  Screens, fatto in casa con HP. Il campo è aperto, ma non vuoto. [D]
- **Riferimento dal settore minerario:** i pannelli modulari in PU da 305 × 305 mm sono uno standard.
  Moduli da 30 cm a incastro sono un formato già accettato.

---

## 6. Settori vicini (stessi acquirenti o stesso PP)

- **Acquacoltura a ricircolo (RAS).**
  - Pezzi: telai dei pannelli dei filtri a tamburo (oggi già in PP), griglie di scarico delle vasche con
    luce per taglia di pesce, piastre di distribuzione dei degasatori, porta-ugelli.
  - Perché: con l'acqua di mare l'inox corrode, e gli allevamenti sono lontani e hanno bisogno di ricambi
    rapidi.
  - Contatti: Sterner (NO/UK), MAT-Kuling, Hydrotech.
- **Torri di raffreddamento.** Ugelli di spruzzo per torri vecchie, adattatori, inserti delle vasche di
  distribuzione.
- **Piscine collettive.** Cestelli di prefiltri e skimmer di modelli fuori produzione. Mercato di serie,
  interessa solo per il ricambio.
- **Irrigazione.** Cestelli di prefiltro ≥2 mm e succhieruole galleggianti per pompe da canale.
- **Acque meteoriche.** Cestelli per caditoie non standard, da fare in moduli.
- **Industria alimentare, casearia, del vino, del pesce.** Ricambi di microgriglie e setacci statici,
  cestelli dei pozzetti. Non presentare il pezzo come adatto al contatto alimentare.
- **Università, laboratori e impianti pilota.** Supporti gyroid, griglie di ritenzione, piccoli tamburi,
  portadiffusori. Accettano il prototipo e fanno da vetrina.

---

## 7. Classifica delle opportunità per Due Pi Greco

1. **Pannelli ed elementi di ricambio per griglie a nastro, a pettine e a tamburo**, dal pezzo vecchio
   (fori ≥2 mm, moduli ≤30 cm). *È il vostro caso in produzione, e ci sono le gare ricambi.*
2. **Ugelli e crepine come seconda fonte**, fuori catalogo o fuori produzione (biofiltri, drenaggi,
   acquacoltura; corpo stampato con cappello fine a parte).
3. **Supporti sonde e cuffie autopulenti** con canale d'aria integrato.
4. **Griglie di ritenzione MBBR** a moduli per impianti piccoli, industriali, di acquacoltura e pilota.
5. **Distributori e collettori di ugelli per scrubber** di deodorizzazione.
6. **Minuterie dei raschiatori** (distanziali, blocchi, punte raschia-schiume).
7. **Ricambi di lavaggio per filtri a dischi, a tela e a tamburo** (spray, pattini, guarnizioni).
8. **Ricambi per nastropresse e ispessitori.**
9. **Periferiche del dosaggio chimico** a bassa pressione (miscelatori statici, filtri di fondo).
10. **Interni per trattamento galvanico e acque industriali** (spruzzatori, miscelatori).
11. **Raccordi di ricambio per vecchie griglie di diffusori.**
12. **Pezzi per costruttori di impianti compatti** (MBBR/SBR italiani): serie piccole su disegno.

**Da provare in casa prima di dichiarare:**
- usura del SAF PP rispetto all'UHMW (spazzola e sabbia);
- creep di un pannello sotto battente;
- invecchiamento in ipoclorito;
- saldatura su PP-H;
- ripetibilità di filetti e fessure;
- svergolamento dei pannelli da 30 cm.
