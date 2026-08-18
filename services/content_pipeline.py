from pathlib import Path
from typing import Optional, Tuple

from agents.description_agent import DescriptionAgent
from agents.research_agent import ResearchAgent
from agents.script_agent import ScriptAgent
from agents.tags_agent import TagsAgent
from agents.thumbnail_agent import ThumbnailAgent
from agents.title_agent import TitleAgent
from config import (
    GENERATE_THUMBNAIL_IMAGE,
    MAX_RETRIES,
    RETRY_FAILED_AGENTS,
)
from models.master_content import MasterContent
from services.editorial_board import EditorialBoard
from services.file_manager import FileManager
from services.retry_manager import RetryManager
from services.thumbnail_renderer import ThumbnailRenderer


PipelineResult = Tuple[MasterContent, Optional[Path], str]


class ContentPipeline:
    def __init__(self) -> None:
        self.research_agent = ResearchAgent()
        self.title_agent = TitleAgent()
        self.script_agent = ScriptAgent()
        self.thumbnail_agent = ThumbnailAgent()
        self.description_agent = DescriptionAgent()
        self.tags_agent = TagsAgent()

        self.editorial_board = EditorialBoard()
        self.file_manager = FileManager()
        self.retry_manager = RetryManager()
        self.thumbnail_renderer = ThumbnailRenderer()

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
            self.thumbnail_agent,
            self.description_agent,
            self.tags_agent,
        ]

        for agent in production_agents:
            agent.run(content)

        # Initial editorial review
        content.review = self.editorial_board.review(content)

        self._display_content_package(content)
        self._display_editorial_report(content)

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

            print(
                f"Editorial Board recommendation: "
                f"{content.review.recommendation}"
            )

            content = self.retry_manager.retry(
                review=content.review,
                content=content,
                pipeline=self,
            )

            self._display_editorial_report(content)

        # Final editorial gate
        if not content.review.approved:
            print(
                "\n❌ Editorial Board rejected this content package."
            )
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

            return content, None, "EDITORIAL_REJECTED"

        # Thumbnail rendering is optional.
        # A rendering/provider failure must not destroy an
        # otherwise approved content package.
        if GENERATE_THUMBNAIL_IMAGE:
            try:
                self.thumbnail_renderer.render(content)

            except Exception as error:
                content.thumbnail_image_path = ""

                print("\n⚠️ Thumbnail rendering failed.")
                print(f"Reason: {error}")
                print(
                    "Atlas will continue and export the "
                    "approved content package."
                )

        # Export approved package regardless of thumbnail
        # rendering success.
        output_path = self.file_manager.save_content(
            title=content.title,
            script=content.script,
            description=content.description,
            tags=content.tags,
            thumbnail_prompt=content.thumbnail_prompt,
        )

        print("\n✅ Pipeline complete.")

        if retry_count:
            print(
                f"🔄 Approved after {retry_count} targeted retry."
            )

        if content.thumbnail_image_path:
            print(
                f"🖼️ Thumbnail image: "
                f"{content.thumbnail_image_path}"
            )
        elif GENERATE_THUMBNAIL_IMAGE:
            print(
                "⚠️ Content exported without a rendered "
                "thumbnail image."
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

        print(
            f"\n🖼️ THUMBNAIL BRIEF\n"
            f"{content.thumbnail_prompt}"
        )

        print(f"\n📝 DESCRIPTION\n{content.description}")
        print(f"\n🏷️ TAGS\n{', '.join(content.tags)}")
        print(f"\n📄 SCRIPT\n{content.script}")

    @staticmethod
    def _display_editorial_report(
        content: MasterContent,
    ) -> None:
        if content.review is None:
            print("\n⚠️ No editorial review available.")
            return

        review = content.review

        print("\n" + "=" * 40)
        print("🧪 EDITORIAL BOARD REPORT")
        print("=" * 40)

        print(
            f"\nApproved: "
            f"{'Yes' if review.approved else 'No'}"
        )

        print(
            f"Overall score: "
            f"{review.overall_score:.1f}/10"
        )

        print(
            f"Recommendation: "
            f"{review.recommendation}"
        )

        if review.scores:
            print("\nSpecialist scores:")

            for area, score in review.scores.items():
                print(
                    f"- {area.title()}: "
                    f"{score:.1f}/10"
                )

        if review.feedback:
            print("\nSpecialist feedback:")

            for area, feedback in review.feedback.items():
                print(
                    f"- {area.title()}: "
                    f"{feedback}"
                )