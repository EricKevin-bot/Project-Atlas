from unittest.mock import MagicMock, patch

from models.editorial_review import EditorialReview
from services.content_pipeline import ContentPipeline


def test_pipeline_exports_when_thumbnail_rendering_fails() -> None:
    pipeline = ContentPipeline()

    pipeline.research_agent = MagicMock()
    pipeline.title_agent = MagicMock()
    pipeline.script_agent = MagicMock()
    pipeline.thumbnail_agent = MagicMock()
    pipeline.description_agent = MagicMock()
    pipeline.tags_agent = MagicMock()
    pipeline.editorial_board = MagicMock()
    pipeline.thumbnail_renderer = MagicMock()
    pipeline.file_manager = MagicMock()

    def populate_research(content):
        content.topic = "Test topic"
        content.audience = "Test audience"
        content.objective = "Test objective"

    pipeline.research_agent.run.side_effect = populate_research

    def populate_title(content):
        content.title = "Test Title"

    pipeline.title_agent.run.side_effect = populate_title

    def populate_script(content):
        content.script = "Test script"

    pipeline.script_agent.run.side_effect = populate_script

    def populate_thumbnail(content):
        content.thumbnail_prompt = "Test thumbnail brief"

    pipeline.thumbnail_agent.run.side_effect = populate_thumbnail

    def populate_description(content):
        content.description = "Test description"

    pipeline.description_agent.run.side_effect = populate_description

    def populate_tags(content):
        content.tags = ["test", "atlas"]

    pipeline.tags_agent.run.side_effect = populate_tags

    pipeline.editorial_board.review.return_value = EditorialReview(
        approved=True,
        overall_score=9.0,
        recommendation="publish",
        scores={
            "seo": 9.0,
            "script": 9.0,
            "audience": 9.0,
            "brand": 9.0,
            "copy": 9.0,
            "thumbnail": 9.0,
        },
        feedback={},
    )

    pipeline.thumbnail_renderer.render.side_effect = RuntimeError(
        "Image provider unavailable"
    )

    pipeline.file_manager.save_content.return_value = (
        "output/test-title.txt"
    )

    with patch("builtins.input", return_value="y"):
        content, output_path, status = pipeline.run()

    assert status == "SUCCESS"
    assert output_path == "output/test-title.txt"

    pipeline.thumbnail_renderer.render.assert_called_once_with(content)

    pipeline.file_manager.save_content.assert_called_once_with(
        title="Test Title",
        script="Test script",
        description="Test description",
        tags=["test", "atlas"],
        thumbnail_prompt="Test thumbnail brief",
    )

    assert content.thumbnail_image_path == ""