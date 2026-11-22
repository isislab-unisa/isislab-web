---
layout: seminar-detail
article_kind: seminar
lang: it
title: 'Seminar: MPI Collective Algorithm Selection in the Presence of Process Arrival Patterns of Majid Salimi'
date: '2024-09-18'
date_display: 18/09/2024
time: 08:00 - 17:00
location: ''
speakers:
- '9'
permalink: /seminars/seminar-mpi-collective-algorithm-selection-in-the-presence-of-pro-2024-09-18/
seminar_image: /assets/img/seminars/36841-5caca0b81c.jpg
---

The Message Passing Interface (MPI) is a programming model for developing high-performance applications on large-scale machines. A key component of MPI is its collective communication operations. While the MPI standard defines the semantics of these operations, it leaves the algorithmic implementation to the MPI libraries. Each MPI library contains various algorithms for each collective, and selecting the best algorithm typically relies on performance metrics obtained from micro-benchmarks. In such micro-benchmarks, processes are typically synchronized using an MPI Barrier before invoking a collective operation. However, in real-world scenarios, processes often arrive at a collective in diverse patterns, often due to resource contention. The performance of collective algorithms can vary significantly depending on the arrival pattern type.In this work, which is accepted in the IEEE CLUSTER 2024, we address the challenge of selecting the most efficient algorithm for a given collective, taking into account process arrival patterns. First, we demonstrate through a simulation study that arrival patterns significantly influence the choice of the optimal collective algorithm for specific communication instances. Second, we conduct a comprehensive micro-benchmark analysis to illustrate the sensitivity of MPI collectives to these arrival patterns. Third, we show that our innovative micro-benchmarking methodology is effective in selecting the best performing collective algorithm for real-world applications.
