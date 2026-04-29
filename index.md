---
layout: default
---

<p class="section-label">Recent posts</p>
<div class="post-list">
  {% for post in site.posts %}
  <a class="post-card" href="{{ post.url | relative_url }}" data-category="{{ post.category }}">
    <div class="post-meta">
      <span class="post-date">{{ post.date | date: "%b %-d, %Y" }}</span>
      {% if post.category %}
        <span class="post-tag {{ post.category | slugify }}">{{ post.category }}</span>
      {% endif %}
    </div>
    <h2>{{ post.title }}</h2>
    {% if post.excerpt %}
      <p>{{ post.excerpt | strip_html | truncatewords: 30 }}</p>
    {% endif %}
  </a>
  {% endfor %}
</div>
