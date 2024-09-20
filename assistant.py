import speech_recognition as sr
import pyttsx3
import webbrowser
import random

# Initialize the speech engine
engine = pyttsx3.init()

# List of responses for unrecognized commands
unknown_responses = [
    "I didn't catch that. Could you please repeat?",
    "I'm not sure what you mean. Can you say it differently?",
    "Hmm, I didn't understand. Try saying it another way.",
    "Could you please clarify? I didn't quite get that."
]

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to the user's voice
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        speak(random.choice(unknown_responses))
        return None

# Function to play a song from YouTube
def play_song(song_name):
    speak(f"Playing {song_name} for you.")
    search_url = f"https://www.youtube.com/results?search_query={song_name}"
    webbrowser.open(search_url)

# Function to provide spelling of a word
def tell_spelling(word):
    spell = " ".join(letter.upper() for letter in word)
    speak(f"The spelling of {word} is: {spell}")

# Function to give exercises for gaining weight and height
def exercises():
    speak("Here are some exercises to help you.")
    speak("For gaining weight, consider doing: Squats, Deadlifts, and Push-ups.")
    speak("To help increase height, try: Stretching exercises, Hanging, and Yoga.")

# Function to perform calculations
def perform_calculation(expression):
    try:
        result = eval(expression)
        speak(f"The result of {expression} is {result}.")
    except:
        speak("I encountered an error while calculating that.")

# Function to respond to greetings
def respond_to_greeting(query):
    greetings = ["Hello! How can I assist you today?", "Hi there! What can I do for you?", "Greetings! How can I help you?"]
    speak(random.choice(greetings))

# Function to respond to goodbyes
def respond_to_goodbye():
    goodbyes = ["Goodbye! Have a great day!", "See you later! Take care!", "Farewell! Come back if you need anything."]
    speak(random.choice(goodbyes))

# Main function
def main():
    speak("AI Assistant is online. You can ask me to play songs, spell words, provide exercises, or calculate things. Say 'exit' to quit.")
    while True:
        query = listen()
        if query is None:
            continue

        if any(greeting in query for greeting in ["hello", "hi", "hey"]):
            respond_to_greeting(query)
        
        elif 'play' in query and 'song' in query:
            song_name = query.replace('play', '').replace('song', '').strip()
            play_song(song_name)
        
        elif 'spelling' in query:
            word = query.split('of')[-1].strip()
            tell_spelling(word)
        
        elif 'exercise' in query:
            exercises()

        elif 'calculate' in query:
            expression = query.replace('calculate', '').strip()
            perform_calculation(expression)

        elif 'goodbye' in query or 'exit' in query:
            respond_to_goodbye()
            break

        else:
            speak(random.choice(unknown_responses))

if __name__ == "__main__":
    main()
