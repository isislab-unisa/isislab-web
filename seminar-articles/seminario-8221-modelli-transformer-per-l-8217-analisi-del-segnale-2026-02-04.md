---
layout: seminar-detail
article_kind: seminar
lang: it
title: 'Seminario:&#8221;Modelli Transformer per l&#8217;Analisi del Segnale Vocale: Potenziale, Limiti e Applicabilità Clinica&#8221;
  di Marco Renella'
date: '2026-02-04'
date_display: 04/02/2026
time: 14:30 - 15:30
location: Laboratorio ISISLab, Dipartimento di Informatica, Università di Salerno (Edificio F, Stecca 7, Lab. 10, II piano)
  &#8211; Via Giovanni Paolo II, 132, 84084 Fisciano (SA)
speakers:
- '9'
permalink: /seminars/seminario-8221-modelli-transformer-per-l-8217-analisi-del-segnale-2026-02-04/
seminar_image: /assets/img/seminars/50742-462808c8ff.png
---

La voce è un biomarcatore non invasivo dello stato neurologico e cognitivo. Alterazioni nella stabilità del pitch, nel ritmo articolatorio e nelle caratteristiche prosodiche sono documentate in depressione, Alzheimer e declino cognitivo, rendendo l'analisi del parlato un potenziale strumento per l'identificazione precoce di patologie neurodegenerative. Gli approcci di machine learning classico — basati su feature ingegnerizzate e modelli intrinsecamente interpretabili come Random Forest — sono attualmente impiegati in ambito clinico, ma mostrano limiti nella cattura di dipendenze temporali complesse e nella rilevazione di pattern sottili che potrebbero emergere in fase preclinica, prima che la malattia diventi clinicamente rilevante.

Questo studio indaga se e come architetture Transformer possano superare i limiti prestazionali dei metodi classici mantenendo applicabilità clinica. Il punto di partenza è un confronto concreto: durante il tirocinio, un approccio Random Forest con feature ingegnerizzate ha raggiunto balanced accuracy ~0.65 su 134 soggetti. Partendo da questo baseline, si studia come i Transformer — modelli progettati per catturare dipendenze temporali — si comportino su dati vocali di dimensioni clinicamente realistiche.
Il lavoro combina analisi compilativa della letteratura con validazione empirica: si testa l'efficacia di encoder pre-addestrati (HuBERT) nel mitigare la scarsità di dati, si confronta la modellazione temporale end-to-end con l'aggregazione di feature statiche, e si applicano tecniche di explainable AI per valutare l'interpretabilità clinica delle decisioni. I risultati mostrano sia potenziale — dove il pre-training offre rappresentazioni utili — sia limiti concreti: requisiti di memoria, instabilità su fold di cross-validation per dataset troppo piccoli, e il trade-off tra complessità e trasparenza. Il contributo sta nel caratterizzare questo spazio di progettazione per applicazioni reali, fornendo indicazioni operative su come combinare capacità rappresentativa e responsabilità clinica nell'uso di biomarcatori vocali.
