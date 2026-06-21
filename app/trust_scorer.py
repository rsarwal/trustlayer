import pandas as pd

def score_stores():

    stores = pd.read_csv("sample-data/stores.csv")

    results = []

    for index, row in stores.iterrows():

        score = 100
        issues = []

        if pd.isna(row["zip code"]):
            score -= 20
            issues.append("Missing ZIP code")

        if pd.isna(row["franchise_owner"]):
            score -= 20
            issues.append("Missing franchise owner")

        if pd.isna(row["Region"]):
            score -= 15
            issues.append("Missing region")

        menu_boards = str(row["# Menu Boards"]).strip().lower()

        if not menu_boards.isdigit():
            score -= 20
            issues.append(f"Invalid menu board count: {row['# Menu Boards']}")

        if score >= 90:
            confidence = "HIGH"
        elif score >= 70:
            confidence = "MEDIUM"
        else:
            confidence = "LOW"

        results.append({
            "store_name": row["Store Name"],
            "store_id": row["store_id"],
            "score": score,
            "confidence": confidence,
            "issues": issues
        })

    return results