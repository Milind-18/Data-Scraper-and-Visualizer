# scraper.py
from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

def fetch_news(keyword):
    url = "https://google.serper.dev/news"
    headers = {"X-API-KEY": SERPER_API_KEY}
    payload = {"q": keyword}

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    news_list = []
    for item in data.get("news", []):
        news_list.append({
            "title": item["title"],
            "link": item["link"],
            "snippet": item["snippet"]
        })

    with open("outputs/raw_news.json", "w") as f:
        json.dump(news_list, f, indent=2)

    return news_list
