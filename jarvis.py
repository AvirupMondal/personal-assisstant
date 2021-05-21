import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import os
import smtplib

userEmail={"avijit":"mondalav@gmail.com", "mukti":"mondalmukti2016@gmail.com", "avirup":"mondalavirup2015@gmail.com"}

engine= pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Hello I am your Personal Assistant ! How may I help You")
def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"You asked me to do {query}\n")
        except Exception as e:
            print(e)
            print("Please Tell me Once again")
            return "None"
        return query

def sendEmail(to,content):
    # server = smtplib.SMTP('smtp.gmail.com', 587)
    # server.ehlo
    # server.starttls
    # server.login('phpcode2020@gmailcom','Avirupphpcode@2020')
    # server.sendmail('phpcode2020@gmail.com',to,content)
    # server.quit()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('phpcode2020@gmailcom','Avirupphpcode@2020')
    server.sendmail('phpcode2020@gmailcom', to, content)
    server.close()

if __name__=='__main__':
    wishMe()
    if 1:
        query= takeCommand().lower()
        if "wikipedia" in query:
            speak("Browsing Wikipedia...")
            query= query.replace("wikipedia","")
            results= wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia..")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "play music" in query:
            music_dr= 'E:\\Avirup Personal\\Clashiers Youtube\\music'
            songs= os.listdir(music_dr)
            os.startfile(os.path.join(music_dr,songs[0]))
        elif "send email" in query:
            
            # try:
            #     speak("To whom you want to send email")
            #     sendTo= takeCommand().lower()
            #     if sendTo in userEmail:
            #         to= userEmail.get(sendTo)
            #        # print(to)
            #         speak("What should I Say?")
            #         content = takeCommand()
            #         sendEmail(to,content)
            #         speak("Email Has been sent successfully")
            #     else:
            #         speak("Sorry Email is not present in your contact")
            # except Exception as e:
            #     print(e)
            #     speak("Sorry due to some technical issue email can't be sent! Please try again later")
            
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "muktimondal2016@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email") 