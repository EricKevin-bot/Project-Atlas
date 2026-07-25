from models.master_content import MasterContent


class DescriptionAgent:
    def __init__(self):
        self.name = "Description Agent"

    def create_description(self, content: MasterContent) -> str:
        print()
        print("📝 Description Agent")
        print(f"Creating description for: {content.topic}")

        description = f"""
{content.topic}

In this video you'll learn:

{chr(10).join(f"• {point}" for point in content.key_points)}

Subscribe for practical financial education every week.

#finance #wealth #investing #money
""".strip()

        return description