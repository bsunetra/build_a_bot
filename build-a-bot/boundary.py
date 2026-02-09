PROHIBITED_KEYWORDS = [
    "will", "predict", "chances", "should",
    "guilty", "innocent", "win", "lose",
    "what to do", "lawyer", "advice"
]

def boundary_check(user_query):
    query = user_query.lower()
    for word in PROHIBITED_KEYWORDS:
        if word in query:
            return False
    return True

def boundary_refusal():
    return (
        "I cannot provide legal advice, predictions, or assess guilt or innocence. "
        "I can explain how bail decisions are legally reasoned based on statutes and principles."
    )
