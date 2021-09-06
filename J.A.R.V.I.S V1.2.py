# Created By Ahmed Arafat
# ahmedmoyousry.bis@gmail.com
# Business Information System
# 1/2021
import ctypes
import pyttsx3  # pip install pyttsx3
import datetime
import speech_recognition as sr
import wikipedia  # pip install wikipedia
import smtplib
import webbrowser as wb
import psutil  # pip install psutil
import pyjokes  # pip install pyjokes
import os
import pyautogui  # pip install pyautogui (For Screenshot)
import random
import wolframalpha
import json
from urllib.request import urlopen
import requests
import time
import winsound
from ctypes import *
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
AI_ID = "JARVIS"
# engine.say("Hello World")
# engine.runAndWait()
# print("hello")


def speak(audio):
    engine.setProperty("rate", 160)
    engine.say(audio)
    engine.runAndWait()


def time_():
    Time = datetime.datetime.now().strftime("%I:%M:%S%p")  # For 12 hour clock
    speak("The Current Time Is")
    speak(Time)

# speak("Hello Arafat")
# time_()


def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    speak("The Current Date Is")
    speak(day)
    speak(month)
    speak(year)

# date_()


def Wishme():
    speak("Welcome Back Mr. Ahmed Arafat")
    time_()
    date_()
    # Greeting
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour < 12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")
    elif hour >= 18 and hour < 24:
        speak("Good Evening Sir")
    else:
        speak("Good Night Sir")

    if AI_ID == "JARVIS":
        speak("JARVIS at your service. Please tell me how can I help you today!")
    else:
        speak("FRIDAY at your service. Please tell me how can I help you today!")

# Wishme()


def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining Sir ....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing Sir ....")
        query = r.recognize_google(audio, language='en-US')
        print(query)

    except Exception as e:
        print(e)
        print("Say That Again Sir")
        speak("Say That Again Sir")
        return "None"
    return query

# TakeCommand()


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Enable low security in gmail
    server.login('Your email', 'Your password')
    server.sendmail('Your email', to, content)
    server.close()


def cpu():
    usage_cpu = str(psutil.cpu_percent())
    speak('CPU is at' + usage_cpu)
    # usage_disk = str(psutil.disk_usage().percent)
    # speak('Disk is at'+ usage_disk)


def jokes():
    x = pyjokes.get_joke()
    print(x)
    speak(x)


def screenshot():
    img = pyautogui.screenshot()
    img.save('D:\Screenshots\screenshot401.png')

# Wishme()


def Introduction():
    if AI_ID == "JARVIS":
        speak("I am JARVIS Version 1.2 , A Personal AI assistant , "
              "I am created by Ahmed Arafat , "
              "I can help you in various regards , "
              "I can search for you on the Internet , "
              "I can also grab definitions for you from wikipedia , "
              "In layman terms , I can try to make your life a bed of roses , "
              "Where you just have to command me , and I will do it for you , ")
    else:
        speak("I am FRIDAY Version 2.5 , A Personal AI assistant , "
              "I am created by Ahmed Arafat , "
              "I can help you in various regards , "
              "I can search for you on the Internet , "
              "I can also grab definitions for you from wikipedia , "
              "In layman terms , I can try to make your life a bed of roses , "
              "Where you just have to command me , and I will do it for you , ")

# code
# def tellTime():
# # This method will give the time
# 	time = str(datetime.datetime.now().strftime("%I:%M:%S%p"))

# 	# the time will be displayed like this "2020-06-05 17:50:14.582630"
# 	# nd then after slicing we can get time
# 	print(time)
# 	hour = time[0:2]
# 	min = time[3:5]
# 	speak("The time is sir" + hour + "Hours and" + min + "Minutes")


def tellDay():

    # This function is for telling the
    # day of the week
    day = datetime.datetime.today().weekday() + 1

    # this line tells us about the number
    # that will help us in telling the day
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)


