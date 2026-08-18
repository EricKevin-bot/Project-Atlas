from unittest.mock import MagicMock

from agents.voiceover_agent import VoiceoverAgent
from models.master_content import MasterContent


def test_voiceover_agent_prepares_voiceover_script() -> None:
    agent = VoiceoverAgent()

    agent.ai = MagicMock()
    agent.prompts = MagicMock()

    agent.prompts.load.return_value = "voiceover test prompt"

    agent.ai.generate.return_value = (
        "This is a clean spoken voiceover script."
    )

    content = MasterContent(
        topic="Test topic",
        audience="Test audience",
        objective="Test objective",
        key_points=[],
        call_to_action="Subscribe",
        title="Test Title",
        script="## Section\nThis is the original script.",
    )

    result = agent.run(content)

    assert result is content

    assert content.voiceover_prompt == (
        "This is a clean spoken voiceover script."
    )

    agent.prompts.load.assert_called_once_with(
        "voiceover",
        title=content.title,
        script=content.script,
        audience=content.audience,
    )

    agent.ai.generate.assert_called_once_with(
        prompt="voiceover test prompt",
        max_tokens=2500,
    )


def test_voiceover_agent_requires_script() -> None:
    agent = VoiceoverAgent()

    content = MasterContent(
        topic="Test topic",
        audience="Test audience",
        objective="Test objective",
        key_points=[],
        call_to_action="Subscribe",
        title="Test Title",
        script="",
    )

    try:
        agent.run(content)

        assert False, "Expected ValueError"

    except ValueError as error:
        assert str(error) == (
            "Cannot prepare voiceover without a script."
        )