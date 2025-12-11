import pyttsx3
import threading

engine = pyttsx3.init()
engine.setProperty('rate', 175)
engine.setProperty('volume', 1.0)
lock = threading.Lock()

def speak(txt: str):
    """Speak text synchronously to avoid timing issues"""
    with lock:
        try:
            engine.stop()
            engine.say(txt)
            engine.runAndWait()
        except Exception as e:
            print("Speech Error:", e)
