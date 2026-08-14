from models.editorial_review import EditorialReview
from services.decision_engine import DecisionEngine


def test_publish_decision() -> None:
    review = EditorialReview(
        approved=True,
        overall_score=9.1,
        recommendation="publish",
        scores={
            "seo": 9.0,
            "script": 9.5,
            "audience": 9.2,
            "brand": 8.8,
            "copy": 9.0,
        },
        feedback={},
    )

    decision = DecisionEngine().summarize(review)

    assert decision["decision"] == "PUBLISH"
    assert decision["strongest_area"] == "Script"
    assert decision["weakest_area"] == "Brand"
    assert decision["next_action"] == "publish"


def test_retry_decision() -> None:
    review = EditorialReview(
        approved=False,
        overall_score=7.4,
        recommendation="improve_tags",
        scores={
            "seo": 6.0,
            "script": 9.0,
            "audience": 8.5,
            "brand": 8.2,
            "copy": 8.0,
        },
        feedback={},
    )

    decision = DecisionEngine().summarize(review)

    assert decision["decision"] == "RETRY"
    assert decision["weakest_area"] == "Seo"
    assert decision["next_action"] == "improve_tags"