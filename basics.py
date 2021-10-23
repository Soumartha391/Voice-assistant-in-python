import pyttsx3
import os
import subprocess
import speech_recognition as sr
import pyaudio
import datetime
hour=int(datetime.datetime.now().hour)
if hour>=0 and hour<12:
    pyttsx3.speak("Good Morning Sir!")
elif hour>=12 and hour<18:
    pyttsx3.speak("Good Afternoon Sir!")
else:
    pyttsx3.speak("Good Evening Sir!")
print('HELLO, I am your assistant.')
pyttsx3.speak("Hello, I am your assistant, Jarvis")
pyttsx3.speak("Please, tell me how may I help you?")
r=sr.Recognizer()
with sr.Microphone() as source:
    print("Listening.....")
    audio=r.listen(source)
    print("Ok processing.....")
order=r.recognize_google(audio)
while True:
    if(("run" in order) or ("execute" in order) or ("open" in order)) and (("chrome" in order) or ("browser" in order)):
        pyttsx3.speak('Opening chrome web browser')
        subprocess.getoutput("chrome")
        pyttsx3.speak('Anything else sir?')
        r=sr.Recognizer()
        with sr.Microphone() as source:
             print("Listening.....")
             audio=r.listen(source)
             print("Ok processing.....")
        order=r.recognize_google(audio)
    elif(("run" in order) or ("execute" in order) or ("open" in order)) and (("notepad" in order) or ("editor" in order)):
        pyttsx3.speak('Opening Notepad text editor')
        subprocess.getoutput("notepad")
        pyttsx3.speak('Anything else sir?')
        r=sr.Recognizer()
        with sr.Microphone() as source:
             print("Listening.....")
             audio=r.listen(source)
             print("Ok processing.....")
        order=r.recognize_google(audio)
    elif(("run" in order) or ("execute" in order) or ("open" in order)) and (("cal" in order) or ("calculator" in order)):
        pyttsx3.speak('Opening Calculator')
        subprocess.getoutput("calc")
        pyttsx3.speak('Anything else sir?')
        r=sr.Recognizer()
        with sr.Microphone() as source:
             print("Listening.....")
             audio=r.listen(source)
             print("Ok processing.....")
        order=r.recognize_google(audio)
    elif ("end" in order) or ("no" in order) or ("stop" in order) or ("close" in order):
        pyttsx3.speak("Terminating assistant")
        print("Terminating Assistant.......")
        break
    else:
        pyttsx3.speak("Sorry, Not supported")
        print("Not Supported.")
        break