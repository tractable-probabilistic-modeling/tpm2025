---
layout: default
permalink: /papers/
title: Accepted Papers
---


# Accepted Papers 

You can see all accpeted papers on [OpenReview](https://openreview.net/group?id=auai.org/UAI/2025/Workshop/TPM#tab-accept) as well.

<ul>
{% assign sortedPapers = site.data.papers | sort: 'title' %}
{% for item in sortedPapers %}
  <li><strong>{{ item.title }}</strong> <a href="{{item.pdf_url}}"><img src="{{ site.baseurl }}/assets/images/pdf_icon_blue.svg" width="25" height="25"  alt="PDF icon" /></a>
  <br/>
  <small><i >{{ item.authors }}</i></small></li>  
{% endfor %}
</ul>
