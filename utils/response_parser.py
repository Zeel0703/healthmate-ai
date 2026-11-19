import re


def extract_sections(response: str) -> dict[str, str]:
    """Extract the two labelled sections from the model response."""
    text = response or ""

    causes_match = re.search(
        r"(?:\*\*)?\s*Possible\s+Causes?\s*(?:\*\*)?\s*:?\s*",
        text,
        flags=re.IGNORECASE,
    )
    remedies_match = re.search(
        r"(?:\*\*)?\s*Home\s+Remedies\s*(?:\*\*)?\s*:?\s*",
        text,
        flags=re.IGNORECASE,
    )

    causes = ""
    remedies = ""

    if causes_match:
        end = remedies_match.start() if remedies_match and remedies_match.start() > causes_match.end() else len(text)
        causes = text[causes_match.end():end].strip()

    if remedies_match:
        remedies = text[remedies_match.end():].strip()

    return {
        "possible_causes": causes,
        "home_remedies": remedies,
    }
