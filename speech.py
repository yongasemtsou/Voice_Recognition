
#principal link: https://www.youtube.com/watch?v=CrqWwYkmnNg
#second link: https://www.youtube.com/watch?v=fXRbnSWJVJY&t=22s
from distutils.cmd import Command
import  speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
#PyAudio
#PyWhatKit
#PyJokes
#OpenweatherApi
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('I am Blaise. What can I do for you?')
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():

    try:
        with sr.Microphone() as source:
            print('Start Speaking!!')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
        #exemple: ask :play some song from shakira
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The current time is ' + time)
        print(time)
        # ask:Ton ton Blaise what is the time
    elif 'where is' in command:
        place = command.replace('where is', '')
        info= wikipedia.summary(place, 1)
        print(info)
        talk(info)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info= wikipedia.summary(person, 1)
        print(info)
        talk(info)
        # exemple: ask: who is Albert Einstein
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'hello' in command:
        talk('Hi!') 
    elif 'how are you doing' in command:
        talk('I am doing good Thanks for asking')
        # exempleask: Hi how are you doing
    elif 'bye' in command:
        quit
    else:
        talk('Please say the command again.')


while  True:
    run_alexa()
