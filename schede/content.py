"""Testi delle schede (IT). I testi sono quelli della rev. 00: qui cambia solo la grafica."""

CONTATTI = {
    "web": "duepigreco3d.it",
    "mail": "info@duepigreco3d.it",
    "tel": "+39 0423 715172",
    "sede": "Resana / Ponzano Veneto (TV)",
}

IN_PRODUZIONE = (
    "Per un costruttore di forni professionali produciamo in serie ricorrente cassetti e "
    "profili raccogligocce in PA2200: componenti a contatto con il prodotto, pareti da "
    "2,5 mm, riordinati in lotti piccoli, lotto tracciato. <strong>Non un prototipo: "
    "una fornitura.</strong>"
)

SCHEDE = [
    {
        "code": "ALI",
        "file": "DPG_Scheda_ALI_IT",
        "doc": "DPG-APP-ALI",
        "rev": "REV. 00 · BOZZA",
        "settore": "Macchine per caffè, vending e food equipment",
        "titolo": ["Condotti e imbuti a contatto", "alimentare, senza stampo"],
        "lead": (
            "Condotti latte, imbuti, convogliatori, cornici e meccanismi di erogazione in "
            "PA2200 sinterizzata con dichiarazione di conformità al contatto alimentare "
            "(Reg. UE 10/2011): serie da 100 a 1.000 pezzi l'anno con varianti frequenti, "
            "dove lo stampo non si ripaga e il restyling arriva prima dell'ammortamento."
        ),
        "kpi": [
            ("100–1.000", "", "pezzi l'anno, varianti frequenti"),
            ("EU 10/2011", "", "contatto alimentare dichiarato"),
            ("+80", "°C", "limite sotto carico della PA2200"),
        ],
        "tavola": "Gruppo erogazione con condotto latte, imbuto e cornice di scarico, tavola isometrica",
        "oggi": (
            "Il condotto latte oggi è tre stampati incollati o un tubo piegato con i suoi "
            "raccordi; l'imbuto ha uno stampo che si ripaga solo se il restyling aspetta. E ogni "
            "variante di macchina, per mercato o per cliente, riapre la discussione "
            "sull'attrezzatura."
        ),
        "additive": (
            "In sinterizzazione il condotto nasce in un pezzo solo, con il canale interno liscio "
            "e la curva che serve al flusso, non quella che permette lo sformo. La PA2200 ha "
            "dichiarazione EU 10/2011 e lavora fino a +80 °C sotto carico: via latte, imbuti e "
            "condotti del prodotto in polvere non cambiano materiale; sulla via caffè calda la "
            "temperatura di esercizio si verifica caso per caso."
        ),
        "vantaggi": [
            ("mono", "Canale interno liscio, in un pezzo",
             "Il condotto nasce intero: niente giunzioni dove il latte si ferma, niente "
             "incollaggi da sanificare, il percorso che serve al flusso.",
             ["monoblocco", "nessuna giunzione da sanificare"]),
            ("food", "Contatto alimentare dichiarato",
             "PA2200 con dichiarazione di conformità al Reg. UE 10/2011; la conformità del pezzo "
             "finito si dichiara per lotto, e la finitura si sceglie di conseguenza.",
             ["DPG-MAT-PA2200", "EU 10/2011"]),
            ("series", "Serie ponte e restyling",
             "Prima dello stampo, o al posto dello stampo: da 100 a 1.000 pezzi l'anno, con la "
             "variante per mercato che entra in produzione in giorni.",
             ["nessun riattrezzaggio", "revisioni in tempo reale"]),
            ("spare", "Ricambi per il parco installato",
             "Il condotto di una macchina fuori produzione si riordina dal file, identico: "
             "tracciabilità di lotto, nessuno scaffale.",
             ["magazzino digitale", "riordino identico"]),
        ],
        "materiali": [
            ("PA2200 (PA12)", "SLS", "contatto alimentare EU 10/2011, fino a +80 °C sotto carico, sterilizzabile", "", "DPG-MAT-PA2200"),
            ("Polipropilene", "SAF", "vie acqua e chimica di sanificazione; serie medie", "", "DPG-MAT-PP"),
            ("Nylon 12CF", "FDM", "staffe e supporti fuori dal contatto prodotto, rigidità estrema a peso minimo", "matrice", "DPG-CAT §01"),
        ],
        "rovescio": (
            "Sopra gli 80 °C sotto carico la PA12 non è la risposta: la via caffè calda e la "
            "caldaia restano dove sono, e ve lo diciamo prima. Sopra i volumi da stampo, torna lo "
            "stampo. E la superficie sinterizzata è opaca e leggermente porosa: dove serve una "
            "parete lucida e lavabile a vista, si finisce o si sceglie altro."
        ),
        "cta": "Mandateci lo STEP di un condotto.",
    },
    {
        "code": "CIL",
        "file": "DPG_Scheda_CIL_IT",
        "doc": "DPG-APP-CIL",
        "rev": "REV. 00 · BOZZA",
        "settore": "Etichettatrici, seminatrici, converting e automazione a vuoto",
        "titolo": ["Tamburi, rulli e rotori", "con i canali già dentro"],
        "lead": (
            "Tamburi a vuoto, rulli aspiranti, rotori di dosaggio e distributori pneumatici in "
            "PA12 sinterizzato: il corpo cilindrico nasce in un pezzo, con i condotti interni che "
            "seguono la funzione e non la punta del trapano. Da 1 a 50 pezzi, fino a 700 mm in "
            "un pezzo, senza fusione, senza foratura profonda, senza incollaggi."
        ),
        "kpi": [
            ("1–50", "pz", "per lotto, da file"),
            ("700", "mm", "in un pezzo, senza incollaggi"),
            ("⅓", "", "del peso dell'alluminio sull'albero"),
        ],
        "tavola": "Tamburo a vuoto con corona di canali, collettore rotante e rullo di dosaggio, tavola isometrica",
        "oggi": (
            "Oggi il tamburo a vuoto è un tornito con decine di fori radiali e canali assiali "
            "forati profondi, tappati e raccordati, oppure un assieme di dischi e distanziali che "
            "perde dove non deve. Ogni formato nuovo è un ciclo di officina, e il prototipo costa "
            "come la serie."
        ),
        "additive": (
            "In sinterizzazione il corpo nasce intero, con i canali della sezione che serve, i "
            "fori già nella geometria e il collettore integrato nella testa. La polvere esce dai "
            "canali passanti; il setto fra i canali si dimensiona per la tenuta, non per "
            "l'utensile."
        ),
        "vantaggi": [
            ("channels", "Canali interni di qualsiasi sezione",
             "Condotti rettangolari, curvi, a sezione variabile, che a foratura non esistono: la "
             "geometria segue il flusso d'aria e il corpo resta uno, senza tappi né raccordi.",
             ["monoblocco", "nessun tappo, nessun raccordo"]),
            ("size", "Fino a 700 mm in un pezzo",
             "La camera da 700 x 380 x 580 mm prende un rullo da 600 mm intero, sdraiato, con "
             "diametri fino a 370: il formato lungo non si spezza in tronchi da incollare.",
             ["camera 700 × 380 × 580", "pezzo unico"]),
            ("file", "Il formato è un file",
             "Il tamburo per il contenitore nuovo, il passo di semina diverso, il rullo per la "
             "banda più larga: una revisione, un lotto, nessun riattrezzaggio. Ricambio identico "
             "anche fra dieci anni.",
             ["da 1 a 50 pezzi", "riordino identico"]),
            ("weight", "Leggero sull'albero",
             "La poliammide pesa un terzo dell'alluminio e un ottavo dell'acciaio: meno inerzia "
             "sul tamburo che gira, cuscinetti meno caricati.",
             ["circa 1,0 g/cm³", "da −40 a +80 °C sotto carico"]),
        ],
        "materiali": [
            ("PA2200 (PA12)", "SLS", "tamburi, rulli, rotori: rigido, tenace, EU 10/2011, da −40 a +80 °C sotto carico", "", "DPG-MAT-PA2200"),
            ("Polipropilene", "SAF", "collettori a contatto con acqua e chimica di lavaggio", "", "DPG-MAT-PP"),
            ("Nylon 12CF", "FDM", "alberi e staffe: rigidità estrema a peso minimo", "matrice", "DPG-CAT §01"),
        ],
        "rovescio": (
            "La tenuta fra canali adiacenti dipende dal setto e dalla porosità residua del "
            "sinterizzato: sotto i 2 mm la verifichiamo sul prototipo, e dove serve si impregna. "
            "Diametri e teste si riprendono al tornio quando la tolleranza standard non basta. Il "
            "rullo che porta carichi alti resta in acciaio: ve lo diciamo sul disegno."
        ),
        "cta": "Mandateci lo STEP di un tamburo o di un rullo.",
    },
    {
        "code": "EOAT",
        "file": "DPG_Scheda_EOAT_IT",
        "doc": "DPG-APP-EOAT",
        "rev": "REV. 00 · BOZZA",
        "settore": "Automazione e macchine di assemblaggio",
        "titolo": ["Dita, nidi e pallet", "al costo di un file"],
        "lead": (
            "Dita di presa, nidi porta-pezzo, pallet, guide filo e fixture in PA12 sinterizzato: "
            "pezzi dedicati a ogni commessa, in lotti da 1 a 50, con canali del vuoto e sedi di "
            "sensore già nel corpo. Un terzo del peso dell'alluminio sul robot, e il ricambio "
            "identico per tutta la vita della macchina."
        ),
        "kpi": [
            ("1–50", "pz", "per lotto, dedicati alla commessa"),
            ("⅓", "", "del peso dell'alluminio sul robot"),
            ("4 → 1", "", "un pezzo al posto di quattro"),
        ],
        "tavola": "Pinza con dita di presa, nido porta-pezzo e pallet, tavola isometrica",
        "oggi": (
            "Ogni macchina custom porta decine di attrezzi dedicati: dita fresate dall'alluminio, "
            "nidi lavorati dal pieno in POM, pallet che nessuno vuole disegnare due volte. Il costo "
            "dell'attrezzaggio si nasconde nelle ore di officina e nel ritardo che sposta il "
            "collaudo."
        ),
        "additive": (
            "In sinterizzazione il dito, il nido e il pallet sono file con una revisione: il "
            "canale del vuoto passa dentro il corpo, la sede del sensore è già nella geometria, il "
            "peso sul polso del robot scende di due terzi. E il ricambio per la macchina venduta si "
            "riordina identico."
        ),
        "vantaggi": [
            ("channels", "Canali e funzioni nel corpo",
             "Vuoto, aria, sedi di sensore e riferimenti di centraggio integrati: un pezzo al "
             "posto di quattro, nessun raccordo esterno da spezzare.",
             ["monoblocco", "nessun assemblaggio"]),
            ("weight", "Peso sul robot",
             "La poliammide pesa un terzo dell'alluminio: meno inerzia, cicli più rapidi, robot "
             "più piccolo a parità di presa.",
             ["circa 1,0 g/cm³ contro 2,7"]),
            ("file", "Dedicato a ogni commessa, senza officina",
             "Il set attrezzi della commessa entra in un lotto solo, con le revisioni che il "
             "collaudo richiede: la modifica è un file, non un'altra settimana di fresa.",
             ["revisioni in giorni", "nessun riattrezzaggio"]),
            ("spare", "Ricambi per tutta la vita macchina",
             "Dita e nidi consumati si riordinano identici dal file: tracciabilità di lotto, "
             "nessuno scaffale.",
             ["magazzino digitale", "riordino identico"]),
        ],
        "materiali": [
            ("PA2200 (PA12)", "SLS", "dita, nidi, pallet: rigidità, tenacità, da −40 a +80 °C sotto carico", "", "DPG-MAT-PA2200"),
            ("Nylon 12CF", "FDM", "bracci e staffe di EOAT dove serve rigidità estrema a peso minimo", "matrice", "DPG-CAT §01"),
            ("TPU 90A", "SLS", "interfacce di presa cedevoli e antiscivolo; contatto pelle, non prodotto", "matrice", "DPG-CAT §01"),
        ],
        "rovescio": (
            "Le dita che stringono con forze alte e i pallet che portano carichi restano in "
            "alluminio: la PA12 non sostituisce il metallo dove serve rigidità strutturale, e ve lo "
            "diciamo sul disegno. Sotto la scala delle macchine da tavolo, il pezzo ve lo fate in "
            "casa e fate bene."
        ),
        "cta": "Mandateci lo STEP di una pinza o di un nido.",
    },
    {
        "code": "FMT",
        "file": "DPG_Scheda_FMT_IT",
        "doc": "DPG-APP-FMT",
        "rev": "REV. 00 · BOZZA",
        "settore": "Cambio formato per macchine di confezionamento, riempimento ed etichettatura",
        "titolo": ["Un set formato per ogni cliente,", "senza fresare il POM"],
        "lead": (
            "Stelle, coclee, tazze, piastre e guide di formato in PA12 sinterizzato: un file per "
            "ogni flacone, bottiglia o vaschetta del cliente, prodotto alla firma dell'ordine, da 1 "
            "a 50 set. Nessuno stampo, nessuna fresatura dal pieno, e il ricambio identico anche "
            "fra vent'anni."
        ),
        "kpi": [
            ("1–50", "set", "prodotti alla firma dell'ordine"),
            ("1", "file", "per ogni flacone del cliente"),
            ("20", "anni", "e il ricambio è ancora identico"),
        ],
        "tavola": "Set di cambio formato: stella, coclea, guide e piastra, tavola isometrica",
        "oggi": (
            "Il set formato oggi nasce fresato dal pieno in POM o PA6: ore macchina per ogni "
            "stella, una coclea che è un lavoro a sé, e a ogni nuovo flacone del cliente si "
            "ricomincia. Sul parco installato il ricambio dipende da un disegno che qualcuno deve "
            "ritrovare e da un'officina che deve avere tempo."
        ),
        "additive": (
            "In sinterizzazione la stella, la coclea e la piastra sono tre file: si producono "
            "insieme, nello stesso lotto, con tasche e alleggerimenti già nella geometria. La "
            "coclea a passo variabile, che a fresa è la parte cara, qui costa quanto una dritta."
        ),
        "vantaggi": [
            ("series", "Il set completo in un lotto solo",
             "Stella, coclea, tazze e guide dello stesso formato entrano insieme in macchina: un "
             "ordine, un lotto, un numero di revisione.",
             ["un file per ogni formato", "nessun riattrezzaggio"]),
            ("channels", "La geometria che a fresa non esce",
             "Coclee a passo variabile, tasche di alleggerimento, canali di soffiaggio e sedi di "
             "sensore integrate nel corpo: nessun vincolo di utensile.",
             ["passo variabile e cavità interne senza sovrapprezzo"]),
            ("spare", "Ricambi a magazzino digitale",
             "Il formato del cliente resta un file con la sua revisione: si riordina identico "
             "quando serve, anche per una macchina venduta vent'anni fa.",
             ["tracciabilità di lotto", "riordino identico"]),
            ("food", "Contatto alimentare, quando serve",
             "La PA2200 ha dichiarazione di conformità al contatto alimentare (Reg. UE 10/2011) e "
             "lavora da −40 a +80 °C sotto carico: stelle e guide sulla linea food, senza "
             "cambiare materiale.",
             ["DPG-MAT-PA2200", "EU 10/2011"]),
        ],
        "materiali": [
            ("PA2200 (PA12)", "SLS", "il materiale del formato: rigido, tenace, contatto alimentare, da −40 a +80 °C sotto carico", "", "DPG-MAT-PA2200"),
            ("Nylon 12CF", "FDM", "guide lunghe e piastre dove serve rigidità estrema a peso minimo", "matrice", "DPG-CAT §01"),
            ("TPU 90A", "SLS", "inserti cedevoli di stella e tazza per il contenitore delicato; contatto pelle, non prodotto", "matrice", "DPG-CAT §01"),
        ],
        "rovescio": (
            "Sopra i volumi da stampo, torna lo stampo, e vi aiutiamo a fare il passaggio. Le "
            "stelle che lavorano sul vetro ad alta cadenza vanno provate sul vostro banco prima di "
            "sostituire il POM: l'usura della PA12 si valuta sul pezzo, non a catalogo. E "
            "l'alluminio resta alluminio dove serve rigidità di macchina."
        ),
        "cta": "Mandateci lo STEP di un set formato.",
    },
]

