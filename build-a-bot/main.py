from boundary import boundary_check, boundary_refusal
from rule_engine import evaluate_case
from explainer import generate_explanation

user_query = input("Ask about bail reasoning: ")

if not boundary_check(user_query):
    print(boundary_refusal())
else:
    reasoning = evaluate_case(case_facts, statutes, risks)
    response = generate_explanation(reasoning, doctrines, evidence)
    print(response)
