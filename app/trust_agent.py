def assess_trust(evidence):

    score = 100

    for item in evidence:

        if item == "No issues detected":
            continue

        score -= 20

    if score >= 90:
        confidence = "HIGH"
    elif score >= 70:
        confidence = "MEDIUM"
    else:
        confidence = "LOW"

    return {
        "score": score,
        "confidence": confidence
    }