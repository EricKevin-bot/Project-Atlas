from pathlib import Path
from typing import List


class FileManager:
    def __init__(self, output_directory: str = "output") -> None:
        self.output_directory = Path(output_directory)
        self.output_directory.mkdir(parents=True, exist_ok=True)

    def save_content(
        self,
        title: str,
        script: str,
        description: str,
        tags: List[str],
        thumbnail_prompt: str = "",
    ) -> Path:
        safe_title = "".join(
            character.lower() if character.isalnum() else "-"
            for character in title
        )

        safe_title = "-".join(
            part for part in safe_title.split("-") if part
        )

        file_path = self.output_directory / f"{safe_title}.txt"

        content = f"""
TITLE
-----
{title}

THUMBNAIL BRIEF
---------------
{thumbnail_prompt}

DESCRIPTION
-----------
{description}

TAGS
----
{", ".join(tags)}

SCRIPT
------
{script}
""".strip()

        file_path.write_text(content, encoding="utf-8")

        print(f"\n💾 Content saved to: {file_path}")

        return file_path