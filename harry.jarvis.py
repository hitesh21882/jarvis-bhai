import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import sys
import datetime
from jarvis.config import api_key1
import json
from google import genai
from google.genai import types




def generate_response(query):
   try:
    client = genai.Client(api_key=api_key1)
    response = client.models.generate_content(
    model="gemini-2.0-flash", contents=query
)
    print(response.text)
    return response.text
   except Exception as e:
     say_jarvis(f"An error occurred: {str(e)}")
     return None



def say_jarvis(text):
    audio = pyttsx3.init()
    audio.setProperty('rate', 150)
    audio.setProperty('volume', 1.0)
    audio.say(text)
    audio.runAndWait()

def save_user_data(response, filename='personalized.json'):
     with open(filename, 'w') as file:
      json.dump(response, file)

def load_user_data(filename='personalized.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    else:
         return {}

'''
def save_chat_history(chat_history, filename='chat_history.json'):
    with open(filename, 'w') as file:
        json.dump(chat_history, file)

def load_chat_history(filename='chat_history.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    else:
        return []
'''   
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            try:
                print("listening....")
                r.adjust_for_ambient_noise(source,duration=1)
                audio=r.listen(source)
                print("recognizing....")
                query=r.recognize_google(audio)
                print(f"you said:{query}")
                site_opened=False #flag
               
                

                
                if query.lower() in ['exit','stop']:
                    say_jarvis("Goodbye Boss")
                    print("Goodbye")
                    break

                #todo:Add more sites here
                sites =[['youtube','https://www.youtube.com'],['hianime','https://www.hianime.com'],['openai','https://www.openai.com'],['google','https://google.com']]
                for i in sites:
                    if f"open {i[0]}".lower() in query.lower():
                     say_jarvis(f"Opening:{i[0]} Boss")
                     webbrowser.open(i[1])
                     say_jarvis("Youtube Opened Boss")
                     site_opened=True#flag
                     sys.exit()#teminates program


                #todo:Add more music here
                music="Kuloso.mp3"
                if "play music" in query.lower():
                    say_jarvis("playing music Boss")
                    os.startfile(music)
                    sys.exit()

                #todo:Add your time here
                if "time" in query.lower():
                    hour=datetime.datetime.now().strftime("%H:%p")
                    mins=datetime.datetime.now().strftime("%M:%p")
                    say_jarvis(f"Boss the time is:{hour} hours {mins} minutes")
                    site_opened=True

                #todo:Add more apps here
                apps=[]
                if "apps" in query.lower():
                    pass
                 
                
                if "using artificial intelligence" in query.lower():
                    say_jarvis("here is the ai generated answer")
                    response=generate_response(query)
                    
                    save_user_data(response)
                    say_jarvis("Done Boss")
                    say_jarvis("anything else boss") 
                elif " yes my boy " in query.lower():
                        say_jarvis("what is it Boss")
                        response=generate_response(query)
                        save_user_data(response)
                else:
                        say_jarvis("Bye Boss")
                        sys.exit()
                    

                #if not any todo is used then this command will run
                if not site_opened:
                    say_jarvis(query)

                
                
                                            
            except sr.UnknownValueError:
                print("Sorry, I didn't catch that.")
                say_jarvis("Sorry, I didn't catch that.")
            except sr.RequestError as e:
                print(f"Error with the speech recognition service: {e}")
                say_jarvis("There was an error with the speech recognition service.")
                break     
           

if __name__ == "__main__":
    say_jarvis("Hello Boss")
    takeCommand()
    
   
     
    
    
    
