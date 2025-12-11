from actions.browser_actions import open_website
from actions.music_actions import play_music
from actions.info_actions import tell_time, tell_date
from actions.fallback_actions import fallback_action
from actions.news_actions import fetch_news
from actions.wiki_actions import wiki_search
from actions.custom_actions import about

def process_command(command):
    if not command:
        return "I didn't hear anything."

    command = command.lower()
    print("Command:", command)

    # Website opening
    if "open " in command:
        site = command.replace("open ", "").strip()
        open_website(site)
        return f"Opening {site} website"
        
    # Time
    elif "time" in command:
        return tell_time()

    # Date
    elif "date" in command:
        return tell_date()

    # Exit
    elif "exit" in command or "quit" in command:
        return "Goodbye!"

    # Music
    elif "play" in command:
        song_name = command.replace("play", "").strip()
        if song_name:
            play_music(song_name)
            return f"Playing {song_name}"
        return "Please tell me the song name."
    
    elif "top headlines of " in command or "news of " in command:
        country = command.replace("top headlines of","").replace("news of ","").strip().lower()
        fetch_news(country=country)

    elif "tell me about " or "who is " in command or "what is " in command:
        topic = command.replace("tell me about ","").replace("who is ","").replace("what is ","").strip()
        wiki_search(topic)  # Using news fetch as a placeholder for info fetching

    elif "about " in command:
        Name = command.replace("about ","").strip()
        about(Name)
    # Fallback AI
    else:
        return fallback_action(command)