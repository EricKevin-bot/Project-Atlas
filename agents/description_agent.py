from models.master_content import MasterContent


class DescriptionAgent:
    def __init__(self) -> None:
        self.name = "Description Agent"

    def run(self, content: MasterContent) -> None:
        print()
        print("📝 Description Agent")
        print(f"Creating description for: {content.topic}")

        bullets = "\n".join(
            f"• {point}" for point in content.key_points
        )

        content.description = f"""
{content.topic}

In this video you'll learn:

{bullets}

Subscribe for practical financial education every week.

#finance #wealth #investing #money
""".strip()
