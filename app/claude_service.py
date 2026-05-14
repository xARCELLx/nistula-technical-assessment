from openai import OpenAI

from app.config import CLAUDE_API_KEY
from app.prompts import build_guest_prompt
from app.constants import FALLBACK_RESPONSES
from app.utils import log_event

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=CLAUDE_API_KEY
)


async def generate_ai_reply(unified_message):

    try:

        prompt = build_guest_prompt(unified_message)

        response = client.chat.completions.create(
            model="deepseek/deepseek-v4-flash:free",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=200,
            extra_body={
                "reasoning": {
                    "enabled": True
                }
            }
        )

        print(response)

        if (
            response.choices
            and len(response.choices) > 0
            and response.choices[0].message
        ):

            return response.choices[0].message.content

        return "We are currently unable to generate a response."

    except Exception as error:

        log_event(
            "AI_ERROR",
            str(error)
        )

        return FALLBACK_RESPONSES.get(
            unified_message.query_type,
            "Our team will get back to you shortly."
        )