from models.editorial_review import EditorialReview


class DecisionEngine:
    def summarize(self, review: EditorialReview) -> dict:
        if not review.scores:
            return {
                "decision": "HUMAN_REVIEW",
                "reason": "No editorial scores were available.",
                "strongest_area": "Unknown",
                "strongest_score": 0.0,
                "weakest_area": "Unknown",
                "weakest_score": 0.0,
                "overall_score": review.overall_score,
                "next_action": "human_review",
            }

        strongest = max(review.scores, key=review.scores.get)
        weakest = min(review.scores, key=review.scores.get)

        strongest_score = review.scores[strongest]
        weakest_score = review.scores[weakest]

        if review.approved:
            decision = "PUBLISH"
            reason = "The Editorial Board approved the content package."
            next_action = "publish"

        elif review.recommendation == "human_review":
            decision = "HUMAN_REVIEW"
            reason = (
                "The Editorial Board requires human review "
                "before publication."
            )
            next_action = "human_review"

        else:
            decision = "RETRY"
            reason = (
                f"{weakest.title()} is the weakest editorial area "
                f"at {weakest_score:.1f}/10."
            )
            next_action = review.recommendation

        return {
            "decision": decision,
            "reason": reason,
            "strongest_area": strongest.title(),
            "strongest_score": strongest_score,
            "weakest_area": weakest.title(),
            "weakest_score": weakest_score,
            "overall_score": review.overall_score,
            "next_action": next_action,
        }