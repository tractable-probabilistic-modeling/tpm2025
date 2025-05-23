---
layout: default
permalink: /cfp/
title: Call for Papers
---

# Call for Papers
We invite three types of submissions:

1. **Novel research** on tractable probabilistic modeling
2. **Retrospective papers** discussing the impact, consequences, and lessons learned from classical TPM papers
3. **Recently accepted papers** at top ML / AI conferences (_in the original format and length_)

## Topics of interest

Topics of interest include, but are not limited to:

* New tractable representations in logical, continuous, and hybrid domains
* Learning algorithms for TPMs
* Theoretical and empirical analysis of TPMs
* Connections between TPM classes
* TPMs for responsible, robust, and explainable AI
* Approximate inference algorithms with guarantees
* Successful applications of TPMs to real-world problems,with a special focus on NeSy AI

## Submission Instructions
Original papers and retrospective papers are required to follow the [style guidelines of UAI](https://www.auai.org/uai2025/submission_instructions). 
Submitted novel and retrospective papers should be **up to 4 pages long**, excluding references. 
Already accepted papers can be submitted in the format and length of the venue they have been accepted to. 
Supplementary material can be put in the same pdf paper (after references); it is entirely up to the reviewers to decide whether they wish to consult this additional material.

All submissions must be electronic (through the link below), and must closely follow the formatting guidelines in the templates, otherwise, they will automatically be rejected. 
Reviewing for TPM is double-blind; i.e., the identity of the authors is not revealed to the reviewers and vice versa, this excludes recently accepted papers, which will be reviewed single-blind.
Therefore, you should refer to your prior work in the third person. 
We encourage links to public anonymous repositories such as GitHub to share code and/or data.

For any questions, please contact us at: [tpmworkshop2025@gmail.com](mailto:tpmworkshop2025@gmail.com)

**Submission using:** [OpenReview](https://openreview.net/group?id=auai.org/UAI/2025/Workshop/TPM)

_**Note:** New OpenReview profiles created without an institutional email will go through a moderation process that can take up to two weeks. OpenReview profiles created with an institutional email will be activated automatically._


## Important Dates

All times are end-of-day AOE.

<ul>

{% for item in site.deadlines  %}

  <li>{{ item.item }}: <strong>{{ item.date }}</strong></li>

{% endfor %}

</ul>
