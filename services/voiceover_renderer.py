from pathlib import Path

from models.master_content import MasterContent


class VoiceoverRenderer:
    def __init__(
        self,
        output_directory: str = "output/voiceovers",
    ) -> None:
        self.output_directory = Path(output_directory)
        self.output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    def render(
        self,
        content: MasterContent,
    ) -> MasterContent:
        if not content.voiceover_prompt.strip():
            raise ValueError(
                "Cannot render voiceover without voiceover text."
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

        audio_path = (
            self.output_directory
            / f"{safe_title}.mp3"
        )

        # Placeholder path until a TTS provider is connected.
        content.voiceover_audio_path = str(audio_path)

        return content