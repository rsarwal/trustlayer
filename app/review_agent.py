def review_recommendation(confidence):
    """
    Review Agent

    Determines the level of human attention
    recommended for a record.

    TrustLayer does not approve or reject data.
    It prioritizes human review.
    """

    if confidence == "HIGH":
        return "No Review Required"

    elif confidence == "MEDIUM":
        return "Review Suggested"

    else:
        return "Human Review Required"