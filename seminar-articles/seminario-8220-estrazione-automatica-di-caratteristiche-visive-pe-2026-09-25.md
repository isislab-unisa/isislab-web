---
layout: seminar-detail
article_kind: seminar
lang: it
title: 'Seminario: &#8220;Estrazione automatica di caratteristiche visive per l&#8217;analisi dello stato emotivo e dei disturbi
  psicologici&#8221; di Marco Battaglia'
date: '2026-09-25'
date_display: 25/09/2026
time: 12:00 - 13:00
location: Laboratorio ISISLab, Dipartimento di Informatica, Università di Salerno (Edificio F, Lab. 10, II piano), Via Giovanni
  Paolo II, 132, 84084 Fisciano SA, Fisciano
speakers:
- '9'
permalink: /seminars/seminario-8220-estrazione-automatica-di-caratteristiche-visive-pe-2026-09-25/
seminar_image: /assets/img/seminars/51208-5750298865.png
---

Negli ultimi anni, l'Affective Computing ha assunto un ruolo centrale nello sviluppo
di sistemi avanzati per l'interazione uomo-macchina, rendendo essenziale l'analisi
automatizzata e quantitativa delle espressioni facciali. Il presente lavoro di tesi illustra la
progettazione e lo sviluppo di una pipeline software modulare dedicata all'estrazione e
all'analisi di feature visive da flussi video, con l'obiettivo di generare serie temporali affidabili
per il riconoscimento degli stati emozionali. Il progetto si articola nello studio e
nell'integrazione di framework allo stato dell'arte per la computer vision, tra cui OpenFace e
Py-Feat. L'architettura implementata elabora i singoli frame video per eseguire il facial
landmark tracking, estraendo parametri spaziali (head pose e gaze) e quantificando
l'attivazione delle Action Units (AU) in conformità con il Facial Action Coding System (FACS).
Per garantire la robustezza e la stabilità dei dati estratti, è stata posta particolare attenzione
alla fase di preprocessing del segnale visivo. Sono state implementate tecniche di smoothing
per la riduzione del rumore algoritmico sui landmark e logiche di rilevamento con memoria di
stato (isteresi) per mitigare il jitter nelle micro-fluttuazioni delle action units. Il sistema
mappa infine le dinamiche di attivazione facciale in macro-espressioni ed emozioni discrete,
restituendo i dati in formati strutturati (JSON e fogli di calcolo) pronti per l'analisi statistica. I
risultati mostrano come l'approccio adottato, unendo strumenti di estrazione avanzati a
rigorose logiche di stabilizzazione del dato temporale, offra una soluzione efficace e scalabile.
Lo strumento sviluppato costituisce una base solida per la classificazione comportamentale
e apre la strada a futuri sviluppi nell'ambito dell'analisi multimodale in tempo reale.
