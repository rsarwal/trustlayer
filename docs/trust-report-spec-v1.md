# Trust Report Specification V1

## Purpose

The Trust Report helps users decide which records can be trusted and which require human review before import.

---

## Record Confidence Levels

### HIGH

Definition:
Record appears valid and complete.

Examples:
- Required fields present
- No duplicate detected
- Values follow expected formats

Recommendation:
Auto-approve

---

### MEDIUM

Definition:
Record contains minor issues.

Examples:
- Missing optional fields
- Ambiguous mappings
- Unusual values

Recommendation:
Verify before import

---

### LOW

Definition:
Record contains significant issues.

Examples:
- Possible duplicate
- Missing required fields
- Invalid values

Recommendation:
Human review required

---

## Example Output

Record 1
Store: Starbucks Chicago

Confidence: HIGH

Evidence:
- All required fields present
- No duplicates found
- Valid address

Recommendation:
Auto-approve

---

Record 7
Store: McDonald's New York

Confidence: MEDIUM

Evidence:
- Address format unusual

Recommendation:
Verify address

---

Record 14
Store: Subway Boston

Confidence: LOW

Evidence:
- Potential duplicate of Record 3

Recommendation:
Human review required