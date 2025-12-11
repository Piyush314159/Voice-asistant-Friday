import speech_recognition as sr
from actions.sound_actions import wakeup_sound

name="friday"
r= sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    r.adjust_for_ambient_noise(source, duration=1)

def listen_wakeWord(timeout=4):
    try :
        with mic as source:
            print("🎤 Listening for wake word...")
            phrase = r.listen(source, timeout=timeout)

        command = r.recognize_google(phrase).lower()
        print("Heard:", command)

        if f"hey {name}" in command:
            wakeup_sound()  # ⭐ Play wakeup sound
            return True
        return False
        
    except sr.WaitTimeoutError:
        return False
    except sr.UnknownValueError:
        return False
    except Exception as e:
        print("Wake word error:", e)
        return False

def listen_command(timeout=4):
    try :
        with mic as source:
            print("🎤 Listening for command...")
            phrase = r.listen(source, timeout=timeout)

        command = r.recognize_google(phrase).lower()
        print("Command:", command)
        return command

    except sr.WaitTimeoutError:
        print("⏳ No speech detected.")
        return None
    except sr.UnknownValueError:
        print("🤷 Didn't understand that.")
        return None
    except Exception as e:
        print("Command error:", e)
        return None