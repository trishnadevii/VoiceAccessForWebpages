import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys
import webbrowser
from datetime import date
engine=pyttsx3.init()
engine.setProperty("rate", 150)
voices = engine.getProperty("voices")
engine.setProperty('voice', voices [1].id)
recognizer=sr.Recognizer()
def engine_talk(text):
 engine.say(text)
 engine.runAndWait()
def run_me():
 with sr.Microphone() as source:
  recognizer.adjust_for_ambient_noise(source,duration=1)
  print('\n')
  print("Start Speaking!!")
  engine_talk("Start Speaking")
  recordedaudio=recognizer.listen(source)

 try:
  command=recognizer.recognize_google(recordedaudio,language='en-in')
  command = command.lower()

  if 'alexa' in command :
       command = command.replace('alexa', '')
       print('you said'+command)
  else :

     print('you said : '+command)
  if 'hello' in command :
     print('hello how can i helpp you ??')
     engine_talk('hello, how can i help you ??')
  elif 'who are you' in command :
     print('I am Jenishs personal assistant .how can i help you ??')
     engine_talk('I am helper of Lazy you. Use keyboard instead of me you lazy fellow.')
  
  elif 'play' in command:
      song = command.replace('play', '')
      print('Playing' +song)
      engine_talk('Playing' +song)
      pywhatkit.playonyt(song)
 
  elif 'tell me about' in command:
      name = command.replace('tell me about' , '')
      info = wikipedia.summary(name, 1)
      print(info)
      engine_talk(info)
  elif 'what is' in command:
      name = command.replace('what is ' , '')
      info = wikipedia.summary(name, 1)
      print(info)
      engine_talk(info)
  elif 'joke' in command:
      _joke = pyjokes.get_joke()
      print(_joke)
      engine_talk(_joke)
  elif 'search' in command :
       search = 'https://www.google.com/search?q='+command
       engine_talk('searching... ')
       webbrowser.open(search)
  elif 'open google' in command :
       print('opening google ...')
       engine_talk('opening google..')
       webbrowser.open_new('https://www.google.co.in/')
  elif 'gmail' in command :
       print('opening gmail ...')
       engine_talk('opening gmail..')
       webbrowser.open_new('https://mail.google.com/')
  elif 'open youtube' in command :
        print('opening you tube ...')
        engine_talk('opening you tube..')
        webbrowser.open_new('https://www.youtube.com/')
  elif 'open instagram' in command :
        print('opening instagram ...')
        engine_talk('opening insta gram...')
        webbrowser.open_new('https://www.instagram.com/')
  elif "who made you" in command or "who created you" in command:
      print("I have been created by Jenish.")
      engine_talk("I have been created by Jenish.")
  elif 'open github' in command :
        print('opening git hub ...')
        engine_talk('opening git hub...')
        webbrowser.open_new('https://github.com/')
  elif 'thank you' in command :
        print("your welcome")
        engine_talk('your welcome')
  elif 'stop' in command:
        print('good bye, have a nice day !!')
        engine_talk('good bye, have a nice day !!')
        sys.exit()
  else:
        print(' Here is what i found on the internet..')
        engine_talk('Here is what i found on the internet..')
        search = 'https://www.google.com/search?q='+command
        webbrowser.open(search)
 except Exception as ex:
     print("Unable to Recognize your voice.")
     engine_talk("Unable to Recognize your voice.")


print('Clearing background noise...Please wait')
engine_talk('Clearing background noise...Please wait')
print('\n')
print("hello, i am Jenish's Personal Assistant. how can i help you ??")
engine_talk ("hello, i am Jenish's Personal Assistan. What You need now")

while True:
 run_me()
