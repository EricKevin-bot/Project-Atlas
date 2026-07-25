from agents.research_agent import ResearchAgent
from agents.title_agent import TitleAgent
from agents.script_agent import ScriptAgent
from agents.description_agent import DescriptionAgent
from agents.tags_agent import TagsAgent
from services.file_manager import FileManager


class ContentPipeline:
    def __init__(self) -> None:
        self.research_agent = ResearchAgent()
        self.title_agent = TitleAgent()
        self.script_agent = ScriptAgent()
        self.description_agent = DescriptionAgent()
        self.tags_agent = TagsAgent()
        self.file_manager = FileManager()

    def run(self) -> None:
        print("\n🚀 Starting Content Pipeline...\n")

        content = self.research_agent.find_video_idea()

        print(f"\n💡 Proposed Topic: {content.topic}")
        print(f"🎯 Audience: {content.audience}")
        print(f"📌 Objective: {content.objective}")

        approval = input("\nApprove this topic? (y/n): ").strip().lower()

        if approval != "y":
            print("\n❌ Content rejected.")
            return

        agents = [
            self.title_agent,
            self.script_agent,
            self.description_agent,
            self.tags_agent,
        ]

        for agent in agents:
            agent.run(content)

        self._display_content_package(content)

        self.file_manager.save_content(
            title=content.title,
            script=content.script,
            description=content.description,
            tags=content.tags,
        )

        print("\n✅ Pipeline complete.")

    @staticmethod
    def _display_content_package(content) -> None:
        print("\n" + "=" * 40)
        print("📦 CONTENT PACKAGE")
        print("=" * 40)

        print(f"\n🎬 TITLE\n{content.title}")
        print(f"\n📝 DESCRIPTION\n{content.description}")
        print(f"\n🏷️ TAGS\n{', '.join(content.tags)}")
        print(f"\n📄 SCRIPT\n{content.script}")