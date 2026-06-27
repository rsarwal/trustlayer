import pandas as pd


def collect_evidence(row):
    """
    Evidence Agent

    Purpose:
    Collect observable facts about a record.

    The Evidence Agent DOES NOT:
    - assign trust scores
    - approve records
    - reject records

    It only gathers evidence that will later
    be evaluated by the Trust Agent.
    """

    evidence = {
        "positive": [],
        "negative": [],
        "warnings": []
    }

    # ----------------------------------
    # ZIP Code Check
    # ----------------------------------

    if pd.isna(row["zip code"]):

        evidence["negative"].append(
            "Missing ZIP code"
        )

    else:

        evidence["positive"].append(
            "ZIP code present"
        )

    # ----------------------------------
    # Franchise Owner Check
    # ----------------------------------

    if pd.isna(row["franchise_owner"]):

        evidence["negative"].append(
            "Missing franchise owner"
        )

    else:

        evidence["positive"].append(
            "Franchise owner present"
        )

    # ----------------------------------
    # Region Check
    # ----------------------------------

    if pd.isna(row["Region"]):

        evidence["negative"].append(
            "Missing region"
        )

    else:

        evidence["positive"].append(
            "Region present"
        )

    # ----------------------------------
    # Menu Board Validation
    # ----------------------------------

    menu_boards = str(
        row["# Menu Boards"]
    ).strip()

    if menu_boards.isdigit():

        evidence["positive"].append(
            "Menu board count valid"
        )

    else:

        evidence["negative"].append(
            f"Invalid menu board count: {row['# Menu Boards']}"
        )

    # ----------------------------------
    # No Issues Detected
    # ----------------------------------

    if len(evidence["negative"]) == 0:

        evidence["positive"].append(
            "No issues detected"
        )

    return evidence