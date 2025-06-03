import os
import importlib

from .base import STTEngine
from .vosk_stt import VoskSTT, DEFAULT_VOSK_MODEL
from .whisper_stt import WhisperSTT, DEFAULT_WHISPER_MODEL

def get_stt_engine(
        engine: str,
        model_path: str = None, 
        sample_rate: int = 16000, 
        language: str = "en") -> STTEngine:
    model_path = model_path
    sample_rate = sample_rate
    language = language

    if engine == "vosk":
        if not model_path:
            model_path = DEFAULT_VOSK_MODEL

        return VoskSTT(model_path, sample_rate)
    elif engine == "whisper":
        if not model_path:
            model_path = DEFAULT_WHISPER_MODEL
            
        return WhisperSTT(model_path, language, sample_rate)
    elif engine == "custom":
        path = os.getenv("AMARA_STT_CLASS")
        if not path:
            raise ValueError("Custom STT engine specified but AMARA_STT_CLASS is not set.")
        
        cls = import_from_path(path)
        if not issubclass(cls, STTEngine):
            raise TypeError(f"{path} is not a subclass of STT_ENGINE")
        
        return cls()
    else:
        raise ValueError(f"Unknown STT engine: {engine}")
    
def import_from_path(path: str):
    try:
        module_path, class_name = path.rsplit(".", 1)
        module = importlib.import_module(module_path)
        cls = getattr(module, class_name)
        return cls
    except (ImportError, AttributeError, ValueError) as e:
        raise ImportError(f"Failed to import '{path}': {e}")