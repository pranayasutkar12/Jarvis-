import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import time
import pyjokes






engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

#text to speech
def speak(audio):
  engine.say(audio)
  print(audio)
  engine.runAndWait()

#to convert voice into text
def  takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
         speak("Say that again please....")
         return "none"
    return query

#to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak(" I Am Jarvis Sir. please tell me  How  May I Help You")

#to send mail
def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('your email id', 'your password')
    server.sendmail('your email id ', to, content)
    server.close()



if __name__ == "__main__":
     wish()
     while True:
     # if 1:

         query = takecommand().lower()

         #logic building for tasks

         if "open notepad" in query:
           npath="C:\\WINDOWS\\system32\\notepad.exe"
           os.startfile(npath)
           speak("sir, do you have any other work ")

         elif "open Mozilla Firefox" in query:
             npath="C:\\Program Files (x86)\\Mozilla Firefox.exe"
             os.startfile(npath)
             speak("sir, do you have any other work ")

         elif "open command prompt" in query:
             os.system("start cmd")
             speak("sir, do you have any other work ")

         elif "open camera" in query:
             cap = cv2.VideoCapture(0)
             while True:
               ret, img = cap.read()
               cv2.imshow('webcam', img)
               k = cv2.waitKey(58)
               if k == 27:
                 break;
             cap.release()
             cv2.destroyAllWindows()
             speak("sir, do you have any other work ")

         elif "play music" in query:
             music_dir ="C:\\Users\\PRANAY\\Music\\Playlists"
             songs = os.listdir(music_dir)
             # rd = random.choice(songs)
             for song in songs:
                 if song.endswith('.mp3'):
                     os.startfile(os.path.join(music_dir, song))
                     speak("sir, do you have any other work ")




         elif  "ip address" in query:
             ip = get('https://api.ipify.org').text
             speak(f"your IP address is {ip} ")
             speak("sir, do you have any other work ")

         elif "wikipedia" in query:
             speak("searching wikipedia.....")
             query = query.replace("wikipedia","")
             results = wikipedia.summary(query, sentences=2)
             speak("according to wikipedia")
             speak(results)
             speak("sir, do you have any other work ")
             # print(results)

         elif"open youtube" in query:
             webbrowser.open("www.youtube.com")
             speak("sir, do you have any other work ")


         elif "open facebook" in query:
             webbrowser.open("www.facebook.com")
             speak("sir, do you have any other work ")

         elif "open instagram" in query:
             webbrowser.open("www.instagram.com")

             speak("sir, do you have any other work ")

         elif "open google" in query:
             speak("sir, what should i search on google")
             cm = takecommand().lower()
             webbrowser.open(f"{cm}")
             speak("sir, do you have any other work ")

         elif "send message" in query:
             kit.sendwhatmsg("+919823787294","this is testing protpcol",2,25)
             speak("sir, do you have any other work ")

         elif "play song on youtube" in query:
             kit.playonyt("see you again")
             speak("sir, do you have any other work ")

         elif "email to pranay" in query:
             try:
                 speak("what should i say?")
                 content = takecommand().lower()
                 to = "pranayasutkar123@gmailcom"
                 sendEmail(to,content)
                 speak("Email has been send to pranay")
                 speak("sir, do you have any other work ")

             except Exception as e:
                 print(e)
                 speak("sorry sir, i am not able to sent this mail to pranay")
                 speak("sir, do you have any other work ")




         elif "close notepad" in query:
             speak("okay sir, closing notepad")
             os.system("tskill/f /in notepad.exe")
             speak("sir, do you have any other work ")

         elif "set alarm" in query:
             nn = int(datetime.datetime.now().hour)
             if nn==22:
                 music_dir = "C:\\Users\\PRANAY\\Music\\Playlists"
                 songs = os.listdir(music_dir)
                 os.startfile(os.path.join(music_dir, songs[0]))
                 speak("sir, do you have any other work ")

         elif "tell me a joke" in query:
             joke = pyjokes.get_joke()
             speak(joke)
             speak("sir, do you have any other work ")


         elif "shutdown the system" in query:
             os.system("shutdown /r /t 5")

         elif " restart the system" in query:
             os.system("shutdown /r /t 5")
             speak("sir, do you have any other work ")

         elif "sleep the system" in query:
             os.system("rundll32.exe powrprof..dll,SetsuspendState 0,1,0")
             speak("sir, do you have any other work ")



         elif "no thanks" in query:
             speak("ok sir, thanks for using me ")
             sys.exit()





































