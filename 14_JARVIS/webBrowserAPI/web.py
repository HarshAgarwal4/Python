import webbrowser
import requests
import sys
import os
import dotenv
dotenv.load_dotenv()

from utils.common import speak

key = os.getenv("WEATHER_API_KEY")

def findLocation():
    res = requests.get("https://ipinfo.io/json")
    data = res.json()
    return data['city']

def fetchLocation():
    res = requests.get("https://ipinfo.io/json")
    data = res.json()
    print(f"You are currently located in {data['city']} , {data['region']}")
    speak(f"You are currently located in {data['city']} , {data['region']}")

def openSite(site):
    print(site)
    if(site): webbrowser.open(site)

def search_on_google(query):
    if not query: return
    webbrowser.open(f"https://www.google.com/search?q={query}")

def weather(value = findLocation()):
    try:
        resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={value}&appid={key}')
        text = resp.json()
        if value == findLocation():
            print(f"The weather is {text['weather'][0]['main']} with {text['weather'][0]['description']} and the temprature is {str(round(text['main']['temp']-273.15 , 2)) + '°C'}")
            speak(f"The weather is {text['weather'][0]['main']} with {text['weather'][0]['description']} and the temprature is {str(round(text['main']['temp']-273.15 , 2))} degree celsius")
        else:
            print(f"The weather of {value} is {text['weather'][0]['main']} with {text['weather'][0]['description']} and the temprature is {str(round(text['main']['temp']-273.15 , 2)) + '°C'}")
            speak(f"The weather of {value} is {text['weather'][0]['main']} with {text['weather'][0]['description']} and the temprature is {str(round(text['main']['temp']-273.15 , 2))} degree celsius")

    except Exception as e:
        print(e)

if __name__ == "__main__":
    fetchLocation()
    pass
    # openSite("youtube.com")
    # search_on_google('jarvis')
    # fetchLocation()
   