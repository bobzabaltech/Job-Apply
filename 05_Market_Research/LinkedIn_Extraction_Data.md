# LinkedIn Extraction Data

## Purpose

This document stores the quantitative extraction results obtained from:

`05_Market_Research/Raw_LinkedIn_Jobs/`

The objective is to preserve the factual layer extracted from LinkedIn job search data before applying strategic interpretation.

This document is the intermediate data layer between:

```
Raw LinkedIn Jobs

↓

Quantitative Extraction

↓

Employer Intelligence Database

↓

Employer Scoring Model

↓

Target Companies Strategy
```

---

# Data Source

## Source Location

```
05_Market_Research/
    Raw_LinkedIn_Jobs/
```

## Analyzed Categories

The dataset contains the following LinkedIn search categories:

1. Manufacturing Systems Engineer
2. Digital Manufacturing Engineer
3. MES Engineer
4. Manufacturing Software Engineer
5. Manufacturing Applications Engineer
6. Manufacturing Intelligence
7. Smart Manufacturing Engineer
8. Industrial Data Engineer

---

# Extraction Methodology

The extraction process identifies:

* employer names;
* job categories;
* job titles;
* geographical information;
* employer frequency;
* category overlap.

The purpose is not to estimate total market size.

The purpose is to identify:

* recurring employers;
* market demand patterns;
* role convergence;
* companies where the candidate's positioning has the highest strategic fit.

---

# Dataset Limitations

The dataset represents LinkedIn search results collected using specific role queries.

Therefore:

## The dataset can determine:

* employer recurrence;
* relative demand signals;
* role terminology;
* geographic distribution;
* market patterns.

## The dataset cannot determine:

* exact salary levels;
* complete hiring volume;
* company compensation strategy;
* complete technical requirements;
* final candidate competitiveness.

All strategic decisions must combine this evidence with:

* candidate experience;
* case studies;
* professional positioning.

---

# Dataset Overview

## Categories analyzed

Total categories:

```
8
```

## Records extracted

Approximate job records analyzed:

```
956
```

## Objective

Identify companies and roles where the following combination is valuable:

```
Manufacturing Experience

+

Industrial Systems

+

Software Development

+

Data Analytics

+

Operational Decision Support
```

---

# Employer Frequency Analysis

Initial employer normalization identified the following recurring organizations.

| Employer              | Mentions |
| --------------------- | -------: |
| Siemens               |       17 |
| Magna International   |       14 |
| Ford Motor Company    |       12 |
| Rheinmetall           |       12 |
| Rolls-Royce           |       12 |
| Philips               |       11 |
| Leonardo              |       11 |
| Raytheon UK           |       10 |
| GKN Aerospace         |       10 |
| Thales                |        9 |
| Lockheed Martin       |        8 |
| Eaton                 |        8 |
| Porsche Consulting    |        8 |
| Milwaukee Tool        |        7 |
| Johnson Controls      |        7 |
| Danfoss               |        7 |
| SEGULA Technologies   |        7 |
| GE Aerospace          |        7 |
| Stellantis            |        6 |
| Siemens Energy        |        6 |
| Airbus                |        6 |
| L3Harris Technologies |        6 |
| Tesla Automation      |        6 |

---

# Employer Pattern Observations

The extracted data shows strong concentration in companies with:

* complex manufacturing operations;
* global production networks;
* industrial automation requirements;
* manufacturing digitalization initiatives;
* operational data challenges.

The strongest recurring sectors are:

## Aerospace & Defense

Examples:

* Rolls-Royce
* Leonardo
* Rheinmetall
* Raytheon
* Lockheed Martin
* Airbus
* GKN Aerospace

Strategic relevance:

High alignment due to:

* precision manufacturing;
* quality requirements;
* traceability;
* process capability analysis;
* risk-based prioritization.

---

## Automotive

Examples:

* Ford Motor Company
* Magna International
* Stellantis

Strategic relevance:

High alignment due to:

* production systems;
* MES;
* smart manufacturing;
* manufacturing analytics.

---

## Industrial Automation

Examples:

* Siemens
* ABB
* Eaton

Strategic relevance:

High alignment due to:

* industrial software;
* automation;
* manufacturing systems;
* OT/IT integration.

---

# Role Landscape

The dataset shows significant overlap between searched categories.

The market does not treat manufacturing software, data, and systems as isolated disciplines.

Observed role families:

---

## Manufacturing Systems

Focus:

* production systems;
* MES;
* integration;
* factory applications.

Typical titles:

* Manufacturing Systems Engineer
* Manufacturing Systems Developer
* Manufacturing Systems Specialist

---

## Digital Manufacturing

Focus:

* Industry 4.0;
* smart factory;
* digital transformation.

Typical titles:

* Digital Manufacturing Engineer
* Industry 4.0 Engineer
* Smart Manufacturing Engineer

---

## MES / Manufacturing Applications

Focus:

* manufacturing execution systems;
* production workflows;
* plant applications.

Typical titles:

* MES Engineer
* Manufacturing Applications Engineer
* MES Developer

---

## Industrial Data

Focus:

* operational data;
* analytics;
* manufacturing intelligence.

Typical titles:

* Industrial Data Engineer
* Manufacturing Data Engineer
* Manufacturing Intelligence Engineer

---

# Strategic Interpretation

The extracted market data supports the existing positioning:

The candidate should not compete as:

* Generic Software Engineer.
* Generic Data Engineer.

The strongest market intersection is:

```
Digital Manufacturing

+

Manufacturing Systems

+

Industrial Data

+

Software Engineering

+

Operational Decision Systems
```

---

# Relationship With Candidate Profile

The extracted market demand aligns with demonstrated capabilities:

## Industrial Measurement Data Platform

Demonstrates:

* industrial data architecture;
* manufacturing analytics;
* quality intelligence;
* process improvement.

---

## Real-Time Quality Prioritization System

Demonstrates:

* decision-support systems;
* predictive prioritization;
* operational intelligence.

---

# Next Processing Steps

This document feeds:

1. `Employer_Intelligence_Database.md`

Purpose:

Detailed employer profiles.

---

2. `Employer_Scoring_Model.md`

Purpose:

Prioritize companies according to strategic fit.

---

3. `Target_Roles.md`

Purpose:

Map market terminology to candidate positioning.

---

4. `Target_50.md`

Purpose:

Generate prioritized employer target list.

---

# Status

Current status:

Initial quantitative extraction completed.

Next step:

Build employer intelligence and scoring layers from this dataset.
