def assess_trust(evidence):
    """
    Trust Agent

    Consumes evidence from the Evidence Agent
    and produces:

    - trust score
    - confidence level
    - human-readable reasoning
    """

    score = 100

    negative_count = len(
        evidence["negative"]
    )

    warning_count = len(
        evidence["warnings"]
    )

    score -= negative_count * 20
    score -= warning_count * 5

    score = max(score, 0)

    # -------------------------------
    # Confidence
    # -------------------------------

    if score >= 90:
        confidence = "HIGH"

    elif score >= 70:
        confidence = "MEDIUM"

    else:
        confidence = "LOW"

    # -------------------------------
    # Reasoning
    # -------------------------------

    reasoning = []

    if confidence == "HIGH":

        reasoning.append(
            "Record appears complete and passed validation checks."
        )

        reasoning.append(
            "No significant issues were detected."
        )

    elif confidence == "MEDIUM":

        reasoning.append(
            "Record is mostly complete but contains issues requiring attention."
        )

        for item in evidence["negative"]:
            reasoning.append(item)

    else:

        reasoning.append(
            "Record contains multiple issues that reduce trust."
        )

        for item in evidence["negative"]:
            reasoning.append(item)

    return {
        "score": score,
        "confidence": confidence,
        "reasoning": reasoning
    }