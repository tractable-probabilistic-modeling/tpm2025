---
layout: default
---

<!-- Information -->
<h2>About</h2>
<div class="information">


<p>Deploying AI and ML systems to assist decision-making in real-world and safety-critical scenarios, requires different forms of <b>complex reasoning under uncertainty</b>. These scenarios include applications in healthcare and finance, as well as when certifying the fairness, robustness and privacy of ML systems. In all these cases, reasoning needs to be <b>reliable and efficient</b> and flexible enough to deal with <b>constraints and background knowledge</b>.
The now consolidated field of tractable probabilistic models (TPMs) offers a very appealing approach as TPMs allow for <b>exact inference or come with approximation guarantees</b>, thus providing reliability while still allowing for efficient reasoning for a wide range of tasks, by design.
</p>

<p>
Furthermore, many TPMs provide <b>a natural way to represent logical constraints and principled ways to incorporate them into larger ML systems</b>. The spectrum of TPMs consists of a wide variety of techniques including models with tractable likelihoods (e.g., <b>normalizing flow</b> and <b>autoregressive models</b>), tractable marginals (e.g., <b>bounded-treewidth models</b> and <b>determinantal point processes</b>), and more complex tractable reasoning tasks (e.g., <b>probabilistic and logic circuits, tensor networks</b>).
</p>

<p>This new edition of the <b>Tractable Probabilistic Modeling</b> workshop focuses on scaling and providing guarantees when used for <b>probabilistic and logical reasoning</b>, e.g., in neuro-symbolic AI where agents have to model both calibrated uncertainties and satisfy given background knowledge while being efficient. We also welcome contributions around the TPM spectrum that consider only one of the two aspects, and hope to bring the two communities together to advance their respective fields.</p>
</div>

<h2>Important dates</h2>

All times are end-of-day AOE.

<ul>

{% for item in site.deadlines  %}

  <li>{{ item.item }}: <strong>{{ item.date }}</strong></li>

{% endfor %}

</ul>


<!-- Content -->

<h2>Confirmed Speakers</h2>

<div class="row justify-content-center people-widget text-center">

{% for item in site.data.speakers  %}

<div class="col-12 col-sm-12 col-md-6 col-lg-4 col-xl-4">
  <a href="{{ item.url }}" target="_blank">
  <div class="team-member">

    {% if item.img %}
    <img src="{{ site.baseurl }}/assets/speakers/{{ item.img }}" class="img-responsive img-circle avatar-x2 avatar-circle" alt="{{ item.name }}">
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
The workshop will happen in person in Rio de Janeiro, Brazil on July 25th, 2025.
See <a href="{{site.baseurl}}/program">program</a> for details!

<h2>Accepted Papers</h2>
The list of accepted papers can be found <a href="{{site.baseurl}}/papers/">here</a>.

<h2>Call for Papers</h2>

We invite three types of submissions:

1. **Novel research** on tractable probabilistic modeling
2. **Retrospective papers** discussing the impact, consequences, and lessons learned from classical TPM papers
3. **Recently accepted papers** at top ML / AI conferences (_in the original format and length_)

### Topics of interest

Topics of interest include, but are not limited to:

* New tractable representations in logical, continuous, and hybrid domains
* Learning algorithms for TPMs
* Theoretical and empirical analysis of TPMs
* Connections between TPM classes
* TPMs for responsible, robust, and explainable AI
* Approximate inference algorithms with guarantees
* Successful applications of TPMs to real-world problems,with a special focus on NeSy AI

### Submission Instructions
Original papers and retrospective papers are required to follow the style guidelines of UAI and should use the adjusted template <a href="/tpm2025/assets/tpm2025-template.zip">TPM format</a>.
Submitted papers should be **up to 4 pages long**, excluding references. 
Already accepted papers can be submitted in the format and length of the venue they have been accepted to. 
Supplementary material can be put in the same pdf paper (after references); it is entirely up to the reviewers to decide whether they wish to consult this additional material.

All submissions must be electronic (through the link below), and must closely follow the formatting guidelines in the templates, otherwise, they will automatically be rejected. 
Reviewing for TPM is double-blind; i.e., the identity of the authors is not revealed to the reviewers and vice versa, this excludes recently accepted papers, which will be reviewed single-blind.
Therefore, you should refer to your prior work in the third person. 
We encourage links to public anonymous repositories such as GitHub to share code and/or data.

For any questions, please contact us at: [tpmworkshop2025@gmail.com](mailto:tpmworkshop2025@gmail.com)

**Submission using:**  [OpenReview](https://openreview.net/group?id=auai.org/UAI/2025/Workshop/TPM)

_**Note:** New OpenReview profiles created without an institutional email will go through a moderation process that can take up to two weeks. OpenReview profiles created with an institutional email will be activated automatically._


<h2>Previous Workshops</h2>
<ul>
<li><a href="https://tractable-probabilistic-modeling.github.io/tpm2024/">7th Workshop on Tractable Probabilistic Modeling (2024)</a></li>
  <li><a href="https://tractable-probabilistic-modeling.github.io/tpm2023/">6th Workshop on Tractable Probabilistic Modeling (2023)</a></li>
  <li><a href="https://tractable-probabilistic-modeling.github.io/tpm2022/">5th Workshop on Tractable Probabilistic Modeling (2022)</a></li>
  <li><a href="https://sites.google.com/view/tpm2021">4th Workshop on Tractable Probabilistic Modeling (2021)</a></li>
  <li><a href="https://sites.google.com/view/icmltpm2019/home">3th Workshop on Tractable Probabilistic Modeling (2019)</a></li>
  <li><a href="https://sites.google.com/site/tpm2018ws">2th Workshop on Tractable Probabilistic Modeling (2018)</a></li>
</ul>

<h2>Organizers</h2>

<div class="row justify-content-center people-widget text-center" style="margin-bottom: 80px;">


{% for item in site.data.organizers  %}

<div class="col-12 col-sm-12 col-md-6 col-lg-4 col-xl-3">
  <a href="{{ item.url }}" target="_blank">
  <div class="team-member">

    {% if item.img %}
    <img src="{{ site.baseurl }}/assets/organisers/{{ item.img }}" class="img-responsive img-circle avatar-x2 avatar-circle" alt="">
    {% else %}
    <div class="avatar-x2 avatar-circle" style="background: #ddd;">
      <i class="fa fa-user" style="font-size: 220px; color: #eee; margin-top:20px;"></i>
    </div>
    {% endif %}

    <h4>{{ item.name }}</h4>
    <!-- <p class="text-muted">{{ item.affiliation }}</p> -->
  </div>
  </a>
</div>

{% endfor %}

</div>




