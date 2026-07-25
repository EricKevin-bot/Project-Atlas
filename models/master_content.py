from dataclasses import dataclass, field
from typing import List


@dataclass
class MasterContent:
    # Research
    topic: str
    audience: str
    objective: str
    key_points: List[str]
    call_to_action: str
    keywords: List[str] = field(default_factory=list)

    # Generated assets
    title: str = ""
    script: str = ""
    description: str = ""
    tags: List[str] = field(default_factory=list)
    thumbnail_prompt: str = ""
    voiceover_prompt: str = ""