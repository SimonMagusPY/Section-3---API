import requests

def get_news_headlines(category, country, api_key):
    """
    Retrieves top news headlines based on the specified category and country using the News API.

    Args:
        category (str): The category of news headlines to retrieve (e.g., 'business', 'technology', 'sports').
        country (str): The country for which to fetch news headlines (e.g., 'us', 'gb', 'ca').
        api_key (str): The API key for accessing the News API.

    Returns:
        list: A list of articles containing news headlines and related information.
    """
    # Construct the URL for the News API request
    url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={api_key}"

    # Send a GET request to the News API
    response = requests.get(url)

    # Parse the response content as JSON
    content = response.json()

    # Extract the list of articles from the JSON content
    articles = content.get('articles', [])

    return articles
