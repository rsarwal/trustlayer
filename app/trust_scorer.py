import pandas as pd
from evidence_agent import collect_evidence
from trust_agent import assess_trust
from duplicate_agent import find_duplicates
from challenge_agent import generate_challenges
from security_agent import inspect_security


def score_stores():

    stores = pd.read_csv("sample-data/stores.csv")

    results = []

    for index, row in stores.iterrows():

        evidence = collect_evidence(row)
        security_findings = inspect_security(row)

        trust = assess_trust(evidence)

        challenges = generate_challenges({
            "confidence": trust["confidence"],
            "evidence": evidence
        })

        results.append({
            "store_name": row["Store Name"],
            "store_id": row["store_id"],
            "score": trust["score"],
            "confidence": trust["confidence"],
            "evidence": evidence,
            "reasoning": trust["reasoning"],
            "challenges": challenges,
            "security": security_findings
        })

    duplicates = find_duplicates(results)

    return {
        "results": results,
        "duplicates": duplicates
    }