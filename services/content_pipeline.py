from agents.research_agent import ResearchAgent
from agents.script_agent import ScriptAgent
from agents.title_agent import TitleAgent
from utils.file_manager import FileManager


class ContentPipeline:
    def __init__(self):
        self.research_agent = ResearchAgent()
        self.script_agent = ScriptAgent()
        self.title_agent = TitleAgent()
        self.file_manager = FileManager()

    def run(self):
        content = self.research_agent.find_video_idea()

        print()
        print("📋 CEO Decision")
        print(f"Proposed video: {content.topic}")

        decision = input("Approve this video? (y/n): ")

        if decision.lower() != "y":
            print("❌ Rejected")
            return

        print(f"✅ Approved: {content.topic}")

        script = self.script_agent.write_script(content)

        print()
        print("📄 Generated Script")
        print(script)

        title = self.title_agent.create_title(content)

        print()
        print("🏷️ Generated Title")
        print(title)

        file_path = self.file_manager.save_content(
            title=title,
            script=script,
        )

        print()
        print(f"💾 Script saved to: {file_path}")