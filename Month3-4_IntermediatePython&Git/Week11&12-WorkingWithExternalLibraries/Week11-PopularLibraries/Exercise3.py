# Scrape the titles of the latest articles from a news website.

# Import the 'requests' library to handle HTTP requests and 'BeautifulSoup' to parse HTML
import requests
from bs4 import BeautifulSoup

# Define the URL of the news website
url = "https://example.com"

# Send a GET request to the specified URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all the elements that contain the titles of the articles
    titles = soup.find_all('h1')
    
    # Loop through the titles and print them
    for title in titles:
        print(title.get_text())
else:
    print(f"Request failed with status code {response.status_code}")

