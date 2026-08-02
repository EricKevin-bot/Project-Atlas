from agents.base_agent import BaseAgent
from config import SCRIPT_MAX_TOKENS


class ScriptAgent(BaseAgent):
    def run(self, content):
        self.log("Generating script")

        prompt = self.prompts.load(
            "script",
            topic=content.topic,
            audience=content.audience,
            objective=content.objective,
        )

        script = self.ai.generate(
            prompt,
            max_tokens=SCRIPT_MAX_TOKENS,
        )

        content.script = script.strip()

        self.log("Script generated")

        return content