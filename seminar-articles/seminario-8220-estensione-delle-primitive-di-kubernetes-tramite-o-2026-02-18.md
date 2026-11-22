---
layout: seminar-detail
article_kind: seminar
lang: it
title: 'Seminario: &#8220;Estensione delle primitive di Kubernetes tramite Operator Pattern: Sviluppo di un controller custom
  e dashboard di gestione integrata&#8221; di Gianluigi Romano'
date: '2026-02-18'
date_display: 18/02/2026
time: 16:00 - 17:00
location: ''
speakers:
- '9'
permalink: /seminars/seminario-8220-estensione-delle-primitive-di-kubernetes-tramite-o-2026-02-18/
seminar_image: /assets/img/seminars/50770-8e8d425dbe.png
---

La crescente adozione di Kubernetes come standard de facto per l'orchestrazione dei container ha introdotto una significativa complessità operativa, caratterizzata dalla gestione manuale di risorse eterogenee e dalla difficoltà di garantire portabilità tra infrastrutture diverse. In questo contesto, l'Operator Pattern rappresenta uno strumento fondamentale per codificare la conoscenza operativa in software, estendendo le primitive del cluster per automatizzare il ciclo di vita delle applicazioni e superare la rigidità delle configurazioni statiche.
Questa tesi presenta la progettazione e lo sviluppo di "SimpleApp Operator", un controller nativo implementato in linguaggio Go tramite il framework Kubebuilder.
La metodologia adottata sfrutta una logica di controllo Level-Triggered, che abilita meccanismi avanzati di Self-Healing e idempontenza: il sistema monitora costantemente lo stato del cluster, rilevando e correggendo autonomamente le discrepanze rispetto allo stato desiderato (Desired State), garantendo così resilienza e continuità operativa.
L'architettura proposta affronta in modo specifico la sfida dell'interoperabilità del networking. Attraverso un approccio modulare basato su Kustomize e sul pattern Base+Variants, il sistema inietta configurazioni dinamiche che rendono l'Operator Infrastructure-Agnostic, assicurando il supporto nativo e trasparente per diversi Ingress Controller senza modifiche al codice sorgente. Il lavoro è completato dall'integrazione di una Dashboard Web che astrae la complessità dei manifest YAML, offrendo un'interfaccia di gestione intuitiva e validando un modello di orchestrazione pienamente dichiarativo e portabile.
