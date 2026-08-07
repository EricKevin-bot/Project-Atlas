from pathlib import Path
from typing import Optional, Tuple

from agents.description_agent import DescriptionAgent
from agents.quality_agent import QualityAgent
from agents.research_agent import ResearchAgent
from agents.script_agent import ScriptAgent
from agents.tags_agent import TagsAgent
from agents.title_agent import TitleAgent
from config import MAX_RETRIES, RETRY_FAILED_AGENTS
from models.master_content import MasterContent
from services.file_manager import FileManager
from services.retry_manager import RetryManager


PipelineResult = Tuple[MasterContent, Optional[Path], str]


class ContentPipeline:
    def __init__(self) -> None:
        self.research_agent = ResearchAgent()
        self.title_agent = TitleAgent()
        self.script_agent = ScriptAgent()
        self.description_agent = DescriptionAgent()
        self.tags_agent = TagsAgent()
        self.quality_agent = QualityAgent()
        self.file_manager = FileManager()
        self.retry_manager = RetryManager()

    def run(self) -> PipelineResult:
        print("\n🚀 Starting Content Pipeline...\n")

        content = MasterContent(
            topic="",
            audience="",
            objective="",
            key_points=[],
            call_to_action="",
        )

        # Research
        self.research_agent.run(content)

        print(f"\n💡 Proposed Topic: {content.topic}")
        print(f"🎯 Audience: {content.audience}")
        print(f"📌 Objective: {content.objective}")

        approval = input(
            "\nApprove this topic? (y/n): "
        ).strip().lower()

        if approval != "y":
            print("\n❌ Content rejected.")
            return content, None, "TOPIC_REJECTED"

        # Production
        production_agents = [
            self.title_agent,
            self.script_agent,
            self.description_agent,
            self.tags_agent,
        ]

        for agent in production_agents:
            agent.run(content)

        # Initial quality review
        content.review = self.quality_agent.run(content)

        self._display_content_package(content)
        self._display_quality_report(content)

        # Targeted retry system
        retry_count = 0

        while (
            not content.review.approved
            and RETRY_FAILED_AGENTS
            and retry_count < MAX_RETRIES
        ):
            retry_count += 1

            print("\n" + "=" * 40)
            print(f"🔄 TARGETED RETRY {retry_count}/{MAX_RETRIES}")
            print("=" * 40)

            previous_recommendation = content.review.recommendation

            print(
                f"Quality Agent recommendation: "
                f"{previous_recommendation}"
            )

            content = self.retry_manager.retry(
                review=content.review,
                content=content,
                pipeline=self,
            )

            self._display_quality_report(content)

        # Final quality gate
        if not content.review.approved:
            print("\n❌ Quality review rejected this content package.")
            print(
                f"Recommendation: "
                f"{content.review.recommendation}"
            )

            if retry_count >= MAX_RETRIES and MAX_RETRIES > 0:
                print(
                    f"Retry limit reached ({MAX_RETRIES}). "
                    "Human review required."
                )

            print("The file will not be exported yet.")

            return content, None, "QUALITY_REJECTED"

        # Export approved package
        output_path = self.file_manager.save_content(
            title=content.title,
            script=content.script,
            description=content.description,
            tags=content.tags,
        )

        print("\n✅ Pipeline complete.")

        if retry_count:
            print(
                f"🔄 Approved after {retry_count} targeted retry."
            )

        return content, output_path, "SUCCESS"

    @staticmethod
    def _display_content_package(
        content: MasterContent,
    ) -> None:
        print("\n" + "=" * 40)
        print("📦 CONTENT PACKAGE")
        print("=" * 40)

        print(f"\n🎬 TITLE\n{content.title}")
        print(f"\n📝 DESCRIPTION\n{content.description}")
        print(f"\n🏷️ TAGS\n{', '.join(content.tags)}")
        print(f"\n📄 SCRIPT\n{content.script}")

    @staticmethod
    def _display_quality_report(
        content: MasterContent,
    ) -> None:
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