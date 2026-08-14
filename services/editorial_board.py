import json

from agents.base_agent import BaseAgent
from models.editorial_review import EditorialReview
from models.master_content import MasterContent


class EditorialBoard(BaseAgent):
    def review(self, content: MasterContent) -> EditorialReview:
        self.log("Running editorial board review")

        prompt = self.prompts.load(
            "editorial_board",
            topic=content.topic,
            title=content.title,
            thumbnail_prompt=content.thumbnail_prompt,
            script=content.script,
            description=content.description,
            tags=", ".join(content.tags),
        )

        response = self.ai.generate(
            prompt=prompt,
            max_tokens=1000,
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
                "Claude returned an invalid editorial review:\n\n"
                f"{cleaned_response}"
            ) from error

        review = EditorialReview(
            approved=bool(data.get("approved", False)),
            overall_score=float(
                data.get("overall_score", 0.0)
            ),
            recommendation=str(
                data.get("recommendation", "human_review")
            ),
            scores={
                key: float(value)
                for key, value in data.get("scores", {}).items()
            },
            feedback={
                key: str(value)
                for key, value in data.get("feedback", {}).items()
            },
        )

        self.log(
            f"Editorial review complete — "
            f"{review.overall_score:.1f}/10"
        )

        return review