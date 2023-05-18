
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
categories = ['business', 'entertainment','general', 'health', 'science', 'sports', 'technology']
countries = ['us', 'za']

# Prompt the user for category and country
category = input(f"Enter a category ({', '.join(categories)}): ")
while category not in categories:
    print("Invalid category. Please choose from the available categories.")
    category = input(f"Enter a category ({', '.join(categories)}): ")

country = input(f"Enter a country ({', '.join(countries)}): ")
while country not in countries:
    print("Invalid country. Please choose from the available countries.")
    country = input(f"Enter a country ({', '.join(countries)}): ")

# Get the news headlines
headlines = get_news_headlines(category, country, api_key)

# Print the headlines
print_headlines(headlines)
