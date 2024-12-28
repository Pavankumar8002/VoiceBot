import requests

def get_news():
    api_key = "6a02eccd26e44375a2e1f2a43f68b930"  # Replace with your News API key
    news_url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"

    try:
        response = requests.get(news_url)
        news_data = response.json()

        if news_data["status"] == "ok":
            articles = news_data["articles"]
            for article in articles:
                title = article["title"]
                source = article["source"]["name"]
                print(f"Title: {title}")
                print(f"Source: {source}")
                print("-" * 50)
        else:
            print("Failed to fetch news.")
    except Exception as e:
        print(f"Error fetching news: {e}")
