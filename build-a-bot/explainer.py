"""
explainer.py
Transforms bail orders + case data into neutral, statute-based explanations
"""

def explain_bail(case, accused, bail_order, statutes, risks, precedents, evidence_list):
    explanation = []

    # 1. Charge & statutory context
    explanation.append("CHARGE AND STATUTORY CONTEXT")
    explanation.append(
        f"The case involves offences classified as {case['offence_category']} "
        f"with a maximum punishment of {case['max_punishment_years']} years. "
        "Bail assessment is governed by statutory provisions of the CrPC."
    )

    for statute in statutes:
        explanation.append(
            f"Statutory Principle ({statute['statute_id']} – {statute['law']}): "
            f"{statute['principle']}."
        )

    # 2. Risk assessment
    explanation.append("\nRISK ASSESSMENT")
    explanation.append(
        f"The accused has a flight risk score of {accused['flight_risk_score']} "
        f"and a witness tampering risk score of {accused['tampering_risk_score']}."
    )

    if accused["prior_convictions"] > 0:
        explanation.append("Prior criminal history is considered during risk evaluation.")
    else:
        explanation.append("No prior convictions are noted in the risk assessment.")

    # 3. Risk mitigation
    explanation.append("\nRISK MITIGATION THROUGH CONDITIONS")
    for risk in risks:
        explanation.append(
            f"For {risk['risk_type']}, courts rely on mitigation measures such as "
            f"{', '.join(risk['mitigation_measures'])}."
        )

    # 4. Evidence classification
    explanation.append("\nEVIDENCE CLASSIFICATION")
    for ev in evidence_list:
        explanation.append(
            f"{ev['type']} evidence is noted. Its assessment at the bail stage "
            "is limited to procedural relevance and not probative value."
        )

    # 5. Statutory timelines / default bail
    explanation.append("\nSTATUTORY TIMELINES")
    explanation.append(
        f"The accused has been in custody for {case['days_in_custody']} days. "
        "Custody duration is assessed against statutory limits, "
        "without examining guilt or innocence."
    )

    # 6. Parity doctrine
    if case["co_accused_present"]:
        explanation.append("\nPARITY DOCTRINE")
        explanation.append(
            "Where co-accused exist, parity is considered to ensure procedural fairness, "
            "subject to individual risk factors."
        )

    # 7. Precedent reference
    explanation.append("\nLEGAL PRECEDENTS")
    for p in precedents:
        explanation.append(
            f"{p['doctrine']} applies as a {p['usage_scope']}, "
            f"subject to the restriction that {p['restriction']}."
        )

    # 8. Neutral justification
    explanation.append("\nNEUTRAL JUSTIFICATION")
    explanation.append(
        "The bail order reflects a procedural balancing of statutory mandates, "
        "risk management, and constitutional liberty. "
        "It does not determine guilt, innocence, or trial outcome."
    )

    return "\n".join(explanation)
