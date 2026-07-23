from services.ai_provider import AIProvider
from models.master_content import MasterContent


class ResearchAgent:
    def __init__(self):
        self.name = "Research Agent"
        self.ai = AIProvider()

    def find_video_idea(self):
        print()
        print("🔎 Research Agent")
        print("Researching a new content idea...")

        video_idea = self.ai.generate_video_idea()

        content = MasterContent(
            topic=video_idea,
            audience="People who want to improve their finances",
            objective="Explain why higher income does not always create wealth",
            key_points=[
                "Lifestyle inflation",
                "High-interest debt",
                "Lack of emergency savings",
                "Not investing consistently",
            ],
            call_to_action="Subscribe for practical financial education",
            keywords=[
                "personal finance",
                "wealth building",
                "money habits",
                "debt",
                "investing",
            ],
        )

        return content