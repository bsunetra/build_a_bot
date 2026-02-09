def generate_explanation(reasoning, doctrines, evidence):
    output = []

    # Charge & statute
    output.append("Charge and Statutory Nature:")
    output.append(
        "The offences involved are assessed according to their statutory classification. "
        "Bail in non-bailable offences depends on judicial discretion guided by legal principles."
    )

    # Risk assessment
    output.append("\nRisk Assessment:")
    if reasoning["flight_risk"]:
        output.append("A potential flight risk is considered at the bail stage.")
    if reasoning["tampering_risk"]:
        output.append("The possibility of evidence tampering is evaluated.")

    # Mitigation
    output.append("\nRisk Mitigation:")
    output.append(
        "Courts rely on bail conditions to mitigate identified risks rather than continued detention."
    )

    # Evidence classification
    output.append("\nEvidence Consideration:")
    output.append(
        "At the bail stage, courts distinguish between oral, documentary, and material evidence "
        "without evaluating their probative value."
    )

    # Default bail
    if reasoning["custody_days"] > 60 and not reasoning["chargesheet_filed"]:
        output.append("\nStatutory Timelines:")
        output.append(
            "Statutory timelines regulate detention. Default bail arises from procedural delay "
            "and does not reflect the merits of the case."
        )

    # Parity
    if reasoning["co_accused_parity"]:
        output.append("\nParity Doctrine:")
        output.append(
            "Parity promotes procedural fairness by ensuring similarly placed co-accused are treated alike."
        )

    # Doctrine
    output.append("\nLegal Principle:")
    output.append(doctrines["bail_not_jail"])

    return "\n".join(output)
