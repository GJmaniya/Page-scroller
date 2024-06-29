import speech_recognition as sr 
import pyttsx3  
import pyautogui    

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to the microphone and recognize speech."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # Wait time before considering the end of a phrase
        r.energy_threshold = 300  # Minimum audio energy to consider for recording
        audio = r.listen(source, timeout=0, phrase_time_limit=4)  # Listen for the user's input

    try:
        print("Recognizing...")
        text = r.recognize_google(audio, language='en-in')  # Recognize speech using Google Web Speech API
        print(f"You said: {text}")
        return text.lower()  # Convert recognized text to lowercase
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")  # Error handling for unrecognized speech
        return None
    except sr.RequestError as e:
        print(f"Request error: {e}")  # Error handling for API request errors
        return None

if __name__ == "__main__":
    pixcl = int(input("Enter a pixel value for page up and page down: - "))  # User input for initial scroll pixel value
    while True:
        text = listen()  # Listen for voice commands
        if text is None:
            continue  # Continue to listen if no valid command is detected
        elif "page up" in text or "scroll up" in text or "upar" in text:
            pyautogui.scroll(pixcl)  # Scroll up the page by the pixel value
        elif "page down" in text or "scroll down" in text or "niche" in text:
            pyautogui.scroll(-pixcl)  # Scroll down the page by the pixel value
        elif "new pixel" in text:
            speak("Please enter the new pixel value")
            try:
                new_value = int(input("Enter new pixel value: "))  # User input for new scroll pixel value
                pixcl = new_value  # Update the pixel value
                speak(f"Pixel value set to {pixcl}")
            except ValueError:
                speak("Invalid value, please try again.")  # Error handling for invalid input
        elif "exit" in text:
            speak("Thank you")  # Exit message
            break  # Exit the loop and end the program
