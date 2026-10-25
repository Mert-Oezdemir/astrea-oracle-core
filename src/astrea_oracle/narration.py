"""Optional provider boundary: implementations must respect consent and privacy."""
from typing import Protocol

class Narrator(Protocol):
    """An integration may summarize already-explained results; no raw PII required."""
    def narrate(self, safe_summary: str) -> str: ...

class LocalNarrator:
    """Dependency-free safe default, useful for tests and offline demos."""
    def narrate(self, safe_summary: str) -> str:
        return ("Reflective preview (not a prediction): " + safe_summary +
                " Have a conversation and make your own decision.")
