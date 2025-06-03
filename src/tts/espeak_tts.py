import subprocess

from pathlib import Path
from .base import TTSEngine

class EspeakTTS(TTSEngine):
    def synthesize(self, text: str, output_path: Path):
        tmp_path = output_path.with_suffix(".tmp.wav")
        subprocess.run(["espeak", "-w", str(tmp_path), text], check=True)
        subprocess.run(["ffmpeg", "-y", "-i", str(tmp_path), "-ar", "16000", "-ac", "1", str(output_path)], check=True)
        tmp_path.unlink()