import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={os.getenv(apiKey)}"

response = requests.get(url)
content = response.json()

print(content)


