---
layout: page
lang: it
title: Notizie ed approfondimenti
description: News in ISISLAb
permalink: /notizie-e-approfondimenti/
alt_url: /en/news-and-insights/
section: Pagina
custom_css:
  - /assets/css/info-box.css
---


{% assign entries = site.pages | where: 'article_kind', 'news' | where: 'lang', 'it' | where_exp: 'item', 'item.archive_hidden != true' | sort: 'date' | reverse %}

<section class="news-intro">
  <h2>Ultime notizie</h2>

  <p>
    Scopri le attività e gli aggiornamenti di ISISLab:
    progetti di ricerca, risultati scientifici, collaborazioni,
    eventi e iniziative del laboratorio.
  </p>

  <p>
    Per approfondire le attività del laboratorio, visita anche
    la sezione dedicata ai
    <a href="{{ '/seminari/' | relative_url }}">seminari</a>.
  </p>
</section>

<section class="media-archive" aria-label="Ultime notizie">
  <div class="news-list">
    {% for item in entries limit:3 %}
      {% assign local_img = item.local_thumbnail_image | default: site.data.media_thumbs[item.feature_source_image] | default: item.local_hero_image | default: site.data.media_local[item.feature_source_image] | default: '/assets/img/news-placeholder.svg' %}

      <article class="news-list-item">
        <a class="archive-thumb" href="{{ item.url | relative_url }}">
          <img class="article-small-img" src="{{ local_img | relative_url }}" alt="" loading="lazy" decoding="async">
        </a>
        <div class="archive-item-copy">
          <time datetime="{{ item.date }}">{{ item.date | date: '%d/%m/%Y' }}</time>
          <h3><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h3>
          <p>{{ item.description | strip_html | truncate: 210 }}</p>
          <a class="archive-read" href="{{ item.url | relative_url }}">Leggi la notizia →</a>
        </div>
      </article>
    {% endfor %}
  </div>

  <p class="news-archive-link">
    <a href="{{ '/news/' | relative_url }}">Consulta l'archivio completo delle news →</a>
  </p>
</section>