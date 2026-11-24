---
layout: page
lang: en
title: News and Insights
description: Latest news, activities and insights from ISISLab.
permalink: /en/news-and-insights/
section: Page
article_kind: imported_page
custom_css:
  - /assets/css/info-box.css
---

{% assign entries = site.pages | where: 'article_kind', 'news' | where: 'lang', 'en' | where_exp: 'item', 'item.archive_hidden != true' | sort: 'date' | reverse %}

<section class="news-intro">
  <h2>Latest news</h2>

  <p>
    Discover the latest news and activities from ISISLab:
    research projects, scientific achievements, collaborations,
    events and initiatives.
  </p>
</section>

<section class="media-archive" aria-label="Latest news">
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
          <a class="archive-read" href="{{ item.url | relative_url }}">Read more →</a>
        </div>
      </article>
    {% endfor %}
  </div>

  <p class="news-archive-link">
    <a href="{{ '/en/news/' | relative_url }}">View all news →</a>
  </p>
</section>