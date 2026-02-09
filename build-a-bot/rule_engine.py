"""
rule_engine.py
Rule-based legal reasoning extractor for LexExplain Bot

Purpose:
- Convert raw case data into structured legal reasoning blocks
- No predictions, no advice, no outcomes
"""

from datetime import datetime


def analyze_case(case, accused, statutes):
    """
    Extracts statutory and procedural observations from case data.
    """
    reasoning = {}

    # Offence severity
    reasoning["offence_category"] = case["offence_category"]
    reasoning["max_punishment"] = case["max_punishment_years"]

    # Custody & investigation status
    reasoning["days_in_custody"] = case["days_in_custody"]
    reasoning["investigation_status"] = case["investigation_status"]

    # Default bail check (purely procedural)
    reasoning["default_bail_applicable"] = False
    for statute in statutes:
        if statute["statute_id"] == "S-167(2)":
            if (
                case["days_in_custody"] >= statute["time_limit_days"]
                and case["investigation_status"] != "Charge Sheet Filed"
            ):
                reasoning["default_bail_applicable"] = True

    # Parity relevance
    reasoning["parity_relevant"] = case["co_accused_present"]

    return reasoning


def analyze_risks(accused):
    """
    Structures risk-related observations without conclusions.
    """
    risk_observation = {}

    risk_observation["flight_risk_score"] = accused["flight_risk_score"]
    risk_observation["tampering_risk_score"] = accused["tampering_risk_score"]

    risk_observation["flight_risk_level"] = (
        "Elevated" if accused["flight_risk_score"] >= 0.7 else "Moderate"
    )

    risk_observation["tampering_risk_level"] = (
        "Elevated" if accused["tampering_risk_score"] >= 0.7 else "Moderate"
    )

    risk_observation["prior_convictions"] = accused["prior_convictions"]
    risk_observation["social_roots"] = accused["social_roots"]

    return risk_observation


def analyze_bail_order(bail_order):
    """
    Extracts reasoning blocks and conditions from bail orders.
    """
    return {
        "bail_status": bail_order["bail_status"],
        "conditions": bail_order["conditions"],
        "reasoning_blocks": bail_order["reasoning_blocks"]
    }


def analyze_evidence(evidence_list):
    """
    Classifies evidence types without assessing credibility.
    """
    classified = {
        "Documentary": 0,
        "Oral": 0,
        "Material": 0
    }

    for ev in evidence_list:
        if ev["type"] in classified:
            classified[ev["type"]] += 1

    return classified
