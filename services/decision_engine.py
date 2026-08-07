from models.review_result import ReviewResult


class DecisionEngine:
    def summarize(self, review: ReviewResult) -> dict:
        scores = {
            "Topic": review.topic_score,
            "Title": review.title_score,
            "Script": review.script_score,
            "Description": review.description_score,
            "Tags": review.tags_score,
        }

        strongest = max(scores, key=scores.get)
        weakest = min(scores, key=scores.get)

        if review.approved:
            decision = "PUBLISH"
            reason = "All quality thresholds were met."
        else:
            decision = "RETRY"
            reason = (
                f"{weakest} scored lowest "
                f"({scores[weakest]:.1f}/10)."
            )

        return {
            "decision": decision,
            "reason": reason,
            "strongest_area": strongest,
            "strongest_score": scores[strongest],
            "weakest_area": weakest,
            "weakest_score": scores[weakest],
            "overall_score": review.overall_score,
        }