try:
    from TTS.api import TTS
except ImportError as e:
    raise ImportError("Coqui TTS is not installed. Please install it with `pip install TTS`") from e

from pathlib import Path
from .base import TTSEngine

DEFAULT_COQUI_MODEL_NAME = "tts_models/en/ljspeech/tacotron2-DDC"

class CoquiTTS(TTSEngine):
    def __init__(self, model_name: str = DEFAULT_COQUI_MODEL_NAME):
        self.tts = TTS(model_name)

    def synthesize(self, text: str, output_path: Path):
        self.tts.tts_to_file(text=text, file_path=output_path)