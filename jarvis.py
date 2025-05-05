import os
import time
import playsound
import speech_recognition as sr
import webbrowser
from gtts import gTTS
import datetime
import pyautogui
import wikipedia
import pywhatkit as pwk
import user_config

def speak(text):
    tts=gTTS(text=text,lang="en")
    filename="voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio= r.listen(source)
        said=""

        try:
            said=r.recognize_google(audio)
            print("trascription :",said)
        except Exception as e:
            print("Error ")
    return said

#speak("hello if fat how are you")
if __name__ == '__main__':
    query=get_audio()
    if "hello" in query:
        speak(" hello if fat ,how are you")
    if "fine" in query:
        speak("What can i do for you")
    elif "what is your name" in query:
        speak(" My name is jarvis")
    while True:
        print("Listening...")
        query = get_audio()

        sites = [
            ["youtube", "https://www.youtube.com"],
            ["wikipedia", "https://www.wikipedia.com"],
            ["google", "https://www.google.com"],
        ]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                #speak(f"Opening {site[0]} sir...")
                speak("O.K")
                webbrowser.open(site[1])
        if "play music" in query:
            speak("playing music")
           # musicPath = "C:\\Users\\RAFEEK MOHAMMAD\\Downloadsbeautiful-loop-253269.mp3"
            #os.system(f"open {musicPath}")
            webbrowser.open("https://www.youtube.com/watch?v=xcWPUWw2fLc")

        elif "the time" in query:
            time1 = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {time1}")

        elif "the date" in query:
            date = datetime.datetime.now().strftime("%d:%m")
            speak(f"sir the date is {date}")

        elif "new task" in query:
            task=query.replace("new task","")
            task=task.strip()
            if task != "":
                speak("Adding task : "+task)
                with open("to_do.txt","a") as f:
                    f.write(task)
        
        elif "read out task" in query:
            with open("to_do.txt","r") as tt:
                speak("Work we have todo is"+tt.read())
        
        elif "open" in query:
            s=query.replace("open","")
            pyautogui.press("super")
            pyautogui.typewrite(s)
            pyautogui.sleep(2)
            pyautogui.press("enter")

        elif "wikipedia" in query:
            req= query.replace("jarvis ","")
            query=query.replace("search wikipedia","")
            res=wikipedia.summary(query ,sentences=2)
            speak(res)

        elif "search google" in query:
            req= query.replace("jarvis","")
            query=query.replace("search google","")
            webbrowser.open("https://www.google.com/search?gs_ssp="+req)

        elif "send email" in query:
            pwk.send_mail("iffatkhatoon2003@gmail.com", user_config.passw,"hello", "how are you",".gmail.com")
            speak("email sent")

        elif "Jarvis Quit" in query.lower():
            exit()

        else:
            exit()
