import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pyaudio
import os
import random
from time import strftime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
##print(voices[0].id)

engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet_me():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning!')

    elif hour>=12 and hour<18:
        speak('Good Afternoon')

    else:
        speak('Good Evening!')

    speak("Hi, I'm Tokyo your voice assistant.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing.....')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        print(e)
        print('oops,can you please say that again? ?')
        speak('oops,can you please say that again?')
        return 'None'
    return query
    

if __name__=="__main__":
    greet_me()

    while True:
        query = takeCommand().lower()

    ## logic that we will use to execute task
        if 'wikipedia' in query:
            speak('looking up for the query in wikipedia....')
            query = query.replace("Wikipedia",'')
            results = wikipedia.summary(query,sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            speak('opening youtube')
            webbrowser.open('youtube.com')
            
        elif 'open google' in query:
            speak('opening google')
            webbrowser.open('google.in')
            
        elif 'about arogya setu' in query:
            print('AarogyaSetu is a mobile application developed by the Government of India to connect essential health services')
            webbrowser.open('https://www.mygov.in/aarogya-setu-app/')

        elif 'play music' in query:
            music_dir = r"D:\music"
            songs = os.listdir(music_dir)
            print(songs)
            ran_num = random.randint(0,len(songs)-1)
            os.startfile(os.path.join(music_dir,songs[ran_num]))
            
        elif 'time' in query:
            new_line = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'the time is {new_line}')

        elif 'goodbye' in query:
            exit()
