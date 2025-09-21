import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()

def take_command(timeout=5, phrase_time_limit=8):
    """
    Listen to the microphone using SoundDevice backend and return recognized text.
    Returns None if speech not recognized or service fails.
    """
    r = sr.Recognizer()
    try:
        # Use SoundDevice backend (no PyAudio required)
        with sr.Microphone(device_index=None) as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            print("Listening...")
            audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        command = r.recognize_google(audio).lower()
        return command
    except sr.UnknownValueError:
        return None
    except sr.RequestError:
        return None
    except Exception as e:
        print("Error:", e)
        return None

# Greet the user
speak("Hello! I am your voice assistant. How can I help you today?")

# Main loop
while True:
    command = take_command()

    if command is None:
        speak("Sorry, I didn't catch that. Please repeat.")
        continue

    print("You said:", command)

    if "hello" in command:
        speak("Hello! Nice to meet you.")

    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {now}")

    elif "date" in command:
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {today}")

    elif "search" in command:
        speak("What should I search for?")
        query = take_command()
        if query:
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            speak(f"Here are the results for {query}")
        else:
            speak("Sorry, I didn't catch your search query.")

    elif "exit" in command or "quit" in command:
        speak("Goodbye! Have a nice day.")
        break

    else:
        speak("Sorry, I don't understand that yet.")
