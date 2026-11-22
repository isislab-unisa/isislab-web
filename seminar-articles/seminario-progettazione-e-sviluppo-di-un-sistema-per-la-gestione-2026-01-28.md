---
layout: seminar-detail
article_kind: seminar
lang: it
title: 'Seminario: Progettazione e sviluppo di un sistema per la gestione, l’analisi e il rilevamento di anomalie in dati
  sensoriali e visivi di Mihaela Bianca Maienza'
date: '2026-01-28'
date_display: 28/01/2026
time: 16:00 - 17:00
location: ''
speakers:
- '9'
permalink: /seminars/seminario-progettazione-e-sviluppo-di-un-sistema-per-la-gestione-2026-01-28/
seminar_image: /assets/img/seminars/50728-8703a1967d.png
---

La crescente diffusione di sistemi di monitoraggio basati su sensori e dispositivi di acquisizione
visiva ha reso centrale la necessità di gestire, analizzare e interpretare grandi volumi di dati
eterogenei in modo automatico ed affidabile. In questo contesto, la presente tesi propone Packillucens Sync, un sistema modulare per la raccolta, l’archiviazione, l’analisi esplorativa e il
rilevamento automatico di anomalie in dati ambientali e visivi acquisiti in parallelo.

Il sistema integra dati provenienti da sensori ambientali (temperatura, umidità, pressione e luce), sensori del suolo (temperatura, umidità, conducibilità elettrica e pH), sensori NPK (azoto, fosforo e potassio) e immagini acquisite nel tempo. I dati vengono sincronizzati da un archivio cloud, preprocessati e archiviati in un database relazionale PostgreSQL, progettato per garantire
coerenza temporale, tracciabilità delle sessioni di acquisizione e integrazione tra misure numeriche e contenuti visivi.

La pipeline di analisi include una fase di analisi esplorativa dei dati (EDA), finalizzata a individuare pattern temporali, correlazioni tra variabili e problematiche di qualità del dato, e una fase di rilevamento delle anomalie basata su tecniche di apprendimento automatico non supervisionato.
Per i dati sensoriali vengono implementati e confrontati due approcci complementari: un LSTM Autoencoder, in grado di modellare l’andamento temporale delle serie multivariate, e un One-Class Support Vector Machine, applicato a feature temporali estratte automaticamente. Le anomalie vengono identificate come deviazioni significative rispetto al comportamento appreso durante una fase di addestramento su dati considerati normali.
Per i dati visivi, le immagini vengono ricostruite in sequenze video e analizzate tramite l’estrazione di un motion index basato su optical flow, successivamente utilizzato come input per un LSTM Autoencoder dedicato al rilevamento di anomalie nel movimento.

L’intero sistema è progettato come una pipeline end-to-end automatizzabile, capace di generare report, visualizzazioni e confronti tra modelli. I risultati mostrano come l’integrazione di approcci differenti consenta un’analisi più robusta e interpretabile, evidenziando il potenziale del sistema come supporto al monitoraggio intelligente e all’individuazione precoce di comportamenti anomali.
