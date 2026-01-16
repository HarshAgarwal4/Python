import wikipedia as wk
import datetime
import difflib
import random
length = 125
from utils.common import speak
from utils.common import listen_for_something

def suggest(query):
    if(not query): return
    print(query)
    try:
        a = wk.search(query , results = 15)
        print("\n" + "="*length) 
        print("📌 Wikipedia Suggestions".center(length)) 
        print("="*length)
        for index,item in enumerate(a, start=1):
            c = str(index)+". "+item
            print(f"{c:<50}" , end="")
            if index%3 == 0 : print()
        print("="*length)
        print("which topic do you want to search from above list")
        speak("which topic do you want to search from above list")
        topic :str = listen_for_something("Listening for wikipedia topic...")
        if(topic == 'exit'): return
        if topic in a:
            b=wk.summary(topic)
            print(b)
        else:
            b = difflib.get_close_matches(topic.lower() , [i.lower() for i in a] , n=1 , cutoff=0.1)
            b = b[0] if len(b) > 0 else random.choice(a)
            print("I think you searched for :",b)
            b=wk.summary(b)
            print(b)
            speak(b)
    except Exception as e:
        print("📌 Wikipedia Error :-\n",e)
    

if __name__ == "__main__":
    # from main import speak
    # l = datetime.datetime.now().strftime("%H:%M:%S")
    # l = datetime.datetime.now().strftime("%m/%d/%Y")
    # print(l , type(l))
    # speak(str(l))
    suggest('modi')