import json

from vosk import Model, KaldiRecognizer
from .base import STTEngine

class VoskSTT(STTEngine):
    def __init__(
            self,
            model_path: str = "models/vosk-model-small-en-us",
            sample_rate: int = 16000):
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