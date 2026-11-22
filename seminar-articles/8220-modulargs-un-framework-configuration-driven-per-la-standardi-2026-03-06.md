---
layout: seminar-detail
article_kind: seminar
lang: it
title: '&#8220;ModularGS: Un Framework Configuration-Driven per la standardizzazione delle pipeline di 3D Gaussian Splatting&#8221;
  di Andrea Amorosini'
date: '2026-03-06'
date_display: 06/03/2026
time: 15:00 - 16:00
location: Laboratorio ISISLab, Dipartimento di Informatica, Università di Salerno (Edificio F, Stecca 7, Lab. 10, II piano)
  &#8211; Via Giovanni Paolo II, 132, 84084 Fisciano (SA).
speakers:
- '9'
permalink: /seminars/8220-modulargs-un-framework-configuration-driven-per-la-standardi-2026-03-06/
seminar_image: /assets/img/seminars/50874-846a55019d.png
---

Il 3D Gaussian Splatting (3DGS) ha rivoluzionato il campo della Novel View Synthesis, offrendo una qualità visiva fotorealistica unita a velocità di rendering in tempo reale. Tuttavia, la rapida proliferazione di queste tecnologie ha generato una grave frammentazione software e una conseguente "crisi della riproducibilità". L'installazione e l'orchestrazione delle pipeline, dall'elaborazione dei dati grezzi allo Structure from Motion fino all'addestramento dei modelli, sono afflitte dal Dependency Hell, richiedendo complesse configurazioni strettamente legate all'hardware (CUDA, compilatori C++) e flussi di lavoro manuali inclini all'errore.
Per risolvere queste criticità, questa tesi presenta Modular GS, un framework Configuration Driven progettato per la standardizzazione, l'automazione e l'esecuzione sicura di algoritmi legati al 3DGS. Attraverso un'architettura a livelli, il sistema disaccoppia la logica di dominio dall'esecuzione tramite file dichiarativi TOML. L'integrazione nativa del gestore di pacchetti Pixi garantisce un isolamento rigoroso (sandboxing) dell'intero ecosistema di compilazione binaria, assicurando configurazioni Zero Setup e deterministiche su qualsiasi sistema host.
Il framework introduce inoltre meccanismi di self healing per la risoluzione automatica delle inconsistenze dimensionali dei dati prima dei crash della GPU e un livello di sicurezza Security by Design basato su validazione crittografica ECDSA per prevenire vulnerabilità della supply chain. Completano l'architettura una doppia interfaccia utente (CLI e Web UI in Streamlit) per un accesso semplificato agli strumenti.
La valutazione sperimentale dimostra che Modular GS azzera l'overhead sistemistico abbattendo il Time to First Run, ottimizza significativamente lo spazio su disco tramite logiche di Shared Environments e permette l'esecuzione automatizzata di pipeline end to end (da file video a modello 3D compresso). Il sistema risulta nativamente estensibile, permettendo ai ricercatori l'integrazione plug and play di nuovi algoritmi e ponendo basi solide per le pratiche MLOps nella ricerca sulla Computer Vision.
