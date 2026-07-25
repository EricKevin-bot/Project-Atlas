from models.master_content import MasterContent


class TagsAgent:
    def __init__(self):
        self.name = "Tags Agent"

    def run(self, content: MasterContent):
        print()
        print("🏷️ Tags Agent")
        print(f"Generating tags for: {content.topic}")

        tags = [
            content.topic.lower(),
            "finance",
            "investing",
            "wealth",
            "money",
            "financial freedom",
            "personal finance",
            "success"
        ]

        # Remove duplicates while preserving order
        content.tags = list(dict.fromkeys(tags))