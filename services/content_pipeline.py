from agents.description_agent import DescriptionAgent
from agents.quality_agent import QualityAgent
from agents.research_agent import ResearchAgent
from agents.script_agent import ScriptAgent
from agents.tags_agent import TagsAgent
from agents.title_agent import TitleAgent
from models.master_content import MasterContent
from services.file_manager import FileManager


class ContentPipeline:
    def __init__(self) -> None:
        self.research_agent = ResearchAgent()
        self.title_agent = TitleAgent()
        self.script_agent = ScriptAgent()
        self.description_agent = DescriptionAgent()
        self.tags_agent = TagsAgent()
        self.quality_agent = QualityAgent()
        self.file_manager = FileManager()

    def run(self) -> None:
        print("\n🚀 Starting Content Pipeline...\n")

        content = MasterContent(
            topic="",
            audience="",
            objective="",
            key_points=[],
            call_to_action="",
        )

        self.research_agent.run(content)

        print(f"\n💡 Proposed Topic: {content.topic}")
        print(f"🎯 Audience: {content.audience}")
        print(f"📌 Objective: {content.objective}")

        approval = input("\nApprove this topic? (y/n): ").strip().lower()

        if approval != "y":
            print("\n❌ Content rejected.")
            return

        production_agents = [
            self.title_agent,
            self.script_agent,
            self.description_agent,
            self.tags_agent,
        ]

        for agent in production_agents:
            agent.run(content)

        content.review = self.quality_agent.run(content)

        self._display_content_package(content)
        self._display_quality_report(content)

        if not content.review.approved:
            print("\n❌ Quality review rejected this content package.")
            print(f"Recommendation: {content.review.recommendation}")
            print("The file will not be exported yet.")
            return

        self.file_manager.save_content(
            title=content.title,
            script=content.script,
            description=content.description,
            tags=content.tags,
        )

        print("\n✅ Pipeline complete.")

    @staticmethod
    def _display_content_package(content: MasterContent) -> None:
        print("\n" + "=" * 40)
        print("📦 CONTENT PACKAGE")
        print("=" * 40)

        print(f"\n🎬 TITLE\n{content.title}")
        print(f"\n📝 DESCRIPTION\n{content.description}")
        print(f"\n🏷️ TAGS\n{', '.join(content.tags)}")
        print(f"\n📄 SCRIPT\n{content.script}")

    @staticmethod
    def _display_quality_report(content: MasterContent) -> None:
        if content.review is None:
            print("\n⚠️ No quality review available.")
            return

        review = content.review

        print("\n" + "=" * 40)
        print("🧪 QUALITY REPORT")
        print("=" * 40)

        print(f"\nApproved: {'Yes' if review.approved else 'No'}")
        print(f"Overall score: {review.overall_score:.1f}/10")
        print(f"Topic score: {review.topic_score:.1f}/10")
        print(f"Title score: {review.title_score:.1f}/10")
        print(f"Script score: {review.script_score:.1f}/10")
        print(
            f"Description score: "
            f"{review.description_score:.1f}/10"
        )
        print(f"Tags score: {review.tags_score:.1f}/10")
        print(f"Recommendation: {review.recommendation}")

        if review.feedback:
            print("\nFeedback:")

            for item in review.feedback:
                print(f"- {item}")