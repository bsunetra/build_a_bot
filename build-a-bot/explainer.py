"""
explainer.py
LexExplain – Bail Decision Justification & Legal Boundary Compliance Bot

Purpose:
- Transform bail orders and case data into neutral, statute-based explanations
- Enforce procedural, non-adjudicatory reasoning
"""

def explain_bail(case, accused, bail_order, statutes, risks, precedents, evidence_list):
    explanation = []

    # 1. Charge & Statutory Context
    explanation.append("CHARGE AND STATUTORY CONTEXT")
    explanation.append(
        f"The case involves offences classified as {case['offence_category']} "
        f"with a maximum punishment of {case['max_punishment_years']} years. "
        "Bail consideration is governed by statutory provisions of the Code of Criminal Procedure."
    )

    for statute in statutes:
        explanation.append(
            f"Statutory Principle ({statute['statute_id']} – {statute['law']}): "
            f"{statute['principle']}."
        )

    # 2. Risk Assessment
    explanation.append("\nRISK ASSESSMENT")
    explanation.append(
        f"Procedural risk indicators reflect a flight risk score of {accused['flight_risk_score']} "
        f"and a witness tampering risk score of {accused['tampering_risk_score']}."
    )

    if accused["prior_convictions"] > 0:
        explanation.append(
            "Prior criminal history is noted as a relevant factor in procedural risk evaluation."
        )
    else:
        explanation.append(
            "No prior convictions are recorded for the purpose of procedural risk assessment."
        )

    # 3. Risk → Condition Mapping (Creative Feature)
    explanation.append("\nRISK TO MITIGATION MAPPING")
    for risk in risks:
        explanation.append(
            f"{risk['risk_type']} → "
            f"{', '.join(risk['mitigation_measures'])}"
        )

    # 4. Evidence Classification + Neutrality Badge
    explanation.append("\nEVIDENCE CLASSIFICATION")
    for ev in evidence_list:
        explanation.append(
            f"{ev['type']} evidence is referenced for procedural context only."
        )

    explanation.append("\nEVIDENCE NEUTRALITY NOTICE")
    explanation.append(
        "At the bail stage, evidence is considered solely for procedural relevance. "
        "No assessment of credibility, sufficiency, or guilt is undertaken."
    )

    # 5. Statutory Timeline Flag (Default Bail Logic)
    explanation.append("\nSTATUTORY TIMELINE CHECK")
    for statute in statutes:
        if statute["statute_id"] == "S-167(2)":
            explanation.append(
                f"Custody Duration: {case['days_in_custody']} days | "
                f"Statutory Threshold: {statute['time_limit_days']} days"
            )

            if case["days_in_custody"] >= statute["time_limit_days"]:
                explanation.append(
                    "Procedural Status: Statutory timeline threshold crossed."
                )
            else:
                explanation.append(
                    "Procedural Status: Custody remains within statutory limits."
                )

    # 6. Parity Doctrine
    if case["co_accused_present"]:
        explanation.append("\nPARITY DOCTRINE")
        explanation.append(
            "Where similarly placed co-accused exist, parity is examined as a "
            "principle of procedural fairness, subject to individual risk factors."
        )

    # 7. Precedent Reference
    explanation.append("\nLEGAL PRECEDENTS")
    for p in precedents:
        explanation.append(
            f"{p['doctrine']} operates as a {p['usage_scope']}, "
            f"subject to the limitation that {p['restriction']}."
        )

    # 8. Neutral Justification
    explanation.append("\nNEUTRAL JUSTIFICATION")
    explanation.append(
        "The bail order reflects a structured application of statutory mandates, "
        "procedural risk management, and constitutional considerations of personal liberty. "
        "It does not adjudicate guilt, innocence, or trial outcomes."
    )

    return "\n".join(explanation)
