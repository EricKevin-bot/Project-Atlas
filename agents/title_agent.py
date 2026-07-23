from models.master_content import MasterContent


class TitleAgent:
    def __init__(self):
        self.name = "Title Agent"

    def create_title(self, content: MasterContent):
        print()
        print("🏷️ Title Agent")
        print(f"Creating title for: {content.topic}")

        return f"{content.topic}: The Truth Nobody Tells You"