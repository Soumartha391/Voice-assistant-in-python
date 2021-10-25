import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import subprocess
import random

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0) and (hour<=12):
        speak("Good Morning!")
    elif(hour>=12) and (hour<=18):
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("I am Jarvis Sir. Please tell me how may I help you.")

def takeCommand():
    #It takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio, language='en-in')
        print("User said: ",query)

    except Exception as e:
        #print(e)
        print("Say that again please.....")
        return "None"
    return query

if __name__=="__main__":
    wishMe()
    #while True:
    if 1:
        query=takeCommand().lower()
        #Logic for executing tasks based on query
        if ('wikipedia' in query) or ('search' in query):
            speak("Searching Wikipedia....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif(("run" in query) or ("execute" in query) or ("open" in query)) and (("chrome" in query) or ("browser" in query)):
            speak('Opening chrome web browser')
            subprocess.getoutput("chrome")
            
        elif(("run" in query) or ("execute" in query) or ("open" in query)) and (("notepad" in query) or ("editor" in query)):
            speak('Opening Notepad text editor')
            subprocess.getoutput("notepad")

        elif(("run" in query) or ("execute" in query) or ("open" in query)) and (("cal" in query) or ("calculator" in query)):
            speak('Opening Calculator')
            subprocess.getoutput("calc")

        elif 'play music' or 'play song' in query:
            value=random.randint(0,3)
            print(value)
            music_dir='C:\\Users\\souma\\OneDrive\\Desktop\\FavMusic'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[value]))

        elif 'no' or 'exit' in query:
            speak("Thank You sir! Terminating Assistant")
            


        
        





