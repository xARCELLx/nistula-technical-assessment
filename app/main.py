from fastapi import FastAPI
from app.schemas import IncomingMessage

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

    return {
        "message_id": "temporary-id",
        "status": "message received",
        "source": payload.source,
        "guest_name": payload.guest_name
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy"
    }