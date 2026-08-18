import base64
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

from config import (
    IMAGE_COUNT,
    IMAGE_FORMAT,
    IMAGE_MODEL,
    IMAGE_QUALITY,
    IMAGE_SIZE,
)
from models.master_content import MasterContent


class ThumbnailRenderer:
    def __init__(
        self,
        output_directory: str = "output/thumbnails",
    ) -> None:
        env_path = Path(__file__).resolve().parent.parent / ".env"
        load_dotenv(dotenv_path=env_path, override=True)

        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise RuntimeError(
                "OPENAI_API_KEY was not found in the project .env file."
            )

        self.client = OpenAI(api_key=api_key)

        self.output_directory = Path(output_directory)
        self.output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    def render(
        self,
        content: MasterContent,
    ) -> MasterContent:
        if not content.thumbnail_prompt.strip():
            raise ValueError(
                "Cannot render thumbnail without a thumbnail prompt."
            )

        safe_title = "".join(
            character.lower()
            if character.isalnum()
            else "-"
            for character in content.title
        )

        safe_title = "-".join(
            part
            for part in safe_title.split("-")
            if part
        )

        image_path = (
            self.output_directory
            / f"{safe_title}.{IMAGE_FORMAT}"
        )

        prompt = (
            "Create a professional YouTube thumbnail.\n\n"
            f"{content.thumbnail_prompt}\n\n"
            "Requirements:\n"
            "- Bold, simple composition.\n"
            "- Immediately understandable at mobile size.\n"
            "- Strong visual hierarchy.\n"
            "- Avoid clutter.\n"
            "- No watermarks.\n"
            "- No unrelated logos.\n"
            "- Suitable for a 16:9 YouTube thumbnail crop."
        )

        result = self.client.images.generate(
            model=IMAGE_MODEL,
            prompt=prompt,
            n=IMAGE_COUNT,
            size=IMAGE_SIZE,
            quality=IMAGE_QUALITY,
            output_format=IMAGE_FORMAT,
        )

        if not result.data:
            raise RuntimeError(
                "OpenAI returned no thumbnail image."
            )

        image_base64 = result.data[0].b64_json

        if not image_base64:
            raise RuntimeError(
                "OpenAI returned empty thumbnail image data."
            )

        image_bytes = base64.b64decode(image_base64)
        image_path.write_bytes(image_bytes)

        content.thumbnail_image_path = str(image_path)

        print(
            f"\n🖼️ Thumbnail image saved to: "
            f"{image_path}"
        )

        return content