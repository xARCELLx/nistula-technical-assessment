BASE_CONFIDENCE_SCORES = {
    "pre_sales_availability": 0.93,
    "pre_sales_pricing": 0.90,
    "post_sales_checkin": 0.88,
    "general_enquiry": 0.82,
    "special_request": 0.72,
    "complaint": 0.40
}

HIGH_RISK_KEYWORDS = [
    "refund",
    "urgent",
    "angry",
    "unacceptable",
    "lawsuit",
    "terrible",
    "horrible",
    "disappointed",
    "money back",
]

def calculate_confidence(unified_message):

    confidence = BASE_CONFIDENCE_SCORES.get(
        unified_message.query_type,
        0.50
    )

    message_text = unified_message.message_text.lower()

    for keyword in HIGH_RISK_KEYWORDS:

        if keyword in message_text:
            confidence -= 0.15

    confidence = max(0.0, min(confidence, 1.0))

    return round(confidence, 2)

def determine_action(query_type, confidence_score):

    if query_type == "complaint":
        return "escalate"

    if confidence_score >= 0.85:
        return "auto_send"

    if confidence_score >= 0.60:
        return "agent_review"

    return "escalate"