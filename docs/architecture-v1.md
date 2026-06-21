# TrustLayer Architecture V1

## Workflow

Input Files
(CSV, Excel)
    ↓

Schema Mapping Agent
    ↓

Normalization Agent
    ↓

Validation Agent
    ↓

Trust Agent
    ↓

Trust Report

---

## Agent Responsibilities

### Schema Mapping Agent

Maps incoming fields to a standard schema.

Examples:

store_name
location_name
restaurant_name

→ store_name

---

### Normalization Agent

Standardizes values.

Examples:

Mon → Monday
California → CA
ACTIVE → Active

---

### Validation Agent

Checks data quality.

Examples:

Missing required fields
Invalid dates
Invalid prices

---

### Trust Agent

Assigns confidence scores.

HIGH
MEDIUM
LOW

Provides explanations and recommendations.