from dataclasses import dataclass, field
from typing import Dict


@dataclass
class EditorialReview:
    approved: bool = False
    overall_score: float = 0.0
    recommendation: str = ""
    scores: Dict[str, float] = field(default_factory=dict)
    feedback: Dict[str, str] = field(default_factory=dict)