import pandas as pd

def collect_evidence(row):

    evidence = []

    if pd.isna(row["zip code"]):
        evidence.append("Missing ZIP code")

    if pd.isna(row["franchise_owner"]):
        evidence.append("Missing franchise owner")

    if pd.isna(row["Region"]):
        evidence.append("Missing region")

    menu_boards = str(row["# Menu Boards"]).strip().lower()

    if not menu_boards.isdigit():
        evidence.append(
            f"Invalid menu board count: {row['# Menu Boards']}"
        )

    if len(evidence) == 0:
        evidence.append("No issues detected")

    return evidence