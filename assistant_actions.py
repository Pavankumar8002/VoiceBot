from tkinter import *
from gtts import gTTS
import os
import speech_recognition as sr
import webbrowser
import pyjokes
import  randfacts
from news import get_news  # Import the get_news function from news.py

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    os.system("afplay output.mp3")  # For macOS, replace 'afplay' with appropriate command for your OS

def fetch_news():
    articles = get_news()
    if articles:
        news_text = "\n".join([f"{article['title']} from {article['source']['name']}" for article in articles])
        news_label.config(text=news_text)
        speak(news_text)  # Speak the news
    else:
        news_label.config(text="Failed to fetch news.")

def open_file(filename):
    # Placeholder function to open a file
    print(f"Opening file: {filename}")

def search_google(query):
    print(f"Searching Google for: {query}")
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

def get_weather(location):
    # Placeholder function to get weather information
    print(f"Getting weather information for: {location}")

def play_video(video_name):
    # Placeholder function to play a video
    print(f"Playing video: {video_name}")

def handle_command(command):
    if "news" in command:
        fetch_news()
    elif "open" in command:
        filename = command.split("open ")[1]
        open_file(filename)
    elif "search" in command:
        query = command.split("search ")[1]
        search_google(query)
    elif "weather" in command:
        if len(command.split("weather ")) > 1:
            location = command.split("weather ")[1]
            get_weather(location)
        else:
            print("Please provide a location for weather information.")
    elif "video" in command:
        if len(command.split("video ")) > 1:
            video_name = command.split("video ")[1]
            play_video(video_name)
        else:
            print("Please provide the name of the video.")
    elif "joke" in command:
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)  # Speak the joke
    elif "fact" in command:
        fact = randfacts.getFact()
        print(fact)
        speak(fact)  # Speak the fact
    elif "exit" in command:
        print("Goodbye!")
        speak("Goodbye!")
        root.quit()
    else:
        print("Sorry, I don't understand that command.")
        speak("Sorry, I don't understand that command.")

def assistant():
    print("Hello sir, how can I assist you?")
    speak("Hello sir, how can I assist you?")  # Speak the greeting
    while True:
        print("Listening...")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, 1.2)
            audio = r.listen(source)

        try:
            command = r.recognize_google(audio).lower()
            print("You said:", command)
            handle_command(command)
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
        except sr.RequestError as e:
            print("Sorry, there was an error processing your request. Please try again later.")

# Create the Tkinter window
root = Tk()
root.title("Voice Assistant")

# Create and configure the news label
news_label = Label(root, text="News will be displayed here.", wraplength=400)
news_label.grid(row=0, column=0, padx=10, pady=10)

# Create the button to trigger the voice assistant
assistant_button = Button(root, text="Activate Assistant", command=assistant)
assistant_button.grid(row=1, column=0, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
