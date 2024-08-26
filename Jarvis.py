import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        
        try:
            command = recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {command}\n")
        except Exception as e:
            print("Sorry, I did not catch that. Could you please repeat?")
            return None
        return command.lower()
def respond_to_command(command):
    if 'time' in command:
        time_now = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"The time is {time_now}")

    elif 'open youtube' in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif 'open google' in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif 'play music' in command:
        music_dir = "path_to_your_music_folder"
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'quit' in command or 'exit' in command:
        speak("Goodbye!")
        exit()

    else:
        speak("I'm sorry, I don't understand that command.")
def jarvis():
    speak("Hello, I am Jarvis, your personal assistant. How can I help you today?")
    
    while True:
        command = listen_command()
        if command:
            respond_to_command(command)
if __name__ == "__main__":
    jarvis()
