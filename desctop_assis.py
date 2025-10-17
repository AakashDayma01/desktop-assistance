# voice_assistant.py
import pyttsx3
import datetime

def speak(text):
    """Speak text using pyttsx3"""
    engine = pyttsx3.init('sapi5')
    engine.say(text)
    engine.runAndWait()

def wishme():
    """Return greeting depending on the time"""
    hour = datetime.datetime.now().hour
    if hour < 12:
        greeting = "Good morning sir!"
    elif hour < 18:
        greeting = "Good afternoon sir!"
    else:
        greeting = "Good evening sir!"
    speak(greeting)
    return greeting

def takeCommand():
    """Simulated command (mocked in tests)"""
    return "hello world"

if __name__ == "__main__":
    wishme()
    cmd = takeCommand()
    print(f"Command received: {cmd}")
