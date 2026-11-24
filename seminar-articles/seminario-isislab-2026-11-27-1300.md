---
layout: seminar-detail
article_kind: seminar
lang: it
title: Seminario ISISLab
date: '2026-11-27'
date_display: 27/11/2026
time: 13:00 - 14:00
location: Laboratorio ISISLab, Dipartimento di Informatica, Università di Salerno (Edificio F, Stecca 7, Lab. 10, II piano)
  &#8211; Via Giovanni Paolo II, 132, 84084 Fisciano (SA).
speakers:
- Jean Claude Coppola
- Carmine Tortoriello
talks:
- title: 'N-Bodies con krABMaga: sviluppo di un modello agent-based in Rust e prospettive di parallelizzazione'
  speakers:
  - Jean Claude Coppola
  abstract: 'Questo lavoro descrive lo sviluppo di un modello N-Bodies con krABMaga, un framework per simulazioni agent-based
    scritto in Rust. Partendo dal modello template della libreria, il modello è stato adattato fino a ottenere una simulazione
    in cui ogni corpo è un agente che subisce la gravità degli altri e aggiorna il proprio moto. Il modello dispone di un’interfaccia
    grafica per scegliere la configurazione iniziale e regolare in tempo reale parametri come la costante gravitazionale,
    il passo temporale e il softening. Il lavoro riporta l’esperienza di sviluppo con la libreria e il risultato finale, e
    si chiude con gli sviluppi futuri, in particolare la realizzazione della parte parallela dell’engine.

    '
- title: Optimizing Particle-in-Cell Simulations for Modern Supercomputers
  subtitle: A GPU-Centric Redesign of the ECsim Code
  speakers:
  - Carmine Tortoriello
  abstract: 'Le simulazioni Particle-in-Cell (PIC) sono ampiamente utilizzate nello studio della dinamica dei plasmi, ma il
    loro elevato costo computazionale rappresenta una sfida per le moderne architetture di supercalcolo.


    Questo lavoro presenta la riprogettazione per GPU di ECsim, un codice PIC semi-implicito a conservazione dell''energia.
    Le principali ottimizzazioni riguardano il calcolo dei momenti delle particelle mediante CUDA, l''accelerazione del solutore
    dei campi elettromagnetici tramite PETSc e la riorganizzazione delle comunicazioni tra GPU attraverso CUDA-aware MPI.


    L''implementazione è stata validata rispetto alla versione OpenACC, raggiungendo un''accelerazione complessiva di circa
    9 volte su quattro GPU NVIDIA GH200. L''analisi delle singole ottimizzazioni evidenzia inoltre l''impatto della gestione
    dei dati sulle prestazioni, mentre gli esperimenti di strong e weak scaling sul supercomputer JUPITER valutano il comportamento
    del codice fino a 4096 GPU.

    '
seminar_image: /assets/img/seminars/copertina-27-11-2026.png
permalink: /seminars/seminario-isislab-2026-11-27-1300/
---

**N-Bodies con krABMaga: sviluppo di un modello agent-based in Rust e prospettive di parallelizzazione**

*Jean Claude Coppola*

**Abstract:**

Questo lavoro descrive lo sviluppo di un modello N-Bodies con krABMaga, un framework per simulazioni agent-based scritto in Rust. Partendo dal modello template della libreria, il modello è stato adattato fino a ottenere una simulazione in cui ogni corpo è un agente che subisce la gravità degli altri e aggiorna il proprio moto. Il modello dispone di un’interfaccia grafica per scegliere la configurazione iniziale e regolare in tempo reale parametri come la costante gravitazionale, il passo temporale e il softening. Il lavoro riporta l’esperienza di sviluppo con la libreria e il risultato finale, e si chiude con gli sviluppi futuri, in particolare la realizzazione della parte parallela dell’engine.

**Optimizing Particle-in-Cell Simulations for Modern Supercomputers: A GPU-Centric Redesign of the ECsim Code**

*Carmine Tortoriello*

**Abstract:**

Le simulazioni Particle-in-Cell (PIC) sono ampiamente utilizzate nello studio della dinamica dei plasmi, ma il loro elevato costo computazionale rappresenta una sfida per le moderne architetture di supercalcolo.

Questo lavoro presenta la riprogettazione per GPU di ECsim, un codice PIC semi-implicito a conservazione dell'energia. Le principali ottimizzazioni riguardano il calcolo dei momenti delle particelle mediante CUDA, l'accelerazione del solutore dei campi elettromagnetici tramite PETSc e la riorganizzazione delle comunicazioni tra GPU attraverso CUDA-aware MPI.

L'implementazione è stata validata rispetto alla versione OpenACC, raggiungendo un'accelerazione complessiva di circa 9 volte su quattro GPU NVIDIA GH200. L'analisi delle singole ottimizzazioni evidenzia inoltre l'impatto della gestione dei dati sulle prestazioni, mentre gli esperimenti di strong e weak scaling sul supercomputer JUPITER valutano il comportamento del codice fino a 4096 GPU.
