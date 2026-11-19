
import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI


class HealthMateConfigurationError(Exception):
    """Raised when the application is missing required configuration."""


def get_health_advice(symptom_text: str, language: str = "English") -> str:
    """Generate general health information in the selected language."""

    load_dotenv()

    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise HealthMateConfigurationError(
            "Google API credentials are not configured. "
            "Add GOOGLE_API_KEY to your local .env file."
        )

    model_name = os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite")

    llm = ChatGoogleGenerativeAI(
        model=model_name,
        temperature=0.2,
        google_api_key=api_key,
        timeout=30,
        max_retries=1,
    )

    supported_languages = ["English", "Hindi", "Gujarati"]

    if language not in supported_languages:
        raise ValueError("Unsupported language selected.")

    prompt = f"""
You provide general health information for educational purposes,
not medical diagnoses.

Respond entirely in {language}.

Do not claim certainty or tell the user what condition they have.
If symptoms could indicate an emergency, advise the user to seek
urgent professional care.

Do not recommend medications or dosages.

IMPORTANT FORMATTING:
Keep the following two section headings EXACTLY as written in English,
even when the rest of the response is in another language:

**Possible Causes**
Briefly describe a few general possibilities in {language},
using plain language and appropriate uncertainty.

**Home Remedies**
Provide 3-5 low-risk general self-care suggestions in {language}.
Mention when professional medical advice is important.

User-described symptoms:
{symptom_text}
"""

    response = llm.invoke([HumanMessage(content=prompt)])
    content = response.content

    if isinstance(content, str):
        return content.strip()

    if isinstance(content, list):
        text_parts = []

        for block in content:
            if isinstance(block, dict):
                text = block.get("text")

                if isinstance(text, str):
                    text_parts.append(text)

            elif isinstance(block, str):
                text_parts.append(block)

        return "\n".join(text_parts).strip()

    raise ValueError("Gemini returned an unsupported response format.")
