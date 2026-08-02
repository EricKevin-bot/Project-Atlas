from agents.base_agent import BaseAgent
from models.master_content import MasterContent


class DescriptionAgent(BaseAgent):
    def run(self, content: MasterContent) -> MasterContent:
        self.log("Generating description")

        prompt = self.prompts.load(
            "description",
            topic=content.topic,
            title=content.title,
            audience=content.audience,
            objective=content.objective,
            script=content.script,
            keywords=", ".join(content.keywords),
        )

        content.description = self.ai.generate(
            prompt,
            max_tokens=700,
        ).strip()

        self.log("Description generated")

        return content