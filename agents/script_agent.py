from models.master_content import MasterContent


class ScriptAgent:
    def __init__(self):
        self.name = "Script Agent"

    def run(self, content: MasterContent):
        print()
        print("📄 Script Agent")
        print(f"Writing script for: {content.topic}")

        script = f"""
Welcome back!

Today we're talking about {content.topic}.

Here's what you'll learn:

"""

        for point in content.key_points:
            script += f"\n- {point}"

        script += f"""

If you enjoyed this video,
{content.call_to_action}
"""

        content.script = script.strip()