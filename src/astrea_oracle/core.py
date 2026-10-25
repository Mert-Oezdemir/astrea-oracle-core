"""Transparent, opt-in social-discovery prototype; NOT a predictive AI model."""
from .models import MatchResult, Profile
from .symbolic import symbolic_pair_note

BLOCKED_PURPOSES = frozenset({
    "health", "medical", "mental_health", "credit", "finance", "employment",
    "hiring", "insurance", "housing", "law_enforcement", "security",
    "legal", "public_benefits", "safety_critical", "education_admissions",
})


def _normalize(items: tuple[str, ...]) -> set[str]:
    return {item.strip().casefold() for item in items if item.strip()}


def _overlap(left: set[str], right: set[str]) -> float:
    """Jaccard similarity for declared opt-in tags (not a prediction)."""
    if not left and not right:
        return 0.0
    return len(left & right) / len(left | right)


class AstreaOracle:
    """Reference matching engine. Does not store, transmit, or infer identities."""

    def match(self, a: Profile, b: Profile, *, purpose: str = "social_discovery") -> MatchResult:
        normalized_purpose = purpose.strip().casefold()
        if normalized_purpose != "social_discovery" or normalized_purpose in BLOCKED_PURPOSES:
            raise ValueError("Only opt-in, non-consequential social_discovery is supported")
        if a.profile_id == b.profile_id:
            raise ValueError("matching a profile with itself is not supported")
        if not a.consent or not b.consent:
            raise PermissionError("both adults must give explicit consent")
        if a.age < 18 or b.age < 18:
            raise PermissionError("social matching is for adults aged 18+ only")
        interests_a, interests_b = _normalize(a.interests), _normalize(b.interests)
        values_a, values_b = _normalize(a.values), _normalize(b.values)
        shared_interests = tuple(sorted(interests_a & interests_b))
        shared_values = tuple(sorted(values_a & values_b))
        # Demonstration weights chosen for clarity, not learned, calibrated, or validated.
        score = round(100 * (0.4 * _overlap(interests_a, interests_b) +
                             0.6 * _overlap(values_a, values_b)), 2)
        explanation = (
            f"Declared interests overlap: {len(shared_interests)} shared; "
            f"declared values overlap: {len(shared_values)} shared. "
            "Score = 40% interests + 60% values Jaccard similarity. "
            "No astrology information is used to calculate the score."
        )
        return MatchResult(score, shared_interests, shared_values, explanation,
                           symbolic_pair_note(a.zodiac_sign, b.zodiac_sign))
