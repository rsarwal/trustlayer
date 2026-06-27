def generate_challenges(result):
    """
    Challenge Agent

    Purpose:
    Identify reasons why the current recommendation
    could be wrong.

    This agent does NOT change the trust score.

    It simply highlights uncertainty and risks
    that a human reviewer should be aware of.
    """

    challenges = []

    confidence = result["confidence"]

    negative = result["evidence"]["negative"]

    warnings = result["evidence"]["warnings"]

    # ----------------------------------
    # Existing Issues
    # ----------------------------------

    for item in negative:
        challenges.append(
            f"Validation issue detected: {item}"
        )

    # ----------------------------------
    # Warnings
    # ----------------------------------

    for item in warnings:
        challenges.append(
            f"Warning present: {item}"
        )

    # ----------------------------------
    # Confidence-Based Challenges
    # ----------------------------------

    

    if confidence == "MEDIUM":

        challenges.append(
            "Missing or invalid fields reduce confidence."
        )

    if confidence == "LOW":

        challenges.append(
            "Multiple data quality issues detected."
        )

 