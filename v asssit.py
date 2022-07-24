import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<17:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am qwerty your virtual assistant. Please tell me how may I help you")

def startCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:

        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:

        startquery = r.recognize_google(audio, language='en-in')
        print(f"User said: {startquery}\n")

    except Exception as e:
        # print(e)
        print("didnot start")
        return "None"
    return startquery

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:  {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('200040015@iitb.ac.in', 'Rgr@k3s8')
    server.sendmail('200040015@iitb.ac.in', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()

    while True :
    # if 1:
        startquery = startCommand().lower()
        if startquery == "suno":
            print("qwerty is listening")
            speak("qwerty is listening")

            query = takeCommand().lower()

            # Logic for executing tasks based on query
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")


            elif 'play music' in query:
                music_dir = 'D:\\songs'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'open teams' in query:
                codePath = "C:\\Users\\kartheek\\Downloads\\Teams_windows_x64"
                os.startfile(codePath)

            elif 'close teams' in query:
                codePath = "C:\\Users\\kartheek\\Downloads\\Teams_windows_x64"
                os.close(codePath)

            elif 'open code' in query:
                codePath = "C:\\Users\\kartheek\\Downloads\\pycharm-community-2021.3.2"
                os.startfile(codePath)

            elif 'send email' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "kk6876575@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend . I am not able to send this email")
            elif 'quit' in query  :
                speak("iam quitting")
                hour = int(datetime.datetime.now().hour)
                if hour>=0 and hour<15 :
                    speak("have a good day")
                elif hour>=15 and hour<20 :
                    speak("have a pleasant evening")
                else:
                    speak("good night")

                quit()
