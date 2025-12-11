import speech_recognition as sr
from core.speech import speak
from core.stt import listen_wakeWord, listen_command,name
from core.command_router import process_command

r= sr.Recognizer()
mic = sr.Microphone()

name = "friday"

def main():
    print(f"Initializing {name} systems")
    speak(f"Initializing {name} systems")

    while True:
        # 1️⃣ Listen for wake word (“hey friday”)
        wake = listen_wakeWord()

        if wake:
            speak("Yes")

            # 3️⃣ Listen for next command
            command_response = listen_command()

            if command_response:
                # speak response only if something returned
                speak(command_response)
                process_command(command_response)
            else:
                speak("Sorry, I didn't understand that.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
