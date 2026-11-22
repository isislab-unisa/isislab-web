---
layout: seminar-detail
article_kind: seminar
lang: it
title: 'Seminar by  Mohammad Vazirpanah: &#8220;A Performance Analysis of Autovectorization on RVV RISC-V Boards&#8221; and
  Seminar by Giuseppe Pagano: &#8220;A Quantitative Analysis of Power of Two Quantization on Modern Hardware&#8221;'
date: '2025-02-14'
date_display: 14/02/2025
time: 14:30 - 15:30
location: ''
speakers:
- '9'
permalink: /seminars/seminar-by-mohammad-vazirpanah-8220-a-performance-analysis-of-aut-2025-02-14/
seminar_image: /assets/img/seminars/49884-2aea5025f6.png
---

Seminar by Mohammad Vazirpanah : " A Performance Analysis of Autovectorization on RVV RISC-V Boards "

Abstract : "The RISC-V instruction set architecture has become increasingly popular due to its open source and extensible design, making it a competitive choice in high-performance computing and embedded systems. The RISC-V Vector extension (RVV) empowers RISC-V processors with length-agnostic vectorization capabilities, a critical feature for efficiently handling parallel processing demands across different hardware. Compiler support for autovectorization allows to generate vector instructions automatically without requiring any effort to programmers. Given the limited yet evolving compiler support for RVV, this paper offers an in-depth examination of autovectorization capabilities in GCC and LLVM, for RVV version 0.7 and 1.0. We evaluated the autovectorization performance of LLVM, LLVM-EPI and GCC compilers across 151 loops from the Test Suite for VectorizingCompilers (TSVC) ans seven real-world applications on the All-Winner D1 and BananaPi-F3 boards, representing RISC-V vector hardware. Our study focuses on quantifying and comparing the level of vectorization each compiler achieves across a diverse range of vectorization patterns and workloads, providing insight into their strengths and limitations with respect to RISC-V RVV.

Our findings highlight that the LLVM-19 compiler outperforms GCC-14 in 76 out of 151 loops, and its performance is more sensitive to the selection of vector length. Additionally, tuning the vector Length Multiplier (LMUL) parameter can lead to performance improvements of up to 3x, and leveraging knowledge of the vector length can further enhance LMUL optimization in compilers."

Seminar by Giuseppe Pagano : " A Quantitative Analysis of Power of Two Quantization on Modern Hardware "

Abstract : " The rising use of AI in the last few years has greatly reshaped day-to-day productivity in many industries and caused a surge in the demand for AI-capable hardware. To reduce the imposing requirements that running a state of the art model entails many quantization techniques have been introduced.Among them there is Power of Two Quantization (PoTQ) a novel quantization technique that replaces multiplications with bitwise shifts operations.

In this seminar we'll go over the details of PoTQ, the algorithms used to leverage it in order to improve performance thanks to it and what are the plans to measure its impact on modern hardware."
