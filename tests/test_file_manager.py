from pathlib import Path

from services.file_manager import FileManager


def test_save_content_creates_file(tmp_path: Path) -> None:
    manager = FileManager(output_directory=str(tmp_path))

    file_path = manager.save_content(
        title="Test Video Title",
        script="Test script",
        description="Test description",
        tags=["test", "atlas"],
    )

    assert file_path.exists()

    saved = file_path.read_text(encoding="utf-8")

    assert "Test Video Title" in saved
    assert "Test script" in saved
    assert "Test description" in saved
    assert "test, atlas" in saved


def test_save_content_uses_safe_filename(tmp_path: Path) -> None:
    manager = FileManager(output_directory=str(tmp_path))

    file_path = manager.save_content(
        title="Hello, Atlas! 2026",
        script="Script",
        description="Description",
        tags=[],
    )

    assert file_path.name == "hello-atlas-2026.txt"