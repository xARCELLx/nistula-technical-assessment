import httpx

from app.config import CLAUDE_API_KEY
from app.prompts import build_guest_prompt

async def generate_ai_reply(unified_message):

    prompt = build_guest_prompt(unified_message)

    headers = {
        "x-api-key": CLAUDE_API_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }

    payload = {
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 200,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    async with httpx.AsyncClient(timeout=30.0) as client:

        response = await client.post(
            "https://api.anthropic.com/v1/messages",
            headers=headers,
            json=payload
        )

    response_data = response.json()
    
    if "content" not in response_data:
        return "We are currently unable to generate a response."

    return response_data["content"][0]["text"]
    