from agents.base_agent import BaseAgent
from config import TITLE_CANDIDATE_LIMIT, TITLE_MAX_TOKENS
from models.master_content import MasterContent


class TitleAgent(BaseAgent):
    def run(self, content: MasterContent) -> MasterContent:
        self.log("Generating title candidates")

        prompt = self.prompts.load(
            "title",
            topic=content.topic,
            audience=content.audience,
            objective=content.objective,
        )

        response = self.ai.generate(
            prompt=prompt,
            max_tokens=TITLE_MAX_TOKENS,
        )

        candidates = []

        for line in response.splitlines():
            title = line.strip()

            if not title:
                continue

            title = title.lstrip("0123456789.-) ").strip()
            title = title.strip('"').strip("'").strip("*")

            if title and title not in candidates:
                candidates.append(title)

        if not candidates:
            raise ValueError("TitleAgent returned no title candidates.")

        content.title_candidates = candidates[:TITLE_CANDIDATE_LIMIT]

        # Budget mode: use the first candidate unless quality review rejects it.
        content.selected_title = content.title_candidates[0]
        content.title = content.selected_title

        self.log(
            f"Generated {len(content.title_candidates)} title candidates"
        )
        self.log(f"Selected: {content.selected_title}")

        return content