---
layout: seminar-detail
article_kind: seminar
lang: it
title: 'Seminari: &#8220;Estrazione automatica di caratteristiche visive per l&#8217;analisi dello stato emotivo e dei disturbi
  psicologici&#8221; Marco Battaglia e &#8220;GPU-Initiated Communication and Application Scalability: From Microbenchmarks
  to Conjugate Gradient Application&#8221; di Nicolás Merenda'
date: '2026-10-16'
date_display: 16/10/2026
time: 12:00 - 13:00
location: ''
speakers:
- '9'
permalink: /seminars/seminari-8220-estrazione-automatica-di-caratteristiche-visive-per-2026-10-16/
seminar_image: /assets/img/seminars/51283-7555d74687.jpg
---

1) Seminario di Marco Battaglia
" Estrazione automatica di caratteristiche visive per l'analisi dello stato emotivo e dei disturbi psicologici "

Abstract: L'affective computing riveste un ruolo importante nello sviluppo di sistemi capaci di interpretare gli stati emotivi a partire da postura ed espressività facciale. Questo lavoro di tesi presenta una pipeline in Python basata sulla libreria Py-Feat, integrata con un'interfaccia grafica, per l'analisi del volto a supporto dell'analisi quantitativa di segnali visivi in contesti clinici. Il sistema elabora flussi video acquisiti in contesti non controllati (in-the-wild), tracciando i landmark facciali, stimando l'orientamento del capo, quantificando l'attivazione delle Action Unit (FACS) e calcolando metriche derivate come l'Eye Aspect Ratio (EAR), generando serie temporali affidabili per la valutazione di stati emotivi e disturbi psicologici.
Per garantire la solidità del segnale, la fase di post-processing applica algoritmi di smoothing per mitigare il jitter delle micro-oscillazioni e maschere geometriche basate sul Mouth Aspect Ratio (MAR) per escludere movimenti legati al parlato. I dati estratti vengono infine riassunti in indicatori statistici ed esportati in formati strutturati (JSON e fogli di calcolo). Il proof of concept convalida l'efficacia e la scalabilità dell'architettura, ponendo le basi per futuri sistemi di supporto alle decisioni (DSS) e analisi multimodali in tempo reale.

2) Presentazione del lavoro di tesi di Nicolás Merenda

"GPU-Initiated Communication and Application Scalability: From Microbenchmarks to Conjugate Gradient Application "

Abstract:
In recent years, the growth of AI has led to increased use of GPUs across High Performance Computing (HPC) clusters. Large models often need multiple GPUs to fit in memory, shorten training time, and reduce inference latency. However, exchanging data and synchronizing work can leave GPUs idle, especially across nodes. This work analyzes when GPU-initiated communication improves performance over CPU-orchestrated communication. It then evaluates a real-world Conjugate Gradient solver to test whether benchmark results can help developers select a stack based on an application’s communication patterns.
A benchmark suite was developed to compare seven CUDA/SYCL stacks using MPI, NCCL, NVSHMEM, OSHMPI, and oneCCL, from individual communication patterns to application microbenchmarks. Experiments used up to 32 NVIDIA A100 GPUs across eight nodes of CINECA’s Leonardo supercomputer. This benchmark comparison also involved extending oneCCL with grouped NCCL send/receive operations and an OSHMPI backend, exposing these communication paths through a common interface.
The evaluation then moves to a complete application: the aCG Conjugate Gradient solver. An OSHMPI backend and a SYCL implementation with MPI or oneCCL reductions were developed and compared with its existing MPI, NCCL, and NVSHMEM variants while solving two large sparse linear systems. This comparison tests whether benchmark results help predict performance when communication is combined with computation.

No communication stack is fastest in every case. In repeated neighbour exchanges on eight nodes with four GPUs each, GPU-initiated NVSHMEM reaches 40.6 GB/s against 35.7 GB/s for CUDA MPI, while NCCL-based paths lead bulk collectives. SYCL solver times are 0.87–1.02 times native CUDA times within one node, and SYCL MPI continues strong scaling to 32 GPUs. Benchmark rankings do not always carry over when the solver introduces irregular exchanges and overlap with computation.

Together, the benchmark and aCG solver results show that improving performance requires choosing a communication stack suited to the application’s data exchanges, synchronization, and topology.
