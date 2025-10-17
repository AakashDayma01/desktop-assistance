# test_greetings.py
import unittest

from unittest.mock import patch
import greetings

class TestGreetings(unittest.TestCase):

    @patch('greetings.datetime')
    def test_get_greeting_morning(self, mock_datetime):
        mock_datetime.datetime.now.return_value.hour = 9
        self.assertEqual(greetings.get_greeting(), "Good morning!")

    @patch('greetings.datetime')
    def test_get_greeting_afternoon(self, mock_datetime):
        mock_datetime.datetime.now.return_value.hour = 15
        self.assertEqual(greetings.get_greeting(), "Good afternoon!")

    @patch('greetings.datetime')
    def test_get_greeting_evening(self, mock_datetime):
        mock_datetime.datetime.now.return_value.hour = 20
        self.assertEqual(greetings.get_greeting(), "Good evening!")

    def test_say_hello(self):
        self.assertEqual(greetings.say_hello("Alice"), "Hello, Alice!")

if __name__ == "__main__":
    unittest.main()
