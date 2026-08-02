import json

from agents.base_agent import BaseAgent
from models.review_result import ReviewResult


class QualityAgent(BaseAgent):
    def run(self, content) -> ReviewResult:
        self.log("Reviewing complete content package")

        prompt = self.prompts.load(
            "quality",
            topic=content.topic,
            title=content.title,
            script=content.script,
            description=content.description,
            tags=", ".join(content.tags),
        )

        response = self.ai.generate(
            prompt,
            max_tokens=800,
        )

        cleaned_response = (
            response.replace("```json", "")
            .replace("```", "")
            .strip()
        )

        try:
            data = json.loads(cleaned_response)
        except json.JSONDecodeError as error:
            raise ValueError(
                "Claude returned an invalid quality report:\n\n"
                f"{cleaned_response}"
            ) from error

        review = ReviewResult(
            approved=bool(data.get("approved", False)),
            overall_score=float(data.get("overall_score", 0.0)),
            topic_score=float(data.get("topic_score", 0.0)),
            title_score=float(data.get("title_score", 0.0)),
            script_score=float(data.get("script_score", 0.0)),
            description_score=float(
                data.get("description_score", 0.0)
            ),
            tags_score=float(data.get("tags_score", 0.0)),
            recommendation=str(
                data.get("recommendation", "human_review")
            ),
            feedback=[
                str(item) for item in data.get("feedback", [])
            ],
        )

        self.log(
            f"Review complete — overall score: "
            f"{review.overall_score:.1f}/10"
        )

        return review