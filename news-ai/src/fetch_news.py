import requests
import os
from dotenv import load_dotenv

load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def fetch_news(query="news", from_date=None, to_date=None, language="en", page_size=20):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "from": from_date,
        "to": to_date,
        "language": language,
        "sortBy": "publishedAt",
        "pageSize": page_size,
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code != 200:
        print("Error:", data.get("message"))
        return []

    articles = data.get("articles", [])

    simplified_articles = [{
        "title": article["title"],
        "url": article["url"],
        "publishedAt": article["publishedAt"],
        "source": article["source"]["name"],
        "content": article["content"] or article["description"] or ""
    } for article in articles]

    return simplified_articles