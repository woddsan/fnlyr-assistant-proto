#imports
from binascii import rlecode_hqx
from cgitb import text
from email import message
from email.mime import audio
from fileinput import filename
import os
from time import sleep
from turtle import done
from unittest import skip
from neuralintents import GenericAssistant
from pyparsing import null_debug_action
import speech_recognition as sr
import pyttsx3 as tts
import sys
import pywhatkit
import webbrowser
from gtts import gTTS
import playsound
import re
import random
import pyjokes
import wikipedia
from socket import timeout
import time
import schedule

from matplotlib.pyplot import title
from plyer import notification


def notif():
        notification.notify(
        title = "Have some water",
        message = "Keep yourself  Hydrated",
        #app_icon = "Iconsmind-Outline-Wine-Bottle.ico",
        timeout=5
        )
        
        
schedule.every(6).seconds.do(notif)   

#login and add user
name = str(input("What's your name? \n"))
if name == "":
    while name=="":
        name = str(input("The one with no name?Surely you must have one \n"))


def texttoSpeech(text):
    my_audio=gTTS(text)
    my_audio.save("noutput.mp3")
    playsound.playsound("noutput.mp3")
    sleep(1)
    os.remove("noutput.mp3")

texttoSpeech("Hello"+name)

#username check and add
names = [line.strip() for line in open("username.txt")]


if name in names:
    print("Yes")
else:
    f=open(name+".txt","w+")
    f.close
    p=open("username.txt","a")
    p.write(name+ "\n")
    p.close


texttoSpeech("How many hours is your average work session?")
timeslot = input("How many hours is your average work session? \n")


texttoSpeech("Please Enter")
water = input("Please enter water intake goal (Liters). A good starting point can be 4 liters. \n")
#interval = input("You can add time interval.")
"""
mappings = {
            "greeting":hello,
            "play":playMusic,
            "exit":quit
}
"""
recognizer = sr.Recognizer()
r=sr.Recognizer()


"""
def addContact():
    #enter name
    #enter contact
    None
"""
def queryExecute(query):
    command=query.split(' ',1)[0]
    if command=="hello":
        hello()
    if command=="play":
        playMusic(query)
    if command=="exit" or command=="quit" or command =="bye":
        exit()
    if command=="send" or command=="email" or command=="mail":
        sendEmail()
    if command=="search":
        searchGoogle(query)
    if command =="joke" or command=="tell":
        tellJoke()
    if command =="summarize" or command =="summary" or command=="summarise":
        sumWiki(query)
        
    else:
        pass


        

    

def tellJoke():
    punchline=pyjokes.get_joke()
    texttoSpeech(punchline)

def searchGoogle(url_build):
    linereq=str(url_build.split(' ',1)[1:])
    webbrowser.open("https://www.google.com/search?q="+linereq)

def sumWiki(wikuery):
    wikreq=str(wikuery.split(' ',1)[1:])
    try:
        summary=wikipedia.summary(wikreq,sentences=1)
        texttoSpeech(summary)
    except Exception as x:
        webbrowser.open("https://en.wikipedia.org/wiki/"+wikreq)





    


def hello():
    greet = ["Hi", "Hello","Hello There","What is up","Hiya","Hey","Hello and Welcome"]
    sel=random.randint(0,7)
    texttoSpeech(greet[sel])

def playMusic(trackName):
    tracks=str(trackName.split(' ',1)[1:])
    texttoSpeech("playing"+tracks)
    sleep(2)
    pywhatkit.playonyt(tracks)

def sendEmail():
    webbrowser.open("https://mail.google.com/mail/u/2/#inbox?compose=new")
"""
def sendMessage():
    None



def waterRemind():
    None



def addContact(name):
    None
"""
def quit():
    
    sys.exit(0)

#listener
while True :
    schedule.run_pending()
    
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)
    try:
        print("Recognizing..")
        query=r.recognize_google(audio,language="en-in")
        run=str(query)
        
        run=run.lower()
        queryExecute(run)

        

        
    except Exception as e:
        print(e)

        
        sleep(2)
    
