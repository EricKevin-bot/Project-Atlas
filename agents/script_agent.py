from agents.base_agent import BaseAgent
from config import SCRIPT_MAX_TOKENS
from models.master_content import MasterContent


class ScriptAgent(BaseAgent):
    def run(self, content: MasterContent) -> MasterContent:
        self.log("Generating script")

        prompt = self.prompts.load(
            "script",
            topic=content.topic,
            audience=content.audience,
            objective=content.objective,
        )

        content.script = self.ai.generate(
            prompt=prompt,
            max_tokens=SCRIPT_MAX_TOKENS,
        ).strip()

        self.log("Script generated")

        return content