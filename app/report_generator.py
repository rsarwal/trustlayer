from trust_scorer import score_stores

results = score_stores()

high_count = sum(1 for r in results if r["confidence"] == "HIGH")
medium_count = sum(1 for r in results if r["confidence"] == "MEDIUM")
low_count = sum(1 for r in results if r["confidence"] == "LOW")

report = []

report.append("TRUSTLAYER REPORT")
report.append("=" * 50)
report.append("")

report.append(f"Records Processed: {len(results)}")
report.append(f"HIGH CONFIDENCE: {high_count}")
report.append(f"MEDIUM CONFIDENCE: {medium_count}")
report.append(f"LOW CONFIDENCE: {low_count}")

report.append("")
report.append("=" * 50)

for result in results:


    report.append("")
    report.append(f"Store: {result['store_name']}")
    report.append(f"Confidence: {result['confidence']}")
    report.append(f"Score: {result['score']}")

    report.append("")
    report.append("Evidence:")

    if result["issues"]:
        for issue in result["issues"]:
            report.append(f"- {issue}")
    else:
        report.append("- No issues detected")

    report.append("")
    report.append("Recommendation:")

    if result["confidence"] == "HIGH":
        report.append("Approve")
    elif result["confidence"] == "MEDIUM":
        report.append("Review Recommended")
    else:
        report.append("Human Review Required")

report.append("")
report.append("-" * 50)



with open("outputs/trust_report.txt", "w") as file:
    file.write("\n".join(report))

print("Trust report generated successfully.")
