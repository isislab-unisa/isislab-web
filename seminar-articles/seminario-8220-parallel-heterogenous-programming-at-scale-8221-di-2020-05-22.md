---
layout: seminar-detail
article_kind: seminar
lang: it
title: 'Seminario: &#8220;Parallel Heterogenous Programming at Scale&#8221; di Biagio Cosenza'
date: '2020-05-22'
date_display: 22/05/2020
time: 16:00 - 17:00
location: ''
speakers:
- '9'
permalink: /seminars/seminario-8220-parallel-heterogenous-programming-at-scale-8221-di-2020-05-22/
seminar_image: /assets/img/seminars/10682-6365f7f569.png
---

"The pursuit of high performance and energy efficiency led to the emergence of heterogeneous computing, where different parts of an application benefit from specialized hardware better suited for the problem. Hardware accelerators such as GPUs, FPGAs, and many-core CPUs are used as co-processors resulting in heterogeneous architectures.

This talk introduces SYCL, a royalty-free open standard published by the Khronos Group intended for programming a wide range of heterogeneous architectures. Its high-level single-source programming model combines the portability of OpenCL with modern C++ constructs and idioms. In SYCL, scheduling, data management, and synchronization are handled implicitly by the SYCL runtime, increasing programmer productivity.

This talk will also present the Celerity programming environment, which builds on the top of SYCL and allow C++ applications to target cluster of accelerators. By having users provide minimal information about how data is accessed within compute kernels, Celerity automatically distributes work and data. The Celerity prototype runtime implementation is shown to have comparable performance to more traditional approaches to distributed memory accelerator programming, such as MPI+OpenCL, with significantly lower implementation overhead."
