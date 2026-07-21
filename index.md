---
layout: home
---

欢迎来访。文章列表：

{% for post in site.posts %}
  {% unless post.categories contains 'trip' %}
- [{{ post.title }}]({{ post.url }}) — {{ post.date | date: "%Y-%m-%d" }}
  {% endunless %}
{% endfor %}