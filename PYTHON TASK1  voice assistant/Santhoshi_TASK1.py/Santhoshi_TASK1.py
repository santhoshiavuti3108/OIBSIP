#python task 3 voice assistant

# Voice ni text ga convert cheyyadaniki
import speech_recognition as sr

# Text ni voice ga cheppadaniki
import pyttsx3

# Date and time kosam
import datetime

# Browser lo search open cheyyadaniki
import webbrowser


# Text-to-speech engine start chesthundi
engine = pyttsx3.init()


# Assistant matladadaniki function
def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


# Microphone nunchi command vinadaniki function
def take_command():
    # Voice recognizer create chesthundi
    recognizer = sr.Recognizer()

    # Microphone use chesthundi
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            # User voice record chesthundi
            audio = recognizer.listen(source)

            # Voice ni text ga convert chesthundi
            command = recognizer.recognize_google(audio)

            # Small letters lo convert chesthundi
            command = command.lower()

            print("You said:", command)
            return command

        # Voice ardham kakapothe
        except sr.UnknownValueError:
            speak("Sorry, I did not understand. Please repeat.")
            return ""

        # Internet/service issue unte
        except sr.RequestError:
            speak("Sorry, speech service is not available.")
            return ""


# Starting greeting
speak("Hello, I am your voice assistant. How can I help you?")


# Main loop
while True:
    command = take_command()

    if "hello" in command:
        speak("Hello! Nice to meet you.")

    elif "time" in command:
        import datetime
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The current time is " + current_time)

    elif "date" in command or "today" in command:
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + current_date)

    elif "search" in command:
        speak("What do you want to search for?")
        search_topic = take_command()

        if search_topic != "":
            webbrowser.open(
                "https://www.google.com/search?q=" + search_topic
            )
            speak("Searching for " + search_topic)

    elif "exit" in command or "stop" in command:
        speak("Goodbye! Have a nice day.")
        break

    else:
        speak("Sorry, I do not know that command.")