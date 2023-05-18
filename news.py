import requests
import os
from dotenv import load_dotenv

load_dotenv()

api = os.getenv('apiKey')

category = 'business'
country = 'us'
url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={api}"

response = requests.get(url)
content = response.json()

# Assuming the JSON response is stored in the 'content' variable
articles = content['articles']  # Access the 'articles' list

headlines = []  # Initialize an empty list to store the headlines

# Iterate over each article and extract the 'title' key
for article in articles:
    title = article['title']  # Extract the 'title' key
    headlines.append(title)  # Add the title to the headlines list

# Print the extracted headlines
for headline in headlines:
    print(headline)



