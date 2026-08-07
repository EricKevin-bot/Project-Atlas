from agents.base_agent import BaseAgent
from models.master_content import MasterContent


class TagsAgent(BaseAgent):
    def run(self, content: MasterContent) -> MasterContent:
        self.log("Generating SEO tags")

        prompt = self.prompts.load(
            "tags",
            topic=content.topic,
            title=content.title,
            script=content.script,
            keywords=", ".join(content.keywords),
        )

        response = self.ai.generate(
            prompt,
            max_tokens=300,
        )

        content.tags = [
            line.strip()
            for line in response.splitlines()
            if line.strip()
        ]

        self.log(f"Generated {len(content.tags)} tags")

        return content