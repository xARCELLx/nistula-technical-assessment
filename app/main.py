from fastapi import FastAPI
from app.schemas import IncomingMessage
from app.utils import normalize_message
from app.claude_service import generate_ai_reply

app = FastAPI(
    title="Nistula Unified Messaging API",
    description="AI-powered guest messaging backend system",
    version="1.0.0"
)


@app.get("/")
async def root():
    return {"message": "Nistula backend is running"}


@app.post("/webhook/message")
async def handle_message(payload: IncomingMessage):

    unified_message = normalize_message(payload)

    drafted_reply = await generate_ai_reply(unified_message)

    return {
        "message_id": str(unified_message.message_id),
        "query_type": unified_message.query_type,
        "drafted_reply": drafted_reply
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy"
    }