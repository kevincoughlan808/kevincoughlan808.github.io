---
layout: default
---

# Welcome to My Blog

This is where I'll journal my progress and share updates.

## Recent Posts

{% for post in site.posts %}
- [{{ post.title }}]({{ post.url }}) - {{ post.date | date: "%B %d, %Y" }}
{% endfor %}