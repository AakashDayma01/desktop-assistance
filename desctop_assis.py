# greetings.py
import datetime

def get_greeting():
    """Return greeting based on current time"""
    hour = datetime.datetime.now().hour
    if hour < 12:
        return "Good morning!"
    elif hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"

def say_hello(name):
    """Return a hello message"""
    return f"Hello, {name}!"
