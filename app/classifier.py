QUERY_CLASSIFICATIONS = {
    "pre_sales_availability": [
        "available",
        "availability",
        "vacant",
        "free"
    ],

    "pre_sales_pricing": [
        "price",
        "pricing",
        "rate",
        "cost",
        "charges"
    ],

    "post_sales_checkin": [
        "check in",
        "check-in",
        "wifi",
        "password",
        "check out"
    ],

    "special_request": [
        "airport transfer",
        "pickup",
        "early check",
        "chef",
        "decoration"
    ],

    "complaint": [
        "not working",
        "bad",
        "refund",
        "complaint",
        "unhappy",
        "issue",
        "problem"
    ]
}

def classify_query(message: str) -> str:

    message = message.lower()

    for query_type, keywords in QUERY_CLASSIFICATIONS.items():

        for keyword in keywords:

            if keyword in message:
                return query_type

    return "general_enquiry"