KIT = {
    "file": "DPG_Kit_Campioni_IT",
    "doc": "DPG-KIT-CAMPIONI",
    "rev": "REV. 01 · 25.08.2026",
    "lead": (
        "Undici piastrine, una per materiale. Su ognuna il nome è inciso nel pezzo, non su "
        "un'etichetta: fra tre settimane si sa ancora cosa si sta toccando."
    ),
    "piastrina": [
        ("Pettine di perni", "Diametri calanti. Dice fino a dove il processo tiene un dettaglio pieno e in rilievo."),
        ("Pettine di fori", "Diametri calanti. Dice fino a dove un foro resta davvero aperto e pulito."),
        ("Scala di pareti", "Spessori calanti. La parete minima reale su questo materiale, non quella di catalogo."),
        ("Linguetta a sbalzo", "Si piega fra le dita. Rigidità e tenacia si sentono, non si leggono in tabella."),
    ],
    "come_si_legge": (
        "Le piastrine servono a scegliere il materiale, non a stimare le tolleranze del vostro "
        "pezzo: quelle dipendono dalla geometria e si valutano sul file. Se avete il 3D la fascia "
        "di prezzo esce in un minuto; se avete solo il pezzo in mano bastano misure e peso."
    ),
    # (processo, materiale, densità, circa, quando si usa, da tenere presente, dichiarazioni, dichiarazione presente)
    "materiali": [
        ("SLS", "PA2200", 0.95, False,
         "Il cavallo di battaglia: pezzi funzionali senza stampo, pareti sottili, geometrie chiuse. Bianco da macchina.",
         "Sopra 80 °C sotto carico esce dal suo inviluppo.",
         "Biocompatibile ISO 10993-1 e USP Classe VI, sterilizzabile. Contatto alimentare EU 10/2011.", True),
        ("SLS", "PA12 caricato vetro", 1.15, True,
         "Quando serve più rigidità e stabilità dimensionale della PA2200, e il pezzo lavora un po' più caldo.",
         "Più rigido vuol dire meno tenace: sugli urti si comporta peggio della PA2200.",
         "Scheda tecnica su richiesta.", False),
        ("SLS", "TPU 90A", 1.20, False,
         "Elastomerico: guarnizioni, smorzatori, prese, tutto quello che deve piegarsi e tornare.",
         "Sopra 70 °C non è più il materiale giusto.",
         "Contatto pelle ISO 10993-5, -23, -10. Non per contatto con prodotto o farmaco.", True),
        ("SAF", "PP polipropilene", 1.02, False,
         "Resistenza chimica, cerniere viventi, ambienti bagnati. È anche il più economico al centimetro cubo che abbiamo.",
         "UL94 HB, quindi mai dove ci sono requisiti al fuoco. Sopra 90 °C si esce dall'inviluppo.",
         "Conformità alimentare da chiedere come dichiarazione del grado di polvere.", False),
        ("FDM", "ABS-M30", 1.04, False,
         "Tecnico generalista, buon rapporto fra prezzo e prestazioni. Attrezzature, mascherine, prototipi funzionali.",
         "Non stabile ai raggi UV: all'aperto ingiallisce e si infragilisce.",
         "Scheda tecnica su richiesta.", False),
        ("FDM", "ASA", 1.07, True,
         "Come l'ABS ma sta fuori: stabile ai raggi UV, per componenti esposti.",
         "Prestazioni meccaniche simili all'ABS, non superiori.",
         "Scheda tecnica su richiesta.", False),
        ("FDM", "Policarbonato", 1.20, True,
         "Rigido e tenace insieme, buona stabilità dimensionale. Quando l'ABS non basta.",
         "Assorbe umidità: conservazione e essiccazione contano.",
         "Scheda tecnica su richiesta.", False),
        ("FDM", "ULTEM 9085", 1.34, False,
         "Il materiale che le stampanti economiche non fanno. Alta temperatura, certificato al fuoco a livello di materiale, tiene il ciclo in autoclave.",
         "La qualifica sul componente si definisce insieme: la certificazione è del materiale, non del pezzo.",
         "Certificazione al fuoco a livello di materiale. Ferroviario e aeronautico su specifica.", True),
        ("FDM", "ULTEM 1010 CG", 1.27, False,
         "Il grado CG dell'Ultem: stesse doti termiche più la dichiarazione per il contatto alimentare. Autoclavabile.",
         "La dichiarazione NSF 51 riguarda il contatto alimentare. Per uso medicale il percorso è un altro e si definisce caso per caso.",
         "Dichiarazione NSF 51 per contatto alimentare (grado CG, non il 1010 base).", True),
        ("FDM", "Nylon 12CF", 1.15, False,
         "Caricato carbonio: molto rigido e leggero. Dime, attrezzature, staffe che devono pesare poco.",
         "La fibra lo rende rigido ma fragile agli urti concentrati.",
         "Scheda tecnica su richiesta.", False),
        ("FDM", "Nylon 12", 1.01, False,
         "Tenace e resistente a fatica, buona resistenza chimica. Dove serve che pieghi senza rompersi.",
         "Assorbe umidità come tutti i nylon.",
         "Scheda tecnica su richiesta.", False),
    ],
}
