import unittest
from desctop_assis import voice_assistant
import pyttsx3

class TestVoiceAssistant(unittest.TestCase):

    def test_engine_initialization(self):
        """Check if pyttsx3 engine initializes"""
        engine = pyttsx3.init('sapi5')
        self.assertIsNotNone(engine)

    def test_speak_function(self):
        """Ensure speak function runs without error"""
        try:
            voice_assistant.speak("Testing speech engine")
        except Exception as e:
            self.fail(f"speak() raised an exception: {e}")

    def test_wishme_output(self):
        """Check if wishme returns expected greetings"""
        result = voice_assistant.wishme().lower()
        valid_outputs = ["good morning sir!", "good afternoon sir!", "good evening sir!"]
        self.assertIn(result, valid_outputs)

    def test_takecommand_return_type(self):
        """Ensure takeCommand() returns a string"""
        output = voice_assistant.takeCommand()
        self.assertIsInstance(output, str)

if __name__ == '__main__':
    unittest.main()
