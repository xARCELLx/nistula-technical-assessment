from pydantic import BaseModel
from datetime import datetime
from typing import Literal


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