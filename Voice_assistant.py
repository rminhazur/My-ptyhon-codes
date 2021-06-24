import pywhatkit
import speech_recognition as tk
import pyttsx3 #import voice package
import datetime
import wikipedia
import pyjokes



listener= tk.Recognizer() #recognizer
engine = pyttsx3.init() #voice engine

voices=engine.getProperty('voices')
engine.setProperty("voice", voices[0].id) #female voice making

def talk(text):
    engine.say(text)
    engine.runAndWait()
    #engine.say('I am your Penny')
    #engine.say('What can I do for you babe')
    #engine.runAndWait()

def take_command():
    try:
        with tk.Microphone() as source:
            talk("Hello Minhaz this is Jarvis, tell me what you want")
            print("listening you Sir......")
            voice=listener.listen(source)
            command= listener.recognize_google(voice)
            command=command.lower()
            if 'jarvis' in command:
                command=command.replace("jarvis","")

    except:
        pass
    return command

def run_jarvis():
    command=take_command()
    print(command)
    if "play" in command:
        song = command.replace('play', '')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime("%I:%M %p")
        talk("Your current time is " + time)
        print(time)
    elif 'who is' or " do you" in command:
        person =command.replace('who is '," ")
        info= wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk("sorry, I love Phoebe Buffay")
    elif "are you single" in command:
        talk(" I am single but I don't like you")
    elif "joke"  in command:
        talk(pyjokes.get_joke())







    else:
        talk("please tell again")
#while True:
run_jarvis()