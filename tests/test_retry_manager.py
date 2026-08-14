from unittest.mock import MagicMock

from models.editorial_review import EditorialReview
from services.retry_manager import RetryManager


def test_retry_improves_tags() -> None:
    review = EditorialReview(
        approved=False,
        overall_score=7.5,
        recommendation="improve_tags",
        scores={"seo": 6.0},
        feedback={},
    )

    content = MagicMock()

    pipeline = MagicMock()

    new_review = EditorialReview(
        approved=True,
        overall_score=8.5,
        recommendation="publish",
        scores={"seo": 8.5},
        feedback={},
    )

    pipeline.editorial_board.review.return_value = new_review

    manager = RetryManager()

    result = manager.retry(
        review=review,
        content=content,
        pipeline=pipeline,
    )

    pipeline.tags_agent.run.assert_called_once_with(content)

    pipeline.title_agent.run.assert_not_called()
    pipeline.script_agent.run.assert_not_called()
    pipeline.description_agent.run.assert_not_called()
    pipeline.research_agent.run.assert_not_called()

    pipeline.editorial_board.review.assert_called_once_with(content)

    assert result is content
    assert content.review is new_review


def test_unknown_retry_action_does_nothing() -> None:
    review = EditorialReview(
        approved=False,
        overall_score=6.0,
        recommendation="unknown_action",
        scores={"seo": 6.0},
        feedback={},
    )

    content = MagicMock()
    pipeline = MagicMock()

    manager = RetryManager()

    result = manager.retry(
        review=review,
        content=content,
        pipeline=pipeline,
    )

    pipeline.tags_agent.run.assert_not_called()
    pipeline.title_agent.run.assert_not_called()
    pipeline.script_agent.run.assert_not_called()
    pipeline.description_agent.run.assert_not_called()
    pipeline.research_agent.run.assert_not_called()
    pipeline.editorial_board.review.assert_not_called()

    assert result is content