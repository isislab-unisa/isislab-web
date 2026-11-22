---
layout: seminar-detail
article_kind: seminar
lang: it
title: 'Seminario: &#8220;Presentazione dei lavori di tesi&#8221; di Gianluigi Romano, Valeria Argenziano e Alessandro Basso'
date: '2026-04-27'
date_display: 27/04/2026
time: 10:30 - 11:30
location: ''
speakers:
- '9'
permalink: /seminars/seminario-8220-presentazione-dei-lavori-di-tesi-8221-di-gianluigi-2026-04-27/
seminar_image: /assets/img/seminars/51023-4c8a66b17c.png
---

1) "Estensione delle primitive di Kubernetes tramite Operator Pattern: Sviluppo di un controller custom e dashboard di gestione integrata" di Gianluigi Romano

Abstract: La crescente adozione di Kubernetes come standard de facto per l’orchestrazione dei container ha introdotto una significativa complessita operativa, caratterizzata dalla gestione manuale di risorse eterogenee e dalla difficolta di garantire portabilita tra infrastrutture diverse. In questo contesto, il pattern Operator rappresenta uno strumento fondamentale per codificare la conoscenza operativa in software, estendendo le primitive del cluster per automatizzare il ciclo di vita delle applicazioni e superare la rigidità delle configurazioni statiche. Questa tesi presenta la progettazione e lo sviluppo di un controller nativo implementato in linguaggio Go tramite il framework Kubebuilder. La metodologia adottata sfrutta una logica di controllo level-triggered, che abilita meccanismi avanzati di self-healing e idempotenza: il sistema monitora costantemente lo stato del cluster, rilevando e correggendo autonomamente le discrepanze rispetto allo stato desiderato, o Desired State, garantendo cosı resilienza e continuita operativa. L’architettura proposta affronta in modo specifico la sfida dell’interoperabilita del networking. Attraverso un approccio modulare basato su Kustomize e sul pattern Base+Variants, il sistema inietta configurazioni dinamiche che rendono l’Operator infrastructure agnostic, assicurando il supporto nativo e trasparente per diversi Ingress Controller senza modifiche al codice sorgente. Il lavoro e completato dall’integrazione di una Dashboard web che astrae la complessità dei manifesti YAML, offrendo un’interfaccia di gestione intuitiva e validando un modello di orchestrazione pienamente dichiarativo e portabile.

2) "Analysis, design and development of an ELT orchestration middleware for Bancassurance data integration: the Flodex case study" di Valeria Argenziano

Abstract: In the fast paced Insurtech era, the seamless flow of data between insurance giants and banking institutions is not just a technical necessity but a business imperative. The Flodex project arises from a critical challenge faced by Credem: moving away from obsolete, manual heavy legacy systems to synchronize complex data streams—policies, financial movements, and balances.

Traditional integration portals, like the legacy ART, function as rigid "black boxes." In these systems, a single minor data discrepancy can trigger a "silent failure," rejecting entire batches and leaving back office operators blind to the root cause. This lack of transparency turns every error into an operational bottleneck, requiring tedious, manual re executions and physical access to servers for data recovery.

This thesis unveils Flodex, an intelligent orchestration middleware engineered with Spring Boot and Apache Camel. Flodex shatters the black box paradigm through a sophisticated three tier architecture: a persistent staging area for data normalization, a logical orchestrator that enforces transactional integrity (preventing "orphan" records), and a front-end built in Vaadin.

The project’s breakthrough is the Dynamic Patching engine. Unlike standard ETL tools, Flodex empowers users to intercept failed transactions, decompose complex JSON payloads into intuitive web forms, and correct data "on the fly" for immediate resubmission. By transforming error handling from a technical failure into a managed business process, Flodex drastically slashes the lead time of data accounting, ensuring data resilience and operational agility in a high stakes financial environment.

3) "Dicegame: un’esperienza di apprendimento in realtà aumentata attraverso un gioco multiutente per il patrimonio culturale" di Alessandro Basso

Abstract: Questa tesi descrive la progettazione e lo sviluppo di un gioco in realtà aumentata per dispositivi mobili che consente a più giocatori di condividere uno spazio di gioco virtuale ancorato all’ambiente reale. Per consentire ai partecipanti di interagire in modo immersivo e collaborativo, il sistema integra gli oggetti digitali nel contesto fisico utilizzando tecnologie di tracciamento e di riconoscimento dello spazio. L’obiettivo del lavoro e sviluppare un sistema in grado di gestire dinamicamente lo stato di gioco e le interazioni tra i giocatori al fine di garantire coerenza, sincronizzazione e continuità dell’esperienza in un contesto di gioco con più giocatori a turni. Con l’obiettivo di aumentare la modularità e l’estendibilità, particolare attenzione e stata dedicata alla progettazione dell’architettura software, distinguendo chiaramente la logica di gioco, i componenti di rete e il modulo di gestione della realtà aumentata. Il lavoro affronta anche le principali questioni relative alla sincronizzazione dei dispositivi, all’ancoraggio coerente degli oggetti virtuali nello spazio condiviso, alla gestione dei turni e alla progettazione di un’interfaccia utente adattiva, analizzando le soluzioni trovate per migliorare l’esperienza utente in un ambiente di realtà aumentata collaborativa.
