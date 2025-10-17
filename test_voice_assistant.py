import unittest
from unittest.mock import patch
import desctop_assis.voice_assistant as va  # import your voice_assistant module

class TestVoiceAssistant(unittest.TestCase):

    @patch('pyttsx3.init')  # Mock pyttsx3 engine
    def test_engine_initialization(self, mock_init):
        engine = va.pyttsx3.init('sapi5')
        self.assertIsNotNone(engine)

    @patch('desctop_assis.voice_assistant.engine.say')  # Mock the say method
    @patch('desctop_assis.voice_assistant.engine.runAndWait')  # Mock runAndWait
    def test_speak_function(self, mock_run, mock_say):
        va.speak("Testing speech engine")
        mock_say.assert_called()
        mock_run.assert_called()

    @patch('desctop_assis.voice_assistant.speak')  # Mock speak in wishme
    @patch('desctop_assis.voice_assistant.datetime')
    def test_wishme_output(self, mock_datetime, mock_speak):
        # Mock morning time
        mock_datetime.datetime.now.return_value.hour = 9
        va.wishme()
        mock_speak.assert_called()

    @patch('desctop_assis.voice_assistant.sr.Recognizer.listen')
    @patch('desctop_assis.voice_assistant.sr.Recognizer.recognize_google', return_value="test command")
    @patch('desctop_assis.voice_assistant.sr.Microphone')
    def test_takecommand_return_type(self, mock_micro, mock_recognize, mock_listen):
        output = va.takeCommand()
        self.assertIsInstance(output, str)

if __name__ == "__main__":
    unittest.main()
