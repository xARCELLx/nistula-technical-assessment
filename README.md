# Nistula Technical Assessment

AI-powered unified guest messaging backend built with FastAPI.

---

# Project Overview

This project is an AI-powered unified guest messaging backend system developed for the Nistula Summer Technology Internship 2026 technical assessment.

The system is designed to receive guest messages from multiple communication channels, normalize them into a unified internal structure, classify guest intent, generate AI-powered drafted replies, and determine operational actions using confidence-based routing.

The primary focus of the project was not only functionality, but also:

* clean backend architecture
* operational reliability
* explainable AI decision-making
* maintainability
* scalability
* graceful degradation handling

The project was intentionally designed with a modular architecture to simulate how a production-grade hospitality messaging platform may be structured internally.

---

# Architecture Overview

```text
Incoming Message
      ↓
FastAPI Webhook Endpoint
      ↓
Payload Validation (Pydantic)
      ↓
Normalization Layer
      ↓
Deterministic Query Classification
      ↓
AI Draft Reply Generation
      ↓
Confidence Scoring
      ↓
Operational Action Routing
      ↓
Structured JSON Response
```

---

# Features

* Unified multi-channel message handling
* Deterministic query classification
* AI-powered guest reply generation
* Confidence-based operational routing
* Automatic escalation handling for complaints
* Graceful fallback response system
* Structured logging and validation
* Modular FastAPI architecture
* PostgreSQL relational schema design
* AI provider abstraction support
* Production-minded error handling

---

# Supported Channels

The webhook currently supports:

* WhatsApp
* Booking.com
* Airbnb
* Instagram
* Direct inquiries

---

# Query Classification Types

The system classifies incoming messages into the following categories:

| Query Type             | Description                                   |
| ---------------------- | --------------------------------------------- |
| pre_sales_availability | Availability inquiries                        |
| pre_sales_pricing      | Pricing-related questions                     |
| post_sales_checkin     | Check-in/check-out and stay-related questions |
| special_request        | Custom operational requests                   |
| complaint              | Guest complaints or escalations               |
| general_enquiry        | General informational questions               |

---

# Tech Stack

| Technology          | Purpose                   |
| ------------------- | ------------------------- |
| Python              | Core programming language |
| FastAPI             | Backend API framework     |
| Pydantic            | Request validation        |
| OpenRouter / Claude | AI response generation    |
| PostgreSQL          | Relational schema design  |
| OpenAI SDK          | AI provider integration   |
| Uvicorn             | ASGI server               |

---

# Project Structure

```text
nistula-technical-assessment/
│
├── app/
│   ├── main.py
│   ├── schemas.py
│   ├── classifier.py
│   ├── claude_service.py
│   ├── confidence.py
│   ├── prompts.py
│   ├── constants.py
│   ├── config.py
│   └── utils.py
│
├── tests/
│   └── sample_payloads.json
│
├── README.md
├── schema.sql
├── thinking.md
├── requirements.txt
├── .env.example
└── .gitignore
```

---

# Module Responsibilities

| File              | Responsibility                                |
| ----------------- | --------------------------------------------- |
| main.py           | FastAPI application and webhook orchestration |
| schemas.py        | Request and unified schema validation         |
| classifier.py     | Deterministic query classification            |
| claude_service.py | AI provider communication layer               |
| confidence.py     | Confidence scoring and routing logic          |
| prompts.py        | AI prompt construction                        |
| constants.py      | Shared constants and fallback responses       |
| config.py         | Environment configuration                     |
| utils.py          | Helper functions and logging utilities        |

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <your_repository_url>
cd nistula-technical-assessment
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

---

## 3. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Configure Environment Variables

Create a `.env` file in the project root.

Example:

```env
OPENROUTER_API_KEY=your_api_key_here
```

---

## 6. Run FastAPI Server

```bash
uvicorn app.main:app --reload
```

---

## 7. Open Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

---

# Environment Variables

| Variable           | Description                             |
| ------------------ | --------------------------------------- |
| OPENROUTER_API_KEY | API key used for AI-generated responses |

---

# API Endpoint Documentation

## POST `/webhook/message`

Receives inbound guest messages from supported channels.

---

# Sample Request

```json
{
  "source": "whatsapp",
  "guest_name": "Rahul Sharma",
  "message": "Is the villa available from April 20 to 24?",
  "timestamp": "2026-05-05T10:30:00Z",
  "booking_ref": "NIS-2024-0891",
  "property_id": "villa-b1"
}
```

---

# Sample Response

```json
{
  "message_id": "b47557fc-5b08-4ce3-9d35-0fae49514019",
  "query_type": "pre_sales_availability",
  "drafted_reply": "Hi Rahul! Great news — Villa B1 is available from April 20–24.",
  "confidence_score": 0.93,
  "action": "auto_send"
}
```

---

# Action Routing Logic

| Action       | Description                     |
| ------------ | ------------------------------- |
| auto_send    | Safe automated AI response      |
| agent_review | Requires human review           |
| escalate     | Operational escalation required |

---

# Message Processing Flow

The backend follows the following operational flow:

1. Incoming payload validated using Pydantic
2. Message normalized into unified internal schema
3. Deterministic query classification applied
4. AI-generated draft reply created
5. Confidence score calculated
6. Operational action determined
7. Structured response returned

---

# Unified Internal Schema

