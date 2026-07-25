from models.master_content import MasterContent


class TitleAgent:
    def __init__(self):
        self.name = "Title Agent"

    def run(self, content: MasterContent):
        print()
        print("🏷️ Title Agent")
        print(f"Creating title for: {content.topic}")

        content.title = f"How to Master {content.topic} in 2026"