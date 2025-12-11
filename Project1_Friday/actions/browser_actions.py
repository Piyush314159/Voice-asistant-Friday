import webbrowser
from core.speech import speak  # ⭐ assuming speak is defined in core.speech

def open_website(site:str):
    url= f"https://{site}.com"
    webbrowser.open(url)
    speak(f"Opening {site} website")