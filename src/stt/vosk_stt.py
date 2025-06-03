import json

from vosk import Model, KaldiRecognizer
from .base import STTEngine

DEFAULT_VOSK_MODEL = "models/vosk-model-small-en-us"
DEFAULT_VOSK_SAMPLE_RATE = 16000

class VoskSTT(STTEngine):
    def __init__(
            self,
            model_path: str = DEFAULT_VOSK_MODEL,
            sample_rate: int = DEFAULT_VOSK_SAMPLE_RATE):
        self.model = Model(model_path)
        self.rec = KaldiRecognizer(self.model, sample_rate)
        self._ready = True

    def transcribe(self, audio_data: bytes):
        if not self._ready:
            return ""
        
        if self.rec.AcceptWaveform(audio_data):
            results = json.loads(self.rec.Result())
            return results.get("text", "")
        
        partial = json.loads(self.rec.PartialResult())
        return partial.get("partial", "")
    
    def is_ready(self):
        return self._ready