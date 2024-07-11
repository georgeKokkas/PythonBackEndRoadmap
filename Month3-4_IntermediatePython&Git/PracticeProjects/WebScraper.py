# This will be a simple web scraper. 
# This project will involve scraping data from a website 
# and extracting specific information. 
# We'll use the requests library to fetch the content of a webpage 
# and the BeautifulSoup library to parse the HTML and extract the data we need.

# A simple web scraper should:

#     Fetch the content of a webpage.
#     Parse the HTML content.
#     Extract specific information (e.g., titles of articles, image URLs).
#     Display the extracted information.

# Import the 'requests' library to handle HTTP requests
import requests

# Import the 'BeautifulSoup' class from the 'bs4' module to parse HTML
from bs4 import BeautifulSoup

# Define a function to fetch the content of a webpage
def fetch_webpage(url):
    # Send a GET request to the specified URL
    response = requests.get(url)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Return the response content
        return response.content
    else:
        # If the request failed, return None
        return None

# Define a function to parse the HTML content
def parse_html(html_content):
    # Parse the HTML content using BeautifulSoup with 'html.parser'
    soup = BeautifulSoup(html_content, 'html.parser')
    # Return the parsed HTML
    return soup

# Define a function to extract information from the parsed HTML
def extract_information(soup):
    # Find all elements that contain the titles of the articles
    titles = soup.find_all('h2')
    # Extract the text content from each title element
    extracted_titles = [title.get_text() for title in titles]
    # Return the extracted titles
    return extracted_titles

# Define a function to display the extracted information
def display_information(extracted_titles):
    print("Extracted Titles:")
    # Loop through the extracted titles and print each one
    for index, title in enumerate(extracted_titles, start=1):
        print(f"{index}. {title}")

def main():
    # URL of the webpage to scrape
    url = "https://theconversation.com/europe/topics/tourism-471"

    # Fetch the content of the webpage
    html_content = fetch_webpage(url)

    # Check if the content was fetched successfully
    if html_content:
        # Parse the HTML content
        soup = parse_html(html_content)

        # Extract information from the parsed HTML
        extracted_titles = extract_information(soup)

        # Display the extracted information
        display_information(extracted_titles)
    else:
        print("Failed to fetch the webpage content.")

# Call the main function to start the program
if __name__ == "__main__":
    main()
