"""Input/output contracts for ASTREA's educational reference engine."""
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Optional, Tuple

VALID_SIGNS = frozenset((
    "aries", "taurus", "gemini", "cancer", "leo", "virgo",
    "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces",
))

@dataclass(frozen=True)
class Profile:
    """Consent is required for each evaluation; no birth times or locations needed."""
    profile_id: str
    age: int
    consent: bool
    interests: Tuple[str, ...] = ()
    values: Tuple[str, ...] = ()
    zodiac_sign: Optional[str] = None

    def __post_init__(self) -> None:
        if not self.profile_id.strip():
            raise ValueError("profile_id must be nonempty")
        if not isinstance(self.age, int) or isinstance(self.age, bool) or self.age < 0:
            raise ValueError("age must be a nonnegative integer")
        if not isinstance(self.consent, bool):
            raise ValueError("consent must be boolean")
        if self.zodiac_sign is not None and self.zodiac_sign.lower() not in VALID_SIGNS:
            raise ValueError("unrecognized zodiac_sign")
        for field_name, items in (("interests", self.interests), ("values", self.values)):
            if any(not isinstance(x, str) or not x.strip() for x in items):
                raise ValueError(f"{field_name} must contain nonempty strings")

@dataclass(frozen=True)
class MatchResult:
    overlap_score: float
    shared_interests: Tuple[str, ...]
    shared_values: Tuple[str, ...]
    explanation: str
    symbolic_note: Optional[str]
    warning: str = (
        "Experimental preference overlap only; not a probability of relationship success "
        "or a validated personality prediction."
    )

    def to_dict(self) -> dict:
        return asdict(self)
