---
layout: default
permalink: /papers/
title: Accepted Papers
---

# Accepted Papers 

See all accepted papers on [OpenReview](https://openreview.net/group?id=auai.org/UAI/2024/Workshop/TPM).

<ul>
{% assign sortedPapers = site.data.papers | sort: 'title' %}
{% for item in sortedPapers %}
  <li><strong>{{ item.title }}</strong>
  <br/>
  <small><i>{{ item.authors }}</i></small></li>
{% endfor %}
</ul>
