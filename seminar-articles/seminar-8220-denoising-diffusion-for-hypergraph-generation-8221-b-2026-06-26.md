---
layout: seminar-detail
article_kind: seminar
lang: it
title: 'Seminar: &#8220;Denoising Diffusion for Hypergraph Generation&#8221; by Valerio Di Pasquale'
date: '2026-06-26'
date_display: 26/06/2026
time: 15:00 - 16:00
location: ''
speakers:
- '9'
permalink: /seminars/seminar-8220-denoising-diffusion-for-hypergraph-generation-8221-b-2026-06-26/
seminar_image: /assets/img/seminars/51157-c841f7e8ba.png
---

Hypergraphs make it possible to model higher-order relationships that standard graphs are unable to express. However, producing realistic hypergraphs is still difficult, since current approaches often depend on predefined structural constraints or fail to capture the intertwined dependencies between nodes and hyperedges. We present Janus, a latent diffusion-based framework that partitions an observed hypergraph into sub-hypergraphs, learns joint latent representations of nodes and hyperedges using a dual-view β-VAE, and synthesizes new hypergraph structures through paired latent diffusion guided by cross-view conditioning. The framework can perform both unconstrained generation and generation conditioned on a given node set. We further propose an evaluation protocol that assesses interactions at micro, meso, and macro levels, together with structural reconstruction and higher-order similarity metrics. Experiments on five real-world datasets against nine baselines show that Janus delivers the most consistent performance across structural scales, achieving notable improvements in meso-scale and higher-order fidelity. Under node-set constraints, it also consistently attains the strongest reconstruction performance.
