---
layout: seminar-detail
article_kind: seminar
lang: it
title: 'Seminar: &#8220;EMPI: Enhanced Message Passing Interface in Modern C++&#8221; of Majid Salimi Beni'
date: '2023-05-26'
date_display: 26/05/2023
time: 16:00 - 17:00
location: ''
speakers:
- '9'
permalink: /seminars/seminar-8220-empi-enhanced-message-passing-interface-in-modern-c-2023-05-26/
seminar_image: /assets/img/seminars/13272-e5af71aa87.png
---

Message Passing Interface (MPI) is a well-known standard for programming distributed and HPC systems. While the community has been continuously improving MPI to address the requirements of next-generation architectures and applications, its interface has not substantially evolved. In fact, MPI only provides an interface to C and Fortran and does not support recent features of modern C++. Moreover, MPI programs are error-prone and subject to different syntactic and semantic errors.

In this presentation, I talk about our recent work, EMPI, an Enhanced Message Passing Interface based on modern C++, which is directly mapped to the OpenMPI implementation and exploits modern C++ for safe and efficient distributed programming. EMPI proposes novel C++ RAII-based semantics and constant specialization to prevent error-prone code patterns such as parameter mismatch and reduce the overhead of handling multiple objects and per-invocation time. Scaling up to 1024 processes showed that EMPI's performance is very similar to native MPI and considerably faster than the MPL C++ interface.
