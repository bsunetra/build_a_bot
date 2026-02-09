"""
boundary.py
LexExplain – Bail Decision Justification & Legal Boundary Compliance Bot
"""

PROHIBITED_KEYWORDS = [
    "will the accused get bail",
    "will the accused get bailed",
    "will i get bail",
    "will get bail",
    "chances of bail",
    "predict",
    "outcome",
    "result",
    "should i",
    "what should i do",
    "what to do",
    "legal advice",
    "lawyer",
    "apply for bail",
    "guilty",
    "innocent",
    "what will the judge do",
    "judge decision"
]

def boundary_check(user_query: str) -> bool:
    query = user_query.lower().strip()
    for phrase in PROHIBITED_KEYWORDS:
        if phrase in query:
            return False
    return True


def boundary_refusal() -> str:
    return (
        "I cannot provide legal advice, predict judicial outcomes, "
        "or assess guilt or innocence. "
        "I can explain the legal reasoning, statutory principles, "
        "and procedural factors used in bail decisions."
    )
