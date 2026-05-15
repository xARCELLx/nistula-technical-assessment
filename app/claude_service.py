import httpx

from app.config import CLAUDE_API_KEY
from app.prompts import build_guest_prompt
from app.constants import FALLBACK_RESPONSES
from app.utils import log_event


async def generate_ai_reply(unified_message):

    try:

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

        if response.status_code != 200:

            log_event(
                "CLAUDE_API_ERROR",
                f"Status Code: {response.status_code}"
            )

            log_event(
                "CLAUDE_API_RESPONSE",
                response.text
            )

            return FALLBACK_RESPONSES.get(
                unified_message.query_type,
                "Our team will get back to you shortly."
            )

        response_data = response.json()

        if (
            "content" in response_data
            and len(response_data["content"]) > 0
        ):

            return response_data["content"][0].get(
                "text",
                FALLBACK_RESPONSES.get(
                    unified_message.query_type,
                    "Our team will get back to you shortly."
                )
            )

        return FALLBACK_RESPONSES.get(
            unified_message.query_type,
            "Our team will get back to you shortly."
        )

    except Exception as error:

        log_event(
            "CLAUDE_EXCEPTION",
            str(error)
        )

        return FALLBACK_RESPONSES.get(
            unified_message.query_type,
            "Our team will get back to you shortly."
        )