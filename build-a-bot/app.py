from flask import Flask, request, jsonify, render_template
import json

from boundary import boundary_check, boundary_refusal
from explainer import explain_bail

app = Flask(__name__)


# ---------- Load Data ----------
def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


statutes = load_json("data/statutes.json")
risk_models = load_json("data/risk_models.json")
precedents = load_json("data/precedents.json")
evidence = load_json("data/evidence.json")
cases = load_json("data/cases.json")
bail_orders = load_json("data/bail_orders.json")
accused_profiles = load_json("data/accused_profiles.json")


# ---------- Serve Frontend ----------
@app.route("/")
def index():
    return render_template("index.html")


# ---------- API ----------
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    user_query = data.get("message", "")
    case_choice = int(data.get("case_id", 1)) - 1

    # Boundary check
    if not boundary_check(user_query):
        return jsonify({
            "blocked": True,
            "response": boundary_refusal()
        })

    # Fetch case data
    case = cases[case_choice]
    accused = next(a for a in accused_profiles if a["case_id"] == case["case_id"])
    bail_order = next(b for b in bail_orders if b["case_id"] == case["case_id"])
    evidence_list = [e for e in evidence if e["case_id"] == case["case_id"]]

    explanation = explain_bail(
        case,
        accused,
        bail_order,
        statutes,
        risk_models,
        precedents,
        evidence_list
    )

    return jsonify({
        "blocked": False,
        "response": explanation
    })


# ---------- Run App ----------
if __name__ == "__main__":
    app.run(debug=True)
