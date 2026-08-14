from agents.base_agent import BaseAgent
from models.master_content import MasterContent


class ThumbnailAgent(BaseAgent):
    def run(self, content: MasterContent) -> MasterContent:
        self.log("Generating thumbnail concept")

        prompt = self.prompts.load(
            "thumbnail",
            title=content.title,
            topic=content.topic,
            audience=content.audience,
            script=content.script,
        )

        content.thumbnail_prompt = self.ai.generate(
            prompt=prompt,
            max_tokens=500,
        ).strip()

        self.log("Thumbnail concept generated")

        return content