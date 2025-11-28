import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os

user = input("Enter your name: ")


engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for up to 5 seconds...")
        try:
            audio = recognizer.listen(source, timeout=2, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            print("No speech detected.")
            return ""

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text.lower()
    except sr.UnknownValueError:
        print("Could not understand what you said.")
        return ""
    except sr.RequestError:
        print("Speech Recognition service error.")
        return ""


def listen_and_print():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for up to 5 seconds...")
        try:
            audio = recognizer.listen(source, timeout=2, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            print("No speech detected.")
            return

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except:
        print("Could not understand.")


def run_jarvis():
    speak(f"Hello {user}, I am Jarvis. How can I help you?")

    while True:
        command = listen()

        if command == "":
            speak("Please repeat that.")
            continue

        if "play" in command:
            song = command.replace("play", "")
            speak(f"Playing {song}")
            pywhatkit.playonyt(song)

run_jarvis()
