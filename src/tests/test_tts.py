import pytest

from tts.factory import get_tts_factory

def test_espeak_text_to_speach(tmp_path):
    tts = get_tts_factory("espeak")
    out_file = tmp_path / "espeak.wav"

    tts.synthesize("this is a test", out_file)
    
    assert out_file.exists()
    assert out_file.stat().st_size > 1000

def test_coqui_text_to_speach(tmp_path):
    tts = get_tts_factory("coqui")
    out_file = tmp_path / "coqui.wav"

    tts.synthesize("this is a test", out_file)
    
    assert out_file.exists()
    assert out_file.stat().st_size > 1000