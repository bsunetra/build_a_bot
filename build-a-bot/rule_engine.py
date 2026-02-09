"""
rule_engine.py
LexExplain – Rule-Based Legal Reasoning Extractor

Purpose:
- Convert raw legal data into structured, explainable reasoning blocks
- Maintain strict neutrality (no prediction, no advice, no adjudication)
"""

from datetime import datetime


def analyze_case(case, accused, statutes):
    """
    Extracts statutory and procedural observations from case data.
    """
    reasoning = {}

    # Offence characteristics
    reasoning["offence_category"] = case["offence_category"]
    reasoning["max_punishment_years"] = case["max_punishment_years"]

    # Custody & investigation status
    reasoning["days_in_custody"] = case["days_in_custody"]
    reasoning["investigation_status"] = case["investigation_status"]

    # Statutory timeline check (Section 167(2) CrPC – procedural only)
    reasoning["statutory_timeline_crossed"] = False
    reasoning["default_bail_reference"] = None

    for statute in statutes:
        if statute.get("statute_id") == "S-167(2)":
            reasoning["default_bail_reference"] = statute["time_limit_days"]

            if (
                case["days_in_custody"] >= statute["time_limit_days"]
                and case["investigation_status"] != "Charge Sheet Filed"
            ):
                reasoning["statutory_timeline_crossed"] = True

    # Parity doctrine relevance
    reasoning["parity_relevant"] = case["co_accused_present"]

    return reasoning


def analyze_risks(accused):
    """
    Structures procedural risk observations without conclusions.
    """
    risk_observation = {}

    # Raw risk indicators
    risk_observation["flight_risk_score"] = accused["flight_risk_score"]
    risk_observation["tampering_risk_score"] = accused["tampering_risk_score"]

    # Risk classification (descriptive, not determinative)
    risk_observation["flight_risk_level"] = (
        "Elevated" if accused["flight_risk_score"] >= 0.7 else "Moderate"
    )

    risk_observation["tampering_risk_level"] = (
        "Elevated" if accused["tampering_risk_score"] >= 0.7 else "Moderate"
    )

    # Background indicators
    risk_observation["prior_convictions"] = accused["prior_convictions"]
    risk_observation["social_roots"] = accused["social_roots"]
    risk_observation["employment_status"] = accused["employment_status"]

    return risk_observation


def analyze_bail_order(bail_order):
    """
    Extracts procedural reasoning blocks and conditions from bail orders.
    """
    return {
        "bail_status_recorded": bail_order["bail_status"],
        "conditions_listed": bail_order["conditions"],
        "reasoning_blocks": bail_order["reasoning_blocks"]
    }


def analyze_evidence(evidence_list):
    """
    Classifies evidence types without evaluating credibility or weight.
    """
    classified = {
        "Documentary": 0,
        "Oral": 0,
        "Material": 0
    }

    for ev in evidence_list:
        ev_type = ev.get("type")
        if ev_type in classified:
            classified[ev_type] += 1

    return {
        "evidence_breakdown": classified,
        "total_items": sum(classified.values()),
        "evaluation_notice": (
            "Evidence classification is procedural and does not assess probative value."
        )
    }
