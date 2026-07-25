import os
from pathlib import Path

from anthropic import Anthropic
from dotenv import load_dotenv


class ClaudeProvider:
    def __init__(self) -> None:
        env_path = Path(__file__).resolve().parent.parent / ".env"
        load_dotenv(dotenv_path=env_path, override=True)

        api_key = os.getenv("ANTHROPIC_API_KEY")

        if not api_key:
            raise RuntimeError(
                "ANTHROPIC_API_KEY was not found in the project .env file."
            )

        self.client = Anthropic(api_key=api_key)
        self.model = "claude-sonnet-4-6"

    def generate(
        self,
        prompt: str,
        max_tokens: int = 1000,
    ) -> str:
        if not prompt.strip():
            raise ValueError("Prompt cannot be empty.")

        response = self.client.messages.create(
            model=self.model,
            max_tokens=max_tokens,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        text_parts = [
            block.text
            for block in response.content
            if block.type == "text"
        ]

        if not text_parts:
            raise RuntimeError("Claude returned no text.")

        return "\n".join(text_parts).strip()
