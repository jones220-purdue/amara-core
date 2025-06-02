import pytest
import wave

from stt.vosk_stt import VoskSTT
from stt.whisper_stt import WhisperSTT

def test_vosk_transcription_from_file(dummy_audio_path):
    stt = VoskSTT("models/vosk-model-small-en-us")
    assert stt.is_ready

    audio_data = read_wav_file(dummy_audio_path)

    text = stt.transcribe(audio_data)
    assert isinstance(text, str)
    assert len(text) > 0
    assert "world" in text.lower()

def test_whisper_transcription_from_file(dummy_audio_path):
    stt = WhisperSTT("tiny")
    assert stt.is_ready

    audio_data = read_wav_file(dummy_audio_path)
    text = stt.transcribe(audio_data)
    assert isinstance(text, str)
    assert len(text) > 0
    assert "world" in text.lower()

def read_wav_file(path):
    with open(path, "rb") as f:
        data = f.read()
        print(f"Size: {len(data)} bytes")
        assert len(data) > 1000, "WAV file is unexpectedly small"
        
    with wave.open(path, "rb") as wf:
        assert wf.getframerate() == 16000
        assert wf.getnchannels() == 1
        return data