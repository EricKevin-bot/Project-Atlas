from agents.base_agent import BaseAgent


class TitleAgent(BaseAgent):
    def run(self, content):
        print("Title Agent: Generating title with Claude...")

        prompt = self.prompts.load(
            "title",
            topic=content.topic,
            audience=content.audience,
            objective=content.objective,
        )

        title = self.ai.generate(
            prompt=prompt,
            max_tokens=100,
        )

        content.title = title.strip().strip('"')

        print(f"Title Agent: {content.title}")

        return content