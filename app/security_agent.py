import re


def inspect_security(record):
    """
    Security Agent

    Purpose:
    Identify sensitive information and
    security concerns within a record.

    This agent does NOT modify data.

    It only reports findings.
    """

    findings = []

    record_text = " ".join(
        str(value)
        for value in record.values
    )

    # -------------------------------
    # Email Detection
    # -------------------------------

    email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    if re.search(email_pattern, record_text):

        findings.append(
            "Email address detected"
        )

    # -------------------------------
    # Phone Detection
    # -------------------------------

    phone_pattern = r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b"

    if re.search(phone_pattern, record_text):

        findings.append(
            "Phone number detected"
        )

    # -------------------------------
    # SSN Detection
    # -------------------------------

    ssn_pattern = r"\b\d{3}-\d{2}-\d{4}\b"

    if re.search(ssn_pattern, record_text):

        findings.append(
            "Possible SSN detected"
        )

    # -------------------------------
    # Prompt Injection Detection
    # -------------------------------

    suspicious_phrases = [
        "ignore previous instructions",
        "ignore all instructions",
        "disregard instructions",
        "override system prompt",
        "system prompt"
    ]

    lower_text = record_text.lower()

    for phrase in suspicious_phrases:

        if phrase in lower_text:

            findings.append(
                f"Potential prompt injection phrase: '{phrase}'"
            )

    # -------------------------------
    # No Findings
    # -------------------------------

    if len(findings) == 0:

        findings.append(
            "No security concerns detected"
        )

    return findings