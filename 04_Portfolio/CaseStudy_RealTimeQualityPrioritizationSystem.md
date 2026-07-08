# Real-Time Quality Prioritization System  
## Manufacturing Decision Intelligence Engine

---

## 1. Project Overview

This project is a real-time manufacturing analytics system designed to prioritize quality characteristics based on statistical risk and predictive degradation.

It transforms raw production measurement data into ranked operational insights to support engineering decision-making.

The system integrates:

- Statistical Process Control (SPC)
- Predictive risk modeling
- Time-series analysis
- Automated prioritization logic
- Dual-layer screening dashboards

---

## 2. Problem Statement

Manufacturing environments generate continuous measurement data across multiple features.

Although SPC metrics exist, they present limitations:

- Engineers must manually analyze each feature
- Prioritization is not automated
- Focus is diluted across many characteristics
- Predictive failure is not explicitly modeled
- Data is fragmented across sources

The core problem:

> There is no system that combines current process capability with predictive risk to prioritize engineering action.

---

## 3. Solution Overview

The system implements a **dual-layer decision engine**:

### Layer 1 — Current Process Capability
### Layer 2 — Predictive Risk Estimation

These layers generate a unified prioritization model that ranks manufacturing features based on operational urgency.

---

## 4. Data Architecture

The system uses a SQL-based analytical pipeline powered by DuckDB.

### Data Sources

Two CSV-based sources:

- `data_features.csv` → measurement values
- `spec_features.csv` → specification limits

---

### Data Processing Flow

1. Data is queried using DuckDB
2. Features are joined by `feature_id`
3. Only valid production data is selected (`to_cep = True`)
4. Data is ordered chronologically (date + time)
5. A sliding window of `n_samples` is applied per feature

---

### Filtering Logic

- Features can be excluded via configuration (`skip_features`)
- Only the latest N samples per feature are analyzed

---

## 5. Core Analytics Engine

The system processes each `feature_id` independently.

---

### 5.1 Statistical Computation (SPC Layer)

For each feature:

- Mean
- Standard deviation (sample-based)
- Cp
- Cpk

#### Formulas:

- Cp = (USL - LSL) / (6 * σ)
- Cpk = min((USL - μ)/(3σ), (μ - LSL)/(3σ))

---

### 5.2 Immediate Risk Detection

A feature is considered **critical (Hops = 0)** if:

- Mean ± 3σ exceeds specification limits

This represents immediate process instability.

---

### 5.3 Predictive Risk Modeling

For stable processes, the system estimates:

> **Hops to NG**

This represents the estimated number of future measurements before a feature becomes non-conforming.

---

### 5.4 Hops Calculation Logic

If process is stable:

- Uses historical trend behavior
- Applies statistical projection logic
- Estimates degradation over time

If instability is detected:

- Hops is set to 0

---

## 6. Dual Screening System

The system produces two independent operational views:

---

### 6.1 Current Process Capability Screener

#### Objective:
Prioritize current quality issues.

#### Logic:
- Ranks features by lowest Cpk
- Highlights unstable processes
- Displays statistical history
- Rotates automatically through top priority features

#### Behavior:
- Fully automated
- No user interaction required
- Continuous display mode

#### Outcome:
- Immediate identification of critical features
- Focus on current production issues

---

### 6.2 Predictive Risk Screener

#### Objective:
Prioritize preventive quality actions.

#### Logic:
- Considers only currently capable features
- Ranks features by Hops to NG
- Identifies future failures before they occur

#### Outcome:
- Early warning system for quality degradation
- Preventive engineering actions

---

## 7. System Execution Model

The system runs as a continuous batch process:

1. Loads configuration (`config.toml`)
2. Retrieves latest production data
3. Applies feature filtering
4. Executes analytical engine
5. Generates prioritized outputs
6. Writes results to storage layer

---

## 8. Configuration System

Defined in `config.toml`:

### Key parameters:

- `n_samples`: number of recent measurements per feature
- `max_hops`: maximum predictive horizon
- `output_type`: csv or sqlite
- `output_path`: export directory
- `skip_features`: excluded feature list

---

## 9. Output System

Two output formats supported:

### CSV output:
- `analisis.csv`
- `data_series.csv`

### SQLite output:
- `screeners_data.db`
  - analisis table
  - data_series table

---

## 10. Code Architecture

### Main modules:

- `main.py` → orchestration layer
- `source_db.py` → data extraction via DuckDB
- `analizer.py` → core analytics engine
- `data_out.py` → output layer
- `types.py` → configuration + data structures

---

## 11. Core Design Principles

- Lightweight architecture
- Modular pipeline design
- SQL-based data access
- Python-native analytics stack
- Config-driven execution
- Portable outputs (CSV/SQLite)

---

## 12. Key Innovation — Hops to NG

### Definition:

A predictive metric estimating how many future measurements remain before a feature becomes non-conforming.

---

### Conceptual Shift:

| Traditional SPC | This System |
|----------------|-------------|
| Detect failure | Predict failure timing |
| Reactive | Proactive |
| Static metrics | Time-based risk evolution |

---

## 13. Operational Philosophy

The system is designed for:

- Continuous execution
- Autonomous monitoring
- Minimal human interaction
- Real-time prioritization

---

## 14. Business Impact

- Reduces time spent analyzing low-impact features
- Improves reaction time to quality issues
- Enables preventive maintenance actions
- Standardizes prioritization logic
- Increases manufacturing efficiency

---

## 15. Strategic Interpretation

This system is best described as:

> A Real-Time Manufacturing Decision Intelligence Engine

It is not a dashboard.

It is not a reporting tool.

It is a **prioritization system for industrial decision-making**.

---

## 16. Resume Translation

Recommended framing:

> Built a real-time manufacturing analytics engine using DuckDB and Python that combines SPC metrics (Cp, Cpk) with predictive risk modeling (Hops to NG) to prioritize quality characteristics and enable proactive decision-making.

---

## 17. Recruiter Takeaway

This project demonstrates:

- Strong understanding of SPC (Cp/Cpk)
- Ability to design predictive analytics systems
- Experience with SQL-based data pipelines (DuckDB)
- Capability in building decision engines, not just dashboards
- Integration of statistical modeling into production systems

---

## 18. Key Differentiators

- Introduces Hops to NG predictive metric
- Combines deterministic SPC with predictive modeling
- Fully automated prioritization engine
- Dual screener architecture (current + predictive)
- Configuration-driven industrial analytics system
