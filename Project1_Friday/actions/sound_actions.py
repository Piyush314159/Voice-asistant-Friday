
import subprocess
import os

def wakeup_sound():
    sound_path = os.path.join("sounds", "wakeup.mp3")
    subprocess.call(["afplay", sound_path])
