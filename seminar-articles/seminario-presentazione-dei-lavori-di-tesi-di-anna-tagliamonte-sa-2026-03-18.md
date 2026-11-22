---
layout: seminar-detail
article_kind: seminar
lang: it
title: 'Seminario: Presentazione dei lavori di tesi di  Anna Tagliamonte, Salvatore Sirica e Sergio Guastaferro'
date: '2026-03-18'
date_display: 18/03/2026
time: 17:00 - 18:00
location: Laboratorio ISISLab, Dipartimento di Informatica, Università di Salerno (Edificio F, Lab. 10, II piano), Via Giovanni
  Paolo II, 132, 84084 Fisciano SA, Fisciano
speakers:
- '9'
permalink: /seminars/seminario-presentazione-dei-lavori-di-tesi-di-anna-tagliamonte-sa-2026-03-18/
seminar_image: /assets/img/seminars/50905-e43328298c.png
---

1) "Dall’identità al codice: avatar su misura tra Makehuman e Unity nella pipeline 3Dify" di Anna Tagliamonte

Abstract:
La tesi si concentra sullo sviluppo di un sistema interattivo per la generazione e la personalizzazione di avatar digitali 3D. L’obiettivo è di trasformare parametri numerici in identità virtuali e offrire un’esperienza utente flessibile e realistica. Il lavoro si concentra sull’integrazione del sistema Unity multipurpose avatar (UMA) all’interno della pipeline esistente di 3Dify, un framework per la generazione automatica di avatar personalizzati a partire da parametri provenienti da Makehuman. Dopo un’analisi approfondita delle corrispondenze tra gli slider dei due ambienti, è stato sviluppato un sistema in Unity in grado di fare mapping tra i due e applicare dinamicamente le caratteristiche antropometriche. La tesi unisce fasi di ricerca, modellazione 3D e sviluppo software, con particolare attenzione agli aspetti di interazione e user experience. Il fine ultimo è di migliorare l’adattabilità e l’efficacia della pipeline esistente per scenari applicativi futuri.

2) "Enabling Portable Collective Communication on Heterogeneous GPU Systems" di Salvatore Sirica

Abstract:
Many distributed HPC applications and data-parallel AI training pipelines depend on MPI-style communication patterns. As systems scale to many GPUs and nodes, collective operations like Allreduce become a primary performance bottleneck, directly impacting scalability. In practice, the highest-performing GPU collectives are typically provided by vendor-specific libraries such as NVIDIA NCCL and AMD RCCL, which exploit hardware and topology-aware optimizations but reduce portability across heterogeneous clusters.

Intel oneAPI Collective Communications Library (oneCCL) is uniquely positioned to mitigate this issue thanks to its SYCL-based interface. However, deep in its implementation it is tightly coupled to Intel Level Zero, effectively preventing execution on non-Intel GPUs.

This work enables portable GPU collectives within oneCCL by introducing NCCL and RCCL as pluggable backends while preserving the existing oneCCL user-facing API. The integration reuses oneCCL’s bootstrap mechanisms to initialize vendor communicators and dispatches collectives on native GPU streams through SYCL interoperability. Micro-benchmarks on the UNISA-HPC cluster with NVIDIA A100 GPUs show that oneCCL+NCCL achieves performance close to native NCCL for key collectives across a broad range of message sizes and data types.

2) "Vettorizzazione Esplicita del Prodotto Matriciale su RISC-V con RVV" di Sergio Guastaferro
Abstract:
Il prodotto matriciale rappresenta un'operazione fondamentale nel calcolo ad alte prestazioni, alla base di framework per l'intelligenza artificiale, simulazioni scientifiche e analisi dati. Con l'emergere di RISC-V come architettura aperta e modulare, diventa cruciale valutare l'efficacia delle sue estensioni vettoriali (RVV) nell'accelerare operazioni numericamente intensive come il prodotto matriciale.

Questa tesi analizza sistematicamente le performance del prodotto matriciale su processori RISC-V dotati di supporto vettoriale, confrontando la vettorizzazione automatica offerta dai compilatori e una vettorizzazione esplicita realizzata mediante intrinseche RVV. L'implementazione proposta si basa su microkernel ottimizzati con formulazione a prodotto esterno, tiling progressivo e gestione dinamica della lunghezza vettoriale a runtime. Un'attenzione particolare è dedicata all'esplorazione del parametro LMUL, che regola il parallelismo vettoriale in relazione alla configurazione hardware (VLEN).

I risultati sperimentali, ottenuti sul processore Spacemit X60 a 8 core, dimostrano che la vettorizzazione esplicita supera significativamente l'approccio automatico, raggiungendo speedup fino a 12.5× rispetto a una baseline non ottimizzata. L'analisi evidenzia inoltre un impatto non lineare di LMUL sulle performance, con un valore ottimale (LMUL=2 per VLEN=256) che massimizza l'utilizzo della banda di memoria e riduce i cache miss. Il lavoro fornisce indicazioni pratiche per lo sviluppo di codice ad alte prestazioni su RISC-V e mette in luce le attuali limitazioni dei compilatori nell'ottimizzare automaticamente codice vettoriale su questa architettura.
