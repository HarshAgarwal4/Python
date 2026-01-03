import speech_recognition as sr
import pyttsx3
import webbrowser
import mtranslate
import wikipedia as wk

recognizer = sr.Recognizer()
state = {'mode' : 'off'}

a = wk.summary("Narendra Modi")
print(a)

def speak(text="Hello"):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    for voice in voices: print(voice)
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate' , 150)
    engine.say(text)
    engine.runAndWait()

def process_command(text):
    print(text)

def listen():
    with sr.Microphone() as source:
        print("Listening...")
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
        return "sorry"

if __name__ == "__main__":
    #initialising JARVIS
    speak("Initializing jarvis")
    
    #obtain audio
    while True:
        a = listen()
        if a:
            print("Heard :" , a)
            translated = mtranslate.translate(a, to_language='en')
            if(state["mode"] == 'on'):
                process_command(translated)
            else:
                if ("jarvis" in translated.lower()):
                    print("JARVIS is avaialble for service")
                    speak("Yes")
                    state["mode"] = 'on'
                else:
                    print("Please wake up jARVIS")
