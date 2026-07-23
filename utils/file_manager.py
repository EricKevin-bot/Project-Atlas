from pathlib import Path
from datetime import datetime


class FileManager:
    def save_content(self, title, script):
        output_folder = Path("output")
        output_folder.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_path = output_folder / f"content_{timestamp}.txt"

        content = f"""
TITLE:
{title}

========================================

SCRIPT:

{script}
""".strip()

        file_path.write_text(content, encoding="utf-8")

        return file_path