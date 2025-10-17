import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os

import datetime
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print (voices[1].id)
engine.setProperty('voices',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sir !")
    elif hour>=12 and hour<18:
        speak("good afternoon sir !")
    else:
        speak("good evening sir !") 
    speak("I am ravi sir . Please tell me how i can hel[p you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language ='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        print(e)
        print("say that again please...")
        return "None"
    return query

if __name__ =="__main__":
    wishme()
    while 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia, sir ')
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(result)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "the time" in query:
            strtime = datetime.datetime.no().strftime("%H:%M:%S")
            speak(f"sir the time is{strtime}" )
        elif "open code" in query:
            codepath ="C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif "shut Down the pc" in query:
            os.system("shutdown /s /t 1")
        elif " open whatsapp" in query:
            os.system("start https://web.whatsapp.com/")
