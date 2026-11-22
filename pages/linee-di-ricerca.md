---
layout: page
lang: it
title: Linee di ricerca
description: Le tre macroaree del laboratorio ISISLab comprendono High Performance Computing, algoritmi su grafi e ipergrafi, analisi delle reti sociali, Web semantico, intelligenza artificiale e tecnologie immersive.
permalink: /linee-di-ricerca/
section: Pagina
article_kind: imported_page
---

Il laboratorio ISISLab studia come rappresentare, analizzare e simulare sistemi complessi e come consentire alle persone di esplorare dati e ambienti digitali. Il laboratorio affianca alla progettazione di algoritmi lo sviluppo di software e la sperimentazione con utenti, scuole, istituzioni culturali e imprese.

Le voci sotto ciascun tema fanno riferimento all’[ACM Computing Classification System 2012](https://www.acm.org/publications/class-2012).

- **[Computazioni Distribuite e Parallele](#computazioni-distribuite-e-parallele)**
  - [Simulazioni ad agenti su larga scala](#simulazioni-ad-agenti-su-larga-scala)
  - [Architetture Parallele](#architetture-parallele)
  - [High Performance Computing, cloud ed edge computing](#high-performance-computing-cloud-ed-edge-computing)
  - [Algoritmi per grafi e ipergrafi](#algoritmi-per-grafi-e-ipergrafi)
- **[Calcolo Collaborativo e Sociale](#calcolo-collaborativo-e-sociale)**
  - [Sistemi collaborativi, open data e learning](#sistemi-collaborativi-open-data-e-learning)
  - [Analisi delle reti sociali](#analisi-delle-reti-sociali)
  - [Web semantico e knowledge graph](#web-semantico-e-knowledge-graph)
  - [Intelligenza artificiale per reti e dati semantici](#intelligenza-artificiale-per-reti-e-dati-semantici)
  - [Sistemi adattivi e personalizzati](#sistemi-adattivi-e-personalizzati)
- **[Visualizzazione e Interazione](#visualizzazione-e-interazione)**
  - [Visualizzazione scalabile di dati e reti](#visualizzazione-scalabile-di-dati-e-reti)
  - [Realtà aumentata ed estesa](#realta-aumentata-ed-estesa)
  - [Digital Twin](#digital-twin)
  - [Interfacce immersive](#interfacce-immersive)

## Computazioni Distribuite e Parallele
{: #computazioni-distribuite-e-parallele}

### Simulazioni ad agenti su larga scala
{: #simulazioni-ad-agenti-su-larga-scala}

- [**CCS**](https://dl.acm.org/ccs/ccs.cfm?id=0&lid=0) → [**Computing methodologies**](https://dl.acm.org/ccs/ccs.cfm?id=10010147&lid=0.10010147) → [**Modeling and simulation**](https://dl.acm.org/ccs/ccs.cfm?id=10010341&lid=0.10010147.10010341) → [**Simulation types and techniques**](https://dl.acm.org/ccs/ccs.cfm?id=10010349&lid=0.10010147.10010341.10010349) → [**Agent / discrete models**](https://dl.acm.org/ccs/ccs.cfm?id=10010355&lid=0.10010147.10010341.10010349.10010355)
- [**CCS**](https://dl.acm.org/ccs/ccs.cfm?id=0&lid=0) → [**Computing methodologies**](https://dl.acm.org/ccs/ccs.cfm?id=10010147&lid=0.10010147) → [**Modeling and simulation**](https://dl.acm.org/ccs/ccs.cfm?id=10010341&lid=0.10010147.10010341) → [**Simulation types and techniques**](https://dl.acm.org/ccs/ccs.cfm?id=10010349&lid=0.10010147.10010341.10010349) → [**Distributed simulation**](https://dl.acm.org/ccs/ccs.cfm?id=10010356&lid=0.10010147.10010341.10010349.10010356)

Da D-MASON a krABMaga, il laboratorio sviluppa ambienti che permettono di descrivere i comportamenti individuali e osservare i fenomeni collettivi che emergono dalle loro interazioni. La ricerca affronta il problema di distribuire gli agenti tra più unità di calcolo, bilanciando il lavoro anche quando gli agenti si concentrano in alcune regioni dello spazio simulato.

[Il simulatore krABMaga](https://github.com/krABMaga/krABMaga)

### Architetture Parallele
{: #architetture-parallele}

- [**CCS**](https://dl.acm.org/ccs/ccs.cfm?id=0&lid=0) → [**Computer systems organization**](https://dl.acm.org/ccs/ccs.cfm?id=10010520&lid=0.10010520) → [**Architectures**](https://dl.acm.org/ccs/ccs.cfm?id=10010521&lid=0.10010520.10010521) → [**Parallel architectures**](https://dl.acm.org/ccs/ccs.cfm?id=10010528&lid=0.10010520.10010521.10010528)

Il laboratorio studia come le caratteristiche delle architetture parallele incidano sulle prestazioni delle applicazioni. Con il benchmark miniLB confronta l’esecuzione di una stessa simulazione su GPU di produttori diversi. Con il framework SYgraph affronta un problema complementare, la portabilità degli algoritmi di analisi dei grafi su GPU.

[Confronto delle prestazioni su GPU con miniLB](https://doi.org/10.1016/j.future.2025.108032)

[SYgraph e analisi parallela dei grafi su GPU](https://doi.org/10.1145/3754598.3754615)

### High Performance Computing, Cloud ed Edge Computing
{: #high-performance-computing-cloud-ed-edge-computing}

- [**CCS**](https://dl.acm.org/ccs/ccs.cfm?id=0&lid=0) → [**Computing methodologies**](https://dl.acm.org/ccs/ccs.cfm?id=10010147&lid=0.10010147) → [**Parallel computing methodologies**](https://dl.acm.org/ccs/ccs.cfm?id=10010169&lid=0.10010147.10010169)
- [**CCS**](https://dl.acm.org/ccs/ccs.cfm?id=0&lid=0) → [**Computer systems organization**](https://dl.acm.org/ccs/ccs.cfm?id=10010520&lid=0.10010520) → [**Architectures**](https://dl.acm.org/ccs/ccs.cfm?id=10010521&lid=0.10010520.10010521) → [**Distributed architectures**](https://dl.acm.org/ccs/ccs.cfm?id=10010537&lid=0.10010520.10010521.10010537) → [**Cloud computing**](https://dl.acm.org/ccs/ccs.cfm?id=10003100&lid=0.10010520.10010521.10010537.10003100)

Tra i lavori del laboratorio sul calcolo distribuito, il framework SOF ha permesso di esplorare i parametri di un modello eseguendo simulazioni su cluster e cloud. Altri lavori hanno studiato come descrivere workflow scientifici da eseguire su più infrastrutture cloud.

[SOF e ottimizzazione delle simulazioni su cloud (2018)](https://doi.org/10.1016/j.simpat.2017.12.005) · [Workflow scientifici su più cloud (2020)](https://doi.org/10.1002/cpe.5802)

### Algoritmi per grafi e ipergrafi
{: #algoritmi-per-grafi-e-ipergrafi}

- [**CCS**](https://dl.acm.org/ccs/ccs.cfm?id=0&lid=0) → [**Mathematics of computing**](https://dl.acm.org/ccs/ccs.cfm?id=10002950&lid=0.10002950) → [**Discrete mathematics**](https://dl.acm.org/ccs/ccs.cfm?id=10003624&lid=0.10002950.10003624) → [**Graph theory**](https://dl.acm.org/ccs/ccs.cfm?id=10003633&lid=0.10002950.10003624.10003633) → [**Graph algorithms**](https://dl.acm.org/ccs/ccs.cfm?id=10010917&lid=0.10002950.10003624.10003633.10010917)
- [**CCS**](https://dl.acm.org/ccs/ccs.cfm?id=0&lid=0) → [**Mathematics of computing**](https://dl.acm.org/ccs/ccs.cfm?id=10002950&lid=0.10002950) → [**Discrete mathematics**](https://dl.acm.org/ccs/ccs.cfm?id=10003624&lid=0.10002950.10003624) → [**Graph theory**](https://dl.acm.org/ccs/ccs.cfm?id=10003633&lid=0.10002950.10003624.10003633) → [**Hypergraphs**](https://dl.acm.org/ccs/ccs.cfm?id=10003637&lid=0.10002950.10003624.10003633.10003637)

Tra i primi contributi su grafi e reti, il laboratorio ha studiato come ridurre il numero di collegamenti necessari per instradare una richiesta in una rete peer-to-peer. Nei lavori successivi sugli ipergrafi ha esaminato come scegliere i nodi da cui avviare un processo di diffusione quando le interazioni coinvolgono interi gruppi.

[Algoritmi di routing per reti peer-to-peer (2009)](https://doi.org/10.1007/s00224-007-9074-x) · [Diffusione sugli ipergrafi (2021)](https://doi.org/10.3390/e23070796)

## Calcolo Collaborativo e Sociale
{: #calcolo-collaborativo-e-sociale}

### Sistemi collaborativi, open data e learning
{: #sistemi-collaborativi-open-data-e-learning}

- [**CCS**](https://dl.acm.org/ccs/ccs.cfm?id=0&lid=0) → [**Information systems**](https://dl.acm.org/ccs/ccs.cfm?id=10002951&lid=0.10002951) → [**Information systems applications**](https://dl.acm.org/ccs/ccs.cfm?id=10003227&lid=0.10002951.10003227) → [**Collaborative and social computing systems and tools**](https://dl.acm.org/ccs/ccs.cfm?id=10003233&lid=0.10002951.10003227.10003233)
- [**CCS**](https://dl.acm.org/ccs/ccs.cfm?id=0&lid=0) → [**Applied computing**](https://dl.acm.org/ccs/ccs.cfm?id=10010405&lid=0.10010405) → [**Education**](https://dl.acm.org/ccs/ccs.cfm?id=10010489&lid=0.10010405.10010489) → [**Computer-assisted instruction**](https://dl.acm.org/ccs/ccs.cfm?id=10010490&lid=0.10010405.10010489.10010490)

Il laboratorio progetta e valuta strumenti con cui gruppi di persone possono produrre dati, discutere e prendere decisioni insieme. Nel progetto europeo ROUTE-TO-PA, cittadini e amministrazioni hanno utilizzato la Social Platform for Open Data per costruire e interpretare dati aperti. In ambito educativo, CoFFEE ha permesso ai docenti di organizzare discussioni in piccoli gruppi e studiare la partecipazione degli studenti. Queste esperienze si affiancano alle ricerche sulla didattica dell’informatica e dell’intelligenza artificiale.

[Il progetto ROUTE-TO-PA su CORDIS (2015–2018)](https://cordis.europa.eu/project/id/645860/it) · [La Social Platform for Open Data nella scheda di ISISLab](/il-progetto-route-to-pa/)

### Analisi delle reti sociali
{: #analisi-delle-reti-sociali}

- [**CCS**](https://dl.acm.org/ccs/ccs.cfm?id=0&lid=0) → [**Human-centered computing**](https://dl.acm.org/ccs/ccs.cfm?id=10003120&lid=0.10003120) → [**Collaborative and social computing**](https://dl.acm.org/ccs/ccs.cfm?id=10003130&lid=0.10003120.10003130) → [**Collaborative and social computing design and evaluation methods**](https://dl.acm.org/ccs/ccs.cfm?id=10003134&lid=0.10003120.10003130.10003134) → [**Social network analysis**](https://dl.acm.org/ccs/ccs.cfm?id=10003293&lid=0.10003120.10003130.10003134.10003293)

Come si diffonde un’informazione quando le persone interagiscono in gruppi? ISISLab studia come la struttura delle relazioni influenzi la propagazione dell’informazione. Un problema concreto è individuare un piccolo insieme di persone da cui avviare la diffusione affinché raggiunga l’intera rete. I modelli basati su ipergrafi permettono di studiare il ruolo dei gruppi in questo processo.

[Diffusione dell’influenza negli ipergrafi](https://doi.org/10.3390/e23070796)

### Web semantico e Knowledge graphs
{: #web-semantico-e-knowledge-graph}

- [**CCS**](https://dl.acm.org/ccs/ccs.cfm?id=0&lid=0) → [**Information systems**](https://dl.acm.org/ccs/ccs.cfm?id=10002951&lid=0.10002951) → [**World Wide Web**](https://dl.acm.org/ccs/ccs.cfm?id=10003260&lid=0.10002951.10003260) → [**Web data description languages**](https://dl.acm.org/ccs/ccs.cfm?id=10003309&lid=0.10002951.10003260.10003309) → [**Semantic web description languages**](https://dl.acm.org/ccs/ccs.cfm?id=10003315&lid=0.10002951.10003260.10003309.10003315)

Per riutilizzare dati pubblicati da organizzazioni diverse occorre sapere che cosa descrivono, come sono collegati e quanto sono affidabili. Il laboratorio studia la rappresentazione della conoscenza mediante *knowledge graph*, la trasformazione di dati tabellari in RDF e l’interrogazione di fonti distribuite. Un tema centrale è la qualità dei *Linked Open Data*. Le ricerche riguardano sia la valutazione di intere collezioni di dati collegati, sia la rappresentazione dei risultati delle valutazioni in una forma che altri sistemi possano interrogare e riutilizzare.

[Qualità della Linked Open Data Cloud](https://doi.org/10.1145/3786331)

### Intelligenza artificiale per reti e dati semantici
{: #intelligenza-artificiale-per-reti-e-dati-semantici}

- [**CCS**](https://dl.acm.org/ccs/ccs.cfm?id=0&lid=0) → [**Computing methodologies**](https://dl.acm.org/ccs/ccs.cfm?id=10010147&lid=0.10010147) → [**Machine learning**](https://dl.acm.org/ccs/ccs.cfm?id=10010257&lid=0.10010147.10010257) → [**Machine learning approaches**](https://dl.acm.org/ccs/ccs.cfm?id=10010293&lid=0.10010147.10010257.10010293) → [**Learning latent representations**](https://dl.acm.org/ccs/ccs.cfm?id=10010319&lid=0.10010147.10010257.10010293.10010319)

ISISLab studia metodi di machine learning che sfruttano le relazioni tra gli elementi di un insieme di dati. Negli ipergrafi, per esempio, il laboratorio analizza come ricavare rappresentazioni dalle configurazioni ricorrenti di interazioni tra gruppi e come generare nuove strutture mediante modelli di diffusione. Un secondo filone riguarda l’impiego di large language models (LLM) per descrivere e classificare i knowledge graph. Lo strumento KGSum integra questi modelli con tecniche di machine learning per caratterizzare collezioni di grafi.

[Hypergraph Motif Representation Learning](https://doi.org/10.1145/3690624.3709274) · [KGSum](https://github.com/isislab-unisa/KGSum)

### Sistemi adattivi e personalizzati
{: #sistemi-adattivi-e-personalizzati}

- [**CCS**](https://dl.acm.org/ccs/ccs.cfm?id=0&lid=0) → [**Human-centered computing**](https://dl.acm.org/ccs/ccs.cfm?id=10003120&lid=0.10003120) → [**Human computer interaction (HCI)**](https://dl.acm.org/ccs/ccs.cfm?id=10003121&lid=0.10003120.10003121) → [**HCI design and evaluation methods**](https://dl.acm.org/ccs/ccs.cfm?id=10003122&lid=0.10003120.10003121.10003122) → [**User models**](https://dl.acm.org/ccs/ccs.cfm?id=10003332&lid=0.10003120.10003121.10003122.10003332)
- [**CCS**](https://dl.acm.org/ccs/ccs.cfm?id=0&lid=0) → [**Information systems**](https://dl.acm.org/ccs/ccs.cfm?id=10002951&lid=0.10002951) → [**World Wide Web**](https://dl.acm.org/ccs/ccs.cfm?id=10003260&lid=0.10002951.10003260) → [**Web searching and information discovery**](https://dl.acm.org/ccs/ccs.cfm?id=10003261&lid=0.10002951.10003260.10003261) → [**Personalization**](https://dl.acm.org/ccs/ccs.cfm?id=10003271&lid=0.10002951.10003260.10003261.10003271)

I laboratorio ISISLab ha sviluppato CHEOPS per adattare la navigazione sul Web al comportamento degli utenti. Con MIMOSA il laboratorio ha poi studiato come adattare l’accesso ai contenuti web al contesto d’uso. Un filone collegato ha riguardato la tutela della privacy durante la navigazione.

[CHEOPS (1997)](https://doi.org/10.1007/BFb0000353) · [Il modello utente di CHEOPS (1998, atti del workshop in PDF)](https://pure.tue.nl/ws/portalfiles/portal/1413144/9910387.pdf) · [MIMOSA (2010)](https://doi.org/10.1007/s00779-009-0232-9)

## Visualizzazione e Interazione
{: #visualizzazione-e-interazione}

### Visualizzazione scalabile di dati e reti
{: #visualizzazione-scalabile-di-dati-e-reti}

- [**CCS**](https://dl.acm.org/ccs/ccs.cfm?id=0&lid=0) → [**Human-centered computing**](https://dl.acm.org/ccs/ccs.cfm?id=10003120&lid=0.10003120) → [**Visualization**](https://dl.acm.org/ccs/ccs.cfm?id=10003145&lid=0.10003120.10003145) → [**Visualization application domains**](https://dl.acm.org/ccs/ccs.cfm?id=10003147&lid=0.10003120.10003145.10003147) → [**Information visualization**](https://dl.acm.org/ccs/ccs.cfm?id=10010923&lid=0.10003120.10003145.10003147.10010923)

Con il Datalet Ecosystem Provider (DEEP), ISISLab ha sviluppato componenti web riutilizzabili che caricano e visualizzano i dati direttamente nel browser. Chi consulta un dataset aperto può così esplorarne i contenuti durante la sua costruzione. Per lo studio delle reti complesse, il laboratorio ha contribuito a SimpleHypergraphs.jl, una libreria per analizzare e visualizzare le relazioni tra nodi e gruppi.

[SimpleHypergraphs.jl](https://doi.org/10.24166/im.01.2020)

### Realtà aumentata ed estesa
{: #realta-aumentata-ed-estesa}

- [**CCS**](https://dl.acm.org/ccs/ccs.cfm?id=0&lid=0) → [**Human-centered computing**](https://dl.acm.org/ccs/ccs.cfm?id=10003120&lid=0.10003120) → [**Human computer interaction (HCI)**](https://dl.acm.org/ccs/ccs.cfm?id=10003121&lid=0.10003120.10003121) → [**Interaction paradigms**](https://dl.acm.org/ccs/ccs.cfm?id=10003124&lid=0.10003120.10003121.10003124) → [**Mixed / augmented reality**](https://dl.acm.org/ccs/ccs.cfm?id=10010392&lid=0.10003120.10003121.10003124.10010392)
- [**CCS**](https://dl.acm.org/ccs/ccs.cfm?id=0&lid=0) → [**Human-centered computing**](https://dl.acm.org/ccs/ccs.cfm?id=10003120&lid=0.10003120) → [**Human computer interaction (HCI)**](https://dl.acm.org/ccs/ccs.cfm?id=10003121&lid=0.10003120.10003121) → [**Interaction paradigms**](https://dl.acm.org/ccs/ccs.cfm?id=10003124&lid=0.10003120.10003121.10003124) → [**Virtual reality**](https://dl.acm.org/ccs/ccs.cfm?id=10010866&lid=0.10003120.10003121.10003124.10010866)

Il laboratorio studia l’uso della realtà aumentata (AR) ed estesa (XR) per la fruizione del patrimonio culturale e la formazione. Le esperienze comprendono visite ibride in cui la posizione del visitatore guida l’esplorazione di una ricostruzione virtuale e serious game che permettono di scoprire siti archeologici e manufatti attraverso il gioco.

### Digital Twin
{: #digital-twin}

- [**CCS**](https://dl.acm.org/ccs/ccs.cfm?id=0&lid=0) → [**Computing methodologies**](https://dl.acm.org/ccs/ccs.cfm?id=10010147&lid=0.10010147) → [**Artificial intelligence**](https://dl.acm.org/ccs/ccs.cfm?id=10010178&lid=0.10010147.10010178) → [**Computer vision**](https://dl.acm.org/ccs/ccs.cfm?id=10010224&lid=0.10010147.10010178.10010224) → [**Computer vision problems**](https://dl.acm.org/ccs/ccs.cfm?id=10010245&lid=0.10010147.10010178.10010224.10010245) → [**Reconstruction**](https://dl.acm.org/ccs/ccs.cfm?id=10010254&lid=0.10010147.10010178.10010224.10010245.10010254)

ISISLab studia come costruire repliche digitali di luoghi reali e impiegarle nella formazione. Il progetto XRTwinScape utilizza il *3D Gaussian Splatting* per ricostruire ambienti di lavoro a partire da immagini. Chi si forma può così esplorare in un ambiente virtuale gli stessi spazi in cui dovrà operare.

[Il progetto XRTwinScape](https://isislab-unisa.github.io/XRTwinScape/)

### Interfacce immersive
{: #interfacce-immersive}

- [**CCS**](https://dl.acm.org/ccs/ccs.cfm?id=0&lid=0) → [**Human-centered computing**](https://dl.acm.org/ccs/ccs.cfm?id=10003120&lid=0.10003120) → [**Human computer interaction (HCI)**](https://dl.acm.org/ccs/ccs.cfm?id=10003121&lid=0.10003120.10003121) → [**Interaction techniques**](https://dl.acm.org/ccs/ccs.cfm?id=10003128&lid=0.10003120.10003121.10003128)
- [**CCS**](https://dl.acm.org/ccs/ccs.cfm?id=0&lid=0) → [**Human-centered computing**](https://dl.acm.org/ccs/ccs.cfm?id=10003120&lid=0.10003120) → [**Human computer interaction (HCI)**](https://dl.acm.org/ccs/ccs.cfm?id=10003121&lid=0.10003120.10003121) → [**Interaction techniques**](https://dl.acm.org/ccs/ccs.cfm?id=10003128&lid=0.10003120.10003121.10003128) → [**Gestural input**](https://dl.acm.org/ccs/ccs.cfm?id=10011755&lid=0.10003120.10003121.10003128.10011755)

Come si orienta un visitatore in uno spazio ricostruito? Come interagisce con gli oggetti che incontra? Il laboratorio studia queste domande attraverso prototipi che utilizzano visori stereoscopici e sensori di movimento, anche nell’ambito dei serious game per il patrimonio culturale.

[Esplora le pubblicazioni scientifiche di ISISLab](/pubblicazioni-scientifiche/)
