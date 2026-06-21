# Sample Dataset Plan V1

## Dataset Source

Synthetic restaurant operations data containing:

* Store locations
* Menu items

The dataset intentionally contains realistic operational data quality issues.

---

## Data Quality Problems Included

### Missing Values

Examples:

* Missing ZIP code
* Missing franchise owner
* Missing region
* Missing menu item category
* Missing item ID

Expected Result:

MEDIUM or LOW confidence.

---

### Inconsistent Formats

Examples:

* Active / active / ACTIVE
* California / CA
* Yes / YES / yes / y / 1

Expected Result:

Automatic normalization.

---

### Invalid Data Types

Examples:

* "four" stored in a numeric field
* "free with meal" stored in a price field

Expected Result:

Validation warning.

---

### Date Normalization

Examples:

* 2026-03-15
* 15/03/2026
* March 15 2026

Expected Result:

Normalize to ISO format.

---

### Duplicate Detection

Examples:

* Classic Cheeseburger appears twice
* Same location
* Same price

Expected Result:

LOW confidence and duplicate warning.

---

### Referential Integrity Issues

Examples:

* Menu item missing location_id

Expected Result:

Human review recommended.

---

## TrustLayer Success Criteria

TrustLayer should:

1. Normalize inconsistent values.
2. Detect missing fields.
3. Detect duplicates.
4. Detect invalid formats.
5. Generate confidence scores.
6. Produce a human-readable Trust Report.
