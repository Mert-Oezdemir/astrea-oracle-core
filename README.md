# ASTREA · Oracle Core

**Open-source infrastructure for explainable, consent-first compatibility research and symbolic AI experiences.**

> **Status: experimental open-source starter (v0.1.0).** ASTREA is a proposed ecosystem, not an operational predictive oracle, clinically validated system, or a product with established adoption. The reference implementation works locally using the Python standard library. An LLM provider, astronomical ephemeris, and scientifically validated prediction service are **not** shipped.

ASTREA's long-term vision is a reusable, provider-agnostic core for new types of social discovery, self-reflection, creative scenario exploration, and future application experiments. It combines structured preferences, transparent rules, optional *symbolic* astrological metadata, and plug-in AI narration. Application developers can create different experiences on a shared core without having to claim that birth charts can predict human behavior or world events.

## Why build this?

1. **Compatibility should be explainable.** A reference matcher prioritizes mutually consented values and interests, not unverifiable claims about people.
2. **Astrology should be labeled.** Zodiac-derived notes are optional, symbolic narratives and **never** determine the numeric match score.
3. **AI should be replaceable.** `Narrator` is a small protocol. By default, ASTREA runs without remote inference; integrations must opt in and enforce privacy constraints.
4. **A single core can power multiple apps.** Human-facing UI, partner applications, and research tools can consume an explicit typed result contract.
5. **Safety and privacy are part of the interface.** Adult-only matching, mutual consent, no persistence, no protected-class inference, and rejection of high-stakes scoring are built into the reference API.

## Quick start

Requires **Python 3.10+**, with no external dependencies.

```bash
python -m astrea_oracle
python -m unittest discover -s tests -v
```

Or run a local example program:

```python
from astrea_oracle import AstreaOracle, Profile

alice = Profile(profile_id="alice", age=26, consent=True,
                interests=("art", "hiking"), values=("kindness", "curiosity"), zodiac_sign="aries")
bob = Profile(profile_id="bob", age=28, consent=True,
              interests=("hiking", "music"), values=("kindness", "humor"), zodiac_sign="libra")
result = AstreaOracle().match(alice, bob)
print(result.to_dict())  # explanation and symbolic note are separate
```

### What exists in this release

| Component | Status |
|---|---|
| Typed, dependency-free Python core | Working reference implementation |
| Consent-aware adult social matching | Working reference implementation |
| Explainable interests/values overlap | Working reference implementation |
| Optional astrology **symbolic** narratives | Working reference implementation |
| Local CLI demo and automated unit tests | Included |
| Optional LLM narrator interface | Extension protocol only; no integration bundled |
| Ephemeris-backed natal and transit computation | Planned, not implemented |
| Event forecasting, behavioral prediction | Research vision only; not supported or validated |
| Dating, health, financial, security, economic applications | Concepts only; not implemented |

## Core principle

**A symbolic interpretation is not a forecast.** Astrology is not established as a scientifically reliable way to predict personalities, compatibility, illness, financial outcomes, threats, or external events. Do not market this starter as accurate personal or event prediction. Match scores are *demo overlap measures*, not measured success probabilities; **a score of 80 is not an 80% chance of a successful relationship.**

We explicitly prohibit using ASTREA's reference results for medical decisions, employment, lending, insurance, law enforcement, safety-critical decisions, or other consequential classifications. See [SAFETY.md](SAFETY.md).

## Architecture

```text
Consent-first profile input ──> Guardrails ──> Explainable match rules ──> Typed result
                                                │
                                                └──> Symbolic notes (optional)
                                                          │
                                                          └──> Optional narrator plug-in
```

- `src/astrea_oracle/models.py`: typed consented input and result schemas
- `src/astrea_oracle/core.py`: explainable deterministic matching
- `src/astrea_oracle/symbolic.py`: clearly labeled interpretive notes
- `src/astrea_oracle/narration.py`: opt-in integration boundary for future models
- `tests/`: runnable unit tests; GitHub Actions workflow verifies tests
- `docs/ARCHITECTURE.md`: integration and data-boundary notes
- `docs/ROADMAP.md`: credible milestones and evidence goals

## Scope, contributors and maintenance

This repository is a self-contained **public open-source reference core**. It is independent from any private research, closed-source applications, datasets, existing commercial IP, or third-party astrology packages. Please open a GitHub issue for a bug, test gap, research proposal, or documentation improvement. All data supplied to the demos are synthetic.

Contributors: review [CONTRIBUTING.md](CONTRIBUTING.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), and [SECURITY.md](SECURITY.md). No commercial integrations are required. The roadmap includes reproducible benchmarks and an evidence-based evaluation process before any claims of predictive benefit.

## Ownership, open source, and brand

Copyright © 2026 **Mert-Oezdemir** and contributors. Original code is released under the [Apache License 2.0](LICENSE). ASTREA / ASTREA Oracle Core branding and logos are **not granted** for third-party product endorsements by the code license; see [TRADEMARKS.md](TRADEMARKS.md). This notice does **not** imply a registered or legally exclusive trademark. The name requires an appropriate clearance search before commercial use.

> The open-source license allows others to use and modify the code (including commercially), subject to its terms. If a future proprietary application is needed, keep its separate code and confidential assets outside this public repository.