import speech_recognition as sr
import pyttsx3

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Initialize the engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            return "None"
        return query

speak("Hello, how can I assist you?")
listen()
import datetime

def greet():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

greet()
import webbrowser
import os

def perform_action(query):
    if 'open youtube' in query.lower():
        webbrowser.open("https://www.youtube.com")
    elif 'open google' in query.lower():
        webbrowser.open("https://www.google.com")
    elif 'play music' in query.lower():
        music_dir = 'path/to/your/music/directory'
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))
    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")
    else:
        speak("I don't understand.")

while True:
    query = listen()
    if query == "None":
        continue
    perform_action(query)