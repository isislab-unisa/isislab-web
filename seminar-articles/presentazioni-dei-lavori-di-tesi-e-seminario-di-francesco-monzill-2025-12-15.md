---
layout: seminar-detail
article_kind: seminar
lang: it
title: Presentazioni dei lavori di tesi e Seminario di Francesco Monzillo
date: '2025-12-15'
date_display: 15/12/2025
time: 16:00 - 17:00
location: ''
speakers:
- '9'
permalink: /seminars/presentazioni-dei-lavori-di-tesi-e-seminario-di-francesco-monzill-2025-12-15/
seminar_image: /assets/img/seminars/50697-88c026bf40.png
---

Presentazioni deilavori di tesi

1) "SeMQuAK: Modellazione Semantica delle Metriche di Qualità dei Knowledge Graph" di Valentina Ferrentino

Abstract: La valutazione automatica della qualità dei Knowledge Graph (KG), come avviene nel progetto KGHeartBeat che monitora oltre 1.600 dataset LOD, genera periodicamente una grande quantità di dati in formato tabellare (CSV). Sebbene accessibile, questo formato offre una visione frammentata, limitando tracciabilità e interoperabilità. Il mio progetto di tesi propone SeMQuAK (Semantic Modeling of Quality Assessment in Knowledge Graphs), un framework che, tramite un modello ontologico e un modulo ETL in Python, trasforma i risultati delle valutazioni in un grafo RDF unificato, conforme ai principi Linked Data. L’approccio abilita una rappresentazione machine-readable che facilita analisi comparative e monitoraggi temporali. Inoltre, mediante una valutazione basata su question answering con LLM, è stato possibile dimostrare che questa rappresentazione semantica migliora la capacità dei modelli di estrarre, collegare e interpretare le informazioni rispetto agli stessi contenuti forniti in formato testuale o tabellare.

2) GenMap: A federation-agnostic SPARQL Query Rewriter di Lukasz Gajewski

Abstract :
Il Web semantico si è evoluto in un vasto ecosistema di grafici di conoscenza distribuiti, ma le tecnologie di query federate rimangono in gran parte inaccessibili al di fuori degli esperti di web semantico. Nonostante i ignificativi progressi nell'ottimizzazione e nell'esecuzione delle query, l'ostacolo fondamentale a una più ampia adozione è cognitivo: gli utenti devono possedere una profonda competenza in SPARQL e una conoscenza completa degli schemi su endpoint eterogenei per formulare query federate.
Questa tesi apporta due contributi principali. In primo luogo, presentiamo una Questa tesi offre due contributi principali. In primo luogo, presentiamo una revisione sistematica della letteratura che analizza gli studi primari sull'elaborazione delle query SPARQL federate pubblicati tra il 2014 e il 2025 attraverso tre lenti complementari: meccanismi architetturali, pratiche di valutazione sperimentale e centralità dell'utente. La revisione rivela alcune lacune critiche: mentre le prestazioni e l'ottimizzazione ricevono ampia attenzione, la formulazione delle query rimane trascurata.
Le valutazioni sperimentali si concentrano fortemente sui domini biomedici e sui set di dati di benchmark consolidati, con i domini emergenti drammaticamente sottorappresentati.
Ancora più significativo è il fatto che la stragrande maggioranza dei sistemi richiede una profonda competenza in SPARQL con un'assistenza minima nella costruzione delle query, esponendo un fondamentale disallineamento tra maturità tecnica e accessibilità pratica.
Sulla base di questi risultati, proponiamo GenMap, un riscrittore di query SPARQL indipendente dalla federazione
che affronta l'eterogeneità semantica negli ambienti federati.
GenMap funziona come un componente intermedio della pipeline:
I sistemi di risposta alle domande generano SPARQL con etichette predicato generiche,
GenMap le traduce in URI specifici per endpoint attraverso l'indicizzazione TF-IDF
e il riclassificamento semantico basato su LLM, mentre i motori di federazione convenzionali
eseguono le query risultanti.
Questa architettura modulare non richiede dati di addestramento specifici per endpoint o
mappature manuali del vocabolario, adattandosi automaticamente quando gli schemi evolvono
o nuovi endpoint si uniscono alla federazione. GenMap rappresenta quindi un approccio
alla democratizzazione dell'accesso alle query federate, affrontando il collo di bottiglia specifico
dell'eterogeneità semantica e integrandosi con le tecnologie esistenti.

Seminario : "Knowledge Graphs quality assessment through Hypergraphs" di Francesco Monzillo

Abstract: "Hypergraph is a mathematical tool on which various applications in social networks, recommendation systems and question answering have been built. Its higher flexibility and higher-order expressiveness make it a great fit for complex dynamic systems with millions of entities and interactions among them. For these reasons, we argue it should also contribute in semantic web related problems. Semantic web technologies, indeed, aim to make the web more interconnected and more intelligent, allowing deeper researches. Therefore, in this article we will initially clarify the State Of The Art (SOTA), potentials and limits on combining hypergraphs with semantic web technologies through a Systematic Literature Review (SLR). Subsequently, a Question Answering problem on a Knowledge Graph quality assessment framework will be presented, and an hypergraph-based solution will be compared to 3 baselines. Experiments show hypergraphs can significantly improve performances particularly in more complex questions.
