import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening...")
    audio = r.listen(source)
try:
    query = r.recognize_google(audio, language='en-GB')
    print('User: ' + query + '\n')

except sr.UnknownValueError:
    engine.say('Sorry, I didn\'t get that, Try typing the command!')
    query = str(input('Command: '))
