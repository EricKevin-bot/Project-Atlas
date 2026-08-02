from pathlib import Path
from typing import Any


class PromptManager:
    def __init__(self) -> None:
        self.prompts_directory = (
            Path(__file__).resolve().parent.parent / "prompts"
        )

        if not self.prompts_directory.exists():
            raise FileNotFoundError(
                f"Prompts directory not found: {self.prompts_directory}"
            )

    def load(self, prompt_name: str, **values: Any) -> str:
        prompt_path = self.prompts_directory / f"{prompt_name}.txt"

        if not prompt_path.exists():
            raise FileNotFoundError(
                f"Prompt file not found: {prompt_path}"
            )

        template = prompt_path.read_text(encoding="utf-8").strip()

        if not template:
            raise ValueError(
                f"Prompt file is empty: {prompt_path}"
            )

        try:
            return template.format(**values)
        except KeyError as error:
            missing_value = error.args[0]

            raise ValueError(
                f"Missing value '{missing_value}' "
                f"for prompt '{prompt_name}'."
            ) from error