if __name__ == "__main__":
    def clear(): return os.system('cls')
    # This Function will clean any
    # command before execution of this python file
    # Wishme()
    while True:
        query = TakeCommand().lower()
        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command
        if 'i want friday' in query:
            speak("Working on it Sir")
            speak("Good bye Sir have a Good day")
            time.sleep(2)
            engine.setProperty('voice', voices[1].id)
            AI_ID = "FRIDAY"
            speak("Hello Sir Friday is Here at your service, how can I help you today!")
        elif 'what is the time' in query:
            time_()

        elif 'what is the date' in query:
            date_()

        elif "which day it is" in query:
            tellDay()

        # elif "tell me the time" in query:
        #     tellTime()

        elif 'wikipedia' in query:
            speak("Searching Sir ...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=3)
            print("According to wikipedia")
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = TakeCommand()
                speak("Who is the Reciever?")
                reciept = input("Enter recieptant's name: ")
                to = (reciept)
                sendEmail(to, content)
                speak(content)
                speak("Email has been sent.")
            except Exception as e:
                print(e)
                speak("Unable to send the email.")

        elif 'search in chrome' in query:
            speak("What should I search ?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'search in youtube' in query:
            speak("What should I search?")
            Search_term = TakeCommand().lower()
            speak("Here we go to Youtube\n")
            wb.open("https://www.youtube.com/results?search_query="+Search_term)
            time.sleep(5)
        elif 'search in google' in query:
            speak("What should I search?")
            Search_term = TakeCommand().lower()
            wb.open('https://www.google.com/search?q='+Search_term)

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()

        # quit
        elif 'sleep' in query:
            speak("Going to Sleep Sir")
            speak("Have a good day")
            quit()

        elif 'word' in query:
            speak("opening MS Word")
            word = r'Word path'
            os.startfile(word)

        elif "write a note" in query:
            speak("What should i write, Sir")
            note = TakeCommand()
            file = open('note.txt', 'w')
            speak("Sir, Should i include date and time")
            dt = TakeCommand()
            if 'yes' in dt or 'sure' in dt:
                strTime = datetime.datetime.now().strftime("%I:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
                speak('done sir')
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("Today.txt", "r")
            speak(file.read())
            print(file.read())

        elif "what we have today" in query:
            speak("It's a busy day Sir")
            file = open("Today.txt", "r")
            print(file.read())
            file = open("Today.txt", "r")
            speak(file.read())

        elif 'take a screenshot' in query:
            screenshot()
            speak("Done sir")

        elif 'play songs' in query:
            video = 'songs path'
            audio = 'Songs path'
            speak("What songs should i play sir? Audio or Video")
            ans = (TakeCommand().lower())
            while(ans != 'audio' and ans != 'video'):
                speak("I could not understand you. Please Try again.")
                ans = (TakeCommand().lower())

            if 'audio' in ans:
                songs_dir = audio
                songs = os.listdir(songs_dir)
                print(songs)
            elif 'video' in ans:
                songs_dir = video
                songs = os.listdir(songs_dir)
                print(songs)

            speak("select a random number sir")
            rand = (TakeCommand().lower())
            # used while loop to keep the jarvis on the speak command untill req. command is given.
            while('number' not in rand and rand != 'random'):
                # first used 'rand' before while then again after, so that rand is already defind, and Input is taken and then checked if it is according to reuirement or not. And if it is not which means while loop is true, then commands under 'while loop' will execute untill desired approach.As it will again ask the user for input in the same block.
                speak("I could not understand you. Please Try again.")
                rand = (TakeCommand().lower())

            if 'number' in rand:
                rand = int(rand.replace("number ", ""))
                os.startfile(os.path.join(songs_dir, songs[rand]))
                # 'continue' is used, so that after executing the commands in 'if' or 'elif' block, it will move to the next part of execution (or code). but in this case as this is the last execution of related function then it will move to the next function (i.e. in this code, it will be TakeCommand() )
                continue
            elif 'random' in rand:
                rand = random.randint(1, 219)
                os.startfile(os.path.join(songs_dir, songs[rand]))
                continue

        elif 'drop my needle' in query:
            audio = 'C:/Users/Ahmed Arafat/Desktop/bitttt'
            songs_dir = audio
            songs = os.listdir(songs_dir)
            print(songs)
            os.startfile(os.path.join(songs_dir, songs[0]))
            time.sleep(180)

        elif 'who are you' in query:
            winsound.PlaySound("D:/JARVIS1.wav", winsound.SND_ASYNC)
            time.sleep(25)
            #delay = input("Press enter to finish")
            # audio = 'C:/Users/Ahmed Arafat/Desktop/bitttt'
            # songs_dir = audio
            # songs = os.listdir(songs_dir)
            # print(songs)
            # os.startfile(os.path.join(songs_dir,songs[1]))

        elif 'remember that' in query:
            speak("What should I remember ?")
            memory = TakeCommand()
            speak("You asked me to remember that"+memory)
            remember = open('memory.txt', 'w')
            remember.write(memory)
            remember.close()

        elif 'do you remember anything' in query:
            remember = open('memory.txt', 'r')
            speak("You asked me to remeber that"+remember.read())

        elif 'news' in query:

            try:
                jsonObj = urlopen(
                    'http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=d170da98624a4813b144e763c4c43496')
                data = json.load(jsonObj)
                i = 1

                speak('here are some top news from the times of United States')
                print('''=============== TOP HEADLINES ============''' + '\n')

                for item in data['articles']:

                    print(str(i) + '. ' + item['title'] + '\n')
                    # print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1

            except Exception as e:
                print(str(e))

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("Sir you asked to Locate")
            speak(location)
            wb.open("https://www.google.com/maps/place/" + location + "")

        elif "tell me more about yourself" in query:
            Introduction()

        # calculation
        elif "calculate" in query:
            app_id = 'P745TJ-L9647GT2X3'
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        # General Questions
        elif "what is" in query or "who is" in query:

            # Use the same API key
            # that we have generated earlier
            app_id = 'P745TJ-L9647GT2X3'
            client = wolframalpha.Client(app_id)
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")

        # sleep-time
        elif "take a break" in query:
            speak("sir, for how much seconds you want me to take a break")
            a = int(TakeCommand())
            time.sleep(a)
            print(a)
##########################################
        elif "weather" in query:

            # Google Open weather website
            # to get API of Open weather
            api_key = "Api key"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ")
            print("City name : ")
            city_name = TakeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()

            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " + str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(
                    current_pressure) + "\n humidity (in percentage) = " + str(current_humidiy) + "\n description = " + str(weather_description))

            else:
                speak(" City Not Found ")

        elif "open geeksforgeeks" in query:
            speak("Opening GeeksforGeeks ")
            # in the open method we just to give the link
            # of the website and it automatically open
            # it in your default browser
            wb.open("www.geeksforgeeks.com")

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            wb.open("youtube.com")

        elif "open google" in query:
            speak("Opening Google ")
            wb.open("www.google.com")

        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            wb.open("stackoverflow.com")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine Sir")

        elif "who i am" in query:
            speak("If you talk then definately your human.")

        elif "why you came to world" in query:
            speak("Thanks to Ahmed Arafat. further It's a secret")

        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif "will you be my girlfriend" in query or "will you be my boyfriend" in query:
            speak("I'm not sure about, may be you should give me some time")

        elif "i love you" in query:
            speak("Oh Sir, You make me shy")

        # System Function
        elif 'log out' in query:
            os.system("shutdown -l")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
