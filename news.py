
import os
from dotenv import load_dotenv
from extract import get_news_headlines
import streamlit as st
import csv


load_dotenv()
api_key = os.getenv('apiKey')

# Set the category and country
categories = ['business', 'entertainment','general', 'health', 'science', 'sports', 'technology']
countries = ['us', 'za']

#Set Page Title
st.title("News Headlines")

#Set Sidebar Title
st.sidebar.title("Select An Option")

# Prompt the user for category and country
category = st.sidebar.selectbox("Select a category", categories)
country = st.sidebar.selectbox("Select a country", countries)
  
# Create a button to fetch and display the headlines and run if clicked
if st.sidebar.button("Fetch Headlines"):
    # Get the news data
    articles = get_news_headlines(category, country, api_key)
    
    # Save the headlines and URLs to a CSV file
    csv_data = []
    csv_data.append(['Headline', 'URL'])  # Add header row # Write header row
    
    # Display the headlines and URLs
    for article in articles:
        headline = article.get('title', 'No Title')
        url = article.get('url', 'No URL')
        st.markdown(f"**Headline:** {headline}")
        st.markdown(f"**URL:** {url}")
        st.write("---")

        # Append data to CSV data list
        csv_data.append([headline, url])

    # Open the CSV file and write the data
    with open('article_data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(csv_data) 