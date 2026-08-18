from pathlib import Path

import pytest

from models.master_content import MasterContent
from services.voiceover_renderer import VoiceoverRenderer


def test_voiceover_renderer_sets_audio_path(tmp_path: Path) -> None:
    renderer = VoiceoverRenderer(
        output_directory=str(tmp_path),
    )

    content = MasterContent(
        topic="Test topic",
        audience="Test audience",
        objective="Test objective",
        key_points=[],
        call_to_action="Subscribe",
        title="Test Voiceover Video",
        script="Test script",
        voiceover_prompt="This is the spoken voiceover text.",
    )

    result = renderer.render(content)

    assert result is content
    assert content.voiceover_audio_path == str(
        tmp_path / "test-voiceover-video.mp3"
    )


def test_voiceover_renderer_requires_voiceover_text(
    tmp_path: Path,
) -> None:
    renderer = VoiceoverRenderer(
        output_directory=str(tmp_path),
    )

    content = MasterContent(
        topic="Test topic",
        audience="Test audience",
        objective="Test objective",
        key_points=[],
        call_to_action="Subscribe",
        title="Test Voiceover Video",
        script="Test script",
        voiceover_prompt="",
    )

    with pytest.raises(
        ValueError,
        match="Cannot render voiceover without voiceover text.",
    ):
        renderer.render(content)