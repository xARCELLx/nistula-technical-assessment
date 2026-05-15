BASE_CONFIDENCE_SCORES = {
    "pre_sales_availability": 0.95,
    "pre_sales_pricing": 0.92,
    "post_sales_checkin": 0.88,
    "general_enquiry": 0.80,
    "special_request": 0.68,
    "complaint": 0.35
}


HIGH_RISK_KEYWORDS = {
    "refund": 0.20,
    "urgent": 0.15,
    "angry": 0.15,
    "unacceptable": 0.20,
    "lawsuit": 0.30,
    "terrible": 0.15,
    "horrible": 0.15,
    "disappointed": 0.10,
    "money back": 0.20,
    "bad service": 0.15,
    "rude": 0.25,
    "dirty": 0.20,
    "unsafe": 0.30,
    "broken": 0.20,
    "not working": 0.20,
    "issue": 0.10,
    "problem": 0.10
}


CRITICAL_ESCALATION_KEYWORDS = [
    "caretaker rude",
    "staff rude",
    "unsafe",
    "harassment",
    "fraud",
    "police",
    "threat",
    "emergency",
    "water leakage",
    "ac not working",
    "electricity issue",
    "power outage",
    "refund immediately"
]


def calculate_confidence(unified_message):

    confidence = BASE_CONFIDENCE_SCORES.get(
        unified_message.query_type,
        0.50
    )

    message_text = unified_message.message_text.lower()

    for keyword, penalty in HIGH_RISK_KEYWORDS.items():

        if keyword in message_text:
            confidence -= penalty

    confidence = max(0.0, min(confidence, 1.0))

    return round(confidence, 2)


def determine_action(
    query_type,
    confidence_score,
    message_text
):

    message_text = message_text.lower()

    for keyword in CRITICAL_ESCALATION_KEYWORDS:

        if keyword in message_text:
            return "escalate"

    if query_type == "complaint":
        return "escalate"

    if confidence_score >= 0.85:
        return "auto_send"

    if confidence_score >= 0.60:
        return "agent_review"

    return "escalate"