def evaluate_case(case_facts, statutes, risks):
    reasoning = {}

    offence = case_facts["offences"][0]
    reasoning["offence_nature"] = statutes.get(offence, {})

    reasoning["flight_risk"] = risks.get("flight_risk", False)
    reasoning["tampering_risk"] = risks.get("tampering_risk", False)

    reasoning["co_accused_parity"] = case_facts.get("co_accused_on_bail", False)

    reasoning["custody_days"] = case_facts.get("custody_days", 0)
    reasoning["chargesheet_filed"] = case_facts.get("chargesheet_filed", True)

    return reasoning
