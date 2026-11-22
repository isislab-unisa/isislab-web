---
layout: seminar-detail
article_kind: seminar
lang: it
title: 'Seminar by Antonio De Caro: SIGMo: High-Throughput Batched Subgraph Isomorphism on GPUs for Molecular Matching'
date: '2025-10-31'
date_display: 31/10/2025
time: 00:30 - 13:00
location: Laboratorio ISISLab, Dipartimento di Informatica, Università di Salerno (Edificio F, Stecca 7, Lab. 10, II piano)
  &#8211; Via Giovanni Paolo II, 132, 84084 Fisciano (SA)
speakers:
- '9'
permalink: /seminars/seminar-by-antonio-de-caro-sigmo-high-throughput-batched-subgraph-2025-10-31/
seminar_image: /assets/img/seminars/50607-d1a97644c8.png
---

Abstract . Subgraph isomorphism is a fundamental graph problem with applications in diverse domains from biology to social network analysis. Of particular interest is molecular matching, which uses a subgraph isomorphism formulation for the drug discovery process. While subgraph isomorphism is known to be NP-complete and computationally expensive, in the molecular matching formulation a number of domain constraints allow for efficient implementations. This paper presents SIGMo, a high-throughput, portable subgraph isomorphism framework for GPUs, specifically designed for batch molecular matching. SIGMo takes advantage of the specific domain formulation to provide a more efficient filter-and-join strategy: the framework introduces a novel multi-level iterative filtering technique based on neighborhood signature encoding to efficiently prune candidates prior to a GPU-optimized join phase using a stack-based DFS traversal. The GPU implementation is written in SYCL, allowing portable execution on AMD, Intel, and NVIDIA GPUs. Our experimental evaluation on a large dataset from ZINC demonstrates up to 1470\times speedup over state-of-the-art subgraph isomorphism frameworks, and achieves a throughput of 7.7 billion matches per second on a cluster with 256 GPUs.

Venue . SC'25: International Conference for High Performance Computing, Networking, Storage, and Analysis
