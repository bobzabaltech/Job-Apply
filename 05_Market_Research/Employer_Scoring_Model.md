# Employer Scoring Model

## Purpose

This document defines the methodology used to prioritize employers identified through LinkedIn market research.

The objective is not to rank companies by size, reputation, or number of openings.

The objective is to maximize expected career ROI:

```text
Expected ROI

=

Market Opportunity

×

Candidate Fit

×

Probability of Interview

/

Required Effort
```

The model converts market evidence into an objective employer prioritization system.

---

# Strategic Context

The candidate's target market is not:

* generic software engineering;
* generic data engineering.

The target positioning is:

```text
Industrial Decision Systems

=

Manufacturing Experience

+

Software Engineering

+

Industrial Data

+

Digital Manufacturing
```

The scoring model therefore prioritizes companies where this combination creates differentiated value.

---

# Scoring Framework

Total score:

```text
100 points
```

The score is divided into five dimensions.

---

# 1. Market Presence

Weight:

```text
20 points
```

Measures evidence that the company actively recruits in the target market.

Criteria:

| Signal                                  | Score |
| --------------------------------------- | ----: |
| Appears frequently in Raw LinkedIn Jobs |    15 |
| Appears occasionally                    |     8 |
| Limited presence                        |     3 |

Additional consideration:

Repeated presence across multiple searches is stronger evidence than multiple openings in a single category.

---

# 2. Role Category Coverage

Weight:

```text
20 points
```

Measures how closely the company matches the target role ecosystem.

Evaluation:

| Categories matched | Score |
| ------------------ | ----: |
| 5+ categories      |    20 |
| 3-4 categories     |    15 |
| 2 categories       |    10 |
| 1 category         |     5 |

Relevant categories:

* Manufacturing Systems Engineer
* Digital Manufacturing Engineer
* MES Engineer
* Manufacturing Software Engineer
* Manufacturing Applications Engineer
* Manufacturing Intelligence
* Smart Manufacturing Engineer
* Industrial Data Engineer

---

# 3. Manufacturing Complexity

Weight:

```text
20 points
```

Measures how valuable industrial expertise is inside the organization.

Evaluation:

## High complexity — 20 points

Examples:

* aerospace;
* defense;
* automotive;
* semiconductor;
* advanced industrial manufacturing.

Characteristics:

* strict quality requirements;
* complex processes;
* high cost of failure.

---

## Medium complexity — 12 points

Examples:

* general industrial equipment;
* consumer manufacturing.

---

## Low complexity — 5 points

Examples:

* organizations where manufacturing is not a core competitive advantage.

---

# 4. Case Study Alignment

Weight:

```text
20 points
```

Measures how naturally the existing portfolio applies.

---

## Very high alignment — 20 points

Company problems likely include:

* quality optimization;
* manufacturing analytics;
* process capability;
* production intelligence;
* operational decision support.

---

## High alignment — 15 points

Company requires:

* manufacturing systems;
* data integration;
* digital transformation.

---

## Medium alignment — 10 points

Some overlap but weaker connection.

---

## Low alignment — 5 points

Limited relationship with demonstrated projects.

---

# 5. Industrial Decision Systems Fit

Weight:

```text
20 points
```

Measures how strongly the company values the candidate's differentiated positioning.

---

## Very high fit — 20 points

Company operates where:

```text
Manufacturing

+

Data

+

Software

+

Operational Decisions
```

are strategic.

---

## High fit — 15 points

Company has digital manufacturing initiatives.

---

## Medium fit — 10 points

Technology exists but is not central.

---

## Low fit — 5 points

Limited relationship.

---

# Final Score Interpretation

## 85-100

## Strategic Target

Priority:

* direct applications;
* networking;
* customized positioning.

Expected ROI:

Very high.

---

## 70-84

## High Priority

Priority:

* targeted applications;
* recruiter outreach.

Expected ROI:

High.

---

## 55-69

## Opportunistic

Priority:

* selective applications.

Expected ROI:

Medium.

---

## Below 55

## Low Priority

Avoid unless additional evidence appears.

---

# Example Application

## Siemens

Estimated score:

| Dimension                       | Score |
| ------------------------------- | ----: |
| Market Presence                 |    20 |
| Role Coverage                   |    20 |
| Manufacturing Complexity        |    20 |
| Case Study Alignment            |    20 |
| Industrial Decision Systems Fit |    20 |

Total:

```text
100/100
```

Classification:

Strategic Target.

---

## Generic Software Company

Estimated score:

| Dimension                       | Score |
| ------------------------------- | ----: |
| Market Presence                 |    10 |
| Role Coverage                   |     5 |
| Manufacturing Complexity        |     5 |
| Case Study Alignment            |     5 |
| Industrial Decision Systems Fit |     5 |

Total:

```text
30/100
```

Classification:

Low Priority.

---

# Usage Rules

The scoring model should be updated when:

* new market evidence appears;
* new employers are discovered;
* company information changes.

The model should not be changed only to justify preferred companies.

Any modification must improve predictive value.

---

# Next Step

The next document generated from this model is:

```text
05_Market_Research/Target_50.md
```

It will contain:

* ranked employers;
* score;
* rationale;
* recommended priority.

