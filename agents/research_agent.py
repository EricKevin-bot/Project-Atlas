import json

from agents.base_agent import BaseAgent


class ResearchAgent(BaseAgent):
    def run(self, content):
        self.log("Researching with Claude...")

        prompt = self.prompts.load("research")

        response = self.ai.generate(prompt, max_tokens=1200)

        # Remove Markdown code fences if Claude includes them
        response = (
            response.replace("```json", "")
                    .replace("```", "")
                    .strip()
        )

        try:
            data = json.loads(response)
        except json.JSONDecodeError as e:
            raise ValueError(
                f"Claude returned invalid JSON:\n\n{response}"
            ) from e

        content.topic = data["topic"]
        content.audience = data["audience"]
        content.objective = data["objective"]
        content.key_points = data["key_points"]
        content.call_to_action = data["call_to_action"]

        self.log("Research complete")

        return content