import speech_recognition as sr
import pyttsx3
import os
import json
def jarvis_speak(text):
    """
    Function to make Jarvis speak the given text.
    :param text: The text to be spoken.
    """
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Set speech rate
    engine.setProperty('volume', 1.0)  # Set volume
    engine.say(text)
    engine.runAndWait()



def save_user_data(text,filename='personalized.json'):
    with open(filename,'w') as file:
        json.dump(text,file)

def load_user_data(filename='personalized.json'):
    if os.path.exists(filename):
        with open(filename,'r') as file:
            return json.load(file)
    else:
        return {}  
     
    


def jarvis_listen_and_repeat():
    """
    Jarvis listens to your voice and repeats what you say.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            try:
                print("Listening... (Say 'exit' to stop)")
                # Adjust for ambient noise
                recognizer.adjust_for_ambient_noise(source, duration=1)

                # Listen to the microphone input
                audio = recognizer.listen(source)

                # Recognize the speech using Google Web Speech API
                text = recognizer.recognize_google(audio)
                print(f"You said: {text}")

                # Exit condition
                if text.lower() in ["exit", "quit", "stop"]:
                    jarvis_speak("Goodbye, Boss.")
                    print("Exiting...")
                    break

                # Jarvis repeats the text
                jarvis_speak(text)
                load_user_data(text)

                #saving text
                save_user_data(text)
            except sr.UnknownValueError:
                print("Sorry, I didn't catch that.")
                jarvis_speak("Sorry, I didn't catch that.")
            except sr.RequestError as e:
                print(f"Error with the speech recognition service: {e}")
                jarvis_speak("There was an error with the speech recognition service.")
                break

if __name__ == "__main__":
    # Initial greeting
    jarvis_speak("Hello, I am Jarvis. What can I do for you, Boss?")
    jarvis_listen_and_repeat()
    