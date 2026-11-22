---
layout: seminar-detail
article_kind: seminar
lang: it
title: 'Seminario: &#8220;Strategie di load balancing per lo storage multi-cloud: progettazione e integrazione nella libreria
  M2CS&#8221; di Luca Mediatore'
date: '2026-11-06'
date_display: 06/11/2026
time: 12:00 - 12:00
location: Laboratorio ISISLab, Dipartimento di Informatica, Università di Salerno (Edificio F, Stecca 7, Lab. 10, II piano)
  &#8211; Via Giovanni Paolo II, 132, 84084 Fisciano (SA).
speakers:
- '9'
permalink: /seminars/seminario-8220-strategie-di-load-balancing-per-lo-storage-multi-c-2026-11-06/
seminar_image: /assets/img/seminars/51325-910c1da925.png
---

La gestione dello storage in ambienti multi-cloud richiede strategie di selezione dei backend capaci di considerare caratteristiche differenti. Questo lavoro presenta la progettazione e l’integrazione di nuove strategie di load balancing in M2CS, una libreria sviluppata in Go per la gestione unificata di backend di storage eterogenei.
A partire dall’analisi dell’architettura esistente, il lavoro approfondisce tre approcci:
La strategia Latency Based privilegia la risorsa con il minor tempo di risposta stimato, con l’obiettivo di ridurre il tempo di accesso ai dati.
Geoproximity si basa invece sulla distanza geografica tra il client e le risorse di storage, favorendo quelle più vicine alla posizione dell’utente.
Infine, Least Latency + Power of Two Choices (P2C) combina una selezione casuale di due risorse candidate con una valutazione basata su latenza, carico attuale e margine di errore, con l’obiettivo di bilanciare la rapidità di risposta e la distribuzione delle richieste.
