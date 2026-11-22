---
layout: seminar-detail
article_kind: seminar
lang: it
title: 'Seminari: &#8220;FLY: definizione di problemi su reti in ambiente multi-cloud&#8221; di Simone Bisogno ed &#8220;Implementing
  reduce collective operation on gpu for hydrodynamics simulation&#8221; di Francesco De Simone'
date: '2021-03-19'
date_display: 19/03/2021
time: 15:00 - 16:00
location: ''
speakers:
- '9'
permalink: /seminars/seminari-8220-fly-definizione-di-problemi-su-reti-in-ambiente-mul-2021-03-19/
seminar_image: /assets/img/seminars/11509-710c4c3ec9.png
---

(1) "FLY: definizione di problemi su reti in ambiente multi-cloud" di Simone Bisogno

Abstract : FLY è un linguaggio di programmazione domain-specific per il calcolo scientifico su multi-cloud che astrae l'utente dall'interazione diretta con il cloud provider facilitando lo sviluppo di applicazioni. In questo seminario verrà presentata l'integrazione dei grafi all'interno di FLY, una struttura dati che cosente di modellare reti, ovvero relazioni tra oggetti appartenenti alla medesima classe. Ciò è stato possibile selezionando le migliori librerie di manipolazione grafi per i linguaggi su cui si basa FLY; in particolare JGraphT per quanto riguarda Java e NetworkX per Python; a partire da esse, è stata definito come API comune un sottoinsieme minimale dell'intersezione degli API delle due librerie, successivamente implementato in due classi Java e Python. L'implementazione così ottenuta è stata integrata nella fase di generazione di codice FLY al fine di permettere all'utente di utilizzare nei programmi FLY i metodi di API come se fossero nativi del linguaggio. L'integrazione del grafo come struttura dati all'interno di FLY permette così all'utente di definire facilmente problemi su reti e di eseguirli su cloud definendo semplicemente l'ambiente di esecuzione, senza necessità di ulteriori configurazioni.

(2)Implementing reduce collective operation on gpu for hydrodynamics simulation di Francesco De Simone

Abstract : In my thesis work, I analyze some techniques to improve data communication in GPU clusters using the high-level programming model Celerity. A part of my work is focused on analyzing collective patterns such as reductions. As reduction is not yet included in Celerity I implemented a reduction prototype on top of it and tested in a number of computational kernel extract from the hydrodynamic simulation code Cloverleaf. I compare my result with other solution to check what advantage I can get using a high-level programming model. Il collegamento alla ISISLab community della piattaforma Discord è disponibile qui o anche utilizzando il seguente QR Code:

ISISLab Community

Il seminario si terrà sul canale vocale # seminars della piattaforma Discord è disponibile qui o utilizzando il seguente QR Code:

ISISLab Seminars in Discord
