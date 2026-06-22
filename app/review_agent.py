def review_recommendation(confidence):

    if confidence == "HIGH":
        return "Approve"

    elif confidence == "MEDIUM":
        return "Review Recommended"

    else:
        return "Human Review Required"