All inbound messages are normalized into the following internal structure:

```json
{
  "message_id": "generated_uuid",
  "source": "whatsapp",
  "guest_name": "Rahul Sharma",
  "message_text": "Is the villa available from April 20 to 24?",
  "timestamp": "2026-05-05T10:30:00Z",
  "booking_ref": "NIS-2024-0891",
  "property_id": "villa-b1",
  "query_type": "pre_sales_availability"
}
```

---

# AI Integration Design

The AI provider layer was intentionally isolated from the core backend pipeline.

This architecture allows:

* provider flexibility
* easier future migration
* improved maintainability
* independent AI orchestration

The backend can support future migration between:

* Anthropic APIs
* OpenRouter
* OpenAI
* Gemini
* local LLMs

without affecting the rest of the backend architecture.

---

# Deterministic Query Classification

The project intentionally uses deterministic keyword-based classification instead of LLM-based classification.

This decision was made to improve:

* reliability
* explainability
* predictability
* operational consistency
* response latency
* infrastructure cost

Deterministic scoring was intentionally chosen over opaque AI confidence estimation to improve explainability and operational reliability.

---

# Confidence Scoring Logic

The confidence engine determines how safely an AI-generated response can be automated.

The scoring system considers:

* query type
* operational risk
* emotional language
* complaint detection
* ambiguity

---

# Base Confidence Scores

| Query Type             | Base Confidence |
| ---------------------- | --------------- |
| pre_sales_availability | 0.93            |
| pre_sales_pricing      | 0.90            |
| post_sales_checkin     | 0.88            |
| general_enquiry        | 0.82            |
| special_request        | 0.72            |
| complaint              | 0.40            |

---

# Risk-Aware Adjustments

Messages containing high-risk keywords such as:

* refund
* urgent
* unacceptable
* angry
* terrible

automatically reduce confidence scores.

Complaints are always escalated regardless of score.

---

# Error Handling Strategy

The backend was intentionally designed with graceful degradation principles.

The system continues functioning even if the AI provider becomes unavailable.

Implemented protections include:

* AI provider fallback responses
* timeout handling
* validation protection
* exception handling
* operational failover responses
* structured logging

---

# Fallback Response System

If the AI provider fails:

* the webhook endpoint remains operational
* structured responses are still returned
* fallback operational responses are generated
* escalation logic still executes

This ensures the messaging pipeline remains resilient under partial failure conditions.

---

# Validation Strategy

Pydantic validation is used for:

* supported source validation
* guest name validation
* message length validation
* payload structure enforcement
* timestamp validation

This improves API reliability and protects against malformed requests.

---

# AI Safety Guardrails

The prompt system includes operational safety rules.

The AI is instructed to:

* avoid fabricating unavailable information
* avoid guaranteeing refunds
* avoid promising unsupported services
* encourage human review when uncertain

This reduces operational risk and improves response safety.

---

# Database Design Overview

The PostgreSQL schema was designed using normalized relational architecture principles.

The schema supports:

* unified guest identities
* reservation linkage
* multi-channel conversations
* message threading
* AI operational metadata
* auditability

---

# Core Tables

| Table               | Purpose                           |
| ------------------- | --------------------------------- |
| guests              | Unified guest identity            |
| reservations        | Booking information               |
| conversations       | Communication threading           |
| messages            | Unified inbound/outbound messages |
| ai_message_metadata | AI operational tracking           |

---

# Hardest Design Decision

The most important architectural decision was separating conversations from reservations.

This design allows:

* guests to communicate before booking
* multiple conversations per reservation
* communication continuity across channels
* future CRM extensibility
* scalable support workflows

This separation more accurately models real-world hospitality communication systems.

---

# Testing

The system was tested using multiple operational scenarios.

---

# Tested Scenarios

| Scenario               | Expected Result    |
| ---------------------- | ------------------ |
| Availability inquiry   | auto_send          |
| Pricing inquiry        | auto_send          |
| Special request        | agent_review       |
| Complaint message      | escalate           |
| Invalid source payload | validation failure |
| AI provider failure    | fallback response  |

---

# Example Complaint Flow

Input:

```json
{
  "message": "The AC is not working and I want a refund."
}
```

Expected Behavior:

* classified as complaint
* confidence reduced
* action escalated
* operational fallback available

---

# Scalability Considerations

The project architecture was intentionally designed to support future scalability.

Key scalability decisions include:

* modular service separation
* AI provider abstraction
* normalized schema design
* reusable processing pipeline
* operational routing isolation

---

# Future Improvements

Potential future improvements include:

* Redis caching
* Celery/RabbitMQ background processing
* real-time WebSocket notifications
* sentiment analysis
* multilingual support
* conversation memory
* vector search / retrieval systems
* AI analytics dashboard
* automated escalation workflows
* property performance analytics
* maintenance issue trend detection
* CRM integration

---

# Production Considerations

Additional production-level improvements could include:

* authentication and authorization
* rate limiting
* containerization with Docker
* CI/CD pipelines
* monitoring and observability
* centralized logging
* database persistence layer
* asynchronous task queues

---

# Conclusion

This project was designed with a strong focus on:

* modular backend architecture
* operational reliability
* explainable AI decision-making
* graceful degradation
* scalability
* maintainability

The overall goal was to build a realistic hospitality messaging backend that balances AI automation with operational safety and human oversight.
