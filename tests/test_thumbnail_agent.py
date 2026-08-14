from unittest.mock import MagicMock

from agents.thumbnail_agent import ThumbnailAgent
from models.master_content import MasterContent


def test_thumbnail_agent_generates_brief() -> None:
    agent = ThumbnailAgent()

    agent.ai = MagicMock()
    agent.prompts = MagicMock()

    agent.prompts.load.return_value = "thumbnail test prompt"
    agent.ai.generate.return_value = (
        "A frustrated learner looking at an unfinished guitar. "
        "Bold text: WHY YOU QUIT"
    )

    content = MasterContent(
        topic="Why people quit learning new skills",
        audience="Self-improvement audience",
        objective="Help viewers become more consistent",
        key_points=[],
        call_to_action="Subscribe",
        title="Why You Always Quit New Skills",
        script="Test script",
    )

    result = agent.run(content)

    assert result is content

    assert content.thumbnail_prompt == (
        "A frustrated learner looking at an unfinished guitar. "
        "Bold text: WHY YOU QUIT"
    )

    agent.prompts.load.assert_called_once_with(
        "thumbnail",
        title=content.title,
        topic=content.topic,
        audience=content.audience,
        script=content.script,
    )

    agent.ai.generate.assert_called_once_with(
        prompt="thumbnail test prompt",
        max_tokens=500,
    )