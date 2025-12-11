import pyttsx3
import threading

# Initialize TTS engine once
engine = pyttsx3.init() #default device voice
engine.setProperty('rate',175)
engine.setProperty('volume',1.0)
lock = threading.Lock() #Creates a "lock" object - think of it as a key to a room. Only one thread can hold this key at a time.

def speak(txt:str): 
    # Run TTS in a separate thread to avoid blocking main program
    def _run():
        with lock: #Only one thread can execute this block at a time who holds the "key"-lock
            # if multiple speak() calls happen simultaneously, they will queue up here and wait for the lock to be free
            try:
                engine.stop() # flush previous speech
                engine.say(txt)
                engine.runAndWait()

            except Exception as e:
                print("Speech Error:", e) # ⭐ Debug if something fails

    threading.Thread(target=_run, daemon=True).start() #creates and starts a new thread
    #daemon=True makes sure thread exits when main program exits