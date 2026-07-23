from config import config


class AIProvider:
    def __init__(self):
        self.provider = config.AI_PROVIDER
        self.model = config.MODEL

    def generate_video_idea(self):
        if self.provider == "mock":
            return "Why Most People Stay Broke Despite Earning More"

        raise ValueError(f"Unsupported AI provider: {self.provider}")

    def generate_script(
        self,
        video_idea,
        audience,
        objective,
        key_points,
        call_to_action,
    ):
        if self.provider == "mock":
            key_points_text = "\n".join(
                f"- {point}" for point in key_points
            )

            return f"""
HOOK:
Why do so many people earn more money but still feel completely stuck?

TITLE:
{video_idea}

TARGET AUDIENCE:
{audience}

OBJECTIVE:
{objective}

KEY POINTS:
{key_points_text}

BODY:
In this video, we will examine the habits, financial decisions, and
psychological patterns that prevent people from building lasting wealth.

We will also break down practical actions viewers can take to regain
control of their money and make measurable progress.

OUTRO:
{call_to_action}
""".strip()

        raise ValueError(f"Unsupported AI provider: {self.provider}")