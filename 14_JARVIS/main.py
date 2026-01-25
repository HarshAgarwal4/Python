import speech_recognition as sr
import pyttsx3
import webbrowser
import mtranslate
import wikipedia
import os
import sys
import dotenv
import datetime
import threading

from utils.common import speak
from utils.common import listen
from utils.common import listen_for_something
from utils.common import resource_path

from pyAutoGUI_mouse import operations as op
from webBrowserAPI import web
from Todo import todo as td
from Gemini import gemini as AI
from wikipedia_query import wiki_search as wk
dotenv.load_dotenv()

recognizer = sr.Recognizer()
state = {'mode' : 'off' , 'status': 'not authenticated' , 'aiMode' : 'off'}
string_length = 25

engine = pyttsx3.init()

def process_command(text):
    if state['aiMode'] == 'on':
        text = AI.generateQueryUsingAI(text)

    if 'who are you' in text or 'who r u' in text or 'hu r u' in text or 'hu are you' in text:
        speak("Hello sir, I am Jarvis , your personal AI assistant")
    elif 'enable ai mode' in text:
        state['aiMode'] = 'on'
        speak("AI mode turned on")
    elif 'disable ai mode' in text:
        state['aiMode'] = 'off'
        speak("AI mode turned on")
    elif 'how are you' in text or 'how r u' in text:
        speak('Sir , I am fine. Thank you for asking')
    elif 'time' in text:
        now_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Curret time is {now_time}")
    elif 'update task' in text:
        td.updateTask()
    elif 'date' in text:
        now_date = datetime.datetime.now().strftime("%m/%d/%Y")
        speak(f"Today's date is {now_date}")
    elif 'search' in text and 'on wikipedia' in text:
        a = wk.suggest(text.split("search",1)[1].split("on wikipedia",1)[0].strip())
        print(a)
        speak(a)
    elif 'search' in text and 'on google' in text:
        web.search_on_google(text.split("search",1)[1].split("on google",1)[0].strip())
    elif 'open google' in text:
        web.openSite("google.com")
    elif 'open youtube' in text:
        web.openSite("youtube.com")
    elif 'open chatgpt' in text:
        web.openSite("chatgpt.com")
    elif 'open linkedin' in text:
        web.openSite("linkedin.com")
    elif 'open my folder' in text:
        op.open(r"C:\Users\Dell\Desktop\Harsh")
    elif 'open' in text and 'website' in text:
        web.openSite(text.split('open')[1].split('website')[0].strip())
    elif 'open' in text:
        op.open(text.split('open')[1].strip())
    elif 'add task' in text:
        td.addTask()
    elif 'show tasks' in text or 'show task' in text:
        td.ReadTasks()
    elif 'show tabs' in text:
        op.showTabs()
    elif 'switch tab' in text or 'change tab' in text:
        op.switchTab()
    elif 'close it' in text:
        op.closeWindow()
    elif 'weather of ' in text:
        web.weather(text.split('weather of')[1].strip())
    elif 'weather now' in text:
        loc = web.findLocation()
        web.weather(loc)
    elif 'clear all chats' in text or 'clear chat' in text or 'clear chats' in text or 'delete all chats' in text or 'delete chats' in text or 'delete chat' in text:
        AI.clearChats()
        speak("Chats cleared")
    elif 'clear all tasks' in text or 'clear task' in text or 'clear tasks' in text or 'delete all tasks' in text or 'delete tasks' in text or 'delete all tasks' in text:
        td.clearTasks()
        speak("Tasks cleared")
    elif 'delete task' in text:
        td.DeleteTask()
    elif 'current location' in text:
        web.fetchLocation()
    elif 'move cursor' in text and 'direction' in text:
        op.move_cursor(text.split('move cursor')[1].split('in')[0].strip() ,text.split('in')[1].split('direction')[0].strip() )
    elif 'write' in text and 'here' in text:
        op.write(text.split('write')[1].split('here')[0].strip())
    elif 'click here' in text:
        op.click()
    elif 'take screenshot' in text:
        speak("Taking screenshot")
        op.screenshot()
    else:
        a = AI.response(text)
        speak(a)

if __name__ == "__main__":
    print("Initializing jarvis")
    speak("Initializing jarvis")
    
    #obtain audio
    while True:
        a = listen()
        if a:
            print("Heard :" , a)
            translated = mtranslate.translate(a, to_language='en')
            if(state["mode"] == 'on' and state["status"] == "authenticated"):
                if(translated != 'sorry I am unable to hear'):
                    request = translated.lower()
                    print(request)
                    process_command(request)
            else:
                if ("jarvis" in translated.lower()):
                    print("JARVIS is avaialble for service")
                    state["mode"] = 'on'
                    speak("Yes , please tell me password")
                    password = listen_for_something("Listening for password...")
                    if ( password.lower() == os.getenv("PASSWORD") ): 
                        state["status"] = "authenticated"
                        speak("Welcome Sir , I am ready to use")
                    elif password.lower() == "exit": print("This process is aborted")
                    else: print("Invalid password")
                else:
                    print("Please wake up jARVIS")

