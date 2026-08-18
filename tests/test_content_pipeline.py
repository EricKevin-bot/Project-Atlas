from unittest.mock import MagicMock, patch

from models.editorial_review import EditorialReview
from services.content_pipeline import ContentPipeline


def build_mock_pipeline() -> ContentPipeline:
    pipeline = ContentPipeline()

    pipeline.research_agent = MagicMock()
    pipeline.title_agent = MagicMock()
    pipeline.script_agent = MagicMock()
    pipeline.voiceover_agent = MagicMock()
    pipeline.thumbnail_agent = MagicMock()
    pipeline.description_agent = MagicMock()
    pipeline.tags_agent = MagicMock()

    pipeline.editorial_board = MagicMock()
    pipeline.voiceover_renderer = MagicMock()
    pipeline.thumbnail_renderer = MagicMock()
    pipeline.file_manager = MagicMock()

    def populate_research(content):
        content.topic = "Test topic"
        content.audience = "Test audience"
        content.objective = "Test objective"

    def populate_title(content):
        content.title = "Test Title"

    def populate_script(content):
        content.script = "Test script"

    def populate_voiceover(content):
        content.voiceover_prompt = "Test voiceover script"

    def populate_thumbnail(content):
        content.thumbnail_prompt = "Test thumbnail brief"

    def populate_description(content):
        content.description = "Test description"

    def populate_tags(content):
        content.tags = ["test", "atlas"]

    pipeline.research_agent.run.side_effect = populate_research
    pipeline.title_agent.run.side_effect = populate_title
    pipeline.script_agent.run.side_effect = populate_script
    pipeline.voiceover_agent.run.side_effect = populate_voiceover
    pipeline.thumbnail_agent.run.side_effect = populate_thumbnail
    pipeline.description_agent.run.side_effect = populate_description
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

    pipeline.file_manager.save_content.return_value = (
        "output/test-title.txt"
    )

    return pipeline


def test_pipeline_exports_when_thumbnail_rendering_fails() -> None:
    pipeline = build_mock_pipeline()

    pipeline.thumbnail_renderer.render.side_effect = RuntimeError(
        "Image provider unavailable"
    )

    with patch("builtins.input", return_value="y"):
        content, output_path, status = pipeline.run()

    assert status == "SUCCESS"
    assert output_path == "output/test-title.txt"

    pipeline.voiceover_renderer.render.assert_called_once_with(content)
    pipeline.thumbnail_renderer.render.assert_called_once_with(content)

    assert content.thumbnail_image_path == ""


def test_pipeline_exports_when_voiceover_rendering_fails() -> None:
    pipeline = build_mock_pipeline()

    pipeline.voiceover_renderer.render.side_effect = RuntimeError(
        "Voice provider unavailable"
    )

    with patch("builtins.input", return_value="y"):
        content, output_path, status = pipeline.run()

    assert status == "SUCCESS"
    assert output_path == "output/test-title.txt"

    pipeline.voiceover_renderer.render.assert_called_once_with(content)
    pipeline.thumbnail_renderer.render.assert_called_once_with(content)

    assert content.voiceover_audio_path == ""