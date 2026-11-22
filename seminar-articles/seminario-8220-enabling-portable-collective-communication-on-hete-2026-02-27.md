---
layout: seminar-detail
article_kind: seminar
lang: it
title: 'Seminario: &#8220;Enabling Portable Collective Communication on Heterogeneous GPU Systems&#8221; di Salvatore Sirica
  e  &#8220;Vettorizzazione Esplicita del Prodotto Matriciale su RISC-V con RVV&#8221; di Sergio Guastaferro'
date: '2026-02-27'
date_display: 27/02/2026
time: 03:00 - 16:00
location: ''
speakers:
- '9'
permalink: /seminars/seminario-8220-enabling-portable-collective-communication-on-hete-2026-02-27/
seminar_image: /assets/img/seminars/50787-82d3840348.png
---

Speaker 1: Salvatore Sirica
Titolo : "Enabling Portable Collective Communication on Heterogeneous GPU Systems" di Salvatore Sirica

Abstract :
Many distributed HPC applications and data-parallel AI training pipelines depend on MPI-style communication patterns. As systems scale to many GPUs and nodes, collective operations like Allreduce become a primary performance bottleneck, directly impacting scalability. In practice, the highest-performing GPU collectives are typically provided by vendor-specific libraries such as NVIDIA NCCL and AMD RCCL, which exploit hardware and topology-aware optimizations but reduce portability across heterogeneous clusters.

Intel oneAPI Collective Communications Library (oneCCL) is uniquely positioned to mitigate this issue thanks to its SYCL-based interface. However, deep in its implementation it is tightly coupled to Intel Level Zero, effectively preventing execution on non-Intel GPUs.

This work enables portable GPU collectives within oneCCL by introducing NCCL and RCCL as pluggable backends while preserving the existing oneCCL user-facing API. The integration reuses oneCCL’s bootstrap mechanisms to initialize vendor communicators and dispatches collectives on native GPU streams through SYCL interoperability. Micro-benchmarks on the UNISA-HPC cluster with NVIDIA A100 GPUs show that oneCCL+NCCL achieves performance close to native NCCL for key collectives across a broad range of message sizes and data types.

Speaker 2: Sergio Guastaferro
Titolo : "Vettorizzazione Esplicita del Prodotto Matriciale su RISC-V con RVV" di Sergio Guastaferro

Abstract :
Il prodotto matriciale rappresenta un'operazione fondamentale nel calcolo ad alte prestazioni, alla base di framework per l'intelligenza artificiale, simulazioni scientifiche e analisi dati. Con l'emergere di RISC-V come architettura aperta e modulare, diventa cruciale valutare l'efficacia delle sue estensioni vettoriali (RVV) nell'accelerare operazioni numericamente intensive come il prodotto matriciale.

Questa tesi analizza sistematicamente le performance del prodotto matriciale su processori RISC-V dotati di supporto vettoriale, confrontando la vettorizzazione automatica offerta dai compilatori e una vettorizzazione esplicita realizzata mediante intrinseche RVV. L'implementazione proposta si basa su microkernel ottimizzati con formulazione a prodotto esterno, tiling progressivo e gestione dinamica della lunghezza vettoriale a runtime. Un'attenzione particolare è dedicata all'esplorazione del parametro LMUL, che regola il parallelismo vettoriale in relazione alla configurazione hardware (VLEN).

I risultati sperimentali, ottenuti sul processore Spacemit X60 a 8 core, dimostrano che la vettorizzazione esplicita supera significativamente l'approccio automatico, raggiungendo speedup fino a 12.5× rispetto a una baseline non ottimizzata. L'analisi evidenzia inoltre un impatto non lineare di LMUL sulle performance, con un valore ottimale (LMUL=2 per VLEN=256) che massimizza l'utilizzo della banda di memoria e riduce i cache miss. Il lavoro fornisce indicazioni pratiche per lo sviluppo di codice ad alte prestazioni su RISC-V e mette in luce le attuali limitazioni dei compilatori nell'ottimizzare automaticamente codice vettoriale su questa architettura.
