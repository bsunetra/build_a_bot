import json

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

accused_profiles = load_json("data/accused_profiles.json")
bail_orders = load_json("data/bail_orders.json.json")
cases = load_json("data/cases.json")
evidence = load_json("data/evidence.json")
precedents = load_json("data/precedents.json")
risk_models = load_json("data/risk_models.json")
statutes = load_json("data/statutes.json)