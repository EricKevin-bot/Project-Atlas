from dataclasses import dataclass, field
from typing import List


@dataclass
class ReviewResult:
    approved: bool = False

    overall_score: float = 0.0

    topic_score: float = 0.0
    title_score: float = 0.0
    script_score: float = 0.0
    description_score: float = 0.0
    tags_score: float = 0.0

    recommendation: str = ""

    feedback: List[str] = field(default_factory=list)


