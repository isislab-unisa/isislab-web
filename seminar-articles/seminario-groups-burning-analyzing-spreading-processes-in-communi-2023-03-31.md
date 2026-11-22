---
layout: seminar-detail
article_kind: seminar
lang: it
title: 'Seminario: Groups Burning: Analyzing Spreading Processes in Community-based Networks di Gennaro Cordasco'
date: '2023-03-31'
date_display: 31/03/2023
time: 12:00 - 12:00
location: ''
speakers:
- '9'
permalink: /seminars/seminario-groups-burning-analyzing-spreading-processes-in-communi-2023-03-31/
seminar_image: /assets/img/seminars/13226-0c4ccbe509.jpg
---

Graph burning is a deterministic, discrete-time process that can be used to model how influence or contagion spreads in a graph. In the graph burning process, each node starts as dormant, and becomes informed/burned over time; when a node is burned, it remains burned until the end of the process. In each round, one can burn a new node (source of fire) in the network. Once a node is burned in round $t$, in round $t+1$, each of its dormant neighbors becomes burned. The process ends when all nodes are burned; the goal is to minimize the number of rounds.
We study a variation of graph burning in order to model spreading processes in community-based networks. With respect to a specific piece of information, a community is {\em satisfied} when this information reaches at least a prescribed number of its members. Specifically, we consider the problem of identifying a minimum length sequence of nodes that, according to a graph burning process, allows to satisfy all the communities of the network.
We investigate this NP-hard problem from an approximation point of view, showing both a lower bound and a matching upper bound. We also investigate the case when the number of communities is constant and show how to solve the problem with a constant approximation factor.
Moreover, we consider the problem of maximizing the number of satisfied groups, given a budget $k$ on the number of rounds.
