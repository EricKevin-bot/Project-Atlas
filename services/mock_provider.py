class MockProvider:
    def generate_video_idea(self):
        return "Why Most People Stay Broke Despite Earning More"

    def generate_script(
        self,
        video_idea,
        audience,
        objective,
        key_points,
        call_to_action,
    ):
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
In this video, we examine the financial habits and behaviours that
keep people from building wealth.

OUTRO:
{call_to_action}
""".strip()