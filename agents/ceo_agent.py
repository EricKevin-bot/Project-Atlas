from datetime import datetime
from time import perf_counter

from config import ATLAS_VERSION, DEVELOPMENT_MODE
from services.content_pipeline import ContentPipeline
from services.decision_engine import DecisionEngine


class CEOAgent:
    def __init__(self) -> None:
        self.name = "CEO Agent"
        self.decision_engine = DecisionEngine()

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

        if content.review is not None:
            decision = self.decision_engine.summarize(content.review)
            self._display_ceo_decision(decision)

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

    @staticmethod
    def _display_ceo_decision(decision: dict) -> None:
        print("\n" + "=" * 40)
        print("🧠 CEO DECISION")
        print("=" * 40)

        print(
            f"\nOverall score: "
            f"{decision['overall_score']:.1f}/10"
        )

        print(
            f"Strongest area: "
            f"{decision['strongest_area']} "
            f"({decision['strongest_score']:.1f}/10)"
        )

        print(
            f"Weakest area: "
            f"{decision['weakest_area']} "
            f"({decision['weakest_score']:.1f}/10)"
        )

        print(f"Decision: {decision['decision']}")
        print(f"Reason: {decision['reason']}")

        print("=" * 40)


if __name__ == "__main__":
    ceo = CEOAgent()
    ceo.morning_briefing()
    ceo.run_company()