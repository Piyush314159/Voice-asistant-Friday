import requests  # ⭐ for news fetching
from core.speech import speak  # ⭐ assuming speak is defined in core.speech

news_api="9dbe660e81b441188aa65d5cc051ce41"  # ⭐ placeholder for news API key

def fetch_news(country,limit=5):
    speak("Fetching top headlines from usa...")
    try:
        r = requests.get(
                    f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={news_api}"
                )

        if r.status_code == 200:
            news_data = r.json()
            articles = news_data.get("articles", [])[:limit]  # Top 5 news

            if not articles:
                        speak("Sorry, I couldn't find any news right now.")
            else:
                for i, article in enumerate(articles, start=1):
                    speak(f"News {i}: {article['title']}")
        else:
            speak("News service is currently unavailable.")
            
    except Exception as e:
        print("News API Error:", e)
        speak("Sorry, I couldn't fetch the news.")