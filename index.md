---
layout: default
---

<!-- Information -->
<div class="jumbotron information">

    <p> For AI and ML systems aimed to assist decision-making in real-world scenarios, it is crucial to perform complex reasoning under uncertainty <b>reliably and efficiently</b>. However, contemporary machine learning is often criticized as being sensitive to data-perturbations, lacking guarantees on their predictions, and having little or no causal and symbolic reasoning capabilities. Further underpinning the relevance of these challenges, various regulatory bodies have released statements and frameworks aimed at building trustworthy AI.</p>

    <p>The field of tractable probabilistic models (TPMs) is a very appealing approach for many of these challenges, as TPMs enable reliable (<b>exact or coming with approximation guarantees</b>) and efficient reasoning for a wide range of tasks, by design. The spectrum of TPMs consists of a wide variety of techniques including models with tractable likelihoods (e.g., <b>normalizing flow</b> and <b>autoregressive models</b>), tractable marginals (e.g., <b>bounded-treewidth models</b> and <b>determinantal point processes</b>), and more complex tractable reasoning tasks (e.g., <b>circuits</b>) and is dynamically evolving.</p>

    <p>This year’s workshop on <b>Tractable Probabilistic Modeling</b> aims to highlight the connection between <b>trustworthy artificial intelligence</b> (in a broad sense) and tractable reasoning. The workshop aims to <b>highlight recent advancements in the field</b> of TPMs and their <b>potential impact in settings of trustworthy AI</b> (e.g. fairness, robustness, causality, neuro-symbolic AI).</p>
</div>


<!-- Content -->

<h2>Confirmed Speakers</h2>

<div class="row justify-content-center people-widget text-center">

{% for item in site.data.speakers  %}

<div class="col-12 col-sm-12 col-md-6 col-lg-4 col-xl-4">
  <a href="{{ item.url }}">
  <div class="team-member">

    {% if item.img %}
    <img src="{{ site.baseurl }}/assets/speakers/{{ item.img }}" class="img-responsive img-circle avatar-x2 avatar-circle" alt="">
    {% else %}
    <div class="avatar-x2 avatar-circle" style="background: #ddd;">
      <i class="fa fa-user" style="font-size: 220px; color: #eee; margin-top:20px;"></i>
    </div>
    {% endif %}
    <h4>{{ item.name }}</h4>
    <p class="text-muted">{{ item.affiliation }}</p>
  </div>
  </a>
</div>

{% endfor %}

</div>

<h2>Workshop Program</h2>
The workshop will happen in person at the Universitat Pompeu Fabra, Barcelona, Spain on July 19th, 2024.
See <a href="{{site.baseurl}}/program">program</a> for details!

<h2>Accepted Papers</h2>
The list of <a href="{{site.baseurl}}/papers">accepted papers</a> is online!


<h2>Call for Papers</h2>

We invite three types of submissions:

1. **Novel research** on tractable probabilistic modeling
2. **Retrospective papers** discussing the impact, consequences, and lessons learned
3. **Recently accepted papers** on tractable probabilistic modeling (_in the original format and length_)

### Topics of interest

Topics of interest include, but are not limited to:

* New tractable representations in logical, continuous, and hybrid domains
* Learning algorithms for TPMs
* Theoretical and empirical analysis of TPMs
* Connections between TPM classes
* TPMs for responsible, robust, and explainable AI
* TPMs for trustworthy ML
* Approximate inference algorithms with guarantees
* Successful applications of TPMs to real-world problems

### Submission Instructions
Original papers and retrospective papers are required to follow the style guidelines of UAI and should use the adjusted template <a href="https://tractable-probabilistic-modeling.github.io/tpm2024//assets/tpm2024-template.zip">TPM format</a>. 
Submitted papers should be **up to 4 pages long**, excluding references. 
Already accepted papers can be submitted in the format of the venue they have been accepted to. 
Supplementary material can be put in the same pdf paper (after references); it is entirely up to the reviewers to decide whether they wish to consult this additional material.

All submissions must be electronic (through the link below), and must closely follow the formatting guidelines in the templates, otherwise, they will automatically be rejected. 
Reviewing for TPM is single-blind; i.e., reviewers will know the authors’ identity but authors won't know the reviewers' identity. 
However, we recommend that you refer to your prior work in the third person wherever possible. 
We also encourage links to public repositories such as GitHub to share code and/or data.

For any questions, please contact us at: [tpmworkshop2024@gmail.com](mailto:tpmworkshop2024@gmail.com)

**Submission using:** [OpenReview](https://openreview.net/group?id=auai.org/UAI/2024/Workshop/TPM).

_**Note:** New OpenReview profiles created without an institutional email will go through a moderation process that can take up to two weeks. OpenReview profiles created with an institutional email will be activated automatically._

<h2>Important Dates</h2>

<p>All times are end of day AOE.</p>

<ul>

{% for item in site.deadlines  %}

  <li>{{ item.item }}: <strong>{{ item.date }}</strong></li>

{% endfor %}

</ul>

<h2>Previous Workshops</h2>
<ul>
  <li><a href="https://tractable-probabilistic-modeling.github.io/tpm2023/">6th Workshop on Tractable Probabilistic Modeling (2023)</a></li>
  <li><a href="https://tractable-probabilistic-modeling.github.io/tpm2022/">5th Workshop on Tractable Probabilistic Modeling (2022)</a></li>
  <li><a href="https://sites.google.com/view/tpm2021">4th Workshop on Tractable Probabilistic Modeling (2021)</a></li>
  <li><a href="https://sites.google.com/view/icmltpm2019/home">3th Workshop on Tractable Probabilistic Modeling (2019)</a></li>
  <li><a href="https://sites.google.com/site/tpm2018ws">2th Workshop on Tractable Probabilistic Modeling (2018)</a></li>
</ul>

<h2>Organizers</h2>

<div class="row justify-content-center people-widget text-center">

<div class="col-12 col-sm-4 col-md-3 col-lg-2 col-xl-2">
  <a href="{{ item.url }}">
  <div class="team-member">
    <!-- <img src="{{ site.baseurl }}/assets/speakers/{{ item.img }}" class="img-responsive img-circle avatar avatar-circle" alt=""></br> -->
    <strong>{{ item.name }}</strong>
    <!-- <p class="text-muted">{{ item.affiliation }}</p> -->
  </div>
  </a>
</div>

</div>


<ul>

{% for item in site.data.organizers  %}

  <li><a href="{{ item.url }}"><strong>{{ item.name }}</strong></a>, {{ item.affiliation }}</li>

{% endfor %}

</ul>



