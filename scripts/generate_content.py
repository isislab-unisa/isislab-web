"""Generate curated Italian Jekyll pages, based on public ISISLab descriptions.
The content is intentionally concise; see each `source_url` for full primary material.
"""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]

PAGES={
'chi-siamo':('Chi siamo','Il laboratorio','Persone, storia e ricerca del laboratorio ISISLab all’Università degli Studi di Salerno.',r'''
## La ricerca

ISISLab è un laboratorio del **Dipartimento di Informatica dell’Università degli Studi di Salerno**, attivo dal **1995**. Le sue attività si sviluppano attorno a calcolo distribuito e parallelo, collaborazione e sistemi sociali, visualizzazione e interazione.

L’esperienza del gruppo comprende più di venti progetti di ricerca nazionali ed europei. Tra questi, il progetto Horizon 2020 **ROUTE-TO-PA**, collegato alla piattaforma collaborativa open-source **SPOD** per i dati aperti.

- [Esplora le linee di ricerca](/tematiche/)
- [Scopri i progetti](/progetti/)
- [Vedi le pubblicazioni](/pubblicazioni-scientifiche/)

## Il gruppo di ricerca {#persone}

### Docenti

Vittorio Scarano · Delfina Malandrino · Gennaro Cordasco · Biagio Cosenza · Carmine Spagnuolo · Maria Angela Pellegrino.

### Dottorandi

Valerio Di Pasquale · Sana Latif · Babar Hussain · Tiziano Citro · Saleh Jamali Golzar · Antonio De Caro · Gabriele Tuozzo.

### Assegnisti e borsisti

Fra i collaboratori elencati sul sito originale: Daniele De Vinco, Daniele Monaco, Lorenzo Carpentieri, Giuseppina Palmieri, Sarah Pellone, Andrea Amorosini, Marianna Ambrosino, Vanja Annunziata, Alberto Accardo e Giusy Gonnella.

Le affiliazioni cambiano nel tempo: per il roster aggiornato consulta la [pagina ufficiale del gruppo](https://www.isislab.it/chi-siamo/).

## Il laboratorio a Fisciano

La sede si trova nell’**Edificio F, Stecca 7, Laboratorio 10, secondo piano**, al campus universitario di Fisciano. [Indicazioni per raggiungerci](/come-raggiungerci/).
'''),
'dicono-di-noi':('Dicono di noi','Il laboratorio','Riconoscimenti e menzioni dei risultati di ricerca di ISISLab.',r'''
## Riconoscimenti: ROUTE-TO-PA

Il progetto europeo **ROUTE-TO-PA** è stato selezionato per l’**Innovation Radar** della Commissione europea, uno strumento per individuare innovazioni nate da progetti finanziati dall’Unione.

I risultati segnalati comprendono una piattaforma sociale per utilizzare e creare open data con il contributo di cittadini e amministrazioni e **SilverDecisions**, un software basato su browser per costruire e analizzare alberi decisionali.

Le schede dell’Innovation Radar sono consultabili alle pagine [Open Data](https://www.innoradar.eu/innovation/29873) e [SilverDecisions](https://www.innoradar.eu/innovation/29875).

## Approfondimenti

I riconoscimenti collegano ricerca applicata, strumenti open-source e innovazione nella partecipazione pubblica. Per informazioni sulla ricerca: [Calcolo collaborativo e sociale](/tematiche/#collaborative-and-social-calculation).
'''),
'rassegna-stampa':('Rassegna stampa','Il laboratorio','Articoli e segnalazioni pubbliche sulle attività del laboratorio.',r'''
## ISISLab sui media

Questa sezione raccoglie i punti di accesso alla comunicazione e alla visibilità pubblica del laboratorio: iniziative con università, territorio, industria e partner internazionali.

Per consultare una raccolta completa di articoli, link e materiali editoriali, fare riferimento alla [rassegna stampa originale](https://www.isislab.it/rassegna-stampa/).

## Percorsi correlati

- [Dicono di noi](/dicono-di-noi/) — il riconoscimento dei risultati ROUTE-TO-PA.
- [Public engagement](/public-engagement/) — coding, Open Science e partecipazione.
- [News](/news/) — aggiornamenti e iniziative del laboratorio.
'''),
'come-raggiungerci':('Come raggiungerci','Il laboratorio','Dove si trova il laboratorio e come arrivare al campus di Fisciano.',r'''
## Dove siamo

**ISISLab · Dipartimento di Informatica · Università di Salerno**  
Edificio F, Stecca 7, Laboratorio 10, **II piano**  
Via Giovanni Paolo II, 132 · 84084 Fisciano (SA)

[Apri la mappa su OpenStreetMap](https://www.openstreetmap.org/search?query=Universit%C3%A0%20di%20Salerno%20Fisciano)

## In auto

### Da Napoli

Le indicazioni pubblicate da ISISLab suggeriscono l’**A30** in direzione Salerno, quindi il raccordo per Avellino e l’uscita **Fisciano**. Seguire l’ingresso del campus e cercare l’Edificio F.

### Da Salerno

Seguire l’autostrada verso Avellino e scegliere l’uscita **Fisciano**. La pagina originale segnala che l’uscita denominata “Università” porta sul lato opposto del campus rispetto al laboratorio.

### Da Avellino

Procedere in direzione Salerno, uscire a **Fisciano** e seguire le indicazioni per l’università.

## All’interno del campus

ISISLab si trova nell’Edificio F, al secondo piano: dall’atrio con scale e ascensore raggiungere il piano indicato e imboccare il corridoio a sinistra. Consultare la [guida fotografica originale](https://www.isislab.it/come-raggiungerci/) per il percorso puntuale.
'''),
'tematiche':('Tematiche di ricerca','Ricerca','Tre direttrici scientifiche: calcolo scalabile, collaborazione e interazione.',r'''
## Computazioni distribuite e parallele {#distributed-and-parallel-computations}

Questa linea studia l’esecuzione di applicazioni su più nodi cooperanti, con particolare attenzione alle prestazioni, alla scalabilità e alle architetture software e hardware.

- **Cloud ed Edge Computing:** infrastrutture e sistemi di esecuzione efficienti.
- **Simulazioni massive:** simulazioni multi-agente con ambienti distribuiti come **D-MASON**.
- **Algoritmi e architetture parallele:** problemi di routing, reti peer-to-peer e metodi per sfruttare più unità di calcolo.

## Calcolo collaborativo e sociale {#collaborative-and-social-calculation}

La ricerca si concentra su sistemi che permettono alle persone di lavorare insieme, condividere dati e coordinare attività, anche in contesti distanti o simultanei.

- **Open Data co-creation:** creazione partecipata e visualizzazione di dati, anche attraverso la piattaforma SPOD.
- **Progettazione e collaborazione sincrona:** groupware e strumenti per processi condivisi, inclusi contesti didattici.
- **Privacy e personalizzazione:** protezione delle informazioni e interfacce adattive.

## Visualizzazione e interazione {#visualization-and-interaction}

L’area affronta il rapporto fra dati, esperienza e modalità di interazione.

- **Visualizzazione scalabile:** componenti interattivi per dati complessi.
- **Realtà virtuale e XR:** ambienti immersivi e applicazioni per il patrimonio culturale.
- **Interfacce innovative:** strumenti grafici e sonori, serious games e tecniche di rendering.

## Dalla ricerca ai progetti

Le tre linee confluiscono in iniziative come [ROUTE-TO-PA, SERMAS, LIGATE e XRTourGuide](/progetti/). Per dettagli metodologici e classificazioni ACM consulta l’articolazione completa della pagina sorgente.
'''),
'pubblicazioni-scientifiche':('Pubblicazioni scientifiche','Ricerca','Output e riferimenti della produzione scientifica del gruppo di ricerca ISISLab.',r'''
## Produzione scientifica

Il laboratorio pubblica risultati su sistemi distribuiti e paralleli, tecnologie cloud ed edge, calcolo collaborativo, open data, privacy, visualizzazione e ambienti immersivi.

Tra i contributi citati nella comunicazione del laboratorio compare **“Hypergraph Motifs Representation Learning”**, presentato a **KDD 2025** da A. Antelmi, G. Cordasco, D. De Vinco, V. Di Pasquale, M. Polato e C. Spagnuolo.

## Dove trovare gli articoli

Le bibliografie aggiornate e i riferimenti completi si consultano sul [sito scientifico del laboratorio](https://www.isislab.it/pubblicazioni-scientifiche/). Sono utili anche [DBLP](https://dblp.org/), [ACM Digital Library](https://dl.acm.org/) e [Google Scholar](https://scholar.google.com/).

## Risorse per scrivere e valutare

Visita le pagine [Risorse utili](/risorse-utili/) e [Systematic Literature Reviews](/systematic-literature-reviews/) per bibliometria, lettura critica e strumenti bibliografici.
'''),
'risorse-utili':('Risorse utili','Ricerca','Strumenti di supporto alla ricerca, bibliometria, letteratura e pubblicazioni.',r'''
## Indicatori bibliometrici

Quando si sceglie una sede di pubblicazione è utile valutarne anzitutto l’aderenza scientifica e poi considerare metriche e repertori complementari.

- [SCImago Journal & Country Rank](https://www.scimagojr.com/) — indicatori relativi a riviste scientifiche.
- [Scopus](https://www.scopus.com/) — pubblicazioni, autori, citazioni e CiteScore.
- [Web of Science](https://www.webofscience.com/) — riferimenti e citazioni.
- [Google Scholar](https://scholar.google.com/) — panoramica sulla produzione dei ricercatori.
- [GRIN](https://www.grin-informatica.it/) — iniziative della comunità informatica italiana.

## Ricerca e documentazione

Le collezioni [ACM Digital Library](https://dl.acm.org/), [IEEE Xplore](https://ieeexplore.ieee.org/), [DBLP](https://dblp.org/) e [arXiv](https://arxiv.org/) offrono diversi strumenti per seguire lo stato dell’arte.

## Materiale per review sistematiche

La sezione [Systematic Literature Reviews](/systematic-literature-reviews/) raccoglie risorse per pianificazione, ricerca, selezione e analisi delle fonti.
'''),
'systematic-literature-reviews':('Systematic Literature Reviews','Risorse','Una guida alle revisioni sistematiche della letteratura e agli strumenti utili.',r'''
## Principi, metodi e strumenti

Questa raccolta nasce dai due seminari di Vittorio Scarano dedicati alle **Systematic Literature Reviews**, svolti il **14 gennaio 2020** per gli studenti di dottorato in Informatica.

Le SLR prevedono una domanda di ricerca definita, criteri espliciti per la selezione degli studi, una strategia di ricerca replicabile e una sintesi trasparente delle evidenze.

## Letture consigliate

- **Barbara Kitchenham** — *Procedures for Performing Systematic Reviews* (2004).
- **Kitchenham e collaboratori** — *Systematic literature reviews in software engineering* (2009).
- **Anders Kofod-Petersen** — guida a una structured literature review in computer science.

## Strumenti

- [Zotero](https://www.zotero.org/) e [JabRef](https://www.jabref.org/) per la gestione delle fonti.
- [ACM Digital Library](https://dl.acm.org/), [IEEE Xplore](https://ieeexplore.ieee.org/) e [ScienceDirect](https://www.sciencedirect.com/) per le ricerche bibliografiche.
- [LaTeX](https://www.latex-project.org/) e BibTeX per la stesura.

La pagina originale contiene l’elenco più ampio di riferimenti, esempi, tutorial e collegamenti alle slide dei seminari.
'''),
'progetti':('Progetti','Progetti','Progetti italiani, europei e internazionali tra calcolo, XR, open data, beni culturali e cybersecurity.',r'''
## Progetti recenti

### XRTwinScape

Formazione per l’industria con **digital twin** degli spazi reali, ambienti XR immersivi e ricostruzione ad alta fedeltà tramite Gaussian Splatting. Periodo indicato: aprile 2025 – marzo 2026.

### CROMO

Piattaforma partecipativa per monitorare beni culturali diffusi attraverso fotografie e analisi basata sull’intelligenza artificiale. Nel partenariato CHANGES, ottobre 2024 – novembre 2025. [Sito del progetto](https://www.progettocromo.it/).

### FUTURAL — XRTourGuide

Sperimentazione di esperienze immersive per l’esplorazione del territorio rurale, nell’ambito di Horizon Europe FUTURAL. Giugno 2025 – giugno 2026.

### NEOLAiA

Alleanza universitaria europea orientata a mobilità, inclusione, collaborazione scientifica e trasformazione digitale. [Portale ufficiale](https://neolaiacampus.eu/).

### LibreRT

Ricerca su sistemi embedded, programmazione eterogenea e requisiti real-time lungo il computing continuum. [Sito di progetto](https://librert.di.unisa.it/).

## Altri progetti e collaborazioni

- **CS-AWARE-NEXT:** gestione collaborativa della cybersecurity.
- **SERMAS:** modelli e sistemi XR socialmente accettabili.
- **LIGATE:** supercalcolo e progettazione computazionale di farmaci.
- **COLTRANE:** educazione collaborativa alla consapevolezza sulla sicurezza informatica.
- **ROUTE-TO-PA:** partecipazione civica e Open Data, con piattaforma SPOD.
- **PAUN, VASARI e SNECS:** nuove tecnologie per la valorizzazione del patrimonio culturale.
- **LEAD e CoFFEE:** strumenti digitali per la collaborazione nell’apprendimento.

Ulteriori iniziative storiche, finanziamenti, consorzi e durate sono documentati nell’elenco originale dei progetti.
'''),
'progetti-con-le-scuole':('Progetti con le scuole','Progetti','Attività scientifiche, formative e di collaborazione con il mondo della scuola.',r'''
## Università e scuola

ISISLab esplora la collaborazione digitale anche nei contesti educativi: strumenti per la discussione, lavori di gruppo, co-creazione e modalità partecipative di apprendimento.

Il progetto europeo **LEAD** ha affrontato l’apprendimento basato sulla discussione e sulla soluzione collaborativa di problemi; da questa ricerca è nato **CoFFEE** (*Cooperative Face-to-Face Educational Environment*).

## Incontri e iniziative

Gli interventi pubblici e i progetti con le scuole si collegano anche alle attività di [Public engagement](/public-engagement/), come Coding Girls e appuntamenti di divulgazione sul digitale.

Per l’elenco documentale e le iniziative locali consulta la [pagina originale dedicata alle scuole](https://www.isislab.it/progetti-con-le-scuole/).
'''),
'public-engagement':('Public engagement','Impatto sociale','Iniziative di comunicazione scientifica, coding, open data e partecipazione sul territorio.',r'''
## Il laboratorio e la comunità

ISISLab porta la ricerca sul digitale fuori dall’università attraverso incontri, hackathon e attività con scuole, associazioni e comunità territoriali.

### Coding Girls a DInfUniSa — 14 novembre 2019

Una tappa del programma nazionale **Coding Girls** ha portato al Dipartimento di Informatica un hackathon con circa 200 studentesse, dedicato all’avvicinamento delle ragazze alla programmazione.

### Open Science e Open Data — 25 marzo 2019

Vittorio Scarano ha presentato Open Data e Open Science in un incontro interattivo della **ALL DIGITAL Week**, con l’associazione Mind the Gaps e Vivarium – Digital Humanities.

### Knowledge loves Wikipedia — 26 marzo 2019

Un’attività di condivisione e produzione collaborativa della conoscenza, con Wikimedia Italia e partner locali.

### Art+Feminism — 8 marzo 2019

Un appuntamento di scrittura collaborativa dedicato a una maggiore rappresentazione delle donne e dei loro contributi alla conoscenza.

## Scopri di più

Le attività uniscono inclusione, cultura digitale, cittadinanza e partecipazione: [Progetti con le scuole](/progetti-con-le-scuole/) e [News](/news/).
'''),
'lauree-triennale-e-magistrale':('Lauree triennale e magistrale','Didattica','Corsi e opportunità formative collegate alle aree di ricerca del laboratorio.',r'''
## Didattica e ricerca

Le attività di ISISLab si inseriscono nell’ecosistema didattico del **Dipartimento di Informatica dell’Università di Salerno**. Gli interessi scientifici del gruppo attraversano infrastrutture distribuite, calcolo parallelo, collaborazione, dati aperti e sistemi immersivi.

## Orientarsi

Per programmi ufficiali, piani di studio e calendario degli insegnamenti visita il [Dipartimento di Informatica](https://www.di.unisa.it/) e la pagina originale dedicata ai corsi.

## Approfondimenti per studenti

- [Indirizzo Cloud Computing](/indirizzo-cloud-computing/)
- [Informazioni per tesi e tirocini](/informazioni-utili/)
- [Seminari](/events/list/)
- [Erasmus ed Erasmus+](/erasmus/)
'''),
'indirizzo-cloud-computing':('Indirizzo Cloud Computing','Didattica','Un percorso introduttivo alle tematiche cloud ed edge del laboratorio.',r'''
## Cloud e Edge Computing

Tra gli ambiti principali di ricerca di ISISLab figurano il calcolo in cloud, l’edge computing, le architetture parallele e la distribuzione di applicazioni e dati su più nodi.

Gli insegnamenti, i requisiti e l’eventuale disponibilità di uno specifico indirizzo didattico vanno sempre verificati sulle [pagine ufficiali del Dipartimento di Informatica](https://www.di.unisa.it/).

## Risorse collegate

Per un’introduzione ai problemi di prestazioni, scalabilità e simulazione, consulta la [linea di ricerca distribuita e parallela](/tematiche/#distributed-and-parallel-computations) e i [progetti](/progetti/).
'''),
'informazioni-utili':('Informazioni utili','Didattica','Indicazioni per chi vuole avviare un tirocinio o svolgere la tesi in ISISLab.',r'''
## Tesi e tirocini in laboratorio

ISISLab valorizza il **confronto continuo** tra studenti e ricercatori. Durante il lavoro di tesi si partecipa ai seminari e si discutono regolarmente obiettivi, approcci e risultati.

## Da dove iniziare

1. Concorda l’argomento e il referente del tuo lavoro.
2. Consulta i materiali e le procedure proposte nelle risorse del laboratorio.
3. Segui i seminari per conoscere le altre attività del gruppo.
4. Organizza la documentazione e aggiornamenti periodici per il tuo progetto.

## Pagine per studenti

- [Cosa si fa in ISISLab durante stage e tesi](/cosa-si-fa-in-isislab-stage-o-tesi/)
- [Sono un nuovo tesista: cosa devo fare?](/sono-un-nuovo-tesista-cosa-devo-fare/)
- [FAQ seminari](/faq-seminari/)
- [Modelli per tesi e seminari](/modelli-per-tesi-e-seminari/)
- [Risorse per gli studenti](/risorse-per-gli-studenti/)
'''),
'cosa-si-fa-in-isislab-stage-o-tesi':('Cosa si fa in ISISLab: stage o tesi','Didattica','Come si lavora a un progetto di stage o tesi all’interno del gruppo.',r'''
## Un percorso di ricerca condiviso

Il lavoro in ISISLab è parte della vita del gruppo: progettazione, sperimentazione, confronto con il proprio referente e presentazione pubblica delle tappe raggiunte.

I seminari aiutano a spiegare le scelte tecniche, raccogliere osservazioni e migliorare la capacità di comunicare il proprio lavoro. Il percorso è collegato alle aree di [ricerca](/tematiche/) e ai [progetti](/progetti/) del laboratorio.

## Strumenti e informazioni

Prima dell’avvio, consulta le [risorse per gli studenti](/risorse-per-gli-studenti/). Per gli aspetti pratici e organizzativi sono disponibili anche la [guida al nuovo tesista](/sono-un-nuovo-tesista-cosa-devo-fare/) e le [FAQ seminari](/faq-seminari/).
'''),
'faq-seminari':('FAQ Seminari','Studenti','Domande frequenti sulle presentazioni e sui seminari del laboratorio.',r'''
## Di cosa si parla?

Del lavoro in corso, di una lettura interessante o di un tema stimolante legato all’informatica. I seminari possono riguardare tecnologie, metodi, risultati ed esperimenti.

## Chi può partecipare?

La partecipazione non è riservata esclusivamente ai tesisti ISISLab: i seminari sono aperti a chi sia interessato e desideri seguire le attività scientifiche del gruppo.

## Chi prepara una tesi deve presentare seminari?

Sì. La pagina originale descrive solitamente **due o tre seminari** per tesista: introduzione al problema, impostazione della soluzione e presentazione dei risultati finali.

## A cosa servono?

Ad allenarsi nell’esposizione e nel confronto scientifico, ricevere suggerimenti e prepararsi a comunicare efficacemente un progetto in ambito accademico o professionale.

## Come prepararsi?

Organizza contenuti chiari, prepara la parte dimostrativa e consulta le [risorse per i nuovi tesisti](/sono-un-nuovo-tesista-cosa-devo-fare/). La presentazione breve per la seduta di laurea richiede un formato differente da quello dei seminari estesi.
'''),
'convenzioni-e-contratti-di-ricerca':('Convenzioni e contratti di ricerca','Enti esterni','Collaborazioni di ricerca con pubbliche amministrazioni, istituzioni e imprese.',r'''
## Ricerca per il territorio

Le attività di ISISLab coinvolgono enti pubblici e privati, con progetti di innovazione digitale e trasferimento di risultati scientifici.

### Analisi di fonti aperte

Collaborazione con il **Consiglio Regionale della Campania** su piattaforme e metodologie per analizzare informazioni provenienti da fonti aperte, all’interno di un accordo quadro del periodo 2017–2019.

### Borgo Accessibile

Iniziativa con il **Comune di Monteverde (AV)** rivolta alla fruizione collaborativa del castello attraverso esperienze di realtà virtuale (2018).

### Laviano Restituita

Ricostruzione virtuale dell’abitato di Laviano precedente al terremoto del 1980, con il **Comune di Laviano (SA)**.

## Collaborare con ISISLab

Per i dettagli sui contratti, sulle iniziative industriali e sulle opportunità istituzionali consulta la [pagina originale delle convenzioni](https://www.isislab.it/convenzioni-e-contratti-di-ricerca/) e [i progetti di ricerca](/progetti/).
'''),
'dottorato-di-ricerca-industriale':('Dottorato di ricerca industriale','Enti esterni','Il collegamento fra ricerca accademica e innovazione d’impresa.',r'''
## Ricerca e industria

Il modello del dottorato industriale valorizza la collaborazione fra gruppi scientifici e organizzazioni esterne, in relazione a problemi tecnologici e applicativi.

Tra i campi in cui ISISLab ha maturato esperienza rientrano cloud/edge computing, simulazioni, interazione immersiva e collaborazione digitale.

La disponibilità e i requisiti di specifiche posizioni vanno verificati presso l’[Università di Salerno](https://www.unisa.it/) e attraverso gli avvisi ufficiali. Per il contesto di collaborazione consulta le [Convenzioni e contratti di ricerca](/convenzioni-e-contratti-di-ricerca/).
'''),
'collaborazioni-con-enti-stranieri':('Collaborazioni con enti stranieri','Enti esterni','Collaborazioni internazionali e progetti di ricerca europei.',r'''
## Una rete internazionale

ISISLab ha partecipato a progetti di ricerca europei insieme a università, enti pubblici, centri di ricerca e realtà industriali.

- **ROUTE-TO-PA:** collaborazione europea sugli Open Data e sulla trasparenza della pubblica amministrazione.
- **SERMAS:** consorzio Horizon Europe per sistemi Extended Reality.
- **COLTRANE:** partenariato Erasmus+ dedicato alla didattica della cybersecurity.
- **NEOLAiA:** alleanza universitaria europea per la collaborazione istituzionale e la ricerca.

Per ulteriori attività di mobilità consulta [Erasmus / Erasmus+](/erasmus/).
'''),
'news':('News','Aggiornamenti','Attività, eventi e progetti raccontati dal laboratorio.',r'''
## Ultime notizie

### 19 maggio 2026 — XRTourGuide al Museo di Morigerati

Il 9 maggio 2026 si è svolta una sperimentazione di **XRTourGuide** presso il Museo Etnografico di Morigerati: un incontro fra tecnologia digitale, cultura e territorio.

### 7 maggio 2026 — Open Day Data Center, Regione Campania

La seconda edizione dell’Open Day Data Center, organizzata in collaborazione con il Dipartimento di Informatica, si è svolta il 5 maggio 2026.

### 17 aprile 2026 — Geckode Hackathon 2026

Il 16 e 17 aprile l’Università degli Studi di Salerno ha ospitato un hackathon su **XR, innovazione e metaverso NEOLAiA**, con UNISA e partner.

## Notizie, seminari e blog

Questi sono alcuni aggiornamenti riportati sulla pagina pubblica di ISISLab; non si tratta di un feed live. Per news più recenti, foto e comunicati consulta l’[archivio ufficiale](https://www.isislab.it/news/). Esplora anche i [seminari](/events/list/) e il [blog](/blog/).
'''),
'erasmus':('Erasmus / Erasmus+','Didattica','Mobilità internazionale, studio e tirocini all’estero.',r'''
## Convenzioni Erasmus — studio e tesi

La pagina ufficiale ISISLab elenca fra le istituzioni collegate alla mobilità **Universität Innsbruck**, **University of Brighton**, **University of Skövde** e **Warsaw School of Economics**.

## Erasmus+ — tirocini esterni

Fra gli enti indicati figurano **AirborneHydroMapping** e **ClockStone** a Innsbruck, **ServiceNow** nel Regno Unito, **Teesside University**, **Everis** e **Fraunhofer FIT**.

L’elenco rappresenta le convenzioni segnalate sul sito del laboratorio, non una conferma di posti attualmente disponibili. Contatta l’università per bandi, requisiti, scadenze e accordi attivi.
'''),
'sono-un-nuovo-tesista-cosa-devo-fare':('Sono un nuovo tesista: cosa devo fare?','Studenti','Prime indicazioni operative per iniziare il lavoro in laboratorio.',r'''
## All’inizio dello stage o della tesi

Secondo le indicazioni pubblicate da ISISLab, è utile coordinarsi con il referente per gli account necessari, gli strumenti di lavoro e l’iscrizione alla mailing list del gruppo.

## Organizzare l’attività

- Mantieni aggiornato il materiale relativo alla tua tesi o al tirocinio.
- Segui gli avvisi sulla mailing list e gli appuntamenti di laboratorio.
- Confrontati con il referente sui progressi e sulle difficoltà.
- Prima dei seminari condividi data, titolo e breve abstract con gli organizzatori.

## I seminari e la seduta di laurea

Il lavoro può prevedere seminari intermedi e una presentazione conclusiva. Per la seduta di laurea è indicata una presentazione breve e mirata: il sito suggerisce di prepararla e provarla con cura.

**Nota:** le procedure relative agli account WordPress e alle macchine del laboratorio si riferiscono al sito e all’infrastruttura originali; questo progetto Jekyll non implementa account utente.

[Leggi le FAQ dei seminari](/faq-seminari/).
'''),
'modelli-per-tesi-e-seminari':('Modelli per tesi e seminari','Studenti','Risorse per preparare materiali di ricerca, seminari e presentazioni.',r'''
## Preparare i materiali

Un documento di tesi o un seminario scientifico beneficia di una struttura chiara: obiettivo, problema, metodo, strumenti, risultati e sviluppi futuri.

## Riferimenti utili

- [FAQ seminari](/faq-seminari/) — preparazione, obiettivi e modalità di presentazione.
- [Systematic Literature Reviews](/systematic-literature-reviews/) — metodi per leggere, selezionare e organizzare la letteratura.
- [Nuovo tesista](/sono-un-nuovo-tesista-cosa-devo-fare/) — attività iniziali e aggiornamenti.

Per i template esatti e i file scaricabili forniti da ISISLab consulta la [pagina originale dei modelli](https://www.isislab.it/modelli-per-tesi-e-seminari/).
'''),
'challenges-in-lab':('Challenges in lab','Studenti','Sfide e opportunità per sperimentare in laboratorio.',r'''
## Sperimentare in ISISLab

Tra i temi che si prestano a esercizi e prototipi ci sono calcolo cloud ed edge, visualizzazione dei dati, sistemi collaborativi e Extended Reality.

Questa pagina introduce l’area **Challenges in lab** e collega alle [tematiche](/tematiche/) e ai [progetti](/progetti/) scientifici.

L’elenco ufficiale di challenge, con regolamenti, materiali e disponibilità corrente, deve essere verificato nella [sezione originale](https://www.isislab.it/challenges-in-lab/).
'''),
'blog':('Blog','Aggiornamenti','Note, racconti e approfondimenti della vita del laboratorio.',r'''
## Dentro ISISLab

Il blog è uno spazio per progetti, persone, appuntamenti e sperimentazioni che attraversano le attività di ricerca e didattica.

### Percorsi da seguire

- [News](/news/): notizie e novità.
- [Progetti](/progetti/): partnership e risultati.
- [Public engagement](/public-engagement/): iniziative con la comunità.
- [Seminari](/events/list/): gli incontri del gruppo.

Per l'archivio completo visita il [blog del sito originale](https://www.isislab.it/blog/).
'''),
'events/list':('Seminari ed eventi','Aggiornamenti','Un punto di accesso agli incontri e alle presentazioni scientifiche in laboratorio.',r'''
## I seminari in ISISLab

I seminari offrono a tesisti e ricercatori un momento di confronto su tecnologie, metodi, esperimenti e risultati della ricerca. Le presentazioni possono accompagnare le diverse fasi del lavoro di tesi.

### Evento del 9 ottobre 2026

La homepage pubblica di ISISLab ha segnalato un incontro dedicato alla **Sail Platform**, piattaforma web per la gestione e il monitoraggio di regate veliche, con **Davide Petracca** e **Armando Pio La Rocca**, e una presentazione del lavoro di tesi di **Anna Chiara Esposito**.

Sede indicata: Laboratorio ISISLab, Edificio F, Stecca 7, II piano, campus di Fisciano.

## Calendario aggiornato

Questa è una pagina statica di esempio, non un calendario sincronizzato. Per programma, date e materiali aggiornati consulta l’[archivio eventi originale](https://www.isislab.it/events/list/) e le [FAQ seminari](/faq-seminari/).
'''),
'risorse-per-gli-studenti':('Risorse per gli studenti','Studenti','Indicazioni per tirocini, seminari e documentazione del percorso di tesi.',r'''
## Informazioni per tesisti

Tirocini e tesi sono svolti nel contesto del laboratorio, con scambio continuo con i membri del gruppo. I seminari servono a conoscere le ricerche degli altri, esercitarsi nella presentazione e ricevere osservazioni sul proprio lavoro.

## Partecipare alle attività

Il sito originale indica la partecipazione alle attività e ai seminari periodici, insieme alla registrazione dei progressi attraverso aggiornamenti condivisi con il referente.

La pagina personale di un tesista può contenere **presentazione, argomento, referente, seminari svolti e diario dei progressi**.

## Risorse collegate

- [Informazioni utili](/informazioni-utili/)
- [Sono un nuovo tesista](/sono-un-nuovo-tesista-cosa-devo-fare/)
- [FAQ seminari](/faq-seminari/)
- [Modelli per tesi e seminari](/modelli-per-tesi-e-seminari/)
'''),
'tesisti-sono-stati-in-isislab':('Tesisti che sono stati in ISISLab','Studenti','Alcuni lavori di tesi svolti negli anni nel laboratorio.',r'''
## Alcune tesi recenti

La pagina originale presenta un ampio archivio, organizzato per anno, degli studenti che hanno svolto la tesi in ISISLab. Ecco alcuni esempi presenti nell’elenco.

### 2026

- **Anna Chiara Esposito:** monitoraggio chatbot e piattaforma agentica cloud-agnostic con DevOps e GitOps.
- **Davide Numelli:** digital forensics e threat intelligence in contesti cloud.
- **Gianluigi Romano:** estensione delle primitive Kubernetes con Operator Pattern e controller dedicato.
- **Francesco Monzillo:** valutazione della qualità dei knowledge graph attraverso gli ipergrafi.

### 2025

- **Valentina Ferrentino:** metriche semantiche per la qualità dei knowledge graph.
- **Lukasz Gajewski:** riscrittura di query SPARQL federate.
- **Antonio Caiazzo:** contenuti audiovisivi con avatar 3D, text-to-speech e lip-sync.

Per l’elenco completo e i titoli originali, consulta l’archivio del laboratorio.
''')
}

for slug, (title, section, description, text) in PAGES.items():
    # Native Jekyll/Liquid-friendly local links support deployment below a baseurl.
    import re
    text=re.sub(r'\]\((/[^)]+)\)',lambda m:"]({{ '"+m.group(1)+"' | relative_url }})",text)
    content='---\nlayout: page\n'
    for key,val in [('title',title),('section',section),('description',description),('source_url','https://www.isislab.it/'+slug+'/')]:
        content+=f'{key}: {json.dumps(val,ensure_ascii=False)}\n'
    content+='permalink: '+json.dumps('/'+slug+'/',ensure_ascii=False)+'\n---\n'+text.strip()+'\n'
    out=ROOT/'pages'/f'{slug.replace("/","-")}.md'
    out.write_text(content,encoding='utf-8')
print('Wrote',len(PAGES),'pages')
