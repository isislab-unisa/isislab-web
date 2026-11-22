---
layout: seminar-detail
article_kind: seminar
lang: it
title: Fine-grained Energy-Efficient Heterogeneous Computing of Kaijie Fan
date: '2023-11-09'
date_display: 09/11/2023
time: 12:00 - 12:00
location: ''
speakers:
- '9'
permalink: /seminars/fine-grained-energy-efficient-heterogeneous-computing-of-kaijie-f-2023-11-09/
seminar_image: /assets/img/seminars/14749-a6338f88a1.png
---

Energy-efficient computing uses power management techniques such as frequency scaling to save energy. Implementing energy-efficient techniques on large-scale computing systems is challenging for several reasons. While most modern architectures, including GPUs, are capable of frequency scaling, these features are often not available on large systems. In addition, achieving higher energy savings requires precise energy tuning because not only applications but also different kernels can have different energy characteristics. We propose SYnergy, a novel energy-efficient approach that spans languages, compilers, runtimes, and job schedulers to achieve unprecedented fine-grained energy savings on large-scale heterogeneous clusters. SYnergy defines an extension to the SYCL programming model that allows programmers to define a specific energy goal for each kernel. For example, a kernel can aim to minimize well-known energy metrics such as EDP and ED2P or to achieve predefined energy-performance tradeoffs, such as the best performance with 25% energy savings. Through compiler integration and a machine learning model, each kernel is statically optimized for the specific target. On large computing systems, a SLURM plugin allows SYnergy to run on all available devices in the cluster, providing scalable energy savings. The methodology is inherently portable and has been evaluated on both NVIDIA and AMD GPUs. Experimental results show unprecedented improvements in energy and energy-related metrics on real-world applications, as well as scalable energy savings on a 64-GPU cluster.
