import requests

def get_news_headlines(category, country, api_key):
    url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={api_key}"
    response = requests.get(url)
    content = response.json()
    articles = content.get('articles', [])
    return articles
