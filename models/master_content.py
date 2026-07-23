from dataclasses import dataclass, field


@dataclass
class MasterContent:
    topic: str

    audience: str = ""

    objective: str = ""

    key_points: list[str] = field(default_factory=list)

    statistics: list[str] = field(default_factory=list)

    stories: list[str] = field(default_factory=list)

    quotes: list[str] = field(default_factory=list)

    call_to_action: str = ""

    keywords: list[str] = field(default_factory=list)