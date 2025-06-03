import pytest
import subprocess

from pathlib import Path

def synthesize_test_audio(path: str, text: str = "hello world"):
    tmp = Path(path).with_suffix(".tmp.wav")

    subprocess.run(["espeak", "-w", str(tmp), text], check=True)
    subprocess.run([
        "ffmpeg", "-y", "-i", str(tmp),
        "-ar", "16000", "-ac", "1", path
    ], check=True)

    tmp.unlink()

@pytest.fixture(scope="session")
def dummy_audio_path(tmp_path_factory):
    final_path = tmp_path_factory.mktemp("audio") / "hello.wav"
    if not final_path.exists():
        synthesize_test_audio(str(final_path), text="hello world")

    return str(final_path)

@pytest.fixture(scope="session")
def dummy_generation_path(tmp_path_factory):
    final_path = tmp_path_factory.mktemp("audio") / "genertion.wav"
    return str(final_path)