---
layout: seminar-detail
article_kind: seminar
lang: it
title: Seminario:&#8221;Towards a SYCL API for Approximate Computing&#8221; di Lorenzo Carpentieri
date: '2023-06-16'
date_display: 16/06/2023
time: 16:00 - 17:00
location: ''
speakers:
- '9'
permalink: /seminars/seminario-8221-towards-a-sycl-api-for-approximate-computing-8221-2023-06-16/
seminar_image: /assets/img/seminars/13292-5ba9081ad1.png
---

Approximate computing exploits the gap between the accuracy provided by a system and the accuracy required by an application. Many applications such as image processing and neural networks, are tolerant of a certain amount of error, and have the potential for significant improvements in terms of execution time and energy consumption if a small amount of error can be accepted. The most advanced software approximation techniques are mixed precision, which uses a lower precision data representation for both integer and floating point variables; perforation, which exploits data locality by skipping some iterations and assuming that nearby data have similar values; and relaxed synchronization.
In this talk, we present SYprox, a SYCL-based API supporting a broad set of approximation techniques in modern C++.
SYprox introduces a set of semantics that extend SYCL’s buffers and accessors to provide a high-level easy-to-use programming API.
SYprox’s approximation framework seamlessly adds three additional stages to standard computational processing implementing perforation, input reconstruction and output reconstruction. It supports data perforation and elision patterns for efficient approximation, as well as signal reconstruction algorithms for error mitigation.
Finally, we present our preliminary results, showing improvements in terms of performance and accuracy over to state-of-the-art approaches, while maintaining at the same time a high-level programming approach.
