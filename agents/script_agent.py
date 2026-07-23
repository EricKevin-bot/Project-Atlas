from models.master_content import MasterContent
from services.ai_provider import AIProvider


class ScriptAgent:
    def __init__(self):
        self.name = "Script Agent"
        self.ai = AIProvider()

    def write_script(self, content: MasterContent) -> str:
        print()
        print("✍️ Script Agent")
        print(f"Writing script for: {content.topic}")

        script = self.ai.generate_script(
            video_idea=content.topic,
            audience=content.audience,
            objective=content.objective,
            key_points=content.key_points,
            call_to_action=content.call_to_action,
        )

        return script