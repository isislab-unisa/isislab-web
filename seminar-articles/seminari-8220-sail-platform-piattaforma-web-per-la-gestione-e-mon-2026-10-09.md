---
layout: seminar-detail
article_kind: seminar
lang: it
title: 'Seminari: &#8220;Sail Platform: piattaforma web per la gestione e monitoraggio di regate veliche&#8221; di Davide
  Petracca e Armando Pio   e Presentazione lavoro di tesi di Anna Chiara Esposito'
date: '2026-10-09'
date_display: 09/10/2026
time: 12:00 - 13:00
location: Laboratorio ISISLab, Dipartimento di Informatica, Università di Salerno (Edificio F, Stecca 7, Lab. 10, II piano)
  &#8211; Via Giovanni Paolo II, 132, 84084 Fisciano (SA)
speakers:
- '9'
permalink: /seminars/seminari-8220-sail-platform-piattaforma-web-per-la-gestione-e-mon-2026-10-09/
seminar_image: /assets/img/seminars/51235-9ade55aa88.png
---

1) "Sail Platform: piattaforma web per la gestione e monitoraggio di regate veliche" di Davide Petracca e Armando Pio La Rocca

Abstract : " Il progetto presenta una piattaforma web per l'organizzazione e la gestione di regate veliche, rivolta a circoli nautici, ufficiali di gara e regatanti. Il sistema consente di creare regate, tracciare il percorso tramite un editor di boe su mappa, gestire circoli e soci, raccogliere le iscrizioni con relativi equipaggi e pagamenti, nonché inoltrare e valutare proteste. L'accesso è regolato da autenticazione JWT con ruoli differenziati (sailor e admin). Due moduli sono dedicati all'analisi sportiva: una mappa di gara simula il movimento delle imbarcazioni lungo il percorso e produce, a fine prova, una classifica a tempo compensato elaborata da un motore di weather routing (WRS), che stima il tempo di percorrenza di ciascuna barca sulla base delle polari di velocità e delle condizioni meteo; una dashboard tattica mostra l'evoluzione temporale di vento, velocità, VMG e fattore meteo tramite grafici SVG. L'architettura è full-stack: frontend sviluppato con React, TypeScript, Vite, Tailwind CSS e Leaflet, con interfaccia multilingue (esattamente cinque ovvero italiano,spagnolo,tedesco,francese e inglese); backend realizzato con FastAPI e SQLModel su PostgreSQL con migrazioni gestite da Alembic. L'intero sistema è orchestrato con Docker Compose. Il seminario illustrerà la visione progettuale della piattaforma e il percorso evolutivo che ha portato dall'analisi di soluzioni esistenti alla definizione di un'architettura e di un'interfaccia originali. "

2) Presentazione del Lavoro di tesi: "Monitoring Chatbot: Progettazione e Deployment di una Piattaforma Agentica Cloud-Agnostic con Approccio DevOps e GitOps" di Anna Chiara Esposito

Abstract: Questa tesi descrive la progettazione e il deployment di Monitoring Chatbot, una piattaforma cloud-native a microservizi pensata per supportare attività di monitoring, troubleshooting e gestione operativa in contesti IT complessi.
L'architettura utilizza Kubernetes per l'orchestrazione dei servizi e integra connettori per l'acquisizione di dati provenienti da sorgenti eterogenee, pipeline di ingestion basate su Apache Kafka e un'architettura Retrieval-Augmented Generation (RAG) per l'accesso alle informazioni contenute nelle sorgenti aziendali.
Una parte centrale del lavoro riguarda l'automazione dell'infrastruttura e del processo di rilascio. Il provisioning viene gestito secondo il paradigma Infrastructure as Code con Terraform, mentre ArgoCD viene utilizzato per la gestione dichiarativa del deployment e delle configurazioni applicative
secondo un approccio GitOps (Git Operations). L'obiettivo è ridurre le operazioni manuali e mantenere coerente lo stato dell'ambiente di esecuzione con quello descritto nei repository di configurazione.
Per affrontare le difficoltà di monitoraggio tipiche delle architetture distribuite, la piattaforma integra inoltre uno stack di osservabilità basato su OpenTelemetry. Metriche, log e tracce distribuite vengono raccolti e resi consultabili attraverso l'impiego combinato di Prometheus, Loki, Tempo e Grafana, fornendo agli operatori una vista più completa sul comportamento dei
servizi e supportando le attività di analisi e individuazione delle anomalie.
Il sistema è progettato per poter essere distribuito sia in ambienti cloud sia on-premise, con l'obiettivo di limitare la dipendenza da uno specifico provider infrastrutturale e mantenere maggiore flessibilità nella gestione dei dati.
Il chatbot integra infine un componente conversazionale orchestrato tramite LangGraph e un meccanismo RAG supportato dal database vettoriale Qdrant, così da recuperare informazioni pertinenti dalle sorgenti disponibili e utilizzarle come contesto nella generazione delle risposte.
Il lavoro mostra quindi come pratiche DevOps e GitOps, Infrastructure as Code, strumenti di osservabilità e componenti basati su modelli linguistici possano essere integrati all'interno di un'unica piattaforma destinata al supporto delle operazioni IT.
