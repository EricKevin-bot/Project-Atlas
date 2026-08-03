from datetime import datetime
from time import perf_counter

from config import ATLAS_VERSION, DEVELOPMENT_MODE
from services.content_pipeline import ContentPipeline


class CEOAgent:
    def __init__(self) -> None:
        self.name = "CEO Agent"

    def morning_briefing(self) -> None:
        mode = "DEVELOPMENT" if DEVELOPMENT_MODE else "PRODUCTION"

        print("=" * 40)
        print(f"🚀 Project Atlas v{ATLAS_VERSION}")
        print(f"Mode: {mode}")
        print("Good morning, Eric.")
        print(
            "Current time: "
            f"{datetime.now().strftime('%A %d %B %Y - %H:%M')}"
        )
        print("Today's mission:")
        print("- Research one winning video idea")
        print("- Create one script")
        print("- Review content quality")
        print("- Export approved content")
        print("=" * 40)

    def run_company(self) -> None:
        started_at = perf_counter()

        pipeline = ContentPipeline()
        content, output_path, status = pipeline.run()

        elapsed_seconds = perf_counter() - started_at

        self._display_run_summary(
            content=content,
            output_path=output_path,
            status=status,
            elapsed_seconds=elapsed_seconds,
        )

    @staticmethod
    def _display_run_summary(
        content,
        output_path,
        status: str,
        elapsed_seconds: float,
    ) -> None:
        mode = "DEVELOPMENT" if DEVELOPMENT_MODE else "PRODUCTION"

        print("\n" + "=" * 40)
        print("📊 ATLAS RUN SUMMARY")
        print("=" * 40)

        print(f"\nVersion: {ATLAS_VERSION}")
        print(f"Mode: {mode}")
        print(f"Status: {status}")

        if content.review is not None:
            print(
                f"Quality score: "
                f"{content.review.overall_score:.1f}/10"
            )
            print(
                f"Recommendation: "
                f"{content.review.recommendation}"
            )
        else:
            print("Quality score: Not available")
            print("Recommendation: Not available")

        print(
            f"Output file: "
            f"{output_path if output_path else 'Not created'}"
        )
        print(f"Runtime: {elapsed_seconds:.1f} seconds")

        print("=" * 40)


if __name__ == "__main__":
    ceo = CEOAgent()
    ceo.morning_briefing()
    ceo.run_company()