from abc import ABC, abstractmethod
from pathlib import Path

class TTSEngine(ABC):
    """
    Abstract base class for speech-to-text engines.
    """

    @abstractmethod
    def synthesize(self, text: str, output_path: Path) -> None:
        """Generate speech from text and save as WAV file"""
        pass