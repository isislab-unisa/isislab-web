---
layout: seminar-detail
article_kind: seminar
lang: it
title: 'Seminario: &#8220;GenMap: a federation-agnostic SPARQL query rewriter&#8221; di LUKASZ GAJEWSKI'
date: '2025-11-14'
date_display: 14/11/2025
time: 14:00 - 15:00
location: Laboratorio ISISLab, Dipartimento di Informatica, Università di Salerno (Edificio F, Stecca 7, Lab. 10, II piano)
  &#8211; Via Giovanni Paolo II, 132, 84084 Fisciano (SA)
speakers:
- '9'
permalink: /seminars/seminario-8220-genmap-a-federation-agnostic-sparql-query-rewriter-2025-11-14/
seminar_image: /assets/img/seminars/50661-5a72857135.png
---

Il presente lavoro di tesi si colloca nell'ambito dei Knowledge Graph Federati e delle Federated SPARQL Queries, con particolare attenzione alle problematiche di usabilità da parte degli utenti finali.
Per comprendere lo stato dell'arte, è stata condotta una systematic literature review focalizzata sui motori di query SPARQL federati, con l'obiettivo di analizzare il processo di interrogazione, i domini applicativi prevalenti e il livello di attenzione verso l'utente finale.
I risultati hanno evidenziato criticità significative: la ricerca assume quasi sempre come punto di partenza query SPARQL già formulate, e soprattutto emerge una scarsa progettazione user-centric, con tecnologie che richiedono competenze tecniche avanzate e presentano barriere all'adozione da parte di utenti non esperti.
A partire da queste evidenze, la tesi propone GenMap, un sistema di federation-agnostic SPARQL query rewriting che consente agli utenti di formulare interrogazioni SPARQL utilizzando predicati generici, automaticamente tradotti nelle corrispondenti URI concrete degli endpoint sottostanti.
Il sistema si basa su un'architettura ibrida: per ciascun Knowledge Graph della federazione viene costruito un indice TF-IDF che seleziona i top-k candidati più probabili per ogni predicato generico, mentre un Large Language Model identifica la mappatura più appropriata tra i candidati o rileva l'assenza di predicati compatibili.
GenMap è progettato per essere completamente indipendente dal motore di federazione utilizzato, garantendo compatibilità con qualsiasi infrastruttura esistente. La validazione sperimentale è stata condotta su una federazione di quattro Knowledge Graph in ambito biomedico, derivati da benchmark consolidati, dimostrando l'efficacia dell'approccio nel facilitare l'accesso a dati distribuiti e semanticamente eterogenei senza richiedere conoscenza a priori degli schemi degli endpoint.
