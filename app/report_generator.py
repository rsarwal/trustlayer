from trust_scorer import score_stores
from review_agent import review_recommendation

data = score_stores()

results = data["results"]
duplicates = data["duplicates"]

high_count = sum(
    1 for r in results
    if r["confidence"] == "HIGH"
)

medium_count = sum(
    1 for r in results
    if r["confidence"] == "MEDIUM"
)

low_count = sum(
    1 for r in results
    if r["confidence"] == "LOW"
)

report = []

# ==================================
# Header
# ==================================

report.append("TRUSTLAYER REPORT")
report.append("=" * 50)
report.append("")

report.append(
    f"Records Processed: {len(results)}"
)

report.append(
    f"HIGH CONFIDENCE: {high_count}"
)

report.append(
    f"MEDIUM CONFIDENCE: {medium_count}"
)

report.append(
    f"LOW CONFIDENCE: {low_count}"
)

report.append("")
report.append("=" * 50)

# ==================================
# Store Reports
# ==================================

for result in results:

    report.append("")
    report.append(
        f"Store: {result['store_name']}"
    )

    report.append(
        f"Confidence: {result['confidence']}"
    )

    report.append(
        f"Score: {result['score']}"
    )
    
    report.append("")
    report.append("Security Findings:")
    

    for item in result["security"]:
        report.append(f"- {item}")

    # ------------------------------
    # Supporting Evidence
    # ------------------------------

    report.append("")
    report.append("Supporting Evidence:")

    for item in result["evidence"]["positive"]:
        report.append(f"+ {item}")

    # ------------------------------
    # Issues
    # ------------------------------

    report.append("")
    report.append("Issues Found:")

    if result["evidence"]["negative"]:

        for item in result["evidence"]["negative"]:
            report.append(f"- {item}")

    else:

        report.append("- None")

    # ------------------------------
    # Warnings
    # ------------------------------

    if result["evidence"]["warnings"]:

        report.append("")
        report.append("Warnings:")

        for item in result["evidence"]["warnings"]:
            report.append(f"! {item}")

    # ------------------------------
    # Reasoning
    # ------------------------------

    report.append("")
    report.append("Reasoning:")

    for item in result["reasoning"]:
        report.append(f"- {item}")

    # ------------------------------
    # Challenges
    # ------------------------------

    report.append("")
    report.append("Potential Concerns:")

    for item in result["challenges"]:
        report.append(f"- {item}")
        
    # ------------------------------
    # Recommendation
    # ------------------------------

    recommendation = review_recommendation(
        result["confidence"]
    )

    report.append("")
    report.append("Recommendation:")
    report.append(recommendation)

    report.append("")
    report.append("-" * 50)

# ==================================
# Duplicate Alerts
# ==================================

report.append("")
report.append("=" * 50)
report.append("DUPLICATE ALERTS")
report.append("=" * 50)

if duplicates:

    for duplicate in duplicates:

        report.append(
            f"{duplicate[0]} <-> {duplicate[1]}"
        )

else:

    report.append(
        "No duplicates detected"
    )

# ==================================
# Save Report
# ==================================

with open(
    "outputs/trust_report.txt",
    "w"
) as file:

    file.write(
        "\n".join(report)
    )

print(
    "Trust report generated successfully."
)