import unittest
from src.speech_to_text import transcribe_audio

class TestSpeechRecognition(unittest.TestCase):
    def test_transcription_output(self):
        text = transcribe_audio("test_audio.wav")
        self.assertIsInstance(text, str)
        self.assertGreater(len(text), 0)

if __name__ == "__main__":
    unittest.main()
