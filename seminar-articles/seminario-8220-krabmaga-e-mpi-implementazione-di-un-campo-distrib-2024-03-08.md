---
layout: seminar-detail
article_kind: seminar
lang: it
title: 'Seminario: &#8220;krABMaga e MPI: implementazione di un campo distribuito per simulazioni basate su agenti&#8221;
  di Andrea Tranquillo'
date: '2024-03-08'
date_display: 08/03/2024
time: 15:00 - 16:00
location: ''
speakers:
- '9'
permalink: /seminars/seminario-8220-krabmaga-e-mpi-implementazione-di-un-campo-distrib-2024-03-08/
seminar_image: /assets/img/seminars/14946-188da16872.png
---

Un Modello Basato su Agenti è un modello computazionale usato per simulare le azioni e le interazioni di agenti autonomi, in maniera da comprendere il comportamento di un sistema complesso e ciò che ne governa gli esiti. Le simulazioni che utilizzano tale modello sono generalmente molto costose in termini di potenza computazionale, quindi, per consentire la creazione di simulazioni molto più complesse, è necessario adottare il paradigma di programmazione distribuita, dividendo tale costo tra diverse macchine. Il problema principale nell'adozione di tale paradigma è trovare un modo per distribuire il campo di simulazione e far sì che gli agenti continuino ad interagire tra loro anche se rilocati su diverse macchine. In questo seminario, verrà presentata una struttura dati da utilizzare come campo di simulazione distribuito, il KdTree, e come i principali problemi di sincronizzazione che possono sorgere in questo tipo di applicazioni sono stati risolti utilizzando MPI. Verranno infine mostrati i risultati ottenuti confrontando il KdTree con la sua controparte sequenziale.
