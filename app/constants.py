SUPPORTED_SOURCES = [
    "whatsapp",
    "booking_com",
    "airbnb",
    "instagram",
    "direct"
]

PROPERTY_CONTEXT = """
Property: Villa B1, Assagao, North Goa
Bedrooms: 3
Max guests: 6
Private pool: Yes

Check-in: 2pm
Check-out: 11am

Base rate: INR 18,000 per night (up to 4 guests)
Extra guest: INR 2,000 per night per person

WiFi password: Nistula@2024

Caretaker: Available 8am to 10pm
Chef on call: Yes, pre-booking required

Availability April 20-24: Available

Cancellation: Free up to 7 days before check-in
"""

FALLBACK_RESPONSES = {
    "pre_sales_availability":
        "Thank you for your inquiry. "
        "Our team will confirm availability shortly.",

    "pre_sales_pricing":
        "Thank you for your interest. "
        "Our team will share pricing details shortly.",

    "post_sales_checkin":
        "Thank you for reaching out. "
        "Our support team will assist you shortly.",

    "special_request":
        "Thank you for your request. "
        "Our team will review and get back to you shortly.",

    "complaint":
        "We sincerely apologize for the inconvenience. "
        "Your concern has been escalated to our support team.",

    "general_enquiry":
        "Thank you for contacting Nistula. "
        "Our team will get back to you shortly."
}