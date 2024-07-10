# Scrape and print all the image URLs from a webpage.

# Import the 'requests' library to handle HTTP requests and 'BeautifulSoup' to parse HTML
import requests
from bs4 import BeautifulSoup

# Define the URL of the webpage
url = "https://www.facebook.com/"

# Send a GET request to the specified URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all the elements that contain images
    images = soup.find_all('img')
    
    # Loop through the images and print the URLs
    for img in images:
        print(img.get('src'))
else:
    print(f"Request failed with status code {response.status_code}")
