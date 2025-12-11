import pywhatkit
from core.speech import speak

def play_music(song_name: str):
    try:
        pywhatkit.playonyt(song_name)
        speak(f"Playing {song_name} on YouTube")
        
    except Exception as e:
        speak(f"Sorry, I couldn't play {song_name}.")

