import json

from boundary import boundary_check, boundary_refusal
from explainer import explain_bail

from rule_engine import (
    analyze_case,
    analyze_risks,
    analyze_bail_order,
    analyze_evidence
)


# -------------------------------
# JSON Loader
# -------------------------------
def load_json(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {path}: {e}")
        return []


# -------------------------------
# Load All Datasets
# -------------------------------
statutes = load_json("data/statutes.json")
risk_models = load_json("data/risk_models.json")
precedents = load_json("data/precedents.json")
evidence = load_json("data/evidence.json")
cases = load_json("data/cases.json")
bail_orders = load_json("data/bail_orders.json")
accused_profiles = load_json("data/accused_profiles.json")


# -------------------------------
# Case Selection Menu
# -------------------------------
def select_case():
    print("\nAvailable Cases:")
    for idx, case in enumerate(cases):
        print(f"{idx + 1}. {case['case_id']} ({case['offence_category']})")

    try:
        choice = int(input("\nSelect case number: ")) - 1
        return cases[choice]
    except:
        print("Invalid selection. Defaulting to Case 1.")
        return cases[0]


# -------------------------------
# MAIN BOT EXECUTION
# -------------------------------
def run_bot():

    print("\n====== LexExplain Bail Reasoning Bot ======\n")

    # Boundary-protected user query
    user_query = input("Ask about bail reasoning: ")

    if not boundary_check(user_query):
        print("\n" + boundary_refusal())
        return

    # Case selection
    case = select_case()

    # Retrieve related records
    try:
        accused = next(a for a in accused_profiles if a["case_id"] == case["case_id"])
        bail_order = next(b for b in bail_orders if b["case_id"] == case["case_id"])
        evidence_list = [e for e in evidence if e["case_id"] == case["case_id"]]
    except StopIteration:
        print("Data mismatch detected for selected case.")
        return

    # -------------------------------
    # RULE ENGINE PROCESSING
    # -------------------------------
    case_analysis = analyze_case(case, accused, statutes)
    risk_analysis = analyze_risks(accused)
    bail_analysis = analyze_bail_order(bail_order)
    evidence_analysis = analyze_evidence(evidence_list)

    # -------------------------------
    # EXPLANATION GENERATION
    # -------------------------------
    response = explain_bail(
        case,
        accused,
        bail_order,
        statutes,
        risk_models,
        precedents,
        evidence_list
    )

    print("\n" + response)


# -------------------------------
# Run Program
# -------------------------------
if __name__ == "__main__":
    run_bot()
