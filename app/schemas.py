from pydantic import BaseModel
from datetime import datetime
from typing import Literal
from uuid import UUID


class UnifiedMessage(BaseModel):
    message_id: UUID
    source: str
    guest_name: str
    message_text: str
    timestamp: datetime
    booking_ref: str
    property_id: str
    query_type: str


class IncomingMessage(BaseModel):
    source: Literal[
        "whatsapp",
        "booking_com",
        "airbnb",
        "instagram",
        "direct"
    ]
    
    guest_name: str
    message: str
    timestamp: datetime
    booking_ref: str
    property_id: str