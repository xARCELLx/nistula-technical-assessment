-- Nistula Unified Messaging Platform Schema

-- This schema is designed to support:
-- - Unified guest profiles across channels
-- - Multi-channel messaging
-- - Conversation threading
-- - Reservation linkage
-- - AI-generated message tracking
-- - Confidence scoring and operational routing




-- TABLE: guests
-- Stores unified guest identity across all channels


CREATE TABLE guests (

    id UUID PRIMARY KEY,

    full_name VARCHAR(255) NOT NULL,

    email VARCHAR(255) UNIQUE,

    phone VARCHAR(50),

    preferred_channel VARCHAR(50)
    CHECK (
        preferred_channel IN (
            'whatsapp',
            'booking_com',
            'airbnb',
            'instagram',
            'direct'
        )
    ),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- TABLE: reservations
-- Stores reservation and booking information
-- One guest can have multiple reservations


CREATE TABLE reservations (

    id UUID PRIMARY KEY,

    booking_ref VARCHAR(100) UNIQUE NOT NULL,

    property_id VARCHAR(100) NOT NULL,

    guest_id UUID REFERENCES guests(id),

    check_in DATE,

    check_out DATE,

    number_of_guests INTEGER
    CHECK (number_of_guests > 0),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- TABLE: conversations
-- Groups messages into communication threads
-- Conversations are intentionally separated from
-- reservations because guests may communicate before booking


CREATE TABLE conversations (

    id UUID PRIMARY KEY,

    guest_id UUID REFERENCES guests(id),

    reservation_id UUID REFERENCES reservations(id),

    source VARCHAR(50) NOT NULL
    CHECK (
        source IN (
            'whatsapp',
            'booking_com',
            'airbnb',
            'instagram',
            'direct'
        )
    ),

    conversation_status VARCHAR(50)
    CHECK (
        conversation_status IN (
            'active',
            'closed',
            'escalated'
        )
    )
    DEFAULT 'active',

    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- TABLE: messages
-- Stores all inbound and outbound communication
-- in a unified structure


CREATE TABLE messages (

    id UUID PRIMARY KEY,

    conversation_id UUID REFERENCES conversations(id),

    sender_type VARCHAR(20)
    CHECK (
        sender_type IN (
            'guest',
            'ai',
            'agent'
        )
    )
    NOT NULL,

    source VARCHAR(50) NOT NULL
    CHECK (
        source IN (
            'whatsapp',
            'booking_com',
            'airbnb',
            'instagram',
            'direct'
        )
    ),

    message_text TEXT NOT NULL,

    query_type VARCHAR(100)
    CHECK (
        query_type IN (
            'pre_sales_availability',
            'pre_sales_pricing',
            'post_sales_checkin',
            'special_request',
            'complaint',
            'general_enquiry'
        )
    ),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



-- TABLE: ai_message_metadata
-- Stores AI operational metadata separately
-- for auditability and scalability


CREATE TABLE ai_message_metadata (

    id UUID PRIMARY KEY,

    message_id UUID REFERENCES messages(id),

    ai_drafted BOOLEAN DEFAULT FALSE,

    agent_edited BOOLEAN DEFAULT FALSE,

    auto_sent BOOLEAN DEFAULT FALSE,

    confidence_score DECIMAL(3,2)
    CHECK (
        confidence_score >= 0
        AND confidence_score <= 1
    ),

    action_taken VARCHAR(50)
    CHECK (
        action_taken IN (
            'auto_send',
            'agent_review',
            'escalate'
        )
    ),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



-- INDEX RECOMMENDATIONS
-- These indexes improve query performance for:
-- - conversation history retrieval
-- - booking lookups
-- - operational dashboards
-- - AI analytics


CREATE INDEX idx_reservations_booking_ref
ON reservations(booking_ref);

CREATE INDEX idx_messages_conversation_id
ON messages(conversation_id);

CREATE INDEX idx_messages_created_at
ON messages(created_at);

CREATE INDEX idx_ai_metadata_message_id
ON ai_message_metadata(message_id);


-- DESIGN DECISION NOTES

-- Hardest Design Decision:
--
-- The most important architectural decision was separating
-- conversations from reservations.
--
-- This design allows:
-- - guests to communicate before booking
-- - multiple conversations per reservation
-- - communication continuity across channels
-- - future scalability for CRM and support workflows
--
-- This separation improves flexibility and more accurately
-- models real-world hospitality communication systems.
