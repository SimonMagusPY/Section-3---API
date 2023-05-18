
import os
from dotenv import load_dotenv
from extract import get_news_headlines
import streamlit as st

def get_api_key():
    load_dotenv()
    return os.getenv('apiKey')

# Get the API key
api_key = get_api_key()

# Set the category and country
categories = ['business', 'entertainment','general', 'health', 'science', 'sports', 'technology']
countries = ['us', 'za']

st.title("News Headlines")
# Prompt the user for category and country
category = st.selectbox("Select a category", categories)
country = st.selectbox("Select a country", countries)
  
# Create a button to fetch and display the headlines
if st.button("Fetch Headlines"):
    # Get the news headlines
    headlines = get_news_headlines(category, country, api_key)

    # Display the headlines
       
    for headline in headlines:
        st.write(headline)
