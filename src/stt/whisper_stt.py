import numpy as np
import whisper
import io
import librosa
import soundfile as sf

from .base import STTEngine

class WhisperSTT(STTEngine):
    def __init__(
            self,
            model_path: str = "small",
            language: str = "en",
            sample_rate=16000):
        print("HELLO")
        self.model = whisper.load_model(model_path)
        print("WORLD")
        self.language = language
        self.sample_rate = sample_rate
        self._ready = True

    def transcribe(self, audio_data: bytes):
        if not self._ready:
            return ""
        
        audio_array = self.decode_wav_bytes(audio_data, self.sample_rate)
        result = self.model.transcribe(audio_array, language=self.language)

        return result["text"]
    
    def is_ready(self):
        return self._ready
    
    
    def decode_wav_bytes(self, audio_data: bytes, target_sr=16000) -> np.ndarray:
        try:
            with io.BytesIO(audio_data) as f:
                audio, sr = sf.read(f)
        except Exception as e:
            raise RuntimeError(f"Failed to decode WAV bytes: {e}")
        
        print(f"Decoded audio shape: {audio.shape}, dtype: {audio.dtype}, sample rate: {sr}")

        if audio.ndim == 2:
            audio = np.mean(audio, axis=1)

        if sr != target_sr:
            audio = librosa.resample(audio, orig_sr=sr, target_sr=target_sr)

        # Normalize to [-1.0, 1.0]
        if audio.dtype == np.int16:
            audio = audio.astype(np.float32) / 32768.0
        elif audio.dtype != np.float32:
            audio = audio.astype(np.float32)

        return audio.copy()
