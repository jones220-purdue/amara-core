import os
import importlib

from .base import TTSEngine
from .espeak_tts import EspeakTTS

def get_tts_factory(
        engine: str) -> TTSEngine:

    if engine == "espeak":
        return EspeakTTS()
    elif engine == "custom":
        path = os.getenv("AMARA_TTS_CLASS")
        if not path:
            raise ValueError("Custom TTS engine specified but AMARA_TTS_CLASS is not set.")
        
        cls = import_from_path(path)
        if not issubclass(cls, TTSEngine):
            raise TypeError(f"{path} is not a subclass of TTS_ENGINE")
        
        return cls()
    else:
        raise ValueError(f"Unknown TTS engine: {engine}")
    
def import_from_path(path: str):
    try:
        module_path, class_name = path.rsplit(".", 1)
        module = importlib.import_module(module_path)
        cls = getattr(module, class_name)
        return cls
    except (ImportError, AttributeError, ValueError) as e:
        raise ImportError(f"Failed to import '{path}': {e}")