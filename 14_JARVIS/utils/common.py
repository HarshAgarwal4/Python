import speech_recognition as sr
import pyttsx3
import os
import sys
import dotenv
import datetime
import threading

recognizer = sr.Recognizer()
string_length = 25

engine = pyttsx3.init()

APP_NAME = "Jarvis"

def speak(text="Hello"):
    if(len(text.split()) > string_length):
        print(text)
        speak(f"Its length is length grater than {string_length} words. Do you want that i read it full")
        a = listen_for_something("Listening for response...")
        if 'yes' in a : 
            engine = pyttsx3.init('sapi5')
            engine.setProperty('rate' , 150)
            engine.say(text)
            engine.runAndWait()
        elif 'exit' in a or 'no' in a:
            return
        else : return
    else:
        engine = pyttsx3.init('sapi5')
        engine.setProperty('rate' , 150)
        engine.say(text)
        engine.runAndWait()

def listen(statement = "Listening..." ):
    with sr.Microphone() as source:
        print(statement)
        try:
            audio = recognizer.listen(source , timeout=3 , phrase_time_limit=5)
        except Exception as e:
            print(e)
    print("recongizing...")
    try:
        result = recognizer.recognize_google(audio)
        return result
    except Exception as e:
        print("Error :" , e)
        return "sorry I am unable to hear"

def listen_for_something(statement):
    while True:
        a = listen(statement)
        print("Heard : " + str(a))
        if not a : continue
        elif(a != "sorry I am unable to hear"):
            return a
        elif a.lower() == 'exit': return 'exit'

def resource_path(relative_path):
    """
    Universal resource handler for:
    - Development (normal python)
    - PyInstaller exe
    - Production user data storage (APPDATA)
    """

    # Normalize path separators
    relative_path = relative_path.replace("\\", "/")

    # Define folders that must persist user data
    USER_DATA_DIRS = ("Todo/", "Gemini/", "logs/", "data/")

    # === PRODUCTION MODE (Persistent storage) ===
    if os.getenv("production") == "true":
        if relative_path.startswith(USER_DATA_DIRS):
            base_path = os.path.join(os.getenv("APPDATA"), APP_NAME)
            full_path = os.path.join(base_path, relative_path)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            return full_path

    # === PYINSTALLER MODE ===
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

