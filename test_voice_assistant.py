# test_voice_assistant.py
import unittest
from unittest.mock import patch
import voice_assistant

class TestVoiceAssistant(unittest.TestCase):

    @patch('voice_assistant.pyttsx3.init')
    def test_speak_function(self, mock_init):
        """Test speak function runs without errors"""
        mock_engine = mock_init.return_value
        mock_engine.say.return_value = None
        mock_engine.runAndWait.return_value = None

        voice_assistant.speak("Testing speak")
        mock_engine.say.assert_called_with("Testing speak")
        mock_engine.runAndWait.assert_called_once()

    @patch('voice_assistant.speak')
    def test_wishme_output(self, mock_speak):
        """Test wishme returns correct greeting"""
        greeting = voice_assistant.wishme()
        self.assertIn(greeting, ["Good morning sir!", "Good afternoon sir!", "Good evening sir!"])
        mock_speak.assert_called_with(greeting)

    def test_takecommand_return_type(self):
        """Test takeCommand returns a string"""
        result = voice_assistant.takeCommand()
        self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()
