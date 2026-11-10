---
layout: project

# IDENTIFICAZIONE
title: "LibreRT"
lang: it
permalink: /progetti/librert/
translation_url: /en/progetti/librert/

# SOTTOTITOLO
subtitle: "Portable Heterogenous Real-time Programming for the Embedded Computing Continuum"

# DATE
date: 2023-09-28
start_date: 2023-09-28
end_date: 2025-09-28

# PROGRAMMA DI FINANZIAMENTO
program: prin-mur

# PROJECT THEMES
# Add only slugs actually listed in _data/project_types.yml
types: 
  - embedded-edge-computing
  - real-time-optimization

# RUOLO E PARTNER
role: "Unità di ricerca"

partners:
  - "Università degli Studi di Salerno"
  - "Politecnico di Milano"

# FINANZIAMENTO
funding: "PRIN 2022 – Ministero dell'Università e della Ricerca (MUR)"

# SITO E IMMAGINI
image: "/assets/media/c3d209fe6e0441-logo-librert-2.png"

logos:
  - /assets/media/d4338e80706013-mur-logo.png
  - /assets/media/44583057a10036-italy-1.png
  - /assets/media/c3d209fe6e0441-logo-librert-2.png

# ULTERIORI COLLEGAMENTI
links:
  - label: "Sito ufficiale del progetto LibreRT"
    url: "https://librert.di.unisa.it/"

# DESCRIZIONE
description: >
  LibreRT (Portable Heterogenous Real-time Programming for the Embedded
  Computing Continuum) è un progetto di ricerca finanziato nell'ambito
  del bando PRIN 2022. Il progetto mira a sviluppare uno stack software
  portatile per la programmazione di sistemi embedded eterogenei,
  capace di garantire prestazioni elevate, reattività e rispetto
  dei vincoli temporali lungo il continuum di elaborazione embedded.

published: true
---

## Obiettivi

I paradigmi emergenti dell'Industrial Internet of Things (IIoT) e dell'edge computing, insieme alla crescente diffusione di applicazioni di apprendimento automatico ed elaborazione delle immagini, hanno aumentato la domanda di sistemi embedded capaci di combinare elevate prestazioni di calcolo e requisiti stringenti di reattività e funzionamento in tempo reale.

LibreRT mira a fornire uno stack software di sistema portatile, in grado di supportare applicazioni altamente reattive, real-time e ad alto throughput lungo il continuum di elaborazione dei sistemi embedded.

## Attività e tecnologie

Il progetto affronta le problematiche legate alla programmazione di sistemi embedded eterogenei, dotati di CPU e GPU a basso consumo, presenti in ambiti quali dispositivi indossabili, mobile computing e sistemi automobilistici.

In particolare, LibreRT propone:

- Un modello di programmazione basato su **SYCL**, con estensioni per il supporto delle applicazioni real-time.
- Meccanismi di scheduling basati su priorità per CPU e GPU, con supporto alla preemption.
- Tecniche di calcolo approssimato, precisione mista e GPU kernel perforation.
- Un modello di programmazione basato sulla semantica moderna di **C++** e su sistemi runtime avanzati.
- Il supporto alle GPU integrate.
- L'utilizzo di **Miosix** per i dispositivi micro-edge e di distribuzioni Linux tradizionali per i dispositivi deep-edge e meta-edge.
- Un livello di autotuning per ottimizzare adattivamente l'accuratezza dell'approssimazione nel rispetto dei vincoli temporali.

## Collaborazione

Il progetto coinvolge due unità di ricerca:

- **Università degli Studi di Salerno** – Biagio Cosenza, ricercatore a tempo determinato.
- **Politecnico di Milano** – Federico Terraneo, ricercatore a tempo determinato.

L'attività di ricerca si sviluppa nell'ambito della collaborazione tra le due università, con competenze nell'architettura dei calcolatori, nei sistemi embedded, nei sistemi operativi e nella programmazione parallela.

## Risultati attesi

LibreRT mira a realizzare un ambiente software portatile per la programmazione efficiente di architetture embedded eterogenee.

Tra i risultati attesi figurano:

- Modelli di programmazione e sistemi runtime adatti alle applicazioni real-time.
- Scheduler per CPU e GPU con supporto alla preemption.
- Tecniche adattive di calcolo approssimato.
- Meccanismi di autotuning per bilanciare accuratezza e vincoli temporali.
- Una maggiore portabilità delle applicazioni lungo il continuum di elaborazione embedded.

## Informazioni sul finanziamento

- **Bando:** PRIN – Progetti di ricerca di rilevante interesse nazionale, 2022.
- **Ente finanziatore:** Ministero dell'Università e della Ricerca (MUR).
- **Importo indicato:** 100.480 euro.
- **Durata:** 24 mesi.
- **Periodo:** 28 settembre 2023 – 28 settembre 2025.
- **Settore ERC principale:** PE – Physical Sciences and Engineering.
- **Sottosettori ERC:**
  - PE6_3 – Software engineering, programming languages and systems.
  - PE6_1 – Computer architecture, embedded systems, operating systems.
  - PE6_2 – Distributed systems, parallel computing, sensor networks, cyber-physical systems.
