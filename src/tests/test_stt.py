import pytest
import wave

from stt.factory import get_stt_engine

def test_vosk_transcription_from_file(dummy_audio_path):
    stt = get_stt_engine("vosk")
    assert stt.is_ready

    audio_data = read_wav_file(dummy_audio_path)

    text = stt.transcribe(audio_data)
    assert isinstance(text, str)
    assert len(text) > 0
    assert "world" in text.lower()

def test_whisper_transcription_from_file(dummy_audio_path):
    stt = get_stt_engine("whisper", model_path="tiny")
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