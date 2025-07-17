---
layout: default
permalink: /program/
title: Program
---

# Program 

The workshop will happen in person in Rio de Janeiro, Brazil on July 25th, 2025.

<table class="table table-striped">
    <colgroup>
       <col span="1" style="width: 20%;">
       <col span="1" style="width: 80%;">
    </colgroup>
    <thead>
    <tr>
        <th scope="col">Time</th>
        <th scope="col">Session</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>9:00 - 9:15</td>
        <td>Welcome and Best Paper Awards</td>
    </tr>
    <tr>
        <td>9:20 - 10:00</td>
        <td>Invited Talk I - Kareem Ahmed</td>
    </tr>
    <tr>
        <td>10:00 - 10:30</td>
        <td>Coffee Break</td>
    </tr>
    <tr>
        <td>10:30 - 11:10</td>
        <td>Invited Talk II - Efthymia Tsamoura</td>
    </tr>
    <tr>
        <td>11:10 - 12:20</td>
        <td>Poster Session I</td>
    </tr>
    <tr>
        <td>12:20 - 14:20</td>
        <td>Lunch Break (on your own)</td>
    </tr>
    <tr>
        <td>14:20 - 15:00</td>
        <td>Invited Talk III - Pedro Zuidberg Dos Martines</td>
    </tr>
    <tr>
        <td>15:00 - 15:30</td>
        <td>Coffee Break</td>
    </tr>
    <tr>
        <td>15:30 - 17:00</td>
        <td>Poster Session II</td>
    </tr>
    <tr>
        <td>17:00 - 17:40</td>
        <td>Invited Talk IV - Cassio De Campos</td>
    </tr>
    <tr>
        <td>17:40 - 18:00</td>
        <td>Closing Remarks</td>
    </tr>
    </tbody>
</table>

---

## Invited Talks

<ul>
{% assign sortedSpeakers = site.data.speakers | sort: 'session' %}
{% for item in sortedSpeakers %}
  {% if item.abstract != "" %}
  <li>
    <h4> {{ item.title }} </h4>
    <p><a href="{{ item.url }}" target="_blank" ><strong>{{ item.name }}</strong></a> ({{ item.affiliation }})</p>
    <p><strong>Abstract: </strong>{{ item.abstract }}</p>
  </li>
  {% endif %}
{% endfor %}
</ul>


