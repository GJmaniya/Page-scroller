# Voice-Controlled Page Scroller
This Python script allows you to control page scrolling using voice commands. It utilizes the speech_recognition library for capturing and recognizing speech, pyttsx3 for text-to-speech functionality, and pyautogui for automating the scrolling action.

# Features
* Voice Commands: Control page scrolling by saying "page up" or "scroll up" to scroll up and "page down" or "scroll down" to scroll down.
* Adjustable Scroll: Change the scroll pixel value by voice command.
* Text-to-Speech: Provides spoken feedback using the pyttsx3 library.
* Error Handling: Gracefully handles unrecognized speech and API request errors
# Setup Instructions
Install Dependencies:  'pip install speechrecognition pyttsx3 pyautogui'

# Usage
* Scroll Up: Say "page up", "scroll up", or "upar".
* Scroll Down: Say "page down", "scroll down", or "niche".
* Change Scroll Pixel Value: Say "new pixel" and follow the instructions to enter a new value.
* Exit: Say "exit" to stop the script.

# Requirements
* Python 3.x
* Microphone for voice input

# Notes
* Adjust the pause_threshold and energy_threshold in the listen function if the recognition is not accurate.
* Modify the language parameter in recognize_google if needed for different accents or languages.

# Contributions
Feel free to fork this repository, submit issues, and make pull requests to improve the functionality or add new features.

# License
This project is licensed under the MIT License.

