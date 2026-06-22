import pandas as pd
from evidence_agent import collect_evidence
from trust_agent import assess_trust


def score_stores():

    stores = pd.read_csv("sample-data/stores.csv")

    results = []

    for index, row in stores.iterrows():

        evidence = collect_evidence(row)
        trust = assess_trust(evidence)


        results.append({
            "store_name": row["Store Name"],
            "store_id": row["store_id"],
            "score": trust["score"],
            "confidence": trust["confidence"],
            "issues": evidence
        })

    return results