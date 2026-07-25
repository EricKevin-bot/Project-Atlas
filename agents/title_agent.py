from models.master_content import MasterContent
from services.claude_provider import ClaudeProvider


class TitleAgent:
    def __init__(self) -> None:
        self.name = "Title Agent"
        self.ai = ClaudeProvider()

    def run(self, content: MasterContent) -> None:
        print()
        print("🏷️ Title Agent")
        print(f"Creating title for: {content.topic}")

        prompt = f"""
You are an expert YouTube title strategist.

Create one compelling YouTube title for this video.

Topic: {content.topic}
Audience: {content.audience}
Objective: {content.objective}

Requirements:
- Make it emotionally compelling
- Create curiosity
- Keep it under 70 characters where possible
- Avoid clickbait that the video cannot deliver
- Return only the title
""".strip()

        title = self.ai.generate(
            prompt=prompt,
            max_tokens=100,
        )

        content.title = title.strip().strip('"').strip("*")
