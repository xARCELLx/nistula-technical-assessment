import uuid
from app.classifier import classify_query
from app.schemas import UnifiedMessage
from datetime import datetime


def log_event(event_type, message):

    timestamp = datetime.utcnow()

    print(f"[{timestamp}] {event_type}: {message}")



def normalize_message(payload):

    query_type = classify_query(payload.message)

    unified_message = UnifiedMessage(
        message_id=uuid.uuid4(),
        source=payload.source,
        guest_name=payload.guest_name,
        message_text=payload.message,
        timestamp=payload.timestamp,
        booking_ref=payload.booking_ref,
        property_id=payload.property_id,
        query_type=query_type
    )

    return unified_message


def generate_message_id():
    return str(uuid.uuid4())