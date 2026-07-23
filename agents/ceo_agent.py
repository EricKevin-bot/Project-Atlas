from datetime import datetime

from services.content_pipeline import ContentPipeline


class CEOAgent:
    def __init__(self):
        self.name = "CEO Agent"

    def morning_briefing(self):
        print("====================================")
        print("🚀 Project Atlas")
        print("Good morning, Eric.")
        print(
            f"Current time: "
            f"{datetime.now().strftime('%A %d %B %Y - %H:%M')}"
        )
        print("Today's mission:")
        print("- Research one winning video idea")
        print("- Create one script")
        print("- Publish one video")
        print("====================================")

    def run_company(self):
        pipeline = ContentPipeline()
        pipeline.run()


if __name__ == "__main__":
    ceo = CEOAgent()
    ceo.morning_briefing()
    ceo.run_company()