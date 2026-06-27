import streamlit as st
import sys
import os

# ----------------------------------
# Python Path
# ----------------------------------

sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        "app"
    )
)

from trust_scorer import score_stores

# ----------------------------------
# Page Config
# ----------------------------------

st.set_page_config(
    page_title="Gatewise",
    page_icon="assets/gatewise_icon.png",
    layout="wide"
)

with st.sidebar:

    st.image(
        "assets/gatewise_icon.png",
        width=70
    )

    st.markdown("## Gatewise")

    st.caption(
        "Evidence-Based Data Intake"
    )

    st.divider()

    st.markdown("### Agent Pipeline")

    st.markdown("""
🛡️ **Security Agent**
PII & security screening

🔎 **Evidence Agent**
Collect observable facts

🎯 **Trust Agent**
Calculate confidence

⚖️ **Challenge Agent**
Question assumptions

🧑‍⚖️ **Review Agent**
Escalate uncertain records

🧬 **Duplicate Agent**
Detect matching records
""")

    st.divider()

    st.info(
        """
Gatewise does not determine truth.

It helps humans decide which records deserve attention.
"""
    )
    # ----------------------------------
# Hero Section
# ----------------------------------

col1, col2 = st.columns([1, 4])

with col1:

    st.image(
        "assets/gatewise_logo.png",
        width=180
    )

with col2:

    st.title(
        "Analyst Workspace"
    )

    st.caption(
        "Evidence-based trust analysis for incoming business records"
    )

    st.write(
        "Identify records that deserve human attention before entering business systems."
    )

    run_analysis = st.button(
        "Analyze Incoming Records",
        type="primary"
    )

# ----------------------------------
# Run Analysis
# ----------------------------------

if run_analysis:

    data = score_stores()

    results = data["results"]
    duplicates = data["duplicates"]

    high_count = sum(
        1 for r in results
        if r["confidence"] == "HIGH"
    )

    medium_count = sum(
        1 for r in results
        if r["confidence"] == "MEDIUM"
    )

    low_count = sum(
        1 for r in results
        if r["confidence"] == "LOW"
    )

    st.divider()

    st.subheader("📊 Analysis Summary")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Records", len(results))
    c2.metric("High Confidence", high_count)
    c3.metric("Medium Confidence", medium_count)
    c4.metric("Low Confidence", low_count)
    st.metric(
        "Requires Review",
        medium_count + low_count
    )

    st.write("")

    st.subheader("🧬 Duplicate Alerts")

    if duplicates:

        for duplicate in duplicates:

            st.error(
                f"{duplicate[0]} ↔ {duplicate[1]}"
            )

    else:

        st.success(
            "No duplicate records detected"
        )

    st.write("")

    st.subheader("🧠 Record Intelligence Workspace")
    for result in results:

        confidence_icons = {
            "HIGH": "🟢",
            "MEDIUM": "🟡",
            "LOW": "🔴"
        }

        with st.expander(
            f"{result['store_name']} | "
            f"{confidence_icons[result['confidence']]} "
            f"{result['confidence']} | "
            f"Score {result['score']}"
        ):

# -----------------------------
# Decision Banner
# -----------------------------

            if result["confidence"] == "HIGH":

                st.success("✅ Decision: APPROVE")
                st.caption(
                    f"Trust Score: {result['score']}/100"
                )

            elif result["confidence"] == "MEDIUM":
            

                st.warning("⚠️ Decision: REVIEW")
                st.caption(
                    f"Trust Score: {result['score']}/100"
                )

            else:

                st.error("🚨 Decision: ESCALATE")
                st.caption(
                    f"Trust Score: {result['score']}/100"
                )


            # -----------------------------
            # Supporting Evidence
             # -----------------------------

            st.markdown("### 🔍 Supporting Evidence")

            for item in result["evidence"]["positive"]:

                if item != "No issues detected":

                    st.write(f"✅ {item}")


            # -----------------------------
            # Issues
            # -----------------------------

            if result["confidence"] != "HIGH":

                st.markdown("### ❌ Issues")

                issues = result["evidence"]["negative"]

                if issues:

                    for item in issues:

                        st.error(item)


            # -----------------------------
           # -----------------------------
            # Review Triggers
            # -----------------------------

            if result["challenges"]:

                st.markdown("### ⚠️ Review Triggers")

                for item in result["challenges"]:
                    st.warning(item)        


        # -----------------------------
        # Analyst Notes
        # -----------------------------

            st.markdown("### 📝 Analyst Notes")

            st.text_area(
                "Reviewer Notes",
                key=f"notes_{result['store_name']}",
                placeholder="Add review comments..."
            )


        # -----------------------------
        # Recommendation
        # -----------------------------

            st.markdown("### 🧑‍⚖️ Recommendation")

            if result["confidence"] == "HIGH":

                st.success(
                    "No analyst review required"
                )

                st.button(
                    "Approve Record",
                    key=f"approve_{result['store_name']}"
                )

            elif result["confidence"] == "MEDIUM":

                st.warning(
                    "Review suggested"
                )

                st.button(
                    "Send to Review Queue",
                    key=f"review_{result['store_name']}"
                )

            else:

                st.error(
                    "Human review required"
                )

                st.button(
                    "Escalate Investigation",
                    key=f"escalate_{result['store_name']}"
                )