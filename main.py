import smtplib
import webbrowser
import os
import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit as kit
import winsound
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def wishme():
    now = datetime.datetime.now()
    hour = now.hour
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 17:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Lucifer. Tell me how I can assist you")



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    winsound.Beep(550, 500)


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        ask = r.recognize_google(audio, language="en-in")
        print(f"User said:{ask}\n")
        return ask
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand you.")
        return "None"


def search_on_wikipedia(search):
    res = wikipedia.summary(query, sentences=2)
    return res


# def search_on_wikipedia(search):
#     try:
#         if not search:
#             raise ValueError("Empty query. Please provide a valid search term.")
#         res = wikipedia.summary(search, sentences=2)
#         return res
#     except wikipedia.DisambiguationError as e:
#         return f"Multiple results found. Please specify the topic. Options: {', '.join(e.options)}"
#     except wikipedia.exceptions.PageError:
#         return "No Wikipedia page found for the given query."
#     except Exception as e:
#         return f"An error occurred: {str(e)}"


def send_whatsapp_message(num, msg):
    kit.sendwhatmsg_instantly(f"+91{num}", msg)


wishme()
if __name__ == '__main__':
    while True:
        query = take_command().lower()
        # Logic for Executing task based on query
        if 'wikipedia' in query:
            speak('What do you want to search on Wikipedia, sir?')
            search_query = take_command().lower()
            results = search_on_wikipedia(search_query)
            print(f"According to Wikipedia, {results}")
            speak(f"According to Wikipedia, {results}")
            # Optionally, print the results to the screen as well

        if 'open google' in query:
            browser = webbrowser.get('windows-default')  # Replace 'windows-default' with the desired browser
            browser.open("https://www.google.com")

        if 'play music' in query:
            music_dir = 'C:\\Users\\ujjma\\Sangeet'
            if not os.path.exists(music_dir):
                speak("Music directory not found.")
            else:
                songs = os.listdir(music_dir)
                if not songs:
                    speak("No music files found in the directory.")
                else:
                    random_song = random.choice(songs)
                    song_path = os.path.join(music_dir, random_song)
                    os.startfile(song_path)

        if 'the time' in query:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {current_time}")

        if "whatsapp" in query:
            number = 9639004871
            speak("What is the message sir?")
            message = take_command().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.")

        if 'email' in query:
            try:
                speak("What should I say?")
                content = take_command()
                to = "udd.mathur@gmail.com"
                send_email(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Can't send E-mail ")

        if 'bye' in query:
            break
