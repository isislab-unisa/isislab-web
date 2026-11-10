---
layout: project

# IDENTIFICATION
title: "LibreRT"
lang: en
permalink: /en/progetti/librert/
translation_url: /progetti/librert/

# SUBTITLE
subtitle: "Portable Heterogenous Real-time Programming for the Embedded Computing Continuum"

# DATES
date: 2023-09-28
start_date: 2023-09-28
end_date: 2025-09-28

# FUNDING PROGRAMME
program: prin-mur

types: 
  - embedded-edge-computing
  - real-time-optimization

# ROLE AND PARTNERS
role: "Research unit"

partners:
  - "University of Salerno"
  - "Politecnico di Milano (Polytechnic University of Milan)"

# FUNDING
funding: "PRIN 2022 – Italian Ministry of University and Research (MUR)"

# WEBSITE AND IMAGES
image: "/assets/media/c3d209fe6e0441-logo-librert-2.png"

logos:
  - /assets/media/d4338e80706013-mur-logo.png
  - /assets/media/44583057a10036-italy-1.png
  - /assets/media/c3d209fe6e0441-logo-librert-2.png

# ADDITIONAL LINKS
links:
  - label: "LibreRT official project website"
    url: "https://librert.di.unisa.it/"

# DESCRIPTION
description: >
  LibreRT (Portable Heterogenous Real-time Programming for the Embedded
  Computing Continuum) is a research project funded under the PRIN 2022
  call. It aims to develop a portable system software stack for programming
  heterogeneous embedded systems, capable of delivering high performance,
  responsiveness and real-time guarantees across the embedded computing
  continuum.

published: true
---

## Objectives

Emerging paradigms such as the Industrial Internet of Things (IIoT) and edge computing, together with the growing adoption of applications involving machine learning and image processing, have increased the demand for embedded systems that combine high computational performance with strict responsiveness and real-time requirements.

LibreRT aims to provide a portable system software stack capable of supporting highly responsive, real-time and high-throughput computing across the embedded computing continuum.

## Activities and Technologies

The project addresses the challenges of programming heterogeneous embedded systems equipped with low-power CPUs and GPUs. Such architectures are increasingly widespread in domains ranging from wearable devices and mobile computing to automotive systems.

In particular, LibreRT proposes:

- A **SYCL-based** programming model with extensions for real-time support.
- Priority-based scheduling mechanisms for CPUs and GPUs, including preemption support.
- Approximate computing techniques, mixed precision and GPU kernel perforation.
- A programming model based on modern **C++** semantics and advanced runtime systems.
- Support for integrated GPUs.
- **Miosix** for micro-edge devices and traditional Linux distributions for deep-edge and meta-edge devices.
- An autotuning layer to adaptively optimise approximation accuracy while meeting real-time constraints.

## Collaboration

The project involves two research units:

- **University of Salerno** – Biagio Cosenza, fixed-term researcher.
- **Politecnico di Milano (Polytechnic University of Milan)** – Federico Terraneo, fixed-term researcher.

The research activities build on the collaboration between the two universities, combining expertise in computer architecture, embedded systems, operating systems and parallel programming.

## Expected Results

LibreRT aims to develop a portable software environment for the efficient programming of heterogeneous embedded architectures.

Expected results include:

- Programming models and runtime systems suitable for real-time applications.
- CPU and GPU schedulers supporting preemption.
- Adaptive approximate computing techniques.
- Autotuning mechanisms to balance computational accuracy and real-time constraints.
- Improved application portability across the embedded computing continuum.

## Funding Information

- **Call:** PRIN – Projects of Relevant National Interest, 2022.
- **Funding body:** Italian Ministry of University and Research (MUR).
- **Reported funding amount:** €100,480.
- **Duration:** 24 months.
- **Period:** 28 September 2023 – 28 September 2025.
- **Main ERC field:** PE – Physical Sciences and Engineering.
- **ERC subfields:**
  - PE6_3 – Software engineering, programming languages and systems.
  - PE6_1 – Computer architecture, embedded systems, operating systems.
  - PE6_2 – Distributed systems, parallel computing, sensor networks, cyber-physical systems.
