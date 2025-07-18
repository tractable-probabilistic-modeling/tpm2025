---
layout: default
permalink: /papers/
title: Accepted Papers
---


# Accepted Papers 

You can see all accpeted papers on [OpenReview](https://openreview.net/group?id=auai.org/UAI/2025/Workshop/TPM#tab-accept) as well.

<ul>
{% assign sortedPapers = site.data.papers %}
{% for item in sortedPapers %}
  <li><strong>{{ item.title }}</strong> <a href="{{item.pdf_url}}"><img src="{{ site.baseurl }}/assets/images/pdf_icon_blue.svg" width="25" height="25"  alt="PDF icon" /></a> 
  {% if item.video %} <a href="{{item.video}}" target="_blank" ><img src="{{ site.baseurl }}/assets/images/video-svgrepo-com.svg" width="25" height="25"  alt="Video icon" /></a> {% endif %} {% if item.session %}<small><i ><strong>
    {% if item.session == 'I' %}
      (<span style="background-color: #FFFF89">Poster Session I</span>)
    {% elsif item.session == 'II' %}
      (<span style="background-color: #89FFCA">Poster Session II</span>)
    {% endif %}
  </strong></i></small>
  {% endif %}
  <br/>
  <small><i >{{ item.authors }}</i></small></li>  
{% endfor %}
</ul>
