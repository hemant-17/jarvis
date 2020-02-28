import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[1].id)
#print(voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour < 12:
        speak("Good Morning")
    elif hour>=12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("Iam jarvis Sir . Please tell me how may i help you ")

#it takes microphone input from user and returns string output
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        #print(Microphone.list_microphone_names()[0])
        r.pause_threshold = 0.8
        r.energy_threshold = 50
        r.dynamic_energy_threshold = False
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-IN')
        print(f"User said:{query}\n")

    except Exception as e:
        print("Say that again...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail','yourpassword')
    server.sendmail('youremail',to,content)
    server.close()

if __name__ =="__main__":
    #speak("hemant is good boy")
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()
        #logic for executing tasks
        if 'wikipedia' in query:
            speak('searching Wikipedia..')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\hp\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[3]))

        elif ' the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir , The time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send email ' in query:
            try:
                speak("what should i say? ")
                content=takeCommand()
                to = "2018.hemantkumar.yadav@ves.ac.in"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir email has not been sent ")
