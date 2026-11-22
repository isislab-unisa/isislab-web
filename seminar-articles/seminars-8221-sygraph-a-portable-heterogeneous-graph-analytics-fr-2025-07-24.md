---
layout: seminar-detail
article_kind: seminar
lang: it
title: 'Seminars:&#8221;SYgraph: A Portable Heterogeneous Graph Analytics Framework for GPUs&#8221; by Antonio De Caro &#8211;
  &#8220;Phase-based Frequency Scaling for Energy-efficient Heterogeneous Computing by Lorenzo Carpentieri'
date: '2025-07-24'
date_display: 24/07/2025
time: 14:00 - 15:00
location: ''
speakers:
- '9'
permalink: /seminars/seminars-8221-sygraph-a-portable-heterogeneous-graph-analytics-fr-2025-07-24/
seminar_image: /assets/img/seminars/50474-fbe4341247.png
---

Speaker : Antonio De Caro

Title : SYgraph: A Portable Heterogeneous Graph Analytics Framework for GPUs

Abstract: Graph analytics play a crucial role in a wide range of fields, including social network analysis, bioinformatics, and scientific computing, due to their ability to model and explore complex relationships. However, optimizing graph algorithms is inherently difficult due to their memory-bound constraints, often resulting in poor performance on modern massively parallel hardware. In addition, most state-of-the-art implementations are designed in CUDA for NVIDIA GPUs, and thus they can not run on supercomputers equipped with AMD and Intel GPUs.
To address these challenges, we propose SYgraph, a portable heterogeneous graph analytics framework written in SYCL.
SYgraph provides an efficient two-layer bitmap data layout optimized for GPU memory, eliminates the need for pre- or post-processing steps, and abstracts the complexity of working with diverse target platforms.
Experimental results demonstrate that SYgraph delivers competitive performance against state-of-the-art frameworks on datasets with up to 21 million nodes and 530 million edges on NVIDIA GPUs while being able to target any SYCL-supported device, such as AMD and Intel GPUs.
Speaker: Lorenzo Carpentieri

Title :
Phase-based Frequency Scaling for Energy-efficient Heterogeneous Computing

Abstract:
Energy efficiency has been a major challenge for exascale computing. Frequency scaling is a powerful technique to achieve energy savings in modern heterogeneous systems, and can be applied either at a coarse granularity, by application, or at a fine granularity, by setting the frequency for each computational kernel.
The chosen granularity significantly impacts the performance and energy consumption of applications due to frequency-change overhead.

We propose a novel phase-based method that minimizes the frequency-change overhead and improves performance and energy efficiency on heterogeneous multi-GPU systems.
Our approach detects different phases through application profiling and DAG analysis, and sets an optimal frequency for each phase.
Our methodology also considers MPI programs, where the overhead can be hidden by overlapping frequency-change with communication.
Experimental results show up to 37% energy saving and 1.87x speedup for various benchmarks on a single GPU, and 68% energy saving and 3.63 x speedup on two multi-GPU applications.
