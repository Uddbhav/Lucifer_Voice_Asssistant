# Necessary Imports
import speech_recognition as sr
import pyttsx3
import datetime
import os
import time
import wikipedia
import webbrowser
import pywinctl as pwc
import smtplib
import pywhatkit
import ctypes

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to greet the user based on the time of day
def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello, Good Morning")
        print("Hello, Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Hello, Good Afternoon")
        print("Hello, Good Afternoon")
    else:
        speak("Hello, Good Evening")
        print("Hello, Good Evening")

# Function to take voice commands from the user
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said: {statement}\n")
        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

# Main code execution starts here
if __name__ == '__main__':
    print("Loading your AI personal assistant Lucifer")
    speak("Loading your AI personal assistant Lucifer")
    wishMe()

    # Dictionary of email addresses
    mail = {"friend1": "friend1@example.com", "friend2": "friend2@example.com"}
    
    # Dictionary of phone numbers
    phone = {"friend1": "+1234567890", "friend2": "+0987654321"}
    
    while True:
        speak("How can I help you now?")
        statement = takeCommand().lower()
        
        if statement == 0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement or "bye" in statement:
            speak('Your personal assistant Lucifer is shutting down, Good bye')
            print('Your personal assistant Lucifer is shutting down, Good bye')
            break
        
        # Open YouTube
        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("YouTube is open now")
            time.sleep(5)
        
        # Open Google
        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google Chrome is open now")
            time.sleep(5)
        
        # Open Gmail
        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://mail.google.com")
            speak("Google Mail is open now")
            time.sleep(5)
        
        # Search Wikipedia
        elif 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(title=statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        # Get news headlines
        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India, Happy reading')
            time.sleep(6)
        
        # Search on the web
        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)
        
        # Introduction of the assistant
        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Lucifer version 1.0, your personal assistant. I can perform minor tasks like '
                  'opening YouTube, Google Chrome, Gmail, and Stack Overflow, predict time, take a photo, '
                  'search Wikipedia, predict weather in different cities, get top headline news from Times of India, '
                  'and answer computational or geographical questions too!')
        
        # Creator of the assistant
        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Uddbhav")
            print("I was built by Uddbhav")
        
        # Minimize the active window
        elif "minimize" in statement:
            active_window = pwc.getActiveWindow()
            if active_window:
                active_window.minimize()
                print("Window minimized.")
            else:
                print("No active window found.")
        
        # Send an email
        elif "email" in statement:
            speak("To whom should I mail?")
            nm = takeCommand().lower()
            speak("What is the message?")
            txt = takeCommand().lower()
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login("your_email@example.com", "your_email_password")
            server.sendmail("your_email@example.com", mail[nm], txt)
            server.close()
            speak("Email has been sent.")
        
        # Send a WhatsApp message
        elif "whatsapp" in statement:
            speak("Who should I send the message to?")
            name = takeCommand().lower()
            speak("What is the message?")
            msg = takeCommand().lower()
            # Ensure to update the phone number and message appropriately
            pywhatkit.sendwhatmsg(phone[name], msg, int(datetime.datetime.now().strftime("%H")), int(datetime.datetime.now().strftime("%M"))+2)
            speak("Message has been sent.")
        
        # Play music
        elif 'play music' in statement or 'play song' in statement:
            speak("Music directory is not set. Please set the directory first.")
        
        # Set an alarm
        elif 'set alarm' in statement:
            speak("Please tell me the time to set the alarm in HH:MM format")
            alarm_time = takeCommand()
            while True:
                current_time = datetime.datetime.now().strftime("%H:%M")
                if current_time == alarm_time:
                    speak("Wake up! It's time to get up!")
                    # Play alarm sound here
                    break
                time.sleep(30)
        
        # Tell the time
        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        
        # Lock the device
        elif 'lock window' in statement:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()
        
        # Exit the program
        elif 'exit' in statement or 'quit' in statement:
            speak("Exiting, have a good day!")
            exit()
