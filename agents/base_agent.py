from services.claude_provider import ClaudeProvider
from services.prompt_manager import PromptManager


class BaseAgent:
    def __init__(self) -> None:
        self.ai = ClaudeProvider()
        self.prompts = PromptManager()

    def log(self, message: str) -> None:
        print(f"[{self.__class__.__name__}] {message}")