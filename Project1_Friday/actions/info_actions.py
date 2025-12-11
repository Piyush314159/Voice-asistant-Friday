from datetime import datetime
from core.speech import speak

def tell_time():
    now = datetime.now().strftime("%I:%M %p")
    speak(f"The time is {now}")

def tell_date():
    today = datetime.now().strftime("%B %d, %Y")
    speak(f"Today's date is {today}")