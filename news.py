import requests
import os
from dotenv import load_dotenv

load_dotenv()

api = os.getenv('apiKey')

url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={api}"

response = requests.get(url)
content = response.json()

print(content)


