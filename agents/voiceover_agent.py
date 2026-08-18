from agents.base_agent import BaseAgent
from models.master_content import MasterContent


class VoiceoverAgent(BaseAgent):
    def run(self, content: MasterContent) -> MasterContent:
        self.log("Preparing voiceover")

        if not content.script.strip():
            raise ValueError(
                "Cannot prepare voiceover without a script."
            )

        prompt = self.prompts.load(
            "voiceover",
            title=content.title,
            script=content.script,
            audience=content.audience,
        )

        response = self.ai.generate(
            prompt=prompt,
            max_tokens=2500,
        )

        content.voiceover_prompt = response.strip()

        self.log("Voiceover script prepared")

        return content