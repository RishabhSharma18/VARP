import asyncio
import datetime
import sys
import time
import ctypes
import requests, json
import pyautogui
from requests import get
from selenium import webdriver

import pyttsx3
import speech_recognition as sr
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import psutil
from youtubesearchpython import VideosSearch
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from varpUI import Ui_MainWindow
import geocoder
from geopy.geocoders import Nominatim
import ChatSystems
import wolframalpha
import pyjokes

client = wolframalpha.Client("P6Q76U-L9EE88H8RE")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)

geoLoc = Nominatim(user_agent="GetLoc")
g = geocoder.ip('me')
l1 = g.latlng
cord = f"{l1[0]}, {l1[1]}"
city = geoLoc.reverse(cord)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('clal37621@gmail.com', 'google security 1')
    server.sendmail('clal37621@gmail.com', to, content)
    server.close()


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.Execution()

    def takeCommand(self):
        # It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone(device_index=0) as source:

            print("Listening...")
            r.pause_threshold = 6
            audio = r.listen(source, phrase_time_limit=2)
            r.adjust_for_ambient_noise(source,duration=1)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio,language='en-us')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)
            print("Say that again please...")
            return "None"
        return query

    def Execution(self):

        wishMe()
        while True:

            self.query = self.takeCommand().lower()

            speak(ChatSystems.response(self.query))

            if 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            elif 'location' in self.query:

                print(city.address)
                speak(city.address)

            elif 'youtube' in self.query:
                speak("what to search for sir?")
                query2 = self.takeCommand()
                query2.lower()

                videosSearch = VideosSearch(query2, limit=2)

                dic = videosSearch.result()
                dic2 = dict(dic['result'][0])
                url = (dic2['link'])
                driver = webdriver.Chrome(
                    executable_path='C:\\Users\\Lenovo\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe')
                driver.get(url)

            elif 'system' in self.query:

                battery = psutil.sensors_battery()
                power = battery.percent
                line = f"Running system diagnosis. Every thing seems fine. we are at {power} percent power"
                speak(line)

            elif 'google' in self.query:
                speak("what for sir")
                query = self.takeCommand()
                abc = query.lower()

                link = f"https://www.google.com/search?q={abc}"
                driver = webdriver.Chrome(
                    executable_path='C:\\Users\\Lenovo\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe')
                driver.get(link)

            elif 'open' and '.com' in self.query:
                dd = self.query.replace('open', '')
                url = f"{dd}"
                webbrowser.open(url)

            elif 'music' in self.query:
                speak("WHAT SONG you wanna listen sir?")
                query3 = self.takeCommand()
                abc = query3.replace(' ', '-').lower()
                try:
                    driver = webdriver.Chrome(
                        executable_path='C:\\Users\\Lenovo\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe')

                    url = f"https://gaana.com/song/{abc}"
                    driver.get(url)
                except Exception as e:
                    speak("Didn't find the song sir.")

            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'switch' in self.query:
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                while True:
                    query3 = self.takeCommand()
                    if 'next' in query3:
                        pyautogui.press('right')
                    elif 'previous' in query3:
                        pyautogui.press('left')
                    elif 'open' in query3:
                        pyautogui.press('enter')
                        pyautogui.keyUp('alt')
                        break
                    else:
                        speak('Did not find the window to open')
            elif 'weather' in self.query:

                base_url = "http://api.openweathermap.org/data/2.5/weather?"
                city_name = "Chandigarh"
                complete_url = base_url + "appid=" + "841cc4cdc4938a11fdd9461ddcf3684a" + "&q=" + city_name

                response = requests.get(complete_url)

                x = response.json()

                if x["cod"] != "404":
                    y = x["main"]

                    current_temperature = int(y["temp"] - 273)

                    current_pressure = y["pressure"]

                    current_humidity = y["humidity"]

                    z = x["weather"]

                    weather_description = z[0]["description"]

                    speak(" Temperature here is " +
                          str(current_temperature) +
                          " degree celsius with pressure of" +
                          str(current_pressure) +
                          "hpa and humidity is" +
                          str(current_humidity) +
                          "percent.The sky is having " +
                          str(weather_description))
            elif 'joke' in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif 'terminate' in self.query or 'kill' in self.query or 'shut' in self.query:
                speak("AS you wish sir")
                break
            elif 'open this' in self.query:
                pyautogui.press('enter')
            elif 'close' in self.query and 'webpage' in self.query:
                driver.close()

            elif 'running' in self.query:
                pyautogui.hotkey('win', 'tab')


            elif 'what' in self.query:
                res = client.query(self.query)
                try:
                    ans = next(res.results).text
                    speak(ans)
                except StopIteration:
                    speak("no idea sir")

            elif 'playlist' in self.query:

                url = "https://gaana.com/playlist/rishabhsharma-nabbn-work-gwwxqqd2bp/play"
                driver = webdriver.Chrome(
                    executable_path='C:\\Users\\Lenovo\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe')
                driver.get(url)


            elif 'maximize' in self.query:
                speak("Maximizing window")
                user32 = ctypes.WinDLL('user32')
                SW_MAXIMIZE = 3
                hWnd = user32.GetForegroundWindow()
                user32.ShowWindow(hWnd, SW_MAXIMIZE)

            elif 'drop' in self.query:
                pyautogui.hotkey('win', 'down')

            elif 'left' in self.query:
                pyautogui.hotkey('win', 'left')

            elif 'right' in self.query:
                pyautogui.hotkey('win', 'right')

            elif 'open command prompt' in self.query or 'open cmd' in self.query:
                os.system('start cmd')


            elif 'play ' in self.query or 'pause' in self.query:
                pyautogui.press('space')

            elif 'mute' in self.query:
                pyautogui.press('f1')
            elif 'close' in self.query:
                pyautogui.hotkey('fn','alt','f4')

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.exitbutton.clicked.connect(self.close)
        self.ui.startbutton.clicked.connect(self.startTask)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("resorce.rec/center2.gif")
        self.ui.roundlabel.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("resorce.rec/center.gif")
        self.ui.linelabel.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startEx.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser_2.setText(label_date)
        self.ui.textBrowser.setText(label_time)


if __name__ == "__main__":
    startEx = MainThread()
    app = QApplication(sys.argv)
    varp = Main()
    varp.show()
    exit(app.exec_())
    startEx.run()
