import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

url = r'https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating'

# Set a User-Agent header to mimic a legitimate browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Introduce a delay between requests
delay = 2  # Set the delay in seconds

# Make the request using a Session object
with requests.Session() as session:
    response = session.get(url, headers=headers)
    time.sleep(delay)  # Introduce a delay before parsing the content to mimic human-like behavior

# Check if the request was successful (status code 200)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup)
else:
    print(f"Error: {response.status_code}")
