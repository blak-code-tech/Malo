import pyttsx3
import webbrowser
from bs4 import BeautifulSoup
import smtplib
import random
import speech_recognition as sr
import wikipedia
import wolframalpha
import os
import sys
import requests
import socket


engine = pyttsx3.init()
engine.setProperty('rate', 150)
client = wolframalpha.Client('KLRAAE-7AHKUY3RLH')
url = "https://www.google.com/search?q="


def speak(audio):
    print('Malo: ' + audio)
    engine.say(audio)
    engine.runAndWait()


def its_connected():
    try:
        a = socket.create_connection(("www.google.com", 80))
        if a is True:
            pass
    except OSError:
        speak("Sorry, the internet and I are not communicating")
        sys.exit()


its_connected()
speak('Listening...')


def my_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio)
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Try typing the command!, if you can')
        query = str(input('Command: '))

    return query


if __name__ == '__main__':

    while True:

        query = my_command()
        query = query.lower()

        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.com')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'send email' in query:
            speak('Who is the recipient? ')
            recipient = my_command()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = my_command()

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except OSError:
                    speak('Sorry Sir! I am unable to send your message at this moment!')

        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'hello' in query:
            speak('Hello')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'play music' in query:
            music_folder = Your_music_folder_path
            music = [music1, music2, music3, music4, music5]
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)

            speak('Okay, here is your music! Enjoy!')

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('Got it.')
                    speak(results)

                except OSError:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)

            except:
                search = url + query
                webbrowser.open(search)
