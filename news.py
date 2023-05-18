
import os
from dotenv import load_dotenv
from extract import get_news_headlines

def get_api_key():
    load_dotenv()
    return os.getenv('apiKey')

def print_headlines(headlines):
    for headline in headlines:
        print(headline)

# Get the API key
api_key = get_api_key()

# Set the category and country
category = 'business'
country = 'us'
# Get the news headlines
headlines = get_news_headlines(category, country, api_key)

# Print the headlines
print_headlines(headlines)
