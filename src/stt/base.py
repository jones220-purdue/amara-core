from abc import ABC, abstractmethod

class STTEngine(ABC):
    """
    Abstract base class for speech-to-text engines.
    """

    @abstractmethod
    def transcribe(self, audio_data: bytes) -> str:
        """
        Convert raw audio (PCM) bytes to transcribed text.
        Should assume 16kHz mono PCM audio.
        """
        pass

    @abstractmethod
    def is_ready(self) -> bool:
        """
        Return True if the STT engine is initialized and ready to process audio.
        """
        pass