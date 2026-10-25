"""Traditional zodiac symbolism is for creative reflection only."""
from typing import Optional

ELEMENT = {
    "aries": "fire", "leo": "fire", "sagittarius": "fire",
    "taurus": "earth", "virgo": "earth", "capricorn": "earth",
    "gemini": "air", "libra": "air", "aquarius": "air",
    "cancer": "water", "scorpio": "water", "pisces": "water",
}

def symbolic_pair_note(sign_a: Optional[str], sign_b: Optional[str]) -> Optional[str]:
    if sign_a is None or sign_b is None:
        return None
    a = ELEMENT[sign_a.lower()]
    b = ELEMENT[sign_b.lower()]
    if a == b:
        contrast = f"Both signs belong to the traditional {a} element."
    else:
        contrast = f"Traditional symbolism pairs {a} and {b} elements here."
    return (
        "Symbolic astrology reflection only: " + contrast +
        " Use it as a conversation prompt, not as a personality assessment, "
        "forecast, or compatibility fact."
    )
