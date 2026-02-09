"""
boundary.py
LexExplain – Bail Decision Justification & Legal Boundary Compliance Bot

Purpose:
- Enforce strict legal boundaries
- Block advice, predictions, guilt assessment
- Provide explainable and transparent refusals
"""

# Explicit prohibited phrases (strong signals)
PROHIBITED_KEYWORDS = [
    # Outcome prediction
    "will the accused get bail",
    "will the accused get bailed",
    "will i get bail",
    "chances of bail",
    "predict",
    "outcome",
    "result",

    # Legal advice
    "should i",
    "what should i do",
    "what to do",
    "legal advice",
    "lawyer",
    "apply for bail",

    # Guilt / innocence
    "guilty",
    "innocent",

    # Judicial intent speculation
    "what will the judge do",
    "judge decision",
    "court will decide"
]


def boundary_check(user_query: str) -> bool:
    """
    Checks whether the user query violates legal boundaries.

    Returns:
        True  -> Allowed (explanatory request)
        False -> Blocked (advice / prediction / guilt / speculation)
    """
    query = user_query.lower().strip()

    # 1️⃣ Explicit phrase blocking
    for phrase in PROHIBITED_KEYWORDS:
        if phrase in query:
            return False

    # 2️⃣ Intent-based prediction blocking
    # Example: "will i get bail", "will i get bail in this case?"
    if "will" in query and "bail" in query:
        return False

    # 3️⃣ Advice-style intent blocking
    if ("should" in query or "advice" in query) and "bail" in query:
        return False

    return True


def boundary_violation_reason(user_query: str) -> str:
    """
    Provides an explainable reason for why a query was blocked.
    """
    q = user_query.lower()

    if "will" in q and "bail" in q:
        return "Outcome prediction is prohibited in bail matters"
    if "should" in q or "advice" in q or "lawyer" in q:
        return "Providing legal advice is outside permitted boundaries"
    if "guilty" in q or "innocent" in q:
        return "Assessing guilt or innocence is prohibited"
    if "judge" in q or "court will" in q:
        return "Speculating on judicial intent is not permitted"

    return "The request exceeds permitted legal explanation boundaries"


def boundary_refusal() -> str:
    """
    Standardized refusal message (mandatory by problem statement).
    """
    return (
        "I cannot provide legal advice, predict judicial outcomes, "
        "or assess guilt or innocence. "
        "I can explain the legal reasoning, statutory principles, "
        "and procedural factors used in bail decisions."
    )
