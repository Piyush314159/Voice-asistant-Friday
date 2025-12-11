import webbrowser
from core.speech import speak  # ⭐ assuming speak is defined in core.speech

def wiki_search(query: str):
    try:
        url = f"https://en.wikipedia.org/wiki/{query.replace(' ', '_')}"
        webbrowser.open(url)
        speak(f"Searching Wikipedia for {query}")

    except Exception as e:
        speak(f"Sorry, I couldn't search Wikipedia for {query}